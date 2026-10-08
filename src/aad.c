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
static uint32_t rd32be(const unsigned char *p) __attribute__((unused));
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
static uint64_t rd64be(const unsigned char *p) {
    uint64_t v = 0;
    for (int i = 0; i < 8; i++) v = (v << 8) | p[i];
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

/* ---- block payload decode (one outer block) ----
 * Tri-state: 0 ok (got==unc, out set); 1 size-mismatch (0<got<unc,
 * out discarded, *got = actual); -1 undecodable (*got = 0). */
static int decode_block(const unsigned char magic[4],
                        const unsigned char *pay, size_t comp,
                        uint32_t unc, Buf *out, size_t *got) {
    *got = 0;
    if (comp == unc) { /* stored */
        unsigned char *d = malloc(comp ? comp : 1);
        memcpy(d, pay, comp);
        out->data = d; out->len = comp;
        *got = comp;
        return 0;
    }
    if (!memcmp(magic, "pbzz", 4)) {
        unsigned char *d = malloc(unc ? unc : 1);
        uLongf dl = unc;
        if (uncompress(d, &dl, pay, comp) == Z_OK) {
            *got = dl;
            if (dl == unc) { out->data = d; out->len = dl; return 0; }
            free(d); return 1;
        }
        /* oracle decodes adler-broken streams (case188): raw fallback */
        if (comp > 2) {
            z_stream zs;
            memset(&zs, 0, sizeof zs);
            if (inflateInit2(&zs, -MAX_WBITS) == Z_OK) {
                zs.next_in = (Bytef *)(pay + 2);
                zs.avail_in = (uInt)(comp - 2);
                zs.next_out = d;
                zs.avail_out = unc;
                int r = inflate(&zs, Z_FINISH);
                size_t tot = zs.total_out;
                inflateEnd(&zs);
                if (r == Z_STREAM_END) {
                    *got = tot;
                    if (tot == unc) { out->data = d; out->len = unc; return 0; }
                    free(d); return 1;
                }
            }
        }
        free(d); return -1;
    }
    /* Whole-frame decode via public <compression.h> buffer API (v0.2).
     * Verified black-box per codec: output == oracle inner, byte-exact. */
    compression_algorithm alg = 0;
    if (!memcmp(magic, "pbze", 4)) alg = COMPRESSION_LZFSE;
    else if (!memcmp(magic, "pbz4", 4)) alg = COMPRESSION_LZ4;
    else if (!memcmp(magic, "pbzm", 4)) alg = COMPRESSION_LZRAVEN;
    else if (!memcmp(magic, "pbzb", 4)) alg = COMPRESSION_LZBITMAP;
    else if (!memcmp(magic, "pbzx", 4)) alg = COMPRESSION_LZMA;
    else { return -1; } /* unreachable: known_pbz gated */
    unsigned char *d = malloc(unc ? unc : 1);
    void *scr = malloc(compression_decode_scratch_buffer_size(alg));
    size_t g = compression_decode_buffer(d, unc, pay, comp, scr, alg);
    free(scr);
    *got = g;
    if (g == unc && unc) { out->data = d; out->len = g; return 0; }
    free(d);
    return g ? 1 : -1;
}

/* ---- outer chain: length ladder + 12B prefix + [16B hdr + comp]* ---- */
static void emit_stream_tail(void) {
    fprintf(stderr, "Extraction failed\n"
            "extract failedError 0xbd011800\n"
            "No more data\nread error\ntruncated stream\n"
            "archive stream read error (header)\nstream cancelled\n");
}

static void emit_nonsupp(void) {
    fprintf(stderr, "Extraction failed\n"
            "extract failedError 0xbd035000\n"
            "Invalid/non-supported archive stream\n"
            "archive stream read error (header)\nstream cancelled\n");
}

static void emit_trunc(const char *what, unsigned long long have,
                       unsigned long long need, int blob) {
    if (!blob)
        fprintf(stderr, "Extraction failed\n"
                "extract failedError 0xbd009800\n"
                "istream read error\n"
                "refill buffer\n"
                "archive stream read error (header)\n"
                "flushing shared buffer\n"
                "Truncated block %s (%llu/%llu bytes read)\n"
                "NOP received\n"
                "processStream\n"
                "decoder failed\n"
                "stream cancelled\n",
                what, have, need);
    else
        fprintf(stderr, "Extraction failed\n"
                "extract failedError 0xbd009800\n"
                "istream read error\n"
                "Refill buffer failed\n"
                "read error\n"
                "archive stream read error (blob)\n"
                "flushing shared buffer\n"
                "Truncated block %s (%llu/%llu bytes read)\n"
                "NOP received\n"
                "processStream\n"
                "decoder failed\n"
                "stream cancelled\n",
                what, have, need);
}

static void emit_badval(unsigned long long pay, unsigned long long raw,
                        unsigned long long bsize, int blob) {
    fprintf(stderr, "Extraction failed\n"
            "extract failedError 0xbd009800\n"
            "istream read error\n");
    if (blob)
        fprintf(stderr, "Refill buffer failed\nread error\n"
                "archive stream read error (blob)\n");
    else
        fprintf(stderr, "refill buffer\n"
                "archive stream read error (header)\n");
    fprintf(stderr, "flushing shared buffer\n"
            "Invalid block header payload=0x%llx raw=0x%llx block=0x%llx\n"
            "\n"
            "NOP received\n"
            "processStream\n"
            "decoder failed\n"
            "stream cancelled\n",
            pay, raw, bsize);
}

/* chained line before the worker stanza (TIP2e chain-together
 * law, DPROBE-15): scan trailing bytes from payload_end as a
 * chain. r<16 -> framing(r/16); pair invalid -> badval STOP;
 * valid + short payload -> truncpay-line STOP; valid + full
 * payload -> skip 16+P + recurse. Header + blob alike (MZT). */
static void emit_chain(const unsigned char *d, size_t pend,
                       unsigned long long h2, unsigned long long bsize) {
    unsigned long long r = h2;
    size_t p = pend;
    for (;;) {
        if (r == 0)
            return;
        if (r < 16) {
            fprintf(stderr, "Truncated block header (%llu/16 bytes read)\n",
                    r);
            return;
        }
        uint64_t R = rd64be(d + p), P = rd64be(d + p + 8);
        if (R > bsize || P > bsize) {
            fprintf(stderr, "Invalid block header payload=0x%llx raw=0x%llx "
                    "block=0x%llx\n\n",
                    (unsigned long long)P, (unsigned long long)R, bsize);
            return;
        }
        if (16 + P > r) {
            fprintf(stderr, "Truncated block payload (%llu/%llu bytes "
                    "read)\n", r - 16, (unsigned long long)P);
            return;
        }
        p += (size_t)(16 + P);
        r -= 16 + P;
    }
}

static void emit_decfail(unsigned long long k, unsigned long long pay,
                         unsigned long long raw, long long out, int blob,
                         const unsigned char *d, size_t pend,
                         unsigned long long h2, unsigned long long bsize) {
    fprintf(stderr, "Extraction failed\n"
            "extract failedError 0xbd009800\n"
            "istream read error\n");
    if (blob)
        fprintf(stderr, "Refill buffer failed\nread error\n"
                "archive stream read error (blob)\n");
    else
        fprintf(stderr, "refill buffer\n"
                "archive stream read error (header)\n");
    fprintf(stderr, "flushing shared buffer\n");
    emit_chain(d, pend, h2, bsize);
    fprintf(stderr, "invalid output size/decoder error: block=%llu, inSize=%llu, "
            "outSize=%lld, expectedOutSize=%llu\n"
            "worker proc reported an error\n"
            "Threads reported errors\n"
            "ThreadPipelineDestroy\n"
            "processStream\n"
            "decoder failed\n"
            "stream cancelled\n",
            k, pay, out, raw);
}

/* mid-chain soft failure: (blob) path extracts the decoded prefix. */
enum { MF_TRUNCHDR = 0, MF_TRUNCPAY, MF_BADVAL, MF_DECFAIL };
typedef struct {
    int kind;
    unsigned long long a, b, c; /* have/need | pay/raw/bsize | k/pay/raw */
    unsigned long long whole;   /* decoded bytes before failing block */
    unsigned long long kcut;    /* failing block index */
    long long out;              /* decfail actual outSize, -1 undecodable */
    unsigned long long h2;      /* decfail trailing bytes after payload */
    unsigned long long pend;    /* decfail payload_end file offset */
    unsigned long long bsize;   /* decfail outer bsize (pair gate) */
} MidFail;

static void emit_midblob(const MidFail *mf, const Buf *file) {
    switch (mf->kind) {
    case MF_TRUNCHDR:
        emit_trunc("header", mf->a, mf->b, 1);
        break;
    case MF_TRUNCPAY:
        emit_trunc("payload", mf->a, mf->b, 1);
        break;
    case MF_BADVAL:
        emit_badval(mf->a, mf->b, mf->c, 1);
        break;
    case MF_DECFAIL:
        emit_decfail(mf->a, mf->b, mf->c, mf->out, 1, file->data,
                     (size_t)mf->pend, mf->h2, mf->bsize);
        break;
    }
}

static int known_pbz(const unsigned char *d) {
    return !memcmp(d, "pbze", 4) || !memcmp(d, "pbz4", 4) ||
           !memcmp(d, "pbzm", 4) || !memcmp(d, "pbzb", 4) ||
           !memcmp(d, "pbzx", 4) || !memcmp(d, "pbzz", 4);
}

/* parse_chain: 0 ok, -1 hard fail (cascade printed), 1 midchain soft
 * fail ((blob) path: inner = decoded prefix, mf filled, cascade later).
 * nblocks = decoded outer-block count (raw/empty single-piece = 1);
 * clean-path presence gate uses (innerlen, nblocks) as (whole, kcut). */
static int parse_chain(const Buf *file, Buf *inner, MidFail *mf,
                       size_t *nblocks, unsigned long long *bsize_out) {
    const unsigned char *d = file->data;
    size_t n = file->len;
    *nblocks = 1;
    *bsize_out = 0;
    if (n == 0) { /* empty archive: silent empty (tr-0, q4) */
        inner->data = malloc(1); inner->len = 0;
        *nblocks = 1;
        return inner->data ? 0 : -1;
    }
    if (n < 6) { emit_stream_tail(); fails = 1; return -1; }
    if (!memcmp(d, "AA01", 4) || !memcmp(d, "YAA1", 4)) {
        unsigned char *c = malloc(n);
        memcpy(c, d, n);
        inner->data = c; inner->len = n;
        *nblocks = 1;
        return 0;
    }
    if (n < 12) { emit_nonsupp(); fails = 1; return -1; }
    if (!known_pbz(d)) { emit_nonsupp(); fails = 1; return -1; }
    unsigned char magic[4];
    memcpy(magic, d, 4);
    /* prefix = magic(4) + bsize u64be; no zero fields (DPROBE-08). */
    uint64_t bsize = rd64be(d + 4);
    *bsize_out = (unsigned long long)bsize;
    if (bsize == 0 || bsize > 0x8000000ULL) {
        fprintf(stderr, "Failed to create decompression stream\n"
                "Error creating input stream\n"
                "extract failedError 0x9404c000\n"
                "invalid block size\n");
        fails = 1;
        return -1;
    }
    Buf acc = { NULL, 0 };
    size_t off = 12;
    unsigned long long k = 0;
    while (off < n) {
        int blob = acc.len >= 262144; /* streaming flavor threshold */
        if (off + 16 > n) {
            if (!blob) {
                emit_trunc("header", (unsigned long long)(n - off), 16ULL, 0);
                fails = 1;
                goto err;
            }
            mf->kind = MF_TRUNCHDR; mf->a = (unsigned long long)(n - off);
            mf->b = 16ULL; mf->c = 0; mf->whole = (unsigned long long)acc.len;
            mf->kcut = k;
            *inner = acc;
            return 1;
        }
        uint64_t raw = rd64be(d + off), pay = rd64be(d + off + 8);
        if (raw > bsize || pay > bsize) {
            if (!blob) {
                emit_badval((unsigned long long)pay, (unsigned long long)raw,
                            (unsigned long long)bsize, 0);
                fails = 1;
                goto err;
            }
            mf->kind = MF_BADVAL; mf->a = (unsigned long long)pay;
            mf->b = (unsigned long long)raw;
            mf->c = (unsigned long long)bsize;
            mf->whole = (unsigned long long)acc.len;
            mf->kcut = k;
            *inner = acc;
            return 1;
        }
        uint32_t unc = (uint32_t)raw, comp = (uint32_t)pay;
        if (off + 16 + comp > n) {
            if (!blob) {
                emit_trunc("payload", (unsigned long long)(n - off - 16),
                           (unsigned long long)pay, 0);
                fails = 1;
                goto err;
            }
            mf->kind = MF_TRUNCPAY; mf->a = (unsigned long long)(n - off - 16);
            mf->b = (unsigned long long)pay; mf->c = 0;
            mf->whole = (unsigned long long)acc.len;
            mf->kcut = k;
            *inner = acc;
            return 1;
        }
        Buf blk = { NULL, 0 };
        size_t got = 0;
        int dr = decode_block(magic, d + off + 16, comp, unc, &blk, &got);
        if (dr) {
            long long out = dr > 0 ? (long long)got : -1;
            unsigned long long have2 =
                (unsigned long long)(n - off - 16 - comp);
            if (!blob) {
                emit_decfail(k, (unsigned long long)pay,
                             (unsigned long long)raw, out, 0, d,
                             off + 16 + comp, have2,
                             (unsigned long long)bsize);
                fails = 1;
                goto err;
            }
            mf->kind = MF_DECFAIL; mf->a = k;
            mf->b = (unsigned long long)pay;
            mf->c = (unsigned long long)raw;
            mf->whole = (unsigned long long)acc.len;
            mf->kcut = k;
            mf->out = out;
            mf->h2 = have2;
            mf->pend = (unsigned long long)(off + 16 + comp);
            mf->bsize = (unsigned long long)bsize;
            *inner = acc;
            return 1;
        }
        unsigned char *nd = realloc(acc.data, acc.len + blk.len);
        if (!nd && acc.len + blk.len) { free(blk.data); goto err; }
        acc.data = nd;
        memcpy(acc.data + acc.len, blk.data, blk.len);
        acc.len += blk.len;
        free(blk.data);
        off += 16 + comp;
        k++;
    }
    if (off != n) { FAIL("chain overrun\n"); goto err; }
    *inner = acc;
    *nblocks = (size_t)k;
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

/* inner parse failure classes (oracle wrapper per class; prefix kept) */
enum { PF_OK = 0, PF_TAIL, PF_BADMAGIC, PF_HDRCUT, PF_ENDMISMATCH,
       PF_VALUEOVERRUN, PF_BADSUBTYPE, PF_BLOBOVERRUN, PF_HSIZEMISMATCH,
       PF_HDRTAIL, PF_STREAMMAGIC };

static int parse_inner(const Buf *inner, Item **items, size_t *nitems,
                       int *fcls, int *fsub, size_t *shortidx,
                       size_t *shortavail, size_t *shortend) {
    const unsigned char *d = inner->data;
    size_t n = inner->len, pos = 0, cap = 0, cnt = 0;
    Item *arr = NULL;
    int cls = PF_OK, sub = 0;
    *shortidx = (size_t)-1;
    *shortavail = 0;
    *shortend = 0;
    while (pos < n) {
        if (pos + 6 > n) { cls = PF_TAIL; break; }
        if (memcmp(d + pos, "AA01", 4) && memcmp(d + pos, "YAA1", 4)) {
            cls = pos == 0 ? PF_STREAMMAGIC : PF_BADMAGIC; break;
        }
        size_t hsize = rd16le(d + pos + 4);
        if (hsize < 6) { cls = PF_HSIZEMISMATCH; sub = (int)hsize; break; }
        size_t end = pos + hsize, p = pos + 6;
        if (end > n) { cls = PF_HDRTAIL; break; }
        Item it = { NULL, 0, NULL, 0 };
        size_t ecap = 0;
        while (p < end) {
            if (p + 4 > end) { cls = PF_HDRCUT; goto itfail; }
            Entry e;
            memcpy(e.key, d + p, 3); e.st = d[p + 3]; p += 4;
            int w = entry_val_len(e.st, d + p, end - p, &e.num, &e.raw,
                                  &e.rawlen);
            if (w < 0) {
                switch (e.st) {
                case '*': case '1': case '2': case '4': case '8':
                case 'A': case 'B': case 'C': case 'F': case 'G':
                case 'H': case 'I': case 'J': case 'S': case 'T':
                case 'P':
                    cls = PF_VALUEOVERRUN; break;
                default:
                    cls = PF_BADSUBTYPE; sub = e.st; break;
                }
                goto itfail;
            }
            p += (size_t)w;
            if (it.nents == ecap) {
                ecap = ecap ? ecap * 2 : 8;
                Entry *ne = realloc(it.ents, ecap * sizeof *ne);
                if (!ne) { free(it.ents); goto fatal; }
                it.ents = ne;
            }
            it.ents[it.nents++] = e;
        }
        if (p != end) { cls = PF_ENDMISMATCH; goto itfail; }
        size_t blen = 0;
        for (size_t i = 0; i < it.nents; i++)
            if ((it.ents[i].st == 'A' || it.ents[i].st == 'B' ||
                 it.ents[i].st == 'C') &&
                memcmp(it.ents[i].key, "TYP", 3))
                blen += (size_t)it.ents[i].num;
        if (end + blen > n) {
            /* Short-blob item: append flagged (midchain makes an empty
             * node; normal path skips it and the wrapper reports). */
            cls = PF_BLOBOVERRUN;
            it.blobs = d + end; it.bloblen = n - end;
            *shortidx = cnt;
            *shortavail = n - end;
            *shortend = end;
            if (cnt == cap) {
                cap = cap ? cap * 2 : 16;
                Item *na = realloc(arr, cap * sizeof *na);
                if (!na) { free(it.ents); goto fatal; }
                arr = na;
            }
            arr[cnt++] = it;
            break;
        }
        it.blobs = d + end; it.bloblen = blen;
        if (cnt == cap) {
            cap = cap ? cap * 2 : 16;
            Item *na = realloc(arr, cap * sizeof *na);
            if (!na) { free(it.ents); goto fatal; }
            arr = na;
        }
        arr[cnt++] = it;
        pos = end + blen;
        continue;
itfail:
        free(it.ents);
        break;
    }
    *items = arr; *nitems = cnt;
    *fcls = cls; *fsub = sub;
    return 0;
fatal:
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
        if (!memcmp(e->key, "TYP", 3)) continue; /* CR-053: bare, no blob */
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

/* 0 ok / -1 invalid-or-unsettable. SILENT: callers print oracle lines. */
static int apply_xattr_blob(const char *target, const unsigned char *blob,
                            size_t blen, int islink) {
    size_t pos = 0;
    while (pos + 4 <= blen) {
        uint32_t size = rd32le(blob + pos);
        if (size < 4 || pos + size > blen) return -1;
        const unsigned char *rec = blob + pos + 4;
        size_t remlen = size - 4, nl = 0;
        while (nl < remlen && rec[nl]) nl++;
        if (nl == remlen) return -1;
        if (setxattr(target, (const char *)rec, rec + nl + 1,
                     remlen - nl - 1, 0,
                     islink ? XATTR_NOFOLLOW : 0)) return -1;
        pos += size;
    }
    if (pos != blen) return -1; /* oracle rejects trailing bytes */
    return 0;
}

/* oracle prints one "Error 0x..." header per run: first class wins. */
static void print_hdr(int *done, unsigned code) {
    if (!*done) { fprintf(stderr, "Error 0x%08x\n", code); *done = 1; }
}

/* EISDIR shape: L1 = basename(arg), L2 = absolute target (epf2 probes). */
static void eisdir_err(int *done, const char *path) {
    char strip[4096], abs[8192];
    size_t n = strlen(path);
    if (n >= sizeof strip) n = sizeof strip - 1;
    memcpy(strip, path, n); strip[n] = 0;
    while (n > 1 && strip[n - 1] == '/') strip[--n] = 0;
    const char *b = strrchr(strip, '/');
    b = b ? b + 1 : strip;
    if (strip[0] == '/') {
        snprintf(abs, sizeof abs, "%s", strip);
    } else {
        char cwd[4096];
        if (getcwd(cwd, sizeof cwd))
            snprintf(abs, sizeof abs, "%s/%s", cwd, strip);
        else
            snprintf(abs, sizeof abs, "%s", strip);
    }
    print_hdr(done, 0xc305ac15);
    fprintf(stderr, "Is a directory: %s\nIs a directory: %s\n"
            "opening output file: %s\n", b, abs, abs);
}

/* xattr step, strict. 0 ok / -1 fail (caller prints + classifies). */
static int apply_xattr_only(const char *target, const Item *it, int islink) {
    size_t xl = 0;
    const unsigned char *xb = blob_for(it, "XAT", &xl);
    if (xb && xl && apply_xattr_blob(target, xb, xl, islink)) return -1;
    return 0;
}

/* mode/owner/times step. Best-effort: never fails the run. */
static void apply_rest(const char *target, const Item *it, int islink) {
    const Entry *e;
    if (!islink) {
        /* chown BEFORE chmod: successful chown strips SUID/SGID (191). */
        e = find_ent(it, "UID");
        uint64_t uid = e ? e->num : (uint64_t)-1;
        e = find_ent(it, "GID");
        uint64_t gid = e ? e->num : (uint64_t)-1;
        if (uid != (uint64_t)-1 || gid != (uint64_t)-1)
            chown(target, (uid_t)uid, (gid_t)gid); /* EPERM-tolerant */
        e = find_ent(it, "MOD");
        if (e && (e->st == '1' || e->st == '2' || e->st == '4' || e->st == '8'))
            chmod(target, (mode_t)(e->num & 07777));
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
}

/* ---- extract ---- */
/* Gated parents (G9 modal, NOTE-048): never create through or write
 * through a non-dir parent. Missing components are created 0755;
 * existing non-dir components (symlink/file/...) are unlinked +
 * replaced with a real dir 0755 and recorded in repl[] (dedup).
 * Children under a replaced prefix fail modally (83058800 pair +
 * `creating fs object` third line on non-F kinds (L/P per A-027#1;
 * F never), flushed in archive order post phase-1 per A-026#5);
 * siblings elsewhere proceed. D-under-replaced takes the F-shape
 * (hypothesis, unprobed); H PATH-side pair is a hypothesis (A-027#2
 * covers TARGET-side only). Head/count shared with other classes
 * (first-failure head, one joint count, A-027#3). */
#define REPLC 64
static int repl_add(char repl[][4096], size_t *nrepl, const char *prefix) {
    for (size_t i = 0; i < *nrepl; i++)
        if (!strcmp(repl[i], prefix)) return 0;
    if (*nrepl >= REPLC) return 0; /* cap: replaced but untracked */
    strcpy(repl[*nrepl], prefix);
    (*nrepl)++;
    return 0;
}
static int mkone(char *prefix, char repl[][4096], size_t *nrepl) {
    struct stat st;
    if (!lstat(prefix, &st)) {
        if (S_ISDIR(st.st_mode)) return 0;
        if (unlink(prefix)) return -1;
        if (mkdir(prefix, 0755)) return -1;
        return repl_add(repl, nrepl, prefix);
    }
    if (mkdir(prefix, 0755)) {
        if (errno == EEXIST && !lstat(prefix, &st) && S_ISDIR(st.st_mode))
            return 0;
        return -1;
    }
    return 0;
}
static int mkdirs(const char *path, char repl[][4096], size_t *nrepl) {
    char tmp[4096];
    size_t i, n = strlen(path);
    if (n >= sizeof tmp) return -1;
    memcpy(tmp, path, n + 1);
    for (i = 1; i < n; i++) {
        if (tmp[i] == '/') {
            tmp[i] = 0;
            int r = mkone(tmp, repl, nrepl);
            tmp[i] = '/';
            if (r) return -1;
        }
    }
    return mkone(tmp, repl, nrepl);
}
/* true if any strict parent-prefix of target was replaced */
static int under_replaced(const char *target, char repl[][4096],
                          size_t nrepl) {
    for (size_t i = 0; i < nrepl; i++) {
        size_t n = strlen(repl[i]);
        if (!strncmp(target, repl[i], n) && target[n] == '/') return 1;
    }
    return 0;
}
/* H-target PAT (A-027#2: an F under a replaced parent that is an H
 * LNK target fails SILENTLY — no pair, no count; the H pass draws
 * the pair-on-target + H diagnostic + trailer + N=1 instead) */
typedef struct { const unsigned char *raw; size_t len; } Hp;
static int is_htarget(Hp *hts, size_t nhts,
                      const unsigned char *raw, size_t len) {
    for (size_t i = 0; i < nhts; i++)
        if (hts[i].len == len && !memcmp(hts[i].raw, raw, len)) return 1;
    return 0;
}
/* one G9 modal child fail; rel = archive-rel PAT bytes (may be non-UTF8) */
typedef struct { char rel[4096]; int islink; } Cf;
static void rec_cf(Cf *cfs, size_t *ncfs, size_t cap,
                   const unsigned char *raw, size_t rawlen, int islink,
                   unsigned *fails, unsigned *sfails) {
    if (*ncfs < cap) {
        size_t rl = rawlen < sizeof cfs[0].rel - 1 ? rawlen :
                    sizeof cfs[0].rel - 1;
        memcpy(cfs[*ncfs].rel, raw, rl);
        cfs[*ncfs].rel[rl] = 0;
        cfs[*ncfs].islink = islink;
        (*ncfs)++;
    }
    (*fails)++; (*sfails)++;
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

static int extract(const Item *items, size_t nitems, const char *root,
                     int fcls, int fsub, size_t shortidx, int midchain,
                     int shortpresent, unsigned long long whole,
                     size_t shortend, unsigned long long obs, int mfkind) {
    char (*repl)[4096] = malloc(REPLC * sizeof *repl);
    size_t nrepl = 0;
    { /* root gated on scratch repl (a replaced root must not taint all) */
        char (*rr)[4096] = malloc(REPLC * sizeof *rr);
        size_t nr = 0;
        int ror = mkdirs(root, rr, &nr);
        free(rr);
        if (ror) { FAIL("mkdir %s\n", root); free(repl); return -1; }
    }
    /* deferred dir metadata (children bump dir mtime; apply last) */
    typedef struct { char path[4096]; size_t idx; int islink; } Rec;
    Rec *files = malloc(nitems * sizeof *files);
    Rec *dirs = malloc(nitems * sizeof *dirs);
    size_t nfiles = 0, ndirs = 0;
    size_t *scols = malloc(nitems * sizeof *scols);
    size_t nscols = 0;
    size_t *fsts = malloc(nitems * sizeof *fsts);
    size_t nfsts = 0;
    Rec *eis = malloc(nitems * sizeof *eis);
    size_t neis = 0;
    /* HLC group -> first member path (hardlink restore) */
    typedef struct { unsigned long long grp; char path[4096]; } Hlc;
    Hlc *hlcs = malloc(nitems * sizeof *hlcs);
    size_t nhlcs = 0;
    typedef struct { char path[4096]; size_t idx; } Hln;
    Hln *hlns = malloc(nitems * sizeof *hlns);
    size_t nhlns = 0;
    /* G9 modal child fails (Cf array); archive-order flush post phase-1 */
    size_t cfcap = nitems ? nitems : 1;
    Cf *cfs = malloc(cfcap * sizeof *cfs);
    size_t ncfs = 0;
    /* H-target PATs pre-scanned (A-027#2 silence rule) */
    Hp *hts = malloc(cfcap * sizeof *hts);
    size_t nhts = 0;
    for (size_t k = 0; k < nitems; k++) {
        const Entry *tt = find_ent(&items[k], "TYP");
        const Entry *ll = find_ent(&items[k], "LNK");
        if (tt && tt->num == 'H' && ll && ll->st == 'P' && ll->rawlen) {
            hts[nhts].raw = ll->raw; hts[nhts].len = ll->rawlen; nhts++;
        }
    }
    unsigned fails = 0, sfails = 0;
    int hdr = 0, dirfail = 0, aborted = 0, shortstop = 0;
    /* phase 1: create everything, forward. aborts stop creation only. */
    for (size_t k = 0; k < nitems && !aborted && !shortstop; k++) {
        const Item *it = &items[k];
        const Entry *t = find_ent(it, "TYP"), *p = find_ent(it, "PAT");
        /* oracle requires TYP on EVERY item (case175, notyp probes) */
        if (!t) {
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xbd03ac00\n"
                    "Invalid entry: no TYP field\n"
                    "archive stream read error (header)\n"
                    "stream cancelled\n");
            fails++; hdr = 1; aborted = 1; break;
        }
        if (t->st != '1' && t->st != '2' && t->st != '4' && t->st != '8') {
            int tn = -1;
            switch (t->st) {
            case 'P': tn = 2; break;
            case 'S': case 'T': tn = 4; break;
            case '*': tn = 0; break;
            case 'F': case 'G': case 'H': case 'I': case 'J':
                tn = 3; break; /* hash family (H probed) */
            case 'A': case 'B': case 'C': tn = 5; break; /* CR-053 */
            default: break; /* blob: content-fragile, internal line */
            }
            if (tn >= 0) {
                fprintf(stderr, "Extraction failed\n"
                        "extract failedError 0xe509b400\n"
                        "invalid type %d, expected UINT\n"
                        "Invalid entry: no TYP field\n"
                        "archive stream read error (header)\n"
                        "stream cancelled\n", tn);
            } else {
                FAIL("TYP non-uint subtype 0x%02x\n", t->st);
            }
            fails++; hdr = 1; aborted = 1; break;
        }
        if (!p || p->st != 'P') continue; /* no PAT key: skip */
        if (!p->rawlen) {
            /* PAT-empty: D=root meta target; F=EISDIR counted; else skip */
            if (t->num == 'D') {
                memcpy(dirs[ndirs].path, root, strlen(root) + 1);
                dirs[ndirs].idx = k; dirs[ndirs].islink = 0; ndirs++;
            } else if (t->num == 'F') {
                memcpy(eis[neis].path, root, strlen(root) + 1);
                eis[neis].idx = k; eis[neis].islink = 0; neis++;
                fails++; sfails++;
            }
            continue;
        }
        char target[4096];
        if (safe_join(root, p->raw, p->rawlen, target)) {
            FAIL("bad path\n"); fails++; hdr = 1; aborted = 1; break;
        }
        if (midchain && shortidx == (size_t)-1 && nitems > 0 &&
            k == nitems - 1)
            continue; /* midchain clean parse: last item dropped (E4) */
        /* DAT-complete short files take the normal path (unclo FULL). */
        int shortfull = 0;
        if (k == shortidx && !midchain && t->num == 'F') {
            size_t sdl = 0;
            const unsigned char *sdd = blob_for(it, "DAT", &sdl);
            if (!sdd) { fsts[nfsts++] = k; fails++; continue; }
            size_t sdoff = (size_t)(sdd - it->blobs);
            size_t sdav = sdoff <= it->bloblen ? it->bloblen - sdoff : 0;
            if (sdav >= sdl)
                shortfull = 1; /* DAT-complete: normal F path (FULL) */
            /* else DAT-short: unified presence+content below (PRE-007) */
        }
        if (k == shortidx && !shortfull) {
            if (t->num == 'F') {
                /* unified presence+content (midchain + clean PRE-007):
                 * whole/kcut = (mf / innerlen,nblocks) per path. */
                /* unified short file (midchain + clean PRE-007):
                 * absent unless present-rule or DAT-complete; FULL
                 * DAT if complete else 256K chunks; want-0 absent. */
                size_t dl = 0;
                const unsigned char *dd = blob_for(it, "DAT", &dl);
                size_t doff = 0, dav = 0;
                if (dd) {
                    doff = (size_t)(dd - it->blobs);
                    dav = doff <= it->bloblen ? it->bloblen - doff : 0;
                }
                int datcomplete = dd && dav >= dl;
                unsigned long long nch = whole >= 786432 ?
                    (whole - 786432) / 262144 + 1 : 0;
                if (!shortpresent && !datcomplete &&
                    (nch < 1 || shortend / 262144ULL > nch))
                    break; /* absent (A-028 LONG-only: create iff
                            * nch>=1 && floor(end/256K) <= nch; SHORT
                            * nch-0 never creates below-gate: po/uc/
                            * mc2-class 20+ absent legs). */
                unsigned long long hch = 0;
                for (unsigned long long j = 0; j < nch; j++) {
                    if (shortend + 0ULL <= (nch - j) * 262144ULL) hch++;
                    else break;
                }
                /* M2-dev (NOTE-060, verified 10/10): truncpay LONG
                 * (nch>=2, !datcomplete): held -= dev; big
                 * (bsize>=192K): dev = nch/2-1; small: dev =
                 * (nch>=4). Trunchdr: held capped at 2ch. w3
                 * (n>=10) + frac + tr6-creation stay OPEN. */
                if (midchain && !datcomplete && nch >= 2 &&
                    mfkind == MF_TRUNCPAY) {
                    unsigned long long dev = obs >= 196608ULL ?
                        nch / 2 - 1 : (nch >= 4 ? 1 : 0);
                    if (dev > hch) dev = hch;
                    hch -= dev;
                } else if (midchain && !datcomplete &&
                           mfkind == MF_TRUNCHDR) {
                    /* TIP2e prefix-scaled cap: 1ch/2ch/4ch per
                     * whole 1M/2M/3M (m2th locks; 128k-HDR
                     * refutes kcut-form; whole>=4M doubling
                     * extrapolated, DPROBE-15). */
                    unsigned long long w1m = whole / 1048576ULL;
                    unsigned sh = w1m > 31 ? 30 : w1m ?
                        (unsigned)(w1m - 1) : 0;
                    unsigned long long cap = w1m ? (1ULL << sh) : 1ULL;
                    if (hch > cap)
                        hch = cap;
                }
                unsigned long long want = hch * 262144ULL;
                size_t wlen = datcomplete ? dl :
                    (want < dav ? (size_t)want : dav);
                if (!datcomplete && wlen == 0 && !midchain &&
                    (shortpresent || shortend / 262144ULL > nch))
                    break; /* clean want-0: absent (v512b1), EXCEPT
                            * below-gate A-028-EMPTY (n6c) which falls
                            * through. Midchain want-0: EMPTY (cxA/E/F,
                            * tr6-class via A-028). */
                char *sl = strrchr(target, '/');
                if (sl) {
                    *sl = 0;
                    if (mkdirs(target, repl, &nrepl)) {
                        FAIL("mkdir %s\n", target);
                        fails++; hdr = 1; aborted = 1; break;
                    }
                    *sl = '/';
                }
                if (under_replaced(target, repl, nrepl)) {
                    if (is_htarget(hts, nhts, p->raw, p->rawlen))
                        break; /* H-target F: silent (A-027#2) */
                    rec_cf(cfs, &ncfs, cfcap, p->raw, p->rawlen, 0,
                           &fails, &sfails);
                    break; /* short rest skipped */
                }
                FILE *f = fopen(target, "wb");
                if (!f) {
                    if (errno == EISDIR) {
                        memcpy(eis[neis].path, target, strlen(target) + 1);
                        eis[neis].idx = k; eis[neis].islink = 0; neis++;
                        fails++; sfails++; break;
                    }
                    FAIL("open %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                if (dd && wlen && fwrite(dd, 1, wlen, f) != wlen) {
                    FAIL("write %s\n", target);
                    fclose(f);
                    fails++; hdr = 1; aborted = 1; break;
                }
                fclose(f);
                memcpy(files[nfiles].path, target, strlen(target) + 1);
                files[nfiles].idx = k; files[nfiles].islink = 0; nfiles++;
                break; /* rest skipped */
            } else {
                shortstop = 1;
            }
        }
        if (t->num == 'D') {
            char *sl0 = strrchr(target, '/');
            if (sl0) {
                *sl0 = 0;
                int mdr = mkdirs(target, repl, &nrepl);
                *sl0 = '/';
                if (mdr) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
            }
            if (under_replaced(target, repl, nrepl)) {
                /* D-under-replaced: same modal rule (hypothesis) */
                rec_cf(cfs, &ncfs, cfcap, p->raw, p->rawlen, 0,
                       &fails, &sfails);
                continue;
            }
            struct stat dst;
            if (!lstat(target, &dst) && !S_ISDIR(dst.st_mode)) {
                /* G9: non-dir occupant -> unlink + replace 0755
                 * (silent; D MOD applies via phase 3). G6 keeps
                 * real-dir occupants only (below, unchanged). */
                if (unlink(target) || mkdir(target, 0755)) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                repl_add(repl, &nrepl, target);
            } else if (lstat(target, &dst)) {
                if (mkdir(target, 0755) && errno != EEXIST) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
            }
            memcpy(dirs[ndirs].path, target, strlen(target) + 1);
            dirs[ndirs].idx = k; dirs[ndirs].islink = 0; ndirs++;
        } else if (t->num == 'F') {
            char *sl = strrchr(target, '/');
            if (sl) {
                *sl = 0;
                if (mkdirs(target, repl, &nrepl)) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                *sl = '/';
            }
            if (under_replaced(target, repl, nrepl)) {
                if (is_htarget(hts, nhts, p->raw, p->rawlen))
                    continue; /* H-target F: silent (A-027#2) */
                rec_cf(cfs, &ncfs, cfcap, p->raw, p->rawlen, 0,
                       &fails, &sfails);
                continue;
            }
            const Entry *h = find_ent(it, "HLC");
            const char *first = NULL;
            if (h)
                for (size_t i = 0; i < nhlcs; i++)
                    if (hlcs[i].grp == h->num) { first = hlcs[i].path; break; }
            if (first) {
                unlink(target);
                if (link(first, target)) {
                    FAIL("link %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
            } else {
                size_t dl = 0;
                const unsigned char *dd = blob_for(it, "DAT", &dl);
                if (!dd) {
                    fsts[nfsts++] = k; /* flushed fwd after S-flush */
                    fails++; continue;
                }
                struct stat fst;
                if (!lstat(target, &fst) && S_ISLNK(fst.st_mode))
                    unlink(target); /* G3: symlink occupant silent-replace */
                FILE *f = fopen(target, "wb");
                if (!f) {
                    if (errno == EISDIR) {
                        memcpy(eis[neis].path, target, strlen(target) + 1);
                        eis[neis].idx = k; eis[neis].islink = 0; neis++;
                        fails++; sfails++; continue;
                    }
                    FAIL("open %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                if (dl && fwrite(dd, 1, dl, f) != dl) {
                    fclose(f); FAIL("write %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                fclose(f);
                if (h) {
                    hlcs[nhlcs].grp = h->num;
                    memcpy(hlcs[nhlcs].path, target, strlen(target) + 1);
                    nhlcs++;
                }
            }
            memcpy(files[nfiles].path, target, strlen(target) + 1);
            files[nfiles].idx = k; files[nfiles].islink = 0; nfiles++;
        } else if (t->num == 'L') {
            const Entry *l = find_ent(it, "LNK");
            if (!l || l->st != 'P') {
                fprintf(stderr, "YAA link entry has no LNK field: %.*s\n",
                        (int)p->rawlen, p->raw);
                fails++; hdr = 1; aborted = 1; break;
            }
            char *sl = strrchr(target, '/');
            if (sl) {
                *sl = 0;
                if (mkdirs(target, repl, &nrepl)) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                *sl = '/';
            }
            if (under_replaced(target, repl, nrepl)) {
                rec_cf(cfs, &ncfs, cfcap, p->raw, p->rawlen, 1,
                       &fails, &sfails);
                continue;
            }
            char lbuf[4096];
            if (l->rawlen >= sizeof lbuf) {
                FAIL("link target too long\n");
                fails++; hdr = 1; aborted = 1; break;
            }
            memcpy(lbuf, l->raw, l->rawlen); lbuf[l->rawlen] = 0;
            unlink(target);
            if (symlink(lbuf, target)) {
                FAIL("symlink %s\n", target);
                fails++; hdr = 1; aborted = 1; break;
            }
            memcpy(files[nfiles].path, target, strlen(target) + 1);
            files[nfiles].idx = k; files[nfiles].islink = 1; nfiles++;
        } else if (t->num == 'H') {
            const Entry *l = find_ent(it, "LNK");
            if (!l || l->st != 'P') {
                fprintf(stderr, "YAA link entry has no LNK field: %.*s\n",
                        (int)p->rawlen, p->raw);
                fails++; hdr = 1; aborted = 1; break;
            }
            memcpy(hlns[nhlns].path, target, strlen(target) + 1);
            hlns[nhlns++].idx = k;
        } else if (t->num == 'P') {
            char *sl = strrchr(target, '/');
            if (sl) {
                *sl = 0;
                if (mkdirs(target, repl, &nrepl)) {
                    FAIL("mkdir %s\n", target);
                    fails++; hdr = 1; aborted = 1; break;
                }
                *sl = '/';
            }
            if (under_replaced(target, repl, nrepl)) {
                /* P-under-replaced: triple (A-027#1, non-F rule) */
                rec_cf(cfs, &ncfs, cfcap, p->raw, p->rawlen, 1,
                       &fails, &sfails);
                continue;
            }
            unlink(target);
            if (mkfifo(target, 0600)) {
                FAIL("mkfifo %s\n", target);
                fails++; hdr = 1; aborted = 1; break;
            }
            memcpy(files[nfiles].path, target, strlen(target) + 1);
            files[nfiles].idx = k; files[nfiles].islink = 0; nfiles++;
        } else if (t->num == 'S') {
            scols[nscols++] = k; /* flushed forward after files-meta */
            fails++; sfails++;
        } else if (t->num == 'B' || t->num == 'C') {
            if (!find_ent(it, "DEV")) {
                fprintf(stderr, "YAA device entry has no DEV field: %.*s\n",
                        (int)p->rawlen, p->raw);
                fails++; hdr = 1; aborted = 1; break;
            }
            scols[nscols++] = k;
            fails++; sfails++;
        } else {
            /* unknown TYP: silent skip (oracle parity, measured) */
        }
    }
    /* G9 modal child-fail flush, archive order (A-026#5: emit fixed
     * archive order; oracle order races, batteries SET-pin). */
    for (size_t i = 0; i < ncfs; i++) {
        print_hdr(&hdr, 0x83058800);
        fprintf(stderr, "a parent of path is not a directory: %s\n"
                "invalid path: %s\n", cfs[i].rel, cfs[i].rel);
        if (cfs[i].islink)
            fprintf(stderr, "creating fs object: %s\n", cfs[i].rel);
    }
    /* parse-fail wrapper (after phase 1, before meta; suppressed on abort:
     * a cancelled stream never reaches the later failure) */
    if (fcls && !aborted && !midchain) {
        fails++;
        hdr = 1;
        switch (fcls) {
        case PF_TAIL:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xbd011800\n"
                    "No more data\nread error\ntruncated stream\n"
                    "archive stream read error (header)\nstream cancelled\n");
            break;
        case PF_BADMAGIC:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xe501e800\n"
                    "invalid header magic\ncorrupted archive header\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n");
            break;
        case PF_HDRCUT: case PF_ENDMISMATCH:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xe5022800\n"
                    "truncated header\ncorrupted archive header\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n");
            break;
        case PF_VALUEOVERRUN:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xe502a400\n"
                    "truncated header\ncorrupted archive header\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n");
            break;
        case PF_BADSUBTYPE:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xe5029c00\n"
                    "invalid field subtype: %d\ncorrupted archive header\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n",
                    fsub);
            break;
        case PF_HSIZEMISMATCH:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xe501f000\n"
                    "header size mismatch: stored %d, got 6\n"
                    "corrupted archive header\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n",
                    fsub);
            break;
        case PF_HDRTAIL:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xbd011800\n"
                    "No more data\nread error\ntruncated stream\n"
                    "parsing entry header\n"
                    "archive stream read error (header)\nstream cancelled\n");
            break;
        case PF_STREAMMAGIC:
            emit_nonsupp();
            break;
        case PF_BLOBOVERRUN:
            fprintf(stderr, "Extraction failed\n"
                    "extract failedError 0xbd011800\n"
                    "No more data\nread error\n"
                    "archive stream read error (blob)\nstream cancelled\n");
            sfails++;
            break;
        }
    }
    /* M1 tails: emitted in main (midchain path only), never here:
     * modal x2 unless short-whole or trunchdr-kcut1 (TIP2e). */
    /* phase 2: files meta, strict reverse (bad2, Q1 re-probe) */
    for (size_t i = nfiles; i-- > 0;) {
        const Item *it = &items[files[i].idx];
        if (files[i].idx == shortidx) {
            apply_rest(files[i].path, it, files[i].islink); /* XAT cut */
            continue;
        }
        if (apply_xattr_only(files[i].path, it, files[i].islink)) {
            const Entry *p = find_ent(it, "PAT");
            print_hdr(&hdr, 0xe8012000);
            fprintf(stderr, "invalid XAT blob\ninvalid XAT blob\n");
            fprintf(stderr, "applyEntryAttributes failed: %.*s\n",
                    (int)p->rawlen, p->raw);
            fails++; sfails++;
        } else {
            apply_rest(files[i].path, it, files[i].islink);
        }
    }
    /* S-flush, forward (S2; after files-meta per E4/E5) */
    for (size_t i = 0; i < nscols; i++) {
        const Entry *p = find_ent(&items[scols[i]], "PAT");
        print_hdr(&hdr, 0xc8055000);
        fprintf(stderr, "not implemented yet\ncreating fs object: %.*s\n",
                (int)p->rawlen, p->raw);
    }
    /* EISDIR flush, forward (es/ne: after S-flush, before nodat) */
    for (size_t i = 0; i < neis; i++) eisdir_err(&hdr, eis[i].path);
    /* F-no-DAT flush, forward (nh2: after EISDIR-flush, before H-pass) */
    for (size_t i = 0; i < nfsts; i++) {
        const Entry *p = find_ent(&items[fsts[i]], "PAT");
        print_hdr(&hdr, 0xc8039000);
        fprintf(stderr, "invalid entry final state 0: %.*s\n",
                (int)p->rawlen, p->raw);
    }
    /* H pass (runs even on abort per HAB; trailer iff failure) */
    {
        int hfailed = 0;
        for (size_t i = 0; i < nhlns; i++) {
            const Entry *l = find_ent(&items[hlns[i].idx], "LNK");
            char src[4096];
            if (safe_join(root, l->raw, l->rawlen, src)) {
                print_hdr(&hdr, 0xc8104800);
                fprintf(stderr, "invalid path: %.*s\ninvalid 'H' LNK\n",
                        (int)l->rawlen, l->raw);
                fails++; hfailed = 1; continue;
            }
            struct stat sb;
            if (lstat(src, &sb) || !S_ISREG(sb.st_mode)) {
                if (under_replaced(src, repl, nrepl)) {
                    /* H TARGET-side (A-027#2): 83058800 pair on
                     * the TARGET + H diagnostic + trailer + N=1 */
                    print_hdr(&hdr, 0x83058800);
                    fprintf(stderr, "a parent of path is not a "
                            "directory: %.*s\ninvalid path: %.*s\n",
                            (int)l->rawlen, l->raw,
                            (int)l->rawlen, l->raw);
                    fprintf(stderr, "'H' LNK not a regular file: "
                            "%.*s\n", (int)l->rawlen, l->raw);
                    fails++; sfails++; hfailed = 1; continue;
                }
                print_hdr(&hdr, 0xc8104800);
                fprintf(stderr, "'H' LNK not a regular file: %.*s\n",
                        (int)l->rawlen, l->raw);
                fails++; hfailed = 1; continue;
            }
            char *sl = strrchr(hlns[i].path, '/');
            if (sl) {
                *sl = 0;
                int merr = mkdirs(hlns[i].path, repl, &nrepl);
                *sl = '/';
                if (merr) {
                    print_hdr(&hdr, 0xc8104800);
                    FAIL("mkdir for link\n");
                    fails++; hfailed = 1; continue;
                }
            }
            if (under_replaced(hlns[i].path, repl, nrepl)) {
                /* H PATH-side: inline pair (hypothesis; A-027#2
                 * covers target-side only) */
                const Entry *hp =
                    find_ent(&items[hlns[i].idx], "PAT");
                print_hdr(&hdr, 0x83058800);
                fprintf(stderr, "a parent of path is not a directory: "
                        "%.*s\ninvalid path: %.*s\n",
                        (int)hp->rawlen, hp->raw,
                        (int)hp->rawlen, hp->raw);
                fails++; sfails++; hfailed = 1; continue;
            }
            unlink(hlns[i].path);
            if (link(src, hlns[i].path)) {
                print_hdr(&hdr, 0xc8104800);
                FAIL("link %s\n", hlns[i].path);
                fails++; hfailed = 1; continue;
            }
        }
        if (hfailed) fprintf(stderr, "process hlinks\n");
    }
    /* phase 3: dirs meta, reverse (children-first); root=outdir in place */
    for (size_t i = ndirs; i-- > 0;) {
        const Item *it = &items[dirs[i].idx];
        if (dirs[i].idx == shortidx) {
            apply_rest(dirs[i].path, it, 0); /* XAT cut */
            continue;
        }
        if (apply_xattr_only(dirs[i].path, it, 0)) {
            print_hdr(&hdr, 0xe8012000);
            fprintf(stderr, "invalid XAT blob\ninvalid XAT blob\n");
            fprintf(stderr, "applyEntryAttributes failed\n");
            fails++; dirfail = 1;
        } else {
            apply_rest(dirs[i].path, it, 0);
        }
    }
    if (dirfail) fprintf(stderr, "process dirs\n");
    if (sfails && !midchain)
        fprintf(stderr, "%u entries failed to extract\n", sfails);
    free(files);
    free(dirs);
    free(scols);
    free(fsts);
    free(eis);
    free(hlcs);
    free(hlns);
    free(repl);
    free(cfs);
    free(hts);
    return fails ? 1 : 0;
}

int main(int argc, char **argv) {
    if (argc != 3) { fprintf(stderr, "usage: aad IN.aar OUTDIR\n"); return 2; }
    Buf file = { NULL, 0 }, inner = { NULL, 0 };
    Item *items = NULL;
    size_t nitems = 0, shortidx = (size_t)-1, shortavail = 0, shortend = 0;
    MidFail mf;
    memset(&mf, 0, sizeof mf);
    size_t nblocks = 1;
    unsigned long long obs = 0;
    int rc = 1;
    if (read_file(argv[1], &file)) goto out;
    int cr = parse_chain(&file, &inner, &mf, &nblocks, &obs);
    if (cr < 0) goto out;
    int fcls = 0, fsub = 0;
    if (parse_inner(&inner, &items, &nitems, &fcls, &fsub, &shortidx,
                    &shortavail, &shortend))
        goto out;
    if (cr > 0) {
        /* midchain (blob) path: extract prefix, then cascade + count. */
        int present = shortidx != (size_t)-1 && mf.whole >= 524288 &&
                      shortavail + 0ULL >= (mf.kcut > 0 ? mf.kcut - 1 : 0) *
                      65536ULL;
        extract(items, nitems, argv[2], fcls, fsub, shortidx, 1, present,
                mf.whole, shortend, obs, mf.kind);
        emit_midblob(&mf, &file);
        /* TIP2e M1: modal x2 tails, except short-whole (<512K:
         * mc2/mc3 x0) and trunchdr-kcut1 (m2th1 x0-locked). */
        if (mf.whole >= 524288ULL &&
            !(mf.kind == MF_TRUNCHDR && mf.kcut == 1))
            fprintf(stderr, "reading payload\nreading payload\n");
        fprintf(stderr, "1 entries failed to extract\n");
        fails = 1;
        goto out;
    }
    /* clean path: presence gate on (innerlen, nblocks) (PRE-007). */
    {
        int present = shortidx != (size_t)-1 && inner.len >= 524288 &&
                      shortavail + 0ULL >= (nblocks > 0 ? nblocks - 1 : 0) *
                      65536ULL;
        if (extract(items, nitems, argv[2], fcls, fsub, shortidx, 0, present,
                    (unsigned long long)inner.len, shortend, obs, -1))
            goto out;
    }
    rc = 0;
out:
    free(file.data); free(inner.data);
    if (items) for (size_t i = 0; i < nitems; i++) free(items[i].ents);
    free(items);
    return fails ? 1 : rc;
}
