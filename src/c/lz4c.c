/* lz4c.c -- see lz4c.h. mirrors ../lz4enc.py exactly. */
#include "lz4c.h"
#include <stdlib.h>
#include <string.h>

typedef struct {
    uint8_t gram[4];
    uint32_t occ; /* gpos */
} cell;

typedef struct {
    cell slots[LZ4_SLOTS];
    uint8_t len;
} bucket;

typedef struct {
    bucket *tab; /* LZ4_BUCKETS, calloc'd */
    const uint8_t *inner;
    size_t ilen;
} tab;

static uint32_t tab_lookup(tab *t, uint32_t gpos) {
    const uint8_t *g = t->inner + gpos;
    uint32_t b = LZ4_BKT(g);
    bucket *bk = &t->tab[b];
    for (int i = 0; i < (int)bk->len; i++) {
        /* oldest-first like py (distinct grams: at most one hit). */
        if (!memcmp(bk->slots[i].gram, g, 4)) {
            uint32_t occ = bk->slots[i].occ;
            if (occ < gpos && gpos - occ <= 65535)
                return occ;
        }
    }
    return UINT32_MAX;
}

/* raw bucket scan ignoring window (for ends-flip probe need full gram
 * equality at bucket level: same as lookup but caller checks BKT). */
static void tab_put(tab *t, uint32_t gpos, const uint8_t *gram) {
    uint32_t b = LZ4_BKT(gram);
    bucket *bk = &t->tab[b];
    for (int i = 0; i < (int)bk->len; i++) {
        if (!memcmp(bk->slots[i].gram, gram, 4)) {
            cell c;
            memcpy(c.gram, gram, 4);
            c.gram[0] = gram[0]; /* keep static analyzers calm */
            c.occ = gpos;
            memmove(&bk->slots[i], &bk->slots[i + 1],
                    (size_t)((int)bk->len - 1 - i) * sizeof(cell));
            bk->slots[bk->len - 1] = c;
            return;
        }
    }
    if (bk->len < LZ4_SLOTS) {
        memcpy(bk->slots[bk->len].gram, gram, 4);
        bk->slots[bk->len].occ = gpos;
        bk->len++;
    } else {
        memmove(&bk->slots[0], &bk->slots[1],
                (LZ4_SLOTS - 1) * sizeof(cell));
        memcpy(bk->slots[LZ4_SLOTS - 1].gram, gram, 4);
        bk->slots[LZ4_SLOTS - 1].occ = gpos;
    }
}

typedef struct {
    uint8_t *p;
    size_t n, cap;
} obuf;

static void oneed(obuf *o, size_t x) {
    if (o->n + x > o->cap) {
        size_t nc = o->cap ? o->cap * 2 : 1024;
        while (nc < o->n + x) nc *= 2;
        o->p = realloc(o->p, nc ? nc : 1);
        if (!o->p) exit(1);
        o->cap = nc;
    }
}

static void oput(obuf *o, const void *s, size_t len) {
    oneed(o, len);
    memcpy(o->p + o->n, s, len);
    o->n += len;
}

static void oputc(obuf *o, uint8_t c) { oput(o, &c, 1); }

static void emit_seq(obuf *o, const uint8_t *lit, size_t litn, size_t ml,
                     uint32_t off) {
    size_t tml = ml ? ml - 4 : 0;
    oputc(o, (uint8_t)(((litn < 15 ? litn : 15) << 4) |
                       (tml < 15 ? tml : 15)));
    if (litn >= 15) {
        size_t x = litn - 15;
        while (x >= 255) {
            oputc(o, 255);
            x -= 255;
        }
        oputc(o, (uint8_t)x);
    }
    if (litn) oput(o, lit, litn);
    if (ml) {
        oputc(o, (uint8_t)(off & 0xFF));
        oputc(o, (uint8_t)((off >> 8) & 0xFF));
        if (tml >= 15) {
            size_t x = tml - 15;
            while (x >= 255) {
                oputc(o, 255);
                x -= 255;
            }
            oputc(o, (uint8_t)x);
        }
    }
}

lz4_chunk *lz4_encode_all(const uint8_t *inner, size_t ilen, size_t *nch) {
    tab t;
    t.tab = calloc(LZ4_BUCKETS, sizeof(bucket));
    if (!t.tab) exit(1);
    t.inner = inner;
    t.ilen = ilen;
    size_t nchs = (ilen + LZ4_CHUNK - 1) / LZ4_CHUNK;
    if (!nchs) nchs = 1;
    lz4_chunk *chs = calloc(nchs ? nchs : 1, sizeof(lz4_chunk));
    if (!chs) exit(1);
    for (size_t ci = 0; ci < nchs; ci++) {
        size_t base = ci * LZ4_CHUNK;
        size_t n = ilen - base > LZ4_CHUNK ? LZ4_CHUNK : ilen - base;
        int fin = ci == nchs - 1;
        uint32_t ilim = fin ? UINT32_MAX : (uint32_t)(base + LZ4_CHUNK - LZ4_NEVER_K);
        uint32_t FBOUND = (uint32_t)(base + n - 122);
        uint32_t LIMB = (uint32_t)(base + n - 121);
        obuf o = {0};
        size_t anchor = 0, ip = 0;
        while (ip < n) {
            uint32_t gpos = (uint32_t)(base + ip);
            if (ip + 12 >= n) break;
            uint32_t occ = UINT32_MAX;
            if (gpos >= 16 && gpos + 4 <= FBOUND) {
                occ = tab_lookup(&t, gpos);
                if (occ == UINT32_MAX && ip == 0 && ci >= 1) {
                    const uint8_t *g = inner + gpos;
                    for (int32_t _o = (int32_t)gpos - 4;
                         _o >= (int32_t)gpos - 8; _o--) {
                        if (_o >= 0 && (uint32_t)_o + 4 <= gpos &&
                            !memcmp(inner + _o, g, 4)) {
                            occ = (uint32_t)_o;
                            break;
                        }
                    }
                }
            }
            if (occ != UINT32_MAX) {
                size_t ml = 4;
                uint32_t dst = gpos + 4;
                uint32_t off = gpos - occ;
                int first = 1;
                for (;;) {
                    if (!first && dst + 8 > LIMB) break;
                    if (dst + 8 > base + n) {
                        while (gpos + ml < base + n &&
                               off > 0 && occ + ml < ilen &&
                               inner[gpos + ml] == inner[occ + ml])
                            ml++;
                        break;
                    }
                    if (!memcmp(inner + dst, inner + dst - off, 8)) {
                        ml += 8;
                        dst += 8;
                        first = 0;
                        continue;
                    }
                    {
                        uint32_t end = dst + 8;
                        while (gpos + ml < end && gpos + ml < base + n &&
                               occ + ml < ilen &&
                               inner[gpos + ml] == inner[occ + ml])
                            ml++;
                    }
                    break;
                }
                emit_seq(&o, inner + base + anchor, gpos - (base + anchor),
                         ml, off);
                uint32_t mend = gpos + (uint32_t)ml;
                if (gpos < ilim && gpos + 4 <= ilen)
                    tab_put(&t, gpos, inner + gpos);
                if (gpos + 1 < mend &&
                    (gpos - (uint32_t)(base + anchor)) % 5 != 4) {
                    uint32_t p1 = gpos + 1;
                    if (p1 < ilim && p1 + 4 <= ilen)
                        tab_put(&t, p1, inner + p1);
                }
                if (mend - (uint32_t)base < n - 12) {
                    if (tab_lookup(&t, mend) == UINT32_MAX) {
                        uint32_t s = LZ4_BKT(inner + mend);
                        uint32_t e2 = mend - 2, e1 = mend - 1;
                        int flip = 0;
                        uint32_t es[2] = {e2, e1};
                        for (int k = 0; k < 2; k++) {
                            uint32_t e = es[k];
                            if (e > gpos + 1 && e + 4 <= ilen &&
                                LZ4_BKT(inner + e) == s &&
                                !memcmp(inner + e, inner + mend, 4))
                                flip = 1;
                        }
                        if (!flip) {
                            if (e2 > gpos + 1 && e2 < ilim && e2 + 4 <= ilen)
                                tab_put(&t, e2, inner + e2);
                            if (e1 > gpos + 1 && e1 < ilim && e1 + 4 <= ilen)
                                tab_put(&t, e1, inner + e1);
                        }
                    }
                }
                anchor = ip + ml;
                ip = anchor;
            } else {
                if (gpos != 0 && gpos < ilim && gpos + 4 <= ilen)
                    tab_put(&t, gpos, inner + gpos);
                ip++;
            }
        }
        emit_seq(&o, inner + base + anchor, base + n - (base + anchor), 0, 0);
        chs[ci].unc = n;
        chs[ci].blk = o.p ? o.p : calloc(1, 1);
        chs[ci].blen = o.n;
    }
    free(t.tab);
    *nch = nchs;
    return chs;
}

void lz4_free_chunks(lz4_chunk *chs, size_t nch) {
    for (size_t i = 0; i < nch; i++) free(chs[i].blk);
    free(chs);
}

static void w32le(uint8_t **p, uint32_t v) {
    (*p)[0] = (uint8_t)v;
    (*p)[1] = (uint8_t)(v >> 8);
    (*p)[2] = (uint8_t)(v >> 16);
    (*p)[3] = (uint8_t)(v >> 24);
    *p += 4;
}

static void w32be(uint8_t **p, uint32_t v) {
    (*p)[0] = (uint8_t)(v >> 24);
    (*p)[1] = (uint8_t)(v >> 16);
    (*p)[2] = (uint8_t)(v >> 8);
    (*p)[3] = (uint8_t)v;
    *p += 4;
}

uint8_t *lz4_wrap_pbz4(const uint8_t *inner, size_t ilen,
                       const lz4_chunk *chs, size_t nch, size_t blocksize,
                       size_t *olen) {
    (void)ilen;
    /* regroup into blocks: pre-count (tail counts, min 1) */
    size_t nbl = 0;
    {
        size_t acc = 0;
        for (size_t i = 0; i < nch; i++) {
            acc += chs[i].unc;
            if (acc >= blocksize) {
                nbl++;
                acc = 0;
            }
        }
        if (acc) nbl++;
        if (!nbl) nbl = 1;
    }
    /* per-block framed-or-store decision needs payload sizes first */
    typedef struct {
        size_t u;
        uint8_t *pay;
        size_t payn;
        int framed;
    } blk;
    blk *bl = calloc(nbl ? nbl : 1, sizeof(blk));
    if (!bl) exit(1);
    {
        /* straightforward regroup mirroring py */
        size_t bi = 0, acc = 0, start = 0, base = 0;
        acc = 0;
        start = 0;
        base = 0;
        for (size_t i = 0; i < nch; i++) {
            acc += chs[i].unc;
            if (acc >= blocksize || i + 1 == nch) {
                size_t u = 0;
                for (size_t j = start; j <= i; j++) u += chs[j].unc;
                /* build payload */
                size_t cap = u + (i - start + 1) * 12 + 4 + 8;
                uint8_t *pay = malloc(cap ? cap : 1);
                if (!pay) exit(1);
                uint8_t *q = pay;
                size_t b2 = base;
                for (size_t j = start; j <= i; j++) {
                    if (chs[j].blen < chs[j].unc) {
                        memcpy(q, "bv41", 4);
                        q += 4;
                        w32le(&q, (uint32_t)chs[j].unc);
                        w32le(&q, (uint32_t)chs[j].blen);
                        memcpy(q, chs[j].blk, chs[j].blen);
                        q += chs[j].blen;
                    } else {
                        memcpy(q, "bv4-", 4);
                        q += 4;
                        w32le(&q, (uint32_t)chs[j].unc);
                        memcpy(q, inner + b2, chs[j].unc);
                        q += chs[j].unc;
                    }
                    b2 += chs[j].unc;
                }
                memcpy(q, "bv4$", 4);
                q += 4;
                size_t payn = (size_t)(q - pay);
                if ((uint64_t)payn * 16 <= (uint64_t)u * 15) {
                    bl[bi].u = u;
                    bl[bi].pay = pay;
                    bl[bi].payn = payn;
                    bl[bi].framed = 1;
                } else {
                    free(pay);
                    uint8_t *rw = malloc(u ? u : 1);
                    if (u) memcpy(rw, inner + base, u);
                    bl[bi].u = u;
                    bl[bi].pay = rw;
                    bl[bi].payn = u;
                    bl[bi].framed = 0;
                }
                base += u;
                bi++;
                acc = 0;
                start = i + 1;
            }
        }
        if (bi == 0) { /* empty inner */
            bl[0].u = 0;
            bl[0].pay = malloc(4);
            memcpy(bl[0].pay, "bv4$", 4);
            bl[0].payn = 4;
            bl[0].framed = 0; /* 4*16 > 0: store empty */
            free(bl[0].pay);
            bl[0].pay = malloc(1);
            bl[0].payn = 0;
            bi = 1;
        }
        nbl = bi;
    }
    size_t total = 4 + 6 * 4;
    for (size_t i = 0; i < nbl; i++) {
        total += bl[i].payn;
        if (i + 1 < nbl) total += 16;
    }
    uint8_t *out = malloc(total ? total : 1);
    if (!out) exit(1);
    uint8_t *q = out;
    memcpy(q, "pbz4", 4);
    q += 4;
    w32be(&q, 0);
    w32be(&q, (uint32_t)blocksize);
    w32be(&q, 0);
    w32be(&q, (uint32_t)bl[0].u);
    w32be(&q, 0);
    w32be(&q, (uint32_t)bl[0].payn);
    for (size_t i = 0; i < nbl; i++) {
        memcpy(q, bl[i].pay, bl[i].payn);
        q += bl[i].payn;
        if (i + 1 < nbl) {
            w32be(&q, 0);
            w32be(&q, (uint32_t)bl[i + 1].u);
            w32be(&q, 0);
            w32be(&q, (uint32_t)bl[i + 1].payn);
        }
        free(bl[i].pay);
    }
    free(bl);
    *olen = total;
    return out;
}
