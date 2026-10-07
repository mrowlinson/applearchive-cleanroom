/* aad.c — AppleArchive decode, cleanroom C port v0.1.
 *
 * Covers: outer chain walk (PRE-002) + inner TLV + all 7 codecs +
 * extract with metadata (MOD/UID/GID/XAT/MTM/CTM-best-effort).
 * Derived from: quiz answers (A-001/PRE-001/PRE-002/A-007/A-008),
 * allow-listed OSS craft (A-006), own oracle runs. No vendor material.
 */
#include <compression.h>
#include <errno.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/attr.h>
#include <sys/stat.h>
#include <sys/xattr.h>
#include <unistd.h>
#include <zlib.h>

static int fails = 0;
#define FAIL(...) do { fprintf(stderr, "aad: " __VA_ARGS__); fails = 1; } while (0)

static uint16_t rd16le(const unsigned char *p) {
    return (uint16_t)(p[0] | ((uint16_t)p[1] << 8));
}
static uint32_t rd32le(const unsigned char *p) __attribute__((unused));
static uint32_t rd32le(const unsigned char *p) {
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) |
           ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24);
}
static uint32_t rd32be(const unsigned char *p) {
    return ((uint32_t)p[0] << 24) | ((uint32_t)p[1] << 16) |
           ((uint32_t)p[2] << 8) | (uint32_t)p[3];
}
static uint64_t rd64le(const unsigned char *p) __attribute__((unused));
static uint64_t rd64le(const unsigned char *p) {
    uint64_t v = 0;
    for (int i = 7; i >= 0; i--) v = (v << 8) | p[i];
    return v;
}

typedef struct { unsigned char *data; size_t len; } Buf;

static int read_file(const char *path, Buf *out) {
    FILE *f = fopen(path, "rb");
    if (!f) { FAIL("open %s: %s\n", path, strerror(errno)); return -1; }
    fseek(f, 0, SEEK_END);
    long n = ftell(f);
    fseek(f, 0, SEEK_SET);
    if (n < 0) { fclose(f); FAIL("size %s\n", path); return -1; }
    unsigned char *d = malloc((size_t)n ? (size_t)n : 1);
    if (n > 0 && fread(d, 1, (size_t)n, f) != (size_t)n) {
        fclose(f); free(d); FAIL("read %s\n", path); return -1;
    }
    fclose(f);
    out->data = d; out->len = (size_t)n;
    return 0;
}

/* ---- block payload decode (one outer block) ---- */
static int decode_block(const unsigned char magic[4],
                        const unsigned char *pay, size_t comp,
                        uint32_t unc, Buf *out) {
    if (comp == unc) { /* stored */
        unsigned char *d = malloc(comp ? comp : 1);
        memcpy(d, pay, comp);
        out->data = d; out->len = comp;
        return 0;
    }
    if (!memcmp(magic, "pbzz", 4)) {
        unsigned char *d = malloc(unc ? unc : 1);
        uLongf dl = unc;
        if (uncompress(d, &dl, pay, comp) != Z_OK || dl != unc) {
            free(d); FAIL("zlib decode\n"); return -1;
        }
        out->data = d; out->len = dl;
        return 0;
    }
    /* Whole-frame decode via public <compression.h> buffer API (v0.2).
     * Verified black-box per codec: output == oracle inner, byte-exact. */
    compression_algorithm alg = 0;
    if (!memcmp(magic, "pbze", 4)) alg = COMPRESSION_LZFSE;
    else if (!memcmp(magic, "pbz4", 4)) alg = COMPRESSION_LZ4;
    else if (!memcmp(magic, "pbzm", 4)) alg = COMPRESSION_LZRAVEN;
    else if (!memcmp(magic, "pbzb", 4)) alg = COMPRESSION_LZBITMAP;
    else if (!memcmp(magic, "pbzx", 4)) alg = COMPRESSION_LZMA;
    else { FAIL("unknown codec %.4s\n", magic); return -1; }
    unsigned char *d = malloc(unc ? unc : 1);
    void *scr = malloc(compression_decode_scratch_buffer_size(alg));
    size_t got = compression_decode_buffer(d, unc, pay, comp, scr, alg);
    free(scr);
    if (!got || got != unc) { free(d); FAIL("codec %.4s decode\n", magic); return -1; }
    out->data = d; out->len = got;
    return 0;
}

/* ---- outer chain: 12B prefix + [16B hdr + comp]* (PRE-002) ---- */
static int parse_chain(const Buf *file, Buf *inner) {
    const unsigned char *d = file->data;
    size_t n = file->len;
    if (n >= 4 && (!memcmp(d, "AA01", 4) || !memcmp(d, "YAA1", 4))) {
        unsigned char *c = malloc(n ? n : 1);
        memcpy(c, d, n);
        inner->data = c; inner->len = n;
        return 0;
    }
    if (n < 28 || memcmp(d, "pbz", 3)) { FAIL("bad outer magic\n"); return -1; }
    unsigned char magic[4];
    memcpy(magic, d, 4);
    if (memcmp(d + 4, "\0\0\0\0", 4)) { FAIL("prefix zeros\n"); return -1; }
    Buf acc = { NULL, 0 };
    size_t off = 12;
    while (off < n) {
        if (off + 16 > n) { FAIL("block hdr past EOF\n"); goto err; }
        if (memcmp(d + off, "\0\0\0\0", 4) ||
            memcmp(d + off + 8, "\0\0\0\0", 4)) {
            FAIL("block zeros @%zu\n", off); goto err;
        }
        uint32_t unc = rd32be(d + off + 4), comp = rd32be(d + off + 12);
        if (off + 16 + comp > n) { FAIL("block data past EOF\n"); goto err; }
        Buf blk = { NULL, 0 };
        if (decode_block(magic, d + off + 16, comp, unc, &blk)) goto err;
        unsigned char *nd = realloc(acc.data, acc.len + blk.len);
        if (!nd && acc.len + blk.len) { free(blk.data); goto err; }
        acc.data = nd;
        memcpy(acc.data + acc.len, blk.data, blk.len);
        acc.len += blk.len;
        free(blk.data);
        off += 16 + comp;
    }
    if (off != n) { FAIL("chain overrun\n"); goto err; }
    *inner = acc;
    return 0;
err:
    free(acc.data);
    return -1;
}

/* ---- inner TLV ---- */
typedef struct {
    char key[3];
    unsigned char st;
    uint64_t num;              /* uint value or blob size */
    const unsigned char *raw;  /* hash/timespec/string bytes */
    size_t rawlen;
} Entry;

typedef struct {
    Entry *ents;
    size_t nents;
    const unsigned char *blobs; /* concatenated blob data */
    size_t bloblen;
} Item;

static int entry_val_len(unsigned char st, const unsigned char *p,
                         size_t avail, uint64_t *num,
                         const unsigned char **raw, size_t *rawlen) {
    switch (st) {
    case '*': *num = 0; *raw = NULL; *rawlen = 0; return 0;
    case '1': case '2': case '4': case '8': {
        size_t w = st == '1' ? 1 : st == '2' ? 2 : st == '4' ? 4 : 8;
        if (avail < w) return -1;
        uint64_t v = 0;
        for (size_t i = 0; i < w; i++) v |= (uint64_t)p[i] << (8 * i);
        *num = v; *raw = NULL; *rawlen = 0; return (int)w;
    }
    case 'A': case 'B': case 'C': {
        size_t w = st == 'A' ? 2 : st == 'B' ? 4 : 8;
        if (avail < w) return -1;
        uint64_t v = 0;
        for (size_t i = 0; i < w; i++) v |= (uint64_t)p[i] << (8 * i);
        *num = v; *raw = NULL; *rawlen = 0; return (int)w;
    }
    case 'F': case 'G': case 'H': case 'I': case 'J': {
        size_t w = st == 'F' ? 4 : st == 'G' ? 20 : st == 'H' ? 32 :
                   st == 'I' ? 48 : 64;
        if (avail < w) return -1;
        *num = 0; *raw = p; *rawlen = w; return (int)w;
    }
    case 'S': case 'T': {
        size_t w = st == 'S' ? 8 : 12;
        if (avail < w) return -1;
        *num = 0; *raw = p; *rawlen = w; return (int)w;
    }
    case 'P': {
        if (avail < 2) return -1;
        size_t ln = rd16le(p);
        if (avail < 2 + ln) return -1;
        *num = ln; *raw = p + 2; *rawlen = ln; return (int)(2 + ln);
    }
    default: return -1;
    }
}

static int parse_inner(const Buf *inner, Item **items, size_t *nitems) {
    const unsigned char *d = inner->data;
    size_t n = inner->len, pos = 0, cap = 0, cnt = 0;
    Item *arr = NULL;
    while (pos < n) {
        if (pos + 6 > n) { FAIL("inner hdr trunc\n"); goto err; }
        if (memcmp(d + pos, "AA01", 4) && memcmp(d + pos, "YAA1", 4)) {
            FAIL("bad inner magic @%zu\n", pos); goto err;
        }
        size_t hsize = rd16le(d + pos + 4);
        size_t end = pos + hsize, p = pos + 6;
        if (end > n) { FAIL("inner hdr overrun\n"); goto err; }
        Item it = { NULL, 0, NULL, 0 };
        size_t ecap = 0;
        while (p < end) {
            if (p + 4 > end) { FAIL("entry trunc\n"); goto eerr; }
            Entry e;
            memcpy(e.key, d + p, 3); e.st = d[p + 3]; p += 4;
            int w = entry_val_len(e.st, d + p, end - p, &e.num, &e.raw,
                                  &e.rawlen);
            if (w < 0) { FAIL("bad subtype 0x%02x\n", e.st); goto eerr; }
            p += (size_t)w;
            if (it.nents == ecap) {
                ecap = ecap ? ecap * 2 : 8;
                Entry *ne = realloc(it.ents, ecap * sizeof *ne);
                if (!ne) goto eerr;
                it.ents = ne;
            }
            it.ents[it.nents++] = e;
        }
        if (p != end) { FAIL("hdr end mismatch\n"); goto eerr; }
        size_t blen = 0;
        for (size_t i = 0; i < it.nents; i++)
            if (it.ents[i].st == 'A' || it.ents[i].st == 'B' ||
                it.ents[i].st == 'C')
                blen += (size_t)it.ents[i].num;
        if (end + blen > n) { FAIL("blob overrun\n"); goto eerr; }
        it.blobs = d + end; it.bloblen = blen;
        if (cnt == cap) {
            cap = cap ? cap * 2 : 16;
            Item *na = realloc(arr, cap * sizeof *na);
            if (!na) goto eerr;
            arr = na;
        }
        arr[cnt++] = it;
        pos = end + blen;
        continue;
eerr:
        free(it.ents);
        goto err;
    }
    *items = arr; *nitems = cnt;
    return 0;
err:
    if (arr) for (size_t i = 0; i < cnt; i++) free(arr[i].ents);
    free(arr);
    return -1;
}

static const Entry *find_ent(const Item *it, const char key[3]) {
    for (size_t i = 0; i < it->nents; i++)
        if (!memcmp(it->ents[i].key, key, 3)) return &it->ents[i];
    return NULL;
}

static const unsigned char *blob_for(const Item *it, const char key[3],
                                     size_t *len) {
    size_t off = 0;
    for (size_t i = 0; i < it->nents; i++) {
        const Entry *e = &it->ents[i];
        if (e->st != 'A' && e->st != 'B' && e->st != 'C') continue;
        if (!memcmp(e->key, key, 3)) {
            *len = (size_t)e->num;
            return it->blobs + off;
        }
        off += (size_t)e->num;
    }
    return NULL;
}

/* ---- metadata ---- */
static void ts_from_raw(const unsigned char *raw, size_t len,
                        struct timespec *ts) {
    ts->tv_sec = (time_t)rd64le(raw);
    ts->tv_nsec = len == 12 ? (long)rd32le(raw + 8) : 0;
}

/* set one commonattr timespec; options FSOPT_NOFOLLOW for links */
static int set_one_time(const char *path, unsigned dirattr_unused,
                        uint32_t which, const struct timespec *ts,
                        int nofollow) {
    (void)dirattr_unused;
    struct attrlist al;
    memset(&al, 0, sizeof al);
    al.bitmapcount = ATTR_BIT_MAP_COUNT;
    al.commonattr = which;
    return setattrlist(path, &al, (void *)ts, sizeof *ts,
                       nofollow ? FSOPT_NOFOLLOW : 0);
}

static int apply_xattr_blob(const char *target, const unsigned char *blob,
                            size_t blen, int islink) {
    size_t pos = 0;
    while (pos + 4 <= blen) {
        uint32_t size = rd32le(blob + pos);
        if (size < 4 || pos + size > blen) { FAIL("bad xattr rec\n"); return -1; }
        const unsigned char *rec = blob + pos + 4;
        size_t remlen = size - 4, nl = 0;
        while (nl < remlen && rec[nl]) nl++;
        if (nl == remlen) { FAIL("xattr name unterminated\n"); return -1; }
        if (setxattr(target, (const char *)rec, rec + nl + 1,
                     remlen - nl - 1, 0,
                     islink ? XATTR_NOFOLLOW : 0)) {
            FAIL("setxattr %s\n", rec); return -1;
        }
        pos += size;
    }
    return 0;
}

static int apply_meta(const char *target, const Item *it, int islink) {
    const Entry *e;
    if (!islink) {
        e = find_ent(it, "MOD");
        if (e && (e->st == '1' || e->st == '2' || e->st == '4' || e->st == '8'))
            chmod(target, (mode_t)(e->num & 07777));
        e = find_ent(it, "UID");
        uint64_t uid = e ? e->num : (uint64_t)-1;
        e = find_ent(it, "GID");
        uint64_t gid = e ? e->num : (uint64_t)-1;
        if (uid != (uint64_t)-1 || gid != (uint64_t)-1)
            chown(target, (uid_t)uid, (gid_t)gid); /* EPERM-tolerant */
    } else {
        e = find_ent(it, "UID");
        uint64_t uid = e ? e->num : (uint64_t)-1;
        e = find_ent(it, "GID");
        uint64_t gid = e ? e->num : (uint64_t)-1;
        if (uid != (uint64_t)-1 || gid != (uint64_t)-1)
            lchown(target, (uid_t)uid, (gid_t)gid);
    }
    e = find_ent(it, "MTM");
    if (e && (e->rawlen == 8 || e->rawlen == 12)) {
        struct timespec ts;
        ts_from_raw(e->raw, e->rawlen, &ts);
        set_one_time(target, 0, ATTR_CMN_MODTIME, &ts, islink);
        set_one_time(target, 0, ATTR_CMN_ACCTIME, &ts, islink);
    }
    e = find_ent(it, "CTM");
    if (e && (e->rawlen == 8 || e->rawlen == 12)) {
        struct timespec ts;
        ts_from_raw(e->raw, e->rawlen, &ts);
        set_one_time(target, 0, ATTR_CMN_CRTIME, &ts, islink); /* best-effort */
    }
    size_t xl = 0;
    const unsigned char *xb = blob_for(it, "XAT", &xl);
    if (xb && xl && apply_xattr_blob(target, xb, xl, islink)) return -1;
    return 0;
}

/* ---- extract ---- */
static int mkdirs(const char *path) {
    char tmp[4096];
    size_t i, n = strlen(path);
    if (n >= sizeof tmp) return -1;
    memcpy(tmp, path, n + 1);
    for (i = 1; i < n; i++) {
        if (tmp[i] == '/') {
            tmp[i] = 0;
            if (mkdir(tmp, 0755) && errno != EEXIST) return -1;
            tmp[i] = '/';
        }
    }
    if (mkdir(tmp, 0755) && errno != EEXIST) return -1;
    return 0;
}

/* join root + rel (no absolute, no ..); out must hold 4096 */
static int safe_join(const char *root, const unsigned char *rel, size_t rlen,
                     char *out) {
    if (!rlen || rel[0] == '/') return -1;
    size_t o = strlen(root);
    if (o + 1 + rlen + 1 > 4096) return -1;
    memcpy(out, root, o);
    out[o++] = '/';
    size_t i = 0;
    while (i < rlen) {
        size_t j = i;
        while (j < rlen && rel[j] != '/') j++;
        size_t seg = j - i;
        if (seg == 0 || (seg == 1 && rel[i] == '.')) { /* skip */ }
        else if (seg == 2 && rel[i] == '.' && rel[i + 1] == '.') return -1;
        else {
            memcpy(out + o, rel + i, seg); o += seg; out[o++] = '/';
        }
        i = j + 1;
    }
    if (o > strlen(root) + 1) o--; /* drop trailing slash */
    out[o] = 0;
    return 0;
}

static int extract(const Item *items, size_t nitems, const char *root) {
    if (mkdirs(root)) { FAIL("mkdir %s\n", root); return -1; }
    /* deferred dir metadata (children bump dir mtime; apply last) */
    typedef struct { char path[4096]; size_t idx; } Def;
    Def *defs = malloc(nitems * sizeof *defs);
    size_t ndefs = 0;
    /* HLC group -> first member path (hardlink restore) */
    typedef struct { unsigned long long grp; char path[4096]; } Hlc;
    Hlc *hlcs = malloc(nitems * sizeof *hlcs);
    size_t nhlcs = 0;
    int rc = -1;
    for (size_t k = 0; k < nitems; k++) {
        const Item *it = &items[k];
        const Entry *t = find_ent(it, "TYP"), *p = find_ent(it, "PAT");
        if (!t || !p || p->st != 'P' || !p->rawlen) continue; /* root desc */
        char target[4096];
        if (safe_join(root, p->raw, p->rawlen, target)) {
            FAIL("bad path\n"); goto out;
        }
        if (t->num == 'D') {
            if (mkdirs(target)) { FAIL("mkdir %s\n", target); goto out; }
            memcpy(defs[ndefs].path, target, strlen(target) + 1);
            defs[ndefs++].idx = k;
        } else if (t->num == 'F') {
            char *sl = strrchr(target, '/');
            if (sl) { *sl = 0; if (mkdirs(target)) goto out; *sl = '/'; }
            const Entry *h = find_ent(it, "HLC");
            const char *first = NULL;
            if (h)
                for (size_t i = 0; i < nhlcs; i++)
                    if (hlcs[i].grp == h->num) { first = hlcs[i].path; break; }
            if (first) {
                unlink(target);
                if (link(first, target)) {
                    FAIL("link %s\n", target); goto out;
                }
            } else {
                size_t dl = 0;
                const unsigned char *dd = blob_for(it, "DAT", &dl);
                FILE *f = fopen(target, "wb");
                if (!f) { FAIL("open %s\n", target); goto out; }
                if (dl && fwrite(dd, 1, dl, f) != dl) {
                    fclose(f); FAIL("write %s\n", target); goto out;
                }
                fclose(f);
                if (h) {
                    hlcs[nhlcs].grp = h->num;
                    memcpy(hlcs[nhlcs].path, target, strlen(target) + 1);
                    nhlcs++;
                }
            }
            if (apply_meta(target, it, 0)) goto out;
        } else if (t->num == 'L') {
            const Entry *l = find_ent(it, "LNK");
            if (!l || l->st != 'P') { FAIL("link w/o target\n"); goto out; }
            char *sl = strrchr(target, '/');
            if (sl) { *sl = 0; if (mkdirs(target)) goto out; *sl = '/'; }
            char lbuf[4096];
            if (l->rawlen >= sizeof lbuf) goto out;
            memcpy(lbuf, l->raw, l->rawlen); lbuf[l->rawlen] = 0;
            unlink(target);
            if (symlink(lbuf, target)) {
                FAIL("symlink %s\n", target); goto out;
            }
            if (apply_meta(target, it, 1)) goto out;
        } else {
            FAIL("entry type %llu\n", (unsigned long long)t->num);
            goto out;
        }
    }
    for (size_t i = ndefs; i-- > 0;)
        if (apply_meta(defs[i].path, &items[defs[i].idx], 0)) goto out;
    rc = 0;
out:
    free(defs);
    free(hlcs);
    return rc;
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: aad IN.aar OUTDIR\n"); return 2; }
    Buf file = { NULL, 0 }, inner = { NULL, 0 };
    Item *items = NULL;
    size_t nitems = 0;
    int rc = 1;
    if (read_file(argv[1], &file)) goto out;
    if (parse_chain(&file, &inner)) goto out;
    if (parse_inner(&inner, &items, &nitems)) goto out;
    if (extract(items, nitems, argv[2])) goto out;
    rc = 0;
out:
    free(file.data); free(inner.data);
    if (items) for (size_t i = 0; i < nitems; i++) free(items[i].ents);
    free(items);
    return fails ? 1 : rc;
}
