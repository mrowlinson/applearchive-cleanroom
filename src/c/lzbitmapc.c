/* lzbitmapc.c -- literal-class ZBM encoder. C port of ../lzbitmap.py.
 * Derived black-box from /usr/bin/aa I/O only. */
#include "lzbitmapc.h"
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define K4 16
#define K3 20
#define K2 32
#define DP_M 4
#define DP_C 2
#define DP_SAV 32
#define SPAN_K 4
#define SPAN_W 64
#define MDIST 8
#define HM1_T 28.0

/* ---- open-addressing gram map (counts + sliding 4-window + tight) ---- */

typedef struct {
    uint32_t key;
    uint32_t count;
    uint32_t pos[4];
    uint8_t npc;
    uint8_t tight;
    uint8_t used;
} ge;

typedef struct {
    ge *t;
    size_t mask;
} gmap;

static uint32_t ghash(uint32_t k) {
    k ^= k >> 16;
    k *= 0x7feb352du;
    k ^= k >> 15;
    return k;
}

static void ginit(gmap *g, int bits) {
    g->t = calloc((size_t)1 << bits, sizeof(ge));
    if (!g->t) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    g->mask = ((size_t)1 << bits) - 1;
}

static ge *gget(gmap *g, uint32_t key) {
    size_t h = ghash(key) & g->mask;
    for (;;) {
        ge *e = &g->t[h];
        if (!e->used) {
            e->used = 1;
            e->key = key;
            return e;
        }
        if (e->key == key) return e;
        h = (h + 1) & g->mask;
    }
}

static void gfree(gmap *g) { free(g->t); }

/* G1+G3 single pass over window (early exit on first breach).
 * Check order per i mirrors the Python exactly: 4gram count,
 * 3gram count, 3gram span, 2gram count, 2gram span. */
static int g13_pass(const uint8_t *W, size_t m, long s,
                    char *reason, size_t rcap) {
    gmap m4, m3;
    ginit(&m4, 18);
    ginit(&m3, 18);
    ge *a2 = calloc(65536, sizeof(ge)); /* direct 2-gram table */
    if (!a2) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    int ndist = 0;
    int rc = 0;
    for (size_t i = 0; i < m && !rc; i++) {
        if (i + 4 <= m) {
            uint32_t g = (uint32_t)W[i] | ((uint32_t)W[i + 1] << 8) |
                          ((uint32_t)W[i + 2] << 16) | ((uint32_t)W[i + 3] << 24);
            ge *e = gget(&m4, g);
            uint32_t k = ++e->count;
            if (k >= K4) {
                snprintf(reason, rcap, "4gram-x%u window@%ld", k, s);
                rc = 1;
                break;
            }
        }
        if (i + 3 <= m) {
            uint32_t g = (uint32_t)W[i] | ((uint32_t)W[i + 1] << 8) |
                         ((uint32_t)W[i + 2] << 16);
            ge *e = gget(&m3, g);
            uint32_t k = ++e->count;
            if (k >= K3) {
                snprintf(reason, rcap, "3gram-x%u window@%ld", k, s);
                rc = 1;
                break;
            }
            e->pos[e->npc++] = (uint32_t)i;
            if (e->npc == SPAN_K) {
                if (i - e->pos[0] <= SPAN_W && !e->tight) {
                    e->tight = 1;
                    if (++ndist >= MDIST) {
                        snprintf(reason, rcap, "mdist window@%ld", s);
                        rc = 1;
                        break;
                    }
                }
                e->pos[0] = e->pos[1];
                e->pos[1] = e->pos[2];
                e->pos[2] = e->pos[3];
                e->npc = 3;
            }
        }
        if (i + 1 < m) {
            uint32_t g = (uint32_t)W[i] | ((uint32_t)W[i + 1] << 8);
            ge *e = &a2[g];
            uint32_t k = ++e->count;
            if (k >= K2) {
                snprintf(reason, rcap, "2gram-x%u window@%ld", k, s);
                rc = 1;
                break;
            }
            e->pos[e->npc++] = (uint32_t)i;
            if (e->npc == SPAN_K) {
                if (i - e->pos[0] <= SPAN_W && !e->tight) {
                    e->tight = 1;
                    if (++ndist >= MDIST) {
                        snprintf(reason, rcap, "mdist window@%ld", s);
                        rc = 1;
                        break;
                    }
                }
                e->pos[0] = e->pos[1];
                e->pos[1] = e->pos[2];
                e->pos[2] = e->pos[3];
                e->npc = 3;
            }
        }
    }
    gfree(&m4);
    gfree(&m3);
    free(a2);
    return rc;
}

/* ---- G2 relaxed-DP LZ savings ---- */

/* longest common prefix of W[a:], W[b:] capped at cap */
static size_t glcp(const uint8_t *W, size_t m, size_t a, size_t b,
                   size_t cap) {
    size_t mx = a > b ? a : b;
    size_t ml = m - mx;
    if (cap > ml) cap = ml;
    size_t l = 0;
    while (l < cap && W[a + l] == W[b + l]) l++;
    return l;
}

/* min-heap of (value, expiry) */
static void hpush(int64_t *hv, int64_t *he, size_t *hn, int64_t v,
                  int64_t x) {
    size_t i = (*hn)++;
    hv[i] = v;
    he[i] = x;
    while (i > 0) {
        size_t p = (i - 1) / 2;
        if (hv[p] <= hv[i]) break;
        int64_t t = hv[p];
        hv[p] = hv[i];
        hv[i] = t;
        t = he[p];
        he[p] = he[i];
        he[i] = t;
        i = p;
    }
}

static void hpop(int64_t *hv, int64_t *he, size_t *hn) {
    size_t n = --(*hn);
    hv[0] = hv[n];
    he[0] = he[n];
    for (size_t i = 0;;) {
        size_t l = 2 * i + 1, r = l + 1, s = i;
        if (l < n && hv[l] < hv[s]) s = l;
        if (r < n && hv[r] < hv[s]) s = r;
        if (s == i) break;
        int64_t t = hv[s];
        hv[s] = hv[i];
        hv[i] = t;
        t = he[s];
        he[s] = he[i];
        he[i] = t;
        i = s;
    }
}

/* relaxed optimal-parse LZ savings over W (matches len>=DP_M at cost
 * DP_C). Returns savings; DP_SAV on the single-match instant-refuse. */
static long dp_savings(const uint8_t *W, size_t m) {
    if (m < (size_t)(DP_M + 1)) return 0;
    /* pass 1: 4-gram counts */
    gmap mc;
    ginit(&mc, 18);
    int rep4 = 0;
    for (size_t i = 0; i + 4 <= m; i++) {
        uint32_t g = (uint32_t)W[i] | ((uint32_t)W[i + 1] << 8) |
                     ((uint32_t)W[i + 2] << 16) | ((uint32_t)W[i + 3] << 24);
        ge *e = gget(&mc, g);
        if (++e->count == 2) rep4 = 1;
    }
    if (!rep4) {
        gfree(&mc);
        return 0;
    }
    /* prefix pass: flat position array */
    size_t ncap = (size_t)1 << 18;
    uint32_t *flat = malloc(m * sizeof *flat);
    int64_t *f = malloc((m + 1) * sizeof *f);
    int64_t *ss = malloc((m + 1) * sizeof *ss);
    int64_t *sv = malloc((m + 1) * sizeof *sv);
    int64_t *se = malloc((m + 1) * sizeof *se);
    int64_t *hv = malloc((m + 2) * sizeof *hv);
    int64_t *he = malloc((m + 2) * sizeof *he);
    if (!flat || !f || !ss || !sv || !se || !hv || !he) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    for (size_t h = 0; h < ncap; h++) {
        ge *e = &mc.t[h];
        if (!e->used) continue;
        e->npc = 0;
        e->pos[0] = e->pos[1] = 0; /* reuse pos[0..1] as (start, fill) */
        e->tight = 0;
    }
    uint32_t next = 0;
    for (size_t h = 0; h < ncap; h++) {
        ge *e = &mc.t[h];
        if (!e->used) continue;
        e->pos[0] = next;
        e->pos[1] = 0;
        next += e->count;
    }
    for (size_t i = 0; i + 4 <= m; i++) {
        uint32_t g = (uint32_t)W[i] | ((uint32_t)W[i + 1] << 8) |
                     ((uint32_t)W[i + 2] << 16) | ((uint32_t)W[i + 3] << 24);
        ge *e = gget(&mc, g);
        flat[e->pos[0] + e->pos[1]++] = (uint32_t)i;
    }
    const int64_t INF = (int64_t)1 << 60;
    for (size_t j = 0; j <= m; j++) f[j] = INF;
    f[0] = 0;
    size_t nst = 0, si = 0, hn = 0;
    long ret = 0;
    for (size_t j = 0; j <= m; j++) {
        while (si < nst && (size_t)ss[si] <= j) {
            hpush(hv, he, &hn, sv[si], se[si]);
            si++;
        }
        while (hn > 0 && he[0] < (int64_t)j) hpop(hv, he, &hn);
        if (hn > 0 && hv[0] < f[j]) f[j] = hv[0];
        if (j >= m) break;
        if (f[j] + 1 < f[j + 1]) f[j + 1] = f[j] + 1;
        if (j + DP_M > m) continue;
        uint32_t g = (uint32_t)W[j] | ((uint32_t)W[j + 1] << 8) |
                     ((uint32_t)W[j + 2] << 16) | ((uint32_t)W[j + 3] << 24);
        /* lookup without inserting */
        size_t h = ghash(g) & mc.mask;
        ge *e = NULL;
        for (;;) {
            ge *c = &mc.t[h];
            if (!c->used) break;
            if (c->key == g) {
                e = c;
                break;
            }
            h = (h + 1) & mc.mask;
        }
        if (!e) continue;
        size_t lm = 0;
        for (uint32_t k = 0; k < e->count; k++) {
            size_t o = flat[e->pos[0] + k];
            if (o == j) continue;
            size_t l = glcp(W, m, j, o, m - j);
            if (l >= 34) {
                ret = DP_SAV;
                goto done;
            }
            if (l > lm) lm = l;
            if (lm >= m - j) break;
        }
        if (lm >= (size_t)DP_M) {
            ss[nst] = (int64_t)(j + DP_M);
            sv[nst] = f[j] + DP_C;
            se[nst] = (int64_t)(j + lm);
            nst++;
        }
    }
    ret = (long)(m - (size_t)f[m]);
done:
    gfree(&mc);
    free(flat);
    free(f);
    free(ss);
    free(sv);
    free(se);
    free(hv);
    free(he);
    return ret;
}

int lzbitmap_refuse(const uint8_t *d, size_t n, char *reason, size_t rcap) {
    for (size_t s = 0; s < n; s += ZBM_CHUNK) {
        size_t clen = n - s > ZBM_CHUNK ? ZBM_CHUNK : n - s;
        const uint8_t *c = d + s;
        /* G4: sparse order-0 single-hot mass (chunk-local) */
        if (clen > 0) {
            size_t hist[256] = {0};
            for (size_t i = 0; i < clen; i++) hist[c[i]]++;
            size_t v = 0;
            for (int b = 0; b < 256; b++)
                if (hist[b] > v) v = hist[b];
            double hm =
                (double)v * (8.0 + log2((double)v / (double)clen)) / 8.0 - 3.0;
            if (hm >= HM1_T) {
                snprintf(reason, rcap, "order0-hot1 chunk@%ld mass=%.1f",
                         (long)s, hm);
                return 1;
            }
        }
        size_t h0 = s > ZBM_WIN ? s - ZBM_WIN : 0;
        const uint8_t *W = d + h0;
        size_t m = s + clen - h0;
        if (m < 2) continue;
        /* G1+G3 */
        if (g13_pass(W, m, (long)s, reason, rcap)) return 1;
        /* G2 */
        if (dp_savings(W, m) >= DP_SAV) {
            snprintf(reason, rcap, "lz-savings window@%ld", (long)s);
            return 1;
        }
    }
    return 0;
}

static void u16le(uint8_t *p, unsigned v) {
    p[0] = (uint8_t)v;
    p[1] = (uint8_t)(v >> 8);
}

static void be32(uint8_t **pp, uint32_t v) {
    uint8_t *p = *pp;
    p[0] = (uint8_t)(v >> 24);
    p[1] = (uint8_t)(v >> 16);
    p[2] = (uint8_t)(v >> 8);
    p[3] = (uint8_t)v;
    *pp = p + 4;
}

static const uint8_t kTrailer[6] = {0x06, 0x00, 0x00, 0x00, 0x00, 0x00};

uint8_t *zbm_encode_literal(const uint8_t *d, size_t n, size_t *on,
                            char *err, size_t errcap) {
    char rsn[256];
    if (lzbitmap_refuse(d, n, rsn, sizeof rsn)) {
        snprintf(err, errcap, "%s", rsn);
        return NULL;
    }
    uint8_t *o;
    if (n == 0) {
        o = malloc(10);
        if (!o) {
            fprintf(stderr, "lzbitmap: out of memory\n");
            exit(1);
        }
        memcpy(o, "ZBM\x09", 4);
        u16le(o + 4, 6);
        o[6] = 0x00;
        u16le(o + 7, 0);
        o[9] = 0x00;
        *on = 10;
        return o;
    }
    if (n <= ZBM_CHUNK) {
        o = malloc(16 + n);
        if (!o) {
            fprintf(stderr, "lzbitmap: out of memory\n");
            exit(1);
        }
        memcpy(o, "ZBM\x09", 4);
        u16le(o + 4, (unsigned)(n + 6));
        o[6] = 0x00;
        u16le(o + 7, (unsigned)n);
        o[9] = 0x00;
        memcpy(o + 10, d, n);
        memcpy(o + 10 + n, kTrailer, 6);
        *on = 16 + n;
        return o;
    }
    /* chunked: 10 + (n+6 trailer) */
    size_t total = 10 + n;
    for (size_t i = ZBM_CHUNK; i < n; i += ZBM_CHUNK) total += 6;
    total += 6;
    o = malloc(total);
    if (!o) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    uint8_t *p = o;
    memcpy(p, "ZBM\x09", 4);
    p += 4;
    u16le(p, ZBM_CHUNK + 6);
    p += 2;
    *p++ = 0x00;
    u16le(p, ZBM_CHUNK);
    p += 2;
    *p++ = 0x00;
    memcpy(p, d, ZBM_CHUNK);
    p += ZBM_CHUNK;
    for (size_t i = ZBM_CHUNK; i < n; i += ZBM_CHUNK) {
        size_t r = n - i > ZBM_CHUNK ? ZBM_CHUNK : n - i;
        u16le(p, (unsigned)(6 + r));
        p += 2;
        *p++ = 0x00;
        u16le(p, (unsigned)r);
        p += 2;
        *p++ = 0x00;
        memcpy(p, d + i, r);
        p += r;
    }
    memcpy(p, kTrailer, 6);
    p += 6;
    *on = (size_t)(p - o);
    return o;
}

uint8_t *lzbitmap_wrap_pbzb(const uint8_t *inner, size_t ilen,
                            size_t blocksize, size_t *on,
                            char *err, size_t errcap) {
    size_t nb = (ilen + blocksize - 1) / blocksize;
    if (nb == 0) nb = 1;
    uint8_t **pay = calloc(nb, sizeof *pay);
    size_t *ul = calloc(nb, sizeof *ul);
    size_t *cl = calloc(nb, sizeof *cl);
    if (!pay || !ul || !cl) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    size_t total = 12;
    for (size_t i = 0; i < nb; i++) {
        size_t off = i * blocksize;
        size_t m = (ilen > off) ? ilen - off : 0;
        if (m > blocksize) m = blocksize;
        ul[i] = m;
        size_t cn = 0;
        uint8_t *cf =
            zbm_encode_literal(inner + off, m, &cn, err, errcap);
        if (!cf) {
            for (size_t k = 0; k < i; k++) free(pay[k]);
            free(pay);
            free(ul);
            free(cl);
            return NULL;
        }
        if ((uint64_t)cn * 16 > (uint64_t)m * 15) {
            /* 15/16 store rule: stored form wins ties */
            free(cf);
            cf = malloc(m ? m : 1);
            if (!cf) {
                fprintf(stderr, "lzbitmap: out of memory\n");
                exit(1);
            }
            if (m) memcpy(cf, inner + off, m);
            cn = m;
        } else {
            /* keep literal stream */
        }
        pay[i] = cf;
        cl[i] = cn;
        total += cn + (i + 1 < nb ? 16 : 0);
    }
    uint8_t *o = malloc(total ? total : 1);
    if (!o) {
        fprintf(stderr, "lzbitmap: out of memory\n");
        exit(1);
    }
    uint8_t *p = o;
    memcpy(p, "pbzb", 4);
    p += 4;
    be32(&p, 0);
    be32(&p, (uint32_t)blocksize);
    be32(&p, 0);
    be32(&p, (uint32_t)ul[0]);
    be32(&p, 0);
    be32(&p, (uint32_t)cl[0]);
    for (size_t i = 0; i < nb; i++) {
        memcpy(p, pay[i], cl[i]);
        p += cl[i];
        if (i + 1 < nb) {
            be32(&p, 0);
            be32(&p, (uint32_t)ul[i + 1]);
            be32(&p, 0);
            be32(&p, (uint32_t)cl[i + 1]);
        }
        free(pay[i]);
    }
    free(pay);
    free(ul);
    free(cl);
    *on = total;
    return o;
}
