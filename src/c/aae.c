/* aae.c — cleanroom AAR encoder (C port of prototype rawenc/pbze/lzmaenc).
 * Derived black-box from /usr/bin/aa I/O only. raw/lzfse/zlib/lzma paths.
 * lzma packets: liblzma preset-6 pinned per quiz A-20 (5.8.4 artifact, see
 * Makefile LZMA_DYLIB + sha256); XZ framing rewritten below (own code).
 * Build: make BUILDDIR=/Volumes/NVME/applearchive-cleanroom-ws/build/aae
 */
#define _DARWIN_C_SOURCE 1
#include <dirent.h>
#include <dlfcn.h>
#include <errno.h>
#include <lzma.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/attr.h>
#include <sys/stat.h>
#include <sys/xattr.h>
#include <unistd.h>
#include <zlib.h>

static const uint8_t kProvVal[] = {0x01, 0x02, 0x00, 0x66, 0x97, 0xd0,
                                   0x7a, 0xbb, 0x10, 0x2c, 0x73};
static const char kProvName[] = "com.apple.provenance";

typedef struct { uint8_t *p; size_t n, cap; } buf;

static void die(const char *msg) { perror(msg); exit(1); }

static void bneed(buf *b, size_t extra) {
    if (b->n + extra <= b->cap) return;
    size_t nc = b->cap ? b->cap : 256;
    while (nc < b->n + extra) nc *= 2;
    b->p = realloc(b->p, nc);
    if (!b->p) die("realloc");
    b->cap = nc;
}

static void bput(buf *b, const void *s, size_t len) {
    bneed(b, len);
    memcpy(b->p + b->n, s, len);
    b->n += len;
}

static void bu16le(buf *b, uint16_t v) {
    uint8_t t[2] = {(uint8_t)v, (uint8_t)(v >> 8)};
    bput(b, t, 2);
}

static void bu32le(buf *b, uint32_t v) {
    uint8_t t[4] = {(uint8_t)v, (uint8_t)(v >> 8), (uint8_t)(v >> 16),
                    (uint8_t)(v >> 24)};
    bput(b, t, 4);
}

static void bu64le(buf *b, uint64_t v) {
    uint8_t t[8];
    for (int i = 0; i < 8; i++) t[i] = (uint8_t)(v >> (8 * i));
    bput(b, t, 8);
}

static void bbe32(buf *b, uint32_t v) {
    uint8_t t[4] = {(uint8_t)(v >> 24), (uint8_t)(v >> 16),
                    (uint8_t)(v >> 8), (uint8_t)v};
    bput(b, t, 4);
}

static void bputc(buf *b, uint8_t c) { bput(b, &c, 1); }

/* minimal-width int field: key(3) + kind(1) + value */
static void put_int(buf *b, const char key[3], uint32_t v) {
    bput(b, key, 3);
    if (v <= 0xFF) {
        bput(b, "1", 1);
        uint8_t t = (uint8_t)v;
        bput(b, &t, 1);
    } else if (v <= 0xFFFF) {
        bput(b, "2", 1);
        bu16le(b, (uint16_t)v);
    } else {
        bput(b, "4", 1);
        bu32le(b, v);
    }
}

/* time field: S iff nsec==0 else T */
static void put_time(buf *b, const char key[3], uint64_t sec, uint32_t nsec) {
    bput(b, key, 3);
    if (nsec == 0) {
        bput(b, "S", 1);
        bu64le(b, sec);
    } else {
        bput(b, "T", 1);
        bu64le(b, sec);
        bu32le(b, nsec);
    }
}

/* birthtime via getattrlist; returns 0 + *out set, or -1 (caller falls back) */
static int crtime_ns(const char *path, int nofollow, uint64_t *out_sec,
                     uint32_t *out_nsec) {
    struct attrlist al;
    memset(&al, 0, sizeof al);
    al.bitmapcount = ATTR_BIT_MAP_COUNT;
    al.commonattr = ATTR_CMN_CRTIME;
    uint8_t ab[4 + sizeof(struct timespec)];
    unsigned long opts = nofollow ? FSOPT_NOFOLLOW : 0;
    if (getattrlist(path, &al, ab, sizeof ab, opts) != 0) return -1;
    struct timespec ts;
    memcpy(&ts, ab + 4, sizeof ts);
    *out_sec = (uint64_t)ts.tv_sec;
    *out_nsec = (uint32_t)ts.tv_nsec;
    return 0;
}

static int cmpbytes(const void *a, const void *b) {
    const char *sa = *(char *const *)a, *sb = *(char *const *)b;
    size_t na = strlen(sa), nb = strlen(sb), n = na < nb ? na : nb;
    int r = memcmp(sa, sb, n);
    if (r) return r;
    return (na > nb) - (na < nb);
}

/* XAT value: provenance record first, then fs xattrs sorted (links: prov only).
 * Fills vout; caller emits header now and payload after all headers. */
static void xat_value(buf *vout, const char *full, int is_link) {
    buf v = {0};
    bu32le(&v, (uint32_t)(4 + strlen(kProvName) + 1 + sizeof kProvVal));
    bput(&v, kProvName, strlen(kProvName) + 1);
    bput(&v, kProvVal, sizeof kProvVal);
    if (!is_link) {
        ssize_t ln = listxattr(full, NULL, 0, XATTR_NOFOLLOW);
        if (ln > 0) {
            char *names = malloc((size_t)ln);
            if (names && listxattr(full, names, (size_t)ln, XATTR_NOFOLLOW) > 0) {
                /* split NUL-separated list, sort */
                size_t cnt = 0;
                for (ssize_t i = 0; i < ln; i++)
                    if (names[i] == '\0') cnt++;
                char **arr = malloc((cnt + 1) * sizeof *arr);
                if (arr) {
                    size_t k = 0;
                    char *p = names;
                    while (p < names + ln) {
                        if (*p) arr[k++] = p;
                        p += strlen(p) + 1;
                    }
                    qsort(arr, k, sizeof *arr, cmpbytes);
                    for (size_t i = 0; i < k; i++) {
                        if (!strcmp(arr[i], kProvName)) continue;
                        ssize_t vsz =
                            getxattr(full, arr[i], NULL, 0, 0, XATTR_NOFOLLOW);
                        if (vsz < 0) continue;
                        uint8_t *val = malloc((size_t)vsz + 1);
                        if (!val) die("malloc");
                        ssize_t got = getxattr(full, arr[i], val, (size_t)vsz, 0,
                                               XATTR_NOFOLLOW);
                        if (got < 0) {
                            free(val);
                            continue;
                        }
                        bu32le(&v, (uint32_t)(4 + strlen(arr[i]) + 1 + got));
                        bput(&v, arr[i], strlen(arr[i]) + 1);
                        bput(&v, val, (size_t)got);
                        free(val);
                    }
                    free(arr);
                }
            }
            free(names);
        }
    }
    *vout = v;
}

static uint8_t *read_all(const char *path, size_t *len_out) {
    FILE *f = fopen(path, "rb");
    if (!f) die(path);
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    if (n < 0) die("ftell");
    uint8_t *d = malloc((size_t)n + 1);
    if (!d) die("malloc");
    if (n > 0 && fread(d, 1, (size_t)n, f) != (size_t)n) die("fread");
    fclose(f);
    *len_out = (size_t)n;
    return d;
}

static const char *g_root;

/* join root + rel (rel "" for root) */
static void fullpath(const char *rel, char *out, size_t cap) {
    if (!rel[0])
        snprintf(out, cap, "%s", g_root);
    else
        snprintf(out, cap, "%s/%s", g_root, rel);
}

static void encode_entry(buf *out, const char *rel, struct stat *st, char typ) {
    buf h = {0};
    uint8_t *dat = NULL;
    size_t datlen = 0;
    buf xat = {0};
    int has_xat = 0;
    char full[4096];
    fullpath(rel, full, sizeof full);

    bput(&h, "TYP1", 4);
    bput(&h, &typ, 1);
    bput(&h, "PATP", 4);
    bu16le(&h, (uint16_t)strlen(rel));
    bput(&h, rel, strlen(rel));
    if (typ == 'L') {
        char tgt[4096];
        ssize_t n = readlink(full, tgt, sizeof tgt);
        if (n < 0) die("readlink");
        bput(&h, "LNKP", 4);
        bu16le(&h, (uint16_t)n);
        bput(&h, tgt, (size_t)n);
    }
    if (typ == 'B' || typ == 'C')
        put_int(&h, "DEV", (uint32_t)st->st_rdev);
    put_int(&h, "UID", st->st_uid);
    put_int(&h, "GID", st->st_gid);
    put_int(&h, "MOD", (uint32_t)(st->st_mode & 0x0FFF));
    put_int(&h, "FLG", st->st_flags);
    uint64_t cs, ms = (uint64_t)st->st_mtimespec.tv_sec;
    uint32_t cn, mn = (uint32_t)st->st_mtimespec.tv_nsec;
    if (crtime_ns(full, typ == 'L', &cs, &cn) != 0) {
        cs = ms;
        cn = mn;
    }
    put_time(&h, "CTM", cs, cn);
    put_time(&h, "MTM", ms, mn);
    if (typ == 'F') {
        dat = read_all(full, &datlen);
        bput(&h, "DAT", 3);
        if (datlen <= 0xFFFF) {
            bput(&h, "A", 1);
            bu16le(&h, (uint16_t)datlen);
        } else if (datlen <= 0xFFFFFFFFu) {
            bput(&h, "B", 1);
            bu32le(&h, (uint32_t)datlen);
        } else {
            bput(&h, "C", 1);
            bu64le(&h, (uint64_t)datlen);
        }
    }
    if (typ == 'D' || typ == 'F' || typ == 'L') {
        xat_value(&xat, full, typ == 'L');
        bput(&h, "XATA", 4);
        bu16le(&h, (uint16_t)xat.n);
        has_xat = 1;
    }
    if (typ == 'F' && st->st_nlink > 1) bput(&h, "HLC1\x00", 5);

    bput(out, "AA01", 4);
    bu16le(out, (uint16_t)(6 + h.n));
    bput(out, h.p, h.n);
    if (dat) bput(out, dat, datlen);
    if (has_xat) bput(out, xat.p, xat.n);
    free(h.p);
    free(dat);
    free(xat.p);
}

static void walk(buf *out, const char *dir, const char *rel) {
    DIR *dp = opendir(dir);
    if (!dp) die(dir);
    char **names = NULL;
    size_t nn = 0, cap = 0;
    struct dirent *de;
    while ((de = readdir(dp))) {
        if (!strcmp(de->d_name, ".") || !strcmp(de->d_name, "..")) continue;
        if (nn == cap) {
            cap = cap ? cap * 2 : 32;
            names = realloc(names, cap * sizeof *names);
            if (!names) die("realloc");
        }
        names[nn++] = strdup(de->d_name);
    }
    closedir(dp);
    qsort(names, nn, sizeof *names, cmpbytes);
    for (size_t i = 0; i < nn; i++) {
        char child[4096], crel[4096];
        snprintf(child, sizeof child, "%s/%s", dir, names[i]);
        if (rel[0])
            snprintf(crel, sizeof crel, "%s/%s", rel, names[i]);
        else
            snprintf(crel, sizeof crel, "%s", names[i]);
        struct stat st;
        if (lstat(child, &st) != 0) die(child);
        mode_t m = st.st_mode;
        if (S_ISLNK(m))
            encode_entry(out, crel, &st, 'L');
        else if (S_ISDIR(m)) {
            encode_entry(out, crel, &st, 'D');
            walk(out, child, crel);
        } else if (S_ISREG(m))
            encode_entry(out, crel, &st, 'F');
        else if (S_ISBLK(m))
            encode_entry(out, crel, &st, 'B');
        else if (S_ISCHR(m))
            encode_entry(out, crel, &st, 'C');
        else if (S_ISSOCK(m))
            encode_entry(out, crel, &st, 'S');
        /* fifo: oracle hangs; skipped */
        free(names[i]);
    }
    free(names);
}

typedef size_t (*lzfse_enc_fn)(uint8_t *, size_t, const uint8_t *, size_t,
                               void *);
static lzfse_enc_fn g_lzfse;
static void *g_lzhandle;

static void lzfse_init(void) {
    if (g_lzfse) return;
    const char *p = getenv("LZFSE_DYLIB");
    if (!p)
        p = "/Volumes/NVME/applearchive-cleanroom-ws/tools/lzfse/build/bin/liblzfse.dylib";
    g_lzhandle = dlopen(p, RTLD_NOW);
    if (!g_lzhandle) {
        fprintf(stderr, "dlopen lzfse: %s\n", dlerror());
        exit(1);
    }
    g_lzfse = (lzfse_enc_fn)dlsym(g_lzhandle, "lzfse_encode_buffer");
    if (!g_lzfse) {
        fprintf(stderr, "dlsym lzfse_encode_buffer failed\n");
        exit(1);
    }
}

/* ---- lzma (pbzx): stock-packet XZ rewritten to oracle framing ---- */

static size_t xz_vint(uint8_t *o, uint64_t v) {
    size_t n = 0;
    for (;;) {
        uint8_t b = (uint8_t)(v & 0x7F);
        v >>= 7;
        if (v)
            o[n++] = (uint8_t)(0x80 | b);
        else {
            o[n++] = b;
            return n;
        }
    }
}

static uint64_t xz_read_vint(const uint8_t *d, size_t *pp) {
    uint64_t n = 0;
    int sh = 0;
    size_t p = *pp;
    for (;;) {
        uint8_t b = d[p++];
        n |= (uint64_t)(b & 0x7F) << sh;
        if (!(b & 0x80)) {
            *pp = p;
            return n;
        }
        sh += 7;
    }
}

/* end offsets of the lzma2 data run: *eos = EOS byte end, return = pad end */
static size_t xz_lzma2_end(const uint8_t *xz, size_t start, size_t *eos) {
    size_t q = start;
    for (;;) {
        uint8_t ctrl = xz[q++];
        if (ctrl == 0) {
            *eos = q;
            while ((q - start) % 4) {
                if (xz[q] != 0) {
                    fprintf(stderr, "bad lzma2 pad\n");
                    exit(1);
                }
                q++;
            }
            return q;
        } else if (ctrl == 1 || ctrl == 2) {
            size_t us = ((size_t)xz[q] << 8 | xz[q + 1]) + 1;
            q += 2 + us;
        } else if (ctrl >= 0x80) {
            int rs = (ctrl >> 5) & 3;
            size_t uhi = (size_t)(ctrl & 0x1F);
            (void)uhi; /* usize recomputed below */
            size_t us = (uhi << 16) + ((size_t)xz[q] << 8 | xz[q + 1]) + 1;
            size_t cs = ((size_t)xz[q + 2] << 8 | xz[q + 3]) + 1;
            (void)us;
            q += 4;
            if (rs >= 2) q += 1;
            q += cs;
        } else {
            fprintf(stderr, "bad lzma2 ctrl %u\n", ctrl);
            exit(1);
        }
    }
}

static void xz_fail(const char *m) {
    fprintf(stderr, "oracle_xz: %s\n", m);
    exit(1);
}

/* rewrite one single-block stock preset-6 check-none XZ to oracle form */
static uint8_t *oracle_xz(const uint8_t *xz, size_t xzn, size_t unc,
                           size_t *out_len) {
    static const uint8_t kMagic[6] = {0xFD, 0x37, 0x7A, 0x58, 0x5A, 0x00};
    if (xzn < 12 || memcmp(xz, kMagic, 6) || xz[6] || xz[7])
        xz_fail("not check-none XZ");
    size_t pos = 12;
    size_t hlen = ((size_t)xz[pos] + 1) * 4;
    uint8_t flags = xz[pos + 1];
    if ((flags & 0x3C) || (flags & 3)) xz_fail("multi-filter block");
    size_t p = pos + 2;
    if (flags & 0x40) xz_read_vint(xz, &p);
    if (flags & 0x80) xz_read_vint(xz, &p);
    if (xz[p] != 0x21) xz_fail("not LZMA2");
    size_t fsize = xz[p + 1];
    const uint8_t *dc = xz + p + 2;
    size_t data_start = pos + hlen;
    size_t eos_end, data_end;
    data_end = xz_lzma2_end(xz, data_start, &eos_end);
    if (data_end % 4) xz_fail("misaligned lzma2");
    size_t lzlen = data_end - data_start;
    size_t ob0 = unc >= ((size_t)1 << 21) ? 4 : 3;
    size_t ohlen = (ob0 + 1) * 4;
    buf o = {0};
    bput(&o, xz, 12);
    size_t hstart = o.n;
    uint8_t vb[16];
    bputc(&o, (uint8_t)ob0);
    bputc(&o, 0xC0);
    bput(&o, vb, xz_vint(vb, (uint64_t)(eos_end - data_start)));
    bput(&o, vb, xz_vint(vb, (uint64_t)unc));
    bputc(&o, 0x21);
    bputc(&o, 0x01);
    bput(&o, dc, fsize);
    while (o.n - hstart < ohlen - 4) bputc(&o, 0);
    if (o.n - hstart != ohlen - 4) xz_fail("header overflow");
    uint32_t hc = (uint32_t)crc32(0L, o.p + hstart, (uInt)(ohlen - 4));
    bu32le(&o, hc);
    size_t unpadded = ohlen + (eos_end - data_start);
    size_t istart = o.n;
    bputc(&o, 0x00);
    bputc(&o, 0x01);
    bput(&o, vb, xz_vint(vb, (uint64_t)unpadded));
    bput(&o, vb, xz_vint(vb, (uint64_t)unc));
    while ((o.n - istart) % 4) bputc(&o, 0);
    /* NOTE: index pad included in crc below (idx bytes then crc) */
    uint32_t ic = (uint32_t)crc32(0L, o.p + istart, (uInt)(o.n - istart));
    bu32le(&o, ic);
    uint8_t back[6];
    uint32_t bw = (uint32_t)((o.n - istart - 4) / 4);
    back[0] = (uint8_t)bw;
    back[1] = (uint8_t)(bw >> 8);
    back[2] = (uint8_t)(bw >> 16);
    back[3] = (uint8_t)(bw >> 24);
    back[4] = back[5] = 0;
    uint32_t fc = (uint32_t)crc32(0L, back, 6);
    bu32le(&o, fc);
    bput(&o, back, 6);
    bputc(&o, 'Y');
    bputc(&o, 'Z');
    /* splice lzdata between header and index: rebuild in order */
    buf f = {0};
    bput(&f, o.p, 12 + ohlen);
    bput(&f, xz + data_start, lzlen);
    bput(&f, o.p + 12 + ohlen, o.n - (12 + ohlen));
    free(o.p);
    *out_len = f.n;
    return f.p;
}

/* stock preset-6 check-none XZ of chunk, rewritten to oracle framing */
static uint8_t *xz_encode(const uint8_t *ch, size_t n, size_t *out_len) {
    size_t bound = lzma_stream_buffer_bound(n);
    uint8_t *std = malloc(bound ? bound : 1);
    if (!std) die("malloc");
    size_t opos = 0;
    lzma_ret r = lzma_easy_buffer_encode(6, LZMA_CHECK_NONE, NULL, ch, n,
                                         std, &opos, bound);
    if (r != LZMA_OK) {
        fprintf(stderr, "lzma_easy_buffer_encode: %d\n", r);
        exit(1);
    }
    uint8_t *rw = oracle_xz(std, opos, n, out_len);
    free(std);
    return rw;
}

/* returns compressed bytes (malloc) or NULL to store */
static uint8_t *code_block(const char *alg, const uint8_t *ch, size_t n,
                           size_t *out_len) {
    uint8_t *dst = NULL;
    size_t cn = 0;
    if (!strcmp(alg, "lzfse")) {
        lzfse_init();
        dst = malloc(n + 4096);
        if (!dst) die("malloc");
        cn = g_lzfse(dst, n + 4096, ch, n, NULL);
        if (cn == 0) {
            free(dst);
            return NULL;
        }
    } else if (!strcmp(alg, "zlib")) {
        uLongf zlen = compressBound((uLong)n);
        dst = malloc((size_t)zlen);
        if (!dst) die("malloc");
        if (compress2(dst, &zlen, ch, (uLong)n, 5) != Z_OK) {
            free(dst);
            return NULL;
        }
        cn = (size_t)zlen;
    } else if (!strcmp(alg, "lzma")) {
        dst = xz_encode(ch, n, &cn);
    } else {
        return NULL;
    }
    /* store iff comp*16 > unc*15 */
    if ((uint64_t)cn * 16 > (uint64_t)n * 15) {
        free(dst);
        return NULL;
    }
    *out_len = cn;
    return dst;
}

static void wrap_pbze(buf *out, const uint8_t *inner, size_t ilen,
                      const char *magic, size_t blocksize, const char *alg) {
    size_t nch = (ilen + blocksize - 1) / blocksize;
    if (nch == 0) nch = 1;
    uint8_t **pay = malloc(nch * sizeof *pay);
    size_t *ul = malloc(nch * sizeof *ul), *cl = malloc(nch * sizeof *cl);
    if (!pay || !ul || !cl) die("malloc");
    for (size_t i = 0; i < nch; i++) {
        size_t off = i * blocksize;
        size_t n = ilen - off > blocksize ? blocksize : ilen - off;
        ul[i] = n;
        size_t cn = 0;
        uint8_t *cf = code_block(alg, inner + off, n, &cn);
        if (cf) {
            pay[i] = cf;
            cl[i] = cn;
        } else {
            pay[i] = malloc(n ? n : 1);
            if (n) memcpy(pay[i], inner + off, n);
            cl[i] = n;
        }
    }
    bput(out, magic, 4);
    bbe32(out, 0);
    bbe32(out, (uint32_t)blocksize);
    bbe32(out, 0);
    bbe32(out, (uint32_t)ul[0]);
    bbe32(out, 0);
    bbe32(out, (uint32_t)cl[0]);
    for (size_t i = 0; i < nch; i++) {
        bput(out, pay[i], cl[i]);
        if (i + 1 < nch) {
            bbe32(out, 0);
            bbe32(out, (uint32_t)ul[i + 1]);
            bbe32(out, 0);
            bbe32(out, (uint32_t)cl[i + 1]);
        }
        free(pay[i]);
    }
    free(pay);
    free(ul);
    free(cl);
}

static size_t parse_size(const char *s) {
    char *e;
    unsigned long long v = strtoull(s, &e, 10);
    if (e == s) goto bad;
    if (*e == 'k' || *e == 'K')
        v *= 1024, e++;
    else if (*e == 'm' || *e == 'M')
        v *= 1024 * 1024, e++;
    else if (*e == 'g' || *e == 'G')
        v *= 1024 * 1024 * 1024, e++;
    else if (*e == 'b' || *e == 'B')
        e++;
    if (*e) goto bad;
    return (size_t)v;
bad:
    fprintf(stderr, "bad size %s\n", s);
    exit(1);
}

int main(int argc, char **argv) {
    const char *src = NULL, *dst = NULL, *alg = "lzfse";
    size_t block = 4 * 1024 * 1024;
    for (int i = 1; i < argc; i++) {
        if (!strcmp(argv[i], "--alg") && i + 1 < argc)
            alg = argv[++i];
        else if (!strcmp(argv[i], "--block") && i + 1 < argc)
            block = parse_size(argv[++i]);
        else if (!strcmp(argv[i], "--threads"))
            i++; /* accepted, deterministic single-threaded */
        else if (!src)
            src = argv[i];
        else if (!dst)
            dst = argv[i];
        else {
            fprintf(stderr, "unexpected arg %s\n", argv[i]);
            return 1;
        }
    }
    if (!src || !dst) {
        fprintf(stderr, "usage: aae SRCDIR OUT.aar [--alg raw|lzfse|zlib|lzma] "
                        "[--block SIZE] [--threads N]\n");
        return 1;
    }
    const char *magic = NULL;
    if (!strcmp(alg, "lzfse"))
        magic = "pbze";
    else if (!strcmp(alg, "zlib"))
        magic = "pbzz";
    else if (!strcmp(alg, "lzma"))
        magic = "pbzx";
    else if (strcmp(alg, "raw")) {
        fprintf(stderr, "unsupported alg %s\n", alg);
        return 1;
    }
    if (block < 1 || block > 134217728) {
        fprintf(stderr, "invalid block size %zu\n", block);
        return 1;
    }
    g_root = src;
    buf inner = {0};
    struct stat st0;
    if (lstat(src, &st0) != 0) die(src);
    encode_entry(&inner, "", &st0, 'D');
    walk(&inner, src, "");
    buf out = {0};
    if (!strcmp(alg, "raw")) {
        bput(&out, inner.p, inner.n);
    } else {
        wrap_pbze(&out, inner.p, inner.n, magic, block, alg);
    }
    FILE *f = fopen(dst, "wb");
    if (!f) die(dst);
    if (out.n > 0 && fwrite(out.p, 1, out.n, f) != out.n) die("fwrite");
    fclose(f);
    return 0;
}
