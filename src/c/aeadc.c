/* aeadc.c -- AEA encrypt/decrypt/id C port. See aeadc.h for provenance. */
#define _DARWIN_C_SOURCE 1
#include "aeadc.h"
#include <CommonCrypto/CommonCryptor.h>
#include <CommonCrypto/CommonDigest.h>
#include <CommonCrypto/CommonHMAC.h>
#include <compression.h>
#include <lzma.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <zlib.h>

char aead_err[256];

#include <stdarg.h>
static int fail(const char *fmt, ...) {
    va_list ap; va_start(ap, fmt);
    vsnprintf(aead_err, sizeof aead_err, fmt, ap); va_end(ap);
    return -1;
}

/* ---------- growable buffer ---------- */
typedef struct { uint8_t *p; size_t n, cap; } buf;
static int bneed(buf *b, size_t extra) {
    if (b->n + extra <= b->cap) return 0;
    size_t nc = b->cap ? b->cap : 256;
    while (nc < b->n + extra) nc *= 2;
    uint8_t *q = realloc(b->p, nc);
    if (!q) return fail("out of memory");
    b->p = q; b->cap = nc; return 0;
}
static int bput(buf *b, const void *s, size_t len) {
    if (!len) return 0;
    if (bneed(b, len)) return -1;
    memcpy(b->p + b->n, s, len); b->n += len; return 0;
}
static int bputc(buf *b, uint8_t c) { return bput(b, &c, 1); }
static void bfree(buf *b) { free(b->p); b->p = 0; b->n = b->cap = 0; }
static void put32le(uint8_t *p, uint32_t v) {
    p[0] = v; p[1] = v >> 8; p[2] = v >> 16; p[3] = v >> 24;
}
static void put64le(uint8_t *p, uint64_t v) {
    for (int i = 0; i < 8; i++) p[i] = (uint8_t)(v >> (8 * i));
}
static uint32_t get32le(const uint8_t *p) {
    return (uint32_t)p[0] | ((uint32_t)p[1] << 8) |
           ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24);
}

/* ---------- files / random ---------- */
static int read_all(const char *path, uint8_t **out, size_t *len) {
    /* "-" is a literal file (oracle + proto agree). */
    FILE *f = fopen(path, "rb");
    if (!f) return fail("cannot open %s", path);
    fseek(f, 0, SEEK_END); long n = ftell(f); fseek(f, 0, SEEK_SET);
    if (n < 0) { fclose(f); return fail("cannot read %s", path); }
    uint8_t *d = malloc((size_t)n + 1);
    if (!d) { fclose(f); return fail("out of memory"); }
    if (n > 0 && fread(d, 1, (size_t)n, f) != (size_t)n) {
        fclose(f); free(d); return fail("cannot read %s", path);
    }
    fclose(f); *out = d; *len = (size_t)n; return 0;
}
static int write_all(const char *path, const uint8_t *d, size_t n) {
    FILE *f = path ? fopen(path, "wb") : stdout;
    if (!f) return fail("cannot open %s", path);
    /* binary mode note: stdout on macOS is untranslated already. */
    if (n > 0 && fwrite(d, 1, n, f) != n) {
        if (path) fclose(f); return fail("cannot write %s", path ? path : "stdout");
    }
    if (path) fclose(f); else fflush(f); return 0;
}
static void randbytes(uint8_t *d, size_t n) { arc4random_buf(d, n); }

/* ---------- base64 (RFC 4648 section 4, own) + hex ---------- */
static int b64val(char c) {
    if (c >= 'A' && c <= 'Z') return c - 'A';
    if (c >= 'a' && c <= 'z') return c - 'a' + 26;
    if (c >= '0' && c <= '9') return c - '0' + 52;
    if (c == '+') return 62; if (c == '/') return 63; return -1;
}
/* lenient like Python b64decode(validate=False): skip non-alphabet. */
static int unb64(const char *s, size_t n, uint8_t **out, size_t *olen) {
    buf b = {0};
    int acc = 0, bits = 0, pad = 0;
    for (size_t i = 0; i < n; i++) {
        char c = s[i];
        if (c == '=') { pad++; continue; }
        int v = b64val(c);
        if (v < 0) continue;
        if (pad) { bfree(&b); return fail("key invalid"); }
        acc = (acc << 6) | v; bits += 6;
        if (bits >= 8) { bits -= 8; uint8_t o = (acc >> bits) & 0xFF;
            if (bputc(&b, o)) { bfree(&b); return -1; } }
    }
    *out = b.p; *olen = b.n; return 0;
}
static int isws(char c) {
    return c == ' ' || c == '\t' || c == '\n' || c == '\r' || c == '\f' || c == '\v';
}
static int unhex(const char *s, size_t n, uint8_t **out, size_t *olen) {
    buf b = {0};
    int hi = -1;
    for (size_t i = 0; i < n; i++) {
        char c = s[i];
        if (isws(c)) continue; /* bytes.fromhex skips ASCII whitespace */
        int v;
        if (c >= '0' && c <= '9') v = c - '0';
        else if (c >= 'a' && c <= 'f') v = c - 'a' + 10;
        else if (c >= 'A' && c <= 'F') v = c - 'A' + 10;
        else { bfree(&b); return fail("key invalid"); }
        if (hi < 0) hi = v;
        else { uint8_t o = (hi << 4) | v; hi = -1;
            if (bputc(&b, o)) { bfree(&b); return -1; } }
    }
    if (hi >= 0) { bfree(&b); return fail("key invalid"); }
    *out = b.p; *olen = b.n; return 0;
}

/* ---------- SHA-256 / HMAC (system CommonCrypto) ---------- */
static void sha256(const uint8_t *d, size_t n, uint8_t out[32]) {
    CC_SHA256(d, (CC_LONG)n, out);
}
static void hmac_sha256(const uint8_t *key, size_t kn,
                        const uint8_t *d, size_t n, uint8_t out[32]) {
    CCHmac(kCCHmacAlgSHA256, key, kn, d, n, out);
}

/* ---------- HKDF-SHA256 (RFC 5869 section 2.2/2.3, own) ---------- */
static void hkdf(const uint8_t *ikm, size_t ikm_len,
                 const uint8_t *info, size_t info_len,
                 const uint8_t *salt, size_t salt_len,
                 uint8_t *okm, size_t L) {
    uint8_t zeros[32]; memset(zeros, 0, 32);
    if (salt_len == 0) { salt = zeros; salt_len = 32; }
    uint8_t prk[32];
    hmac_sha256(salt, salt_len, ikm, ikm_len, prk);
    uint8_t t[32]; size_t tlen = 0;
    uint8_t ctr = 1;
    size_t pos = 0;
    uint8_t in[32 + 256 + 1]; /* info capped: AEA infos are short */
    while (pos < L) {
        size_t il = tlen + info_len + 1;
        memcpy(in, t, tlen); memcpy(in + tlen, info, info_len);
        in[tlen + info_len] = ctr;
        hmac_sha256(prk, 32, in, il, t); tlen = 32;
        size_t take = L - pos < 32 ? L - pos : 32;
        memcpy(okm + pos, t, take); pos += take; ctr++;
    }
}

/* mac(key32, data, salt) = HMAC(key32, salt+data+LE64(len(salt))) */
static void amac(const uint8_t key[32], const uint8_t *data, size_t dn,
                 const uint8_t *salt, size_t sn, uint8_t out[32]) {
    buf b = {0};
    bput(&b, salt, sn); bput(&b, data, dn);
    uint8_t le[8]; put64le(le, sn); bput(&b, le, 8);
    hmac_sha256(key, 32, b.p, b.n, out);
    bfree(&b);
}

/* ---------- AES-256-CTR (CommonCrypto, BE counter per SP 800-38A 6.5) --- */
static int aes256ctr(const uint8_t key[32], const uint8_t iv[16],
                      const uint8_t *in, uint8_t *out, size_t n) {
    CCCryptorRef cr = NULL;
    CCCryptorStatus st = CCCryptorCreateWithMode(
        kCCEncrypt, kCCModeCTR, kCCAlgorithmAES, ccNoPadding,
        iv, key, 32, NULL, 0, 0, kCCModeOptionCTR_BE, &cr);
    if (st != kCCSuccess || !cr) return fail("AES unavailable");
    size_t moved = 0;
    st = CCCryptorUpdate(cr, in, n, out, n, &moved);
    if (st != kCCSuccess || moved != n) { CCCryptorRelease(cr); return fail("AES unavailable"); }
    CCCryptorRelease(cr); return 0;
}

/* ---------- PBKDF2-HMAC-SHA256 (RFC 2898 section 5.2, own) ---------- */
static void pbkdf2_hmac_sha256(const uint8_t *pw, size_t pwn,
                               const uint8_t *salt, size_t sn,
                               uint32_t iter, uint8_t *dk, size_t dklen) {
    uint8_t u[32], t[32];
    /* salt + BE32(i) built on malloc'd sb below */
    uint8_t *sb = malloc(sn + 4);
    memcpy(sb, salt, sn);
    uint32_t i = 1;
    size_t pos = 0;
    while (pos < dklen) {
        sb[sn] = i >> 24; sb[sn+1] = i >> 16; sb[sn+2] = i >> 8; sb[sn+3] = i;
        hmac_sha256(pw, pwn, sb, sn + 4, u);
        memcpy(t, u, 32);
        for (uint32_t k = 1; k < iter; k++) {
            hmac_sha256(pw, pwn, u, 32, u);
            for (int j = 0; j < 32; j++) t[j] ^= u[j];
        }
        size_t take = dklen - pos < 32 ? dklen - pos : 32;
        memcpy(dk + pos, t, take); pos += take; i++;
    }
    free(sb);
}

/* ---------- Salsa20/8 core (Bernstein Salsa20 spec, public domain;
 * invoked by RFC 7914 section 5 BlockMix) ---------- */
#define SROTL(v, n) (((v) << (n)) | ((v) >> (32 - (n))))
static void salsa208(uint32_t B[16]) {
    uint32_t x[16]; memcpy(x, B, 64);
    for (int d = 0; d < 4; d++) {
        /* columnround */
        x[ 4] ^= SROTL(x[ 0]+x[12], 7); x[ 8] ^= SROTL(x[ 4]+x[ 0], 9);
        x[12] ^= SROTL(x[ 8]+x[ 4],13); x[ 0] ^= SROTL(x[12]+x[ 8],18);
        x[ 9] ^= SROTL(x[ 5]+x[ 1], 7); x[13] ^= SROTL(x[ 9]+x[ 5], 9);
        x[ 1] ^= SROTL(x[13]+x[ 9],13); x[ 5] ^= SROTL(x[ 1]+x[13],18);
        x[14] ^= SROTL(x[10]+x[ 6], 7); x[ 2] ^= SROTL(x[14]+x[10], 9);
        x[ 6] ^= SROTL(x[ 2]+x[14],13); x[10] ^= SROTL(x[ 6]+x[ 2],18);
        x[ 3] ^= SROTL(x[15]+x[11], 7); x[ 7] ^= SROTL(x[ 3]+x[15], 9);
        x[11] ^= SROTL(x[ 7]+x[ 3],13); x[15] ^= SROTL(x[11]+x[ 7],18);
        /* rowround */
        x[ 1] ^= SROTL(x[ 0]+x[ 3], 7); x[ 2] ^= SROTL(x[ 1]+x[ 0], 9);
        x[ 3] ^= SROTL(x[ 2]+x[ 1],13); x[ 0] ^= SROTL(x[ 3]+x[ 2],18);
        x[ 6] ^= SROTL(x[ 5]+x[ 4], 7); x[ 7] ^= SROTL(x[ 6]+x[ 5], 9);
        x[ 4] ^= SROTL(x[ 7]+x[ 6],13); x[ 5] ^= SROTL(x[ 4]+x[ 7],18);
        x[11] ^= SROTL(x[10]+x[ 9], 7); x[ 8] ^= SROTL(x[11]+x[10], 9);
        x[ 9] ^= SROTL(x[ 8]+x[11],13); x[10] ^= SROTL(x[ 9]+x[ 8],18);
        x[12] ^= SROTL(x[15]+x[14], 7); x[13] ^= SROTL(x[12]+x[15], 9);
        x[14] ^= SROTL(x[13]+x[12],13); x[15] ^= SROTL(x[14]+x[13],18);
    }
    for (int i = 0; i < 16; i++) B[i] += x[i];
}

/* ---------- scrypt (RFC 7914, own; r=8 p=1 N from SCRYPT_N) ---------- */
static void blockmix(uint8_t *B, uint32_t *Y, uint32_t *X, int r) {
    /* B: 2r 64B blocks. RFC 7914 section 4. */
    for (int i = 0; i < 16; i++) X[i] = ((uint32_t *)B)[(2*r-1)*16+i];
    for (int i = 0; i < 2*r; i++) {
        for (int j = 0; j < 16; j++) X[j] ^= ((uint32_t *)B)[i*16+j];
        salsa208(X);
        memcpy(&Y[i*16], X, 64);
    }
    for (int i = 0; i < r; i++) memcpy(&B[i*64], &Y[(i*2)*16], 64);
    for (int i = 0; i < r; i++) memcpy(&B[(i+r)*64], &Y[(i*2+1)*16], 64);
}
static int scrypt(const uint8_t *pw, size_t pwn, const uint8_t *salt, size_t sn,
                  uint32_t N, uint8_t *dk /*32*/) {
    const int r = 8, blen = 128 * r;
    uint8_t *B = malloc(blen);
    uint8_t *V = malloc((size_t)N * blen);
    uint32_t *XY = malloc((2 * 16 * r + 16) * 4);
    if (!B || !V || !XY) { free(B); free(V); free(XY); return fail("out of memory"); }
    uint32_t *Y = XY, *X = XY + 32 * (size_t)r;
    pbkdf2_hmac_sha256(pw, pwn, salt, sn, 1, B, blen);
    for (uint32_t i = 0; i < N; i++) {
        memcpy(V + (size_t)i * blen, B, blen);
        blockmix(B, Y, X, r);
    }
    for (uint32_t i = 0; i < N; i++) {
        uint32_t j = ((uint32_t *)B)[(2*r-1)*16] & (N - 1);
        uint8_t *Vj = V + (size_t)j * blen;
        for (int k = 0; k < blen / 64; k++)
            for (int w = 0; w < 16; w++)
                ((uint32_t *)B)[k*16+w] ^= ((uint32_t *)Vj)[k*16+w];
        blockmix(B, Y, X, r);
    }
    pbkdf2_hmac_sha256(pw, pwn, B, blen, 1, dk, 32);
    memset(B, 0, blen); memset(V, 0, (size_t)N * blen);
    free(B); free(V); free(XY);
    return 0;
}

/* ---------- murmur64a: line-port of own proto ---------- */
#define M64C 0xC6A4A7935BD1E995ULL
#define MUR_SEED 0xE2236FDC26A5F6D2ULL
static void murmur64a(const uint8_t *d, size_t n, uint8_t out[8]) {
    uint64_t h = MUR_SEED ^ ((uint64_t)n * M64C);
    size_t nblk = n & ~(size_t)7;
    for (size_t i = 0; i < nblk; i += 8) {
        uint64_t k = (uint64_t)d[i] | ((uint64_t)d[i+1] << 8) |
                     ((uint64_t)d[i+2] << 16) | ((uint64_t)d[i+3] << 24) |
                     ((uint64_t)d[i+4] << 32) | ((uint64_t)d[i+5] << 40) |
                     ((uint64_t)d[i+6] << 48) | ((uint64_t)d[i+7] << 56);
        k *= M64C; k ^= k >> 47; k *= M64C; h ^= k; h *= M64C;
    }
    size_t tail = n - nblk;
    if (tail) {
        uint64_t t = 0;
        for (size_t j = 0; j < tail; j++) t |= (uint64_t)d[nblk+j] << (8*j);
        h ^= t; h *= M64C;
    }
    h ^= h >> 47; h *= M64C; h ^= h >> 47;
    put64le(out, h);
}

/* ================= P-256 (SEC1 v2.0 s2 domain params; FIPS 186-4) ====== */
typedef struct { uint32_t v[8]; } u256;   /* LE limbs */
typedef struct { uint32_t v[16]; } u512;

static int hexdig(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10; return -1;
}
static void u256_fromhex(u256 *r, const char *h) { /* 64 hex chars BE */
    memset(r, 0, sizeof *r);
    for (int i = 0; i < 32; i++) {
        int a = hexdig(h[2*i]), b = hexdig(h[2*i+1]);
        ((uint8_t *)r->v)[31 - i] = (uint8_t)((a << 4) | b);
    }
}
static void u256_tobytes_be(const u256 *a, uint8_t out[32]) {
    for (int i = 0; i < 32; i++) out[i] = ((uint8_t *)a->v)[31 - i];
}
static void u256_frombytes_be(u256 *r, const uint8_t in[32]) {
    for (int i = 0; i < 32; i++) ((uint8_t *)r->v)[31 - i] = in[i];
}
static int u256_cmp(const u256 *a, const u256 *b) {
    for (int i = 7; i >= 0; i--) {
        if (a->v[i] != b->v[i]) return a->v[i] < b->v[i] ? -1 : 1;
    }
    return 0;
}
static int u256_iszero(const u256 *a) {
    uint32_t z = 0; for (int i = 0; i < 8; i++) z |= a->v[i]; return z == 0;
}
static void u256_add_raw(u256 *r, const u256 *a, const u256 *b, uint32_t *cy) {
    uint64_t c = 0;
    for (int i = 0; i < 8; i++) {
        c += (uint64_t)a->v[i] + b->v[i]; r->v[i] = (uint32_t)c; c >>= 32;
    }
    *cy = (uint32_t)c;
}
static void u256_sub_raw(u256 *r, const u256 *a, const u256 *b, uint32_t *bw) {
    uint64_t c = 0;
    for (int i = 0; i < 8; i++) {
        uint64_t t = (uint64_t)a->v[i] - b->v[i] - c;
        r->v[i] = (uint32_t)t; c = (t >> 63) & 1; /* borrow if wrapped */
        /* careful: t>>63 works since t mod 2^64 of possibly-negative */
    }
    *bw = (uint32_t)c;
}
static void u256_mul(u512 *r, const u256 *a, const u256 *b) {
    memset(r, 0, sizeof *r);
    for (int i = 0; i < 8; i++) {
        uint64_t c = 0;
        for (int j = 0; j < 8; j++) {
            c += (uint64_t)a->v[i] * b->v[j] + r->v[i+j]; r->v[i+j] = (uint32_t)c; c >>= 32;
        }
        r->v[i+8] = (uint32_t)c;
    }
}
/* rem = x mod m; x 512b, m 256b. shift-subtract (generic, any modulus). */
static void u512_mod(const u512 *x, const u256 *m, u256 *rem) {
    uint32_t r[9]; memset(r, 0, sizeof r);
    for (int bit = 511; bit >= 0; bit--) {
        uint32_t carry = 0;
        for (int i = 0; i < 9; i++) {
            uint32_t nv = (r[i] << 1) | carry; carry = r[i] >> 31; r[i] = nv;
        }
        r[0] |= (x->v[bit >> 5] >> (bit & 31)) & 1u;
        /* if r >= m: r -= m */
        int ge = 0;
        if (r[8]) ge = 1;
        else {
            u256 t; for (int i = 0; i < 8; i++) t.v[i] = r[i];
            ge = u256_cmp(&t, m) >= 0;
        }
        if (ge) {
            uint64_t c = 0;
            for (int i = 0; i < 8; i++) {
                uint64_t t = (uint64_t)r[i] - m->v[i] - c;
                r[i] = (uint32_t)t; c = (t >> 63) & 1;
            }
            r[8] -= (uint32_t)c;
        }
    }
    for (int i = 0; i < 8; i++) rem->v[i] = r[i];
}
static void mod_add(u256 *r, const u256 *a, const u256 *b, const u256 *m) {
    u256 t; uint32_t cy, bw;
    u256_add_raw(&t, a, b, &cy);
    if (!cy) {
        /* s = t < 2^256: subtract m iff t >= m. */
        if (u256_cmp(&t, m) < 0) { *r = t; return; }
        u256_sub_raw(&t, &t, m, &bw);
        *r = t; return;
    }
    /* cy==1: s = t+2^256 > m always; r = s-m = t+(2^256-m),
     * single wrapped add (both t>=m and t<m sub-cases exact). */
    {
        u256 neg, z; memset(&z, 0, sizeof z);
        u256_sub_raw(&neg, &z, m, &bw);
        u256_add_raw(r, &t, &neg, &cy);
    }
}
static void mod_sub(u256 *r, const u256 *a, const u256 *b, const u256 *m) {
    u256 t; uint32_t bw;
    u256_sub_raw(&t, a, b, &bw);
    if (!bw) { *r = t; return; }
    uint32_t cy; u256_add_raw(r, &t, m, &cy);
}
static void mod_mul(u256 *r, const u256 *a, const u256 *b, const u256 *m) {
    u512 p; u256_mul(&p, a, b); u512_mod(&p, m, r);
}
static void mod_pow(u256 *r, const u256 *a, const u256 *e, const u256 *m) {
    u256 base = *a, one; memset(&one, 0, sizeof one); one.v[0] = 1;
    u256 acc = one;
    for (int bit = 255; bit >= 0; bit--) {
        mod_mul(&acc, &acc, &acc, m);
        if ((e->v[bit >> 5] >> (bit & 31)) & 1u) mod_mul(&acc, &acc, &base, m);
    }
    *r = acc;
}

static u256 P256_P, P256_N, P256_GX, P256_GY, P256_B;
static void p256_init(void) {
    static int done = 0; if (done) return; done = 1;
    u256_fromhex(&P256_P, "FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF");
    u256_fromhex(&P256_N, "FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551");
    u256_fromhex(&P256_GX, "6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296");
    u256_fromhex(&P256_GY, "4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5");
    u256_fromhex(&P256_B, "5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B");
}

typedef struct { u256 x, y, z; } jpt; /* Jacobian; z==0 => infinity */
static int pt_isinf(const jpt *p) { return u256_iszero(&p->z); }
static void pt_inf(jpt *p) { memset(p, 0, sizeof *p); }
static void pt_set_aff(jpt *r, const u256 *x, const u256 *y) {
    r->x = *x; r->y = *y; memset(&r->z, 0, sizeof r->z); r->z.v[0] = 1;
}
static void pt_dbl(const jpt *p, jpt *r) { /* a=-3 Jacobian doubling */
    if (pt_isinf(p)) { *r = *p; return; }
    if (u256_iszero(&p->y)) { pt_inf(r); return; }
    u256 XX, YY, YYYY, ZZ, S, M, T, E, X3, Y3, Z3;
    mod_mul(&XX, &p->x, &p->x, &P256_P);
    mod_mul(&YY, &p->y, &p->y, &P256_P);
    mod_mul(&YYYY, &YY, &YY, &P256_P);
    mod_mul(&ZZ, &p->z, &p->z, &P256_P);
    mod_add(&S, &p->x, &YY, &P256_P); mod_mul(&S, &S, &S, &P256_P);
    mod_sub(&S, &S, &XX, &P256_P); mod_sub(&S, &S, &YYYY, &P256_P);
    mod_add(&S, &S, &S, &P256_P);              /* S = 2((X+Y^2)^2-XX-YYYY) */
    mod_mul(&M, &ZZ, &ZZ, &P256_P);              /* M = Z^4 */
    mod_sub(&T, &XX, &M, &P256_P);             /* T = XX-Z^4 */
    mod_add(&M, &T, &T, &P256_P);
    mod_add(&M, &M, &T, &P256_P);              /* M = 3(XX-Z^4) */
    /* E = M^2 - 2S ; X3 = E ; Y3 = M(S-E) - 8YYYY ; Z3 = 2YZ */
    mod_mul(&E, &M, &M, &P256_P); mod_sub(&E, &E, &S, &P256_P); mod_sub(&E, &E, &S, &P256_P);
    X3 = E;
    mod_sub(&T, &S, &E, &P256_P); mod_mul(&T, &M, &T, &P256_P);
    u256 e8; mod_add(&e8, &YYYY, &YYYY, &P256_P); mod_add(&e8, &e8, &e8, &P256_P);
    mod_add(&e8, &e8, &e8, &P256_P);
    mod_sub(&Y3, &T, &e8, &P256_P);
    mod_mul(&Z3, &p->y, &p->z, &P256_P); mod_add(&Z3, &Z3, &Z3, &P256_P);
    r->x = X3; r->y = Y3; r->z = Z3; /* alias-safe commit */
}
static void pt_add(const jpt *a, const jpt *b, jpt *r) { /* generic add */
    if (pt_isinf(a)) { *r = *b; return; }
    if (pt_isinf(b)) { *r = *a; return; }
    u256 Z1Z1, Z2Z2, U1, U2, S1, S2, H, I, J, Rv, V, T, X3, Y3, Z3;
    mod_mul(&Z1Z1, &a->z, &a->z, &P256_P);
    mod_mul(&Z2Z2, &b->z, &b->z, &P256_P);
    mod_mul(&U1, &a->x, &Z2Z2, &P256_P);
    mod_mul(&T, &b->z, &Z2Z2, &P256_P); mod_mul(&S1, &a->y, &T, &P256_P);
    mod_mul(&U2, &b->x, &Z1Z1, &P256_P);
    mod_mul(&T, &a->z, &Z1Z1, &P256_P); mod_mul(&S2, &b->y, &T, &P256_P);
    if (!u256_cmp(&U1, &U2)) {
        if (!u256_cmp(&S1, &S2)) { pt_dbl(a, r); return; }
        pt_inf(r); return;
    }
    mod_sub(&H, &U2, &U1, &P256_P);
    mod_add(&I, &H, &H, &P256_P); mod_mul(&I, &I, &I, &P256_P);
    mod_mul(&J, &H, &I, &P256_P);
    mod_sub(&Rv, &S2, &S1, &P256_P); mod_add(&Rv, &Rv, &Rv, &P256_P);
    mod_mul(&V, &U1, &I, &P256_P);
    mod_mul(&X3, &Rv, &Rv, &P256_P);
    mod_sub(&X3, &X3, &J, &P256_P);
    mod_sub(&X3, &X3, &V, &P256_P); mod_sub(&X3, &X3, &V, &P256_P);
    mod_sub(&T, &V, &X3, &P256_P); mod_mul(&T, &Rv, &T, &P256_P);
    mod_mul(&S1, &S1, &J, &P256_P); mod_add(&S1, &S1, &S1, &P256_P);
    mod_sub(&Y3, &T, &S1, &P256_P);
    mod_add(&T, &a->z, &b->z, &P256_P); mod_mul(&T, &T, &T, &P256_P);
    mod_sub(&T, &T, &Z1Z1, &P256_P); mod_sub(&T, &T, &Z2Z2, &P256_P);
    mod_mul(&Z3, &T, &H, &P256_P);
    r->x = X3; r->y = Y3; r->z = Z3; /* alias-safe commit */
}
static void pt_mul(const jpt *p, const u256 *k, jpt *r) { /* L-to-R dbl-add */
    jpt acc; pt_inf(&acc);
    for (int bit = 255; bit >= 0; bit--) {
        pt_dbl(&acc, &acc);
        if ((k->v[bit >> 5] >> (bit & 31)) & 1u) {
            jpt t; pt_add(&acc, p, &t); acc = t;
        }
    }
    *r = acc;
}
static void pt_to_aff(const jpt *p, u256 *x, u256 *y) {
    u256 zi, z2; /* z^-1 via Fermat; z^2 */
    u256 e; e = P256_P; /* e = p-2 */
    u256 two; memset(&two, 0, sizeof two); two.v[0] = 2;
    uint32_t bw; u256_sub_raw(&e, &e, &two, &bw);
    mod_pow(&zi, &p->z, &e, &P256_P);
    mod_mul(&z2, &zi, &zi, &P256_P);
    mod_mul(x, &p->x, &z2, &P256_P);
    mod_mul(&z2, &z2, &zi, &P256_P);
    mod_mul(y, &p->y, &z2, &P256_P);
}
static int pt_oncurve(const u256 *x, const u256 *y) {
    u256 l, r, t, three;
    mod_mul(&l, y, y, &P256_P);
    mod_mul(&t, x, x, &P256_P); mod_mul(&r, &t, x, &P256_P);
    memset(&three, 0, sizeof three); three.v[0] = 3;
    mod_mul(&t, &three, x, &P256_P); mod_sub(&r, &r, &t, &P256_P);
    mod_add(&r, &r, &P256_B, &P256_P);
    return !u256_cmp(&l, &r);
}

/* ---- Shamir simultaneous mul: u*G + v*Q (FIPS 186-4 verify, own) ---- */
static void pt_mul2(const u256 *u, const jpt *G,
                    const u256 *v, const jpt *Q, jpt *r) {
    jpt T[4]; pt_inf(&T[0]); T[1] = *Q; T[2] = *G; pt_add(G, Q, &T[3]);
    jpt acc; pt_inf(&acc);
    for (int bit = 255; bit >= 0; bit--) {
        pt_dbl(&acc, &acc);
        int ui = (u->v[bit >> 5] >> (bit & 31)) & 1u;
        int vi = (v->v[bit >> 5] >> (bit & 31)) & 1u;
        if (ui | vi) { jpt t; pt_add(&acc, &T[(ui << 1) | vi], &t); acc = t; }
    }
    *r = acc;
}

/* ---- PEM/DER (own parser; key bytes only, no crypto copied) ---- */
static const uint8_t OID_P256[] = {0x06,0x08,0x2A,0x86,0x48,0xCE,0x3D,0x03,0x01,0x07};
static int pem_dearmor(const uint8_t *pem, size_t n,
                       uint8_t **der, size_t *dlen) {
    /* find first -----BEGIN...----- / -----END block, unb64 payload */
    const uint8_t *b = NULL, *e = NULL;
    for (size_t i = 0; i + 10 < n; i++)
        if (!memcmp(pem + i, "-----BEGIN", 10)) { b = pem + i; break; }
    if (!b) return fail("bad PEM");
    for (size_t i = 0; i + 8 < n; i++)
        if (!memcmp(pem + i, "-----END", 8)) { e = pem + i; break; }
    if (!e || e <= b) return fail("bad PEM");
    const uint8_t *p = memchr(b, '\n', e - b);
    if (!p) return fail("bad PEM");
    p++;
    buf body = {0};
    for (const uint8_t *q = p; q < e; q++)
        if (!isws(*q) && bputc(&body, *q)) { bfree(&body); return -1; }
    uint8_t *out = NULL; size_t ol = 0;
    int rc = unb64((char *)body.p, body.n, &out, &ol);
    bfree(&body);
    if (rc) return fail("bad PEM");
    *der = out; *dlen = ol; return 0;
}
/* structural TLV walk: collect 32B scalar OCTET STRING + 04||X||Y point */
typedef struct { int has_scalar; uint8_t scalar[32];
                 int has_point; uint8_t point[65]; } ecmat;
static int der_len(const uint8_t *d, size_t n, size_t *hlen, size_t *vlen) {
    if (n < 2) return -1;
    if (d[1] < 0x80) { *hlen = 2; *vlen = d[1]; return 0; }
    int nb = d[1] & 0x7F;
    if (nb < 1 || nb > 4 || (size_t)2 + nb > n) return -1;
    size_t v = 0;
    for (int i = 0; i < nb; i++) v = (v << 8) | d[2+i];
    *hlen = 2 + nb; *vlen = v; return 0;
}
static void der_walk(const uint8_t *d, size_t n, ecmat *m) {
    size_t pos = 0;
    while (pos < n) {
        if (pos + 2 > n) return;
        uint8_t tag = d[pos];
        size_t hl, vl;
        if (der_len(d + pos, n - pos, &hl, &vl)) return;
        if (pos + hl + vl > n) return;
        const uint8_t *v = d + pos + hl;
        if (tag == 0x04 && vl == 32 && !m->has_scalar) {
            memcpy(m->scalar, v, 32); m->has_scalar = 1;
        } else if (tag == 0x03 && vl == 66 && v[0] == 0x00 && v[1] == 0x04
                   && !m->has_point) {
            memcpy(m->point, v + 1, 65); m->has_point = 1;
        } else if ((tag & 0x20) || tag == 0x04) {
            /* constructed OR octet-string: contents may be DER (PKCS8). */
            if (tag != 0x04 || vl != 32) der_walk(v, vl, m);
        }
        pos += hl + vl;
    }
}
static int ec_parse(const uint8_t *pem, size_t pemn, const char *name,
                    int need_priv, u256 *priv, jpt *pub) {
    p256_init();
    uint8_t *der = NULL; size_t dl = 0;
    if (pem_dearmor(pem, pemn, &der, &dl)) return fail("%s invalid", name);
    int ok = 0;
    if (dl >= 10 && memmem(der, dl, OID_P256, sizeof OID_P256)) {
        ecmat m; memset(&m, 0, sizeof m);
        /* top must be SEQ; walk children */
        size_t hl, vl;
        if (!der_len(der + 1 - 1, dl, &hl, &vl) && der[0] == 0x30 &&
            hl + vl <= dl)
            der_walk(der + hl, vl, &m);
        if (need_priv && m.has_scalar) {
            u256 d; u256_frombytes_be(&d, m.scalar);
            u256 one; memset(&one, 0, sizeof one); one.v[0] = 1;
            if (u256_cmp(&d, &one) >= 0 && u256_cmp(&d, &P256_N) < 0) {
                *priv = d; ok = 1;
                if (pub) { /* priv->pub via scalar mult (uniform) */
                    jpt G, R; pt_set_aff(&G, &P256_GX, &P256_GY);
                    pt_mul(&G, &d, &R);
                    *pub = R; /* Jacobian; affine on use */
                }
            }
        }
        if (!need_priv && m.has_point) {
            u256 x, y;
            u256_frombytes_be(&x, m.point + 1);
            u256_frombytes_be(&y, m.point + 33);
            if (u256_cmp(&x, &P256_P) < 0 && u256_cmp(&y, &P256_P) < 0 &&
                pt_oncurve(&x, &y)) {
                if (pub) pt_set_aff(pub, &x, &y);
                ok = 1;
            }
        }
    }
    memset(der, 0, dl); free(der);
    if (!ok) return fail("%s invalid", name);
    return 0;
}
/* peer point from 65B blob (decrypt profiles 3/4 sender field). */
static int ec_peer(const uint8_t *raw65, jpt *pub) {
    p256_init();
    if (raw65[0] != 0x04) return -1;
    u256 x, y;
    u256_frombytes_be(&x, raw65 + 1); u256_frombytes_be(&y, raw65 + 33);
    if (u256_cmp(&x, &P256_P) >= 0 || u256_cmp(&y, &P256_P) >= 0) return -1;
    if (!pt_oncurve(&x, &y)) return -1;
    pt_set_aff(pub, &x, &y); return 0;
}
static void ec_x962(const jpt *pub, uint8_t out[65]) {
    u256 x, y; pt_to_aff(pub, &x, &y);
    out[0] = 0x04; u256_tobytes_be(&x, out + 1); u256_tobytes_be(&y, out + 33);
}
/* ECDH: x-coordinate of d*Q, 32B BE (SEC1 section 3.3.1). */
static int ecdh(const u256 *d, const jpt *Q, uint8_t out[32]) {
    jpt R; pt_mul(Q, d, &R);
    if (pt_isinf(&R)) return fail("ECDH failed");
    u256 x, y; pt_to_aff(&R, &x, &y);
    u256_tobytes_be(&x, out); return 0;
}
/* ECDSA sign (FIPS 186-4 section 6.4, random k) -> DER. */
static int ecdsa_sign(const u256 *d, const uint8_t hash[32],
                      uint8_t *der, size_t *derlen) {
    u256 z; u256_frombytes_be(&z, hash);
    /* reduce z mod n (equal-size hash: z as integer, mod n) */
    u512 ze; memset(&ze, 0, sizeof ze); memcpy(ze.v, z.v, 32);
    u256 zm; u512_mod(&ze, &P256_N, &zm);
    jpt G; pt_set_aff(&G, &P256_GX, &P256_GY);
    for (;;) {
        uint8_t kb[32]; u256 k;
        do { randbytes(kb, 32); u256_frombytes_be(&k, kb); }
        while (u256_iszero(&k) || u256_cmp(&k, &P256_N) >= 0);
        jpt R; pt_mul(&G, &k, &R);
        if (pt_isinf(&R)) continue;
        u256 rx, ry; pt_to_aff(&R, &rx, &ry);
        u512 re; memset(&re, 0, sizeof re); memcpy(re.v, rx.v, 32);
        u256 r; u512_mod(&re, &P256_N, &r);
        if (u256_iszero(&r)) continue;
        /* kinv via Fermat */
        u256 e, kinv; e = P256_N;
        uint32_t bw; u256 two; memset(&two, 0, sizeof two); two.v[0] = 2;
        u256_sub_raw(&e, &e, &two, &bw);
        mod_pow(&kinv, &k, &e, &P256_N);
        u256 rd; mod_mul(&rd, &r, d, &P256_N);
        u256 s1; mod_add(&s1, &rd, &zm, &P256_N);
        u256 s; mod_mul(&s, &kinv, &s1, &P256_N);
        if (u256_iszero(&s)) continue;
        uint8_t rb[32], sb[32];
        u256_tobytes_be(&r, rb); u256_tobytes_be(&s, sb);
        /* DER encode INTEGERs minimally */
        int ri = 0; while (ri < 31 && rb[ri] == 0) ri++;
        int si = 0; while (si < 31 && sb[si] == 0) si++;
        int rln = 32 - ri + (rb[ri] & 0x80 ? 1 : 0);
        int sln = 32 - si + (sb[si] & 0x80 ? 1 : 0);
        size_t tot = 2 + rln + 2 + sln;
        if (tot + 2 > 160) return fail("signature too long");
        uint8_t *p = der;
        *p++ = 0x30; *p++ = (uint8_t)tot;
        *p++ = 0x02; *p++ = (uint8_t)rln;
        if (rb[ri] & 0x80) *p++ = 0x00;
        memcpy(p, rb + ri, 32 - ri); p += 32 - ri;
        *p++ = 0x02; *p++ = (uint8_t)sln;
        if (sb[si] & 0x80) *p++ = 0x00;
        memcpy(p, sb + si, 32 - si); p += 32 - si;
        *derlen = p - der; return 0;
    }
}
/* ECDSA verify (FIPS 186-4); 0 valid / -1 invalid(fail msg set). */
static int ecdsa_verify(const jpt *Q, const uint8_t hash[32],
                        const uint8_t *der, size_t dl) {
    u256 r, s;
    do {
        if (dl < 8 || der[0] != 0x30) break;
        size_t tot = der[1];
        if (der[1] & 0x80) break; /* long form: reject (never valid here) */
        if (tot + 2 != dl) break;
        if (der[2] != 0x02) break;
        size_t rl = der[3];
        if (4 + rl + 2 > dl || der[4+rl] != 0x02) break;
        size_t sl = der[4+rl+1];
        if (4 + rl + 2 + sl != dl) break;
        const uint8_t *rb = der + 4, *sb = der + 4 + rl + 2;
        if (rl < 1 || rl > 33 || sl < 1 || sl > 33) break;
        uint8_t rbf[32]; memset(rbf, 0, 32);
        uint8_t sbf[32]; memset(sbf, 0, 32);
        const uint8_t *rp = rb; size_t rn = rl;
        /* DER INTEGER: one leading zero iff high bit set; strip at most one. */
        if (rn > 1 && *rp == 0x00) { rp++; rn--; }
        if (rn < 1 || rn > 32) break;
        memcpy(rbf + 32 - rn, rp, rn);
        const uint8_t *sp = sb; size_t sn = sl;
        if (sn > 1 && *sp == 0x00) { sp++; sn--; }
        if (sn < 1 || sn > 32) break;
        memcpy(sbf + 32 - sn, sp, sn);
        u256_frombytes_be(&r, rbf); u256_frombytes_be(&s, sbf);
        u256 one; memset(&one, 0, sizeof one); one.v[0] = 1;
        if (u256_cmp(&r, &one) < 0 || u256_cmp(&r, &P256_N) >= 0) break;
        if (u256_cmp(&s, &one) < 0 || u256_cmp(&s, &P256_N) >= 0) break;
        u256 z; u256_frombytes_be(&z, hash);
        u512 ze; memset(&ze, 0, sizeof ze); memcpy(ze.v, z.v, 32);
        u256 zm; u512_mod(&ze, &P256_N, &zm);
        u256 e, w; e = P256_N;
        uint32_t bw; u256 two; memset(&two, 0, sizeof two); two.v[0] = 2;
        u256_sub_raw(&e, &e, &two, &bw);
        mod_pow(&w, &s, &e, &P256_N);
        u256 u1, u2; mod_mul(&u1, &zm, &w, &P256_N); mod_mul(&u2, &r, &w, &P256_N);
        jpt G; pt_set_aff(&G, &P256_GX, &P256_GY);
        jpt P; pt_mul2(&u1, &G, &u2, Q, &P);
        if (pt_isinf(&P)) break;
        u256 px, py; pt_to_aff(&P, &px, &py);
        u512 pe; memset(&pe, 0, sizeof pe); memcpy(pe.v, px.v, 32);
        u256 pm; u512_mod(&pe, &P256_N, &pm);
        if (!u256_cmp(&pm, &r)) return 0;
        break;
    } while (0);
    return fail("signature invalid");
}

/* ================= LZ4 block (public LZ4 Block Format Description) == */
static int lz4_decompress(const uint8_t *in, size_t il,
                          uint8_t *out, size_t ol, size_t *produced) {
    size_t ip = 0, op = 0;
    for (;;) {
        if (ip >= il) return -1;
        uint8_t tok = in[ip++];
        size_t lit = tok >> 4;
        if (lit == 15) { uint8_t c; do { if (ip >= il) return -1; c = in[ip++]; lit += c; } while (c == 255); }
        if (op + lit > ol || ip + lit > il) return -1;
        memcpy(out + op, in + ip, lit); op += lit; ip += lit;
        if (ip >= il) break; /* last literals */
        if (ip + 2 > il) return -1;
        size_t off = in[ip] | ((size_t)in[ip+1] << 8); ip += 2;
        if (off == 0 || off > op) return -1;
        size_t mt = (tok & 0xF) + 4;
        if ((tok & 0xF) == 15) { uint8_t c; do { if (ip >= il) return -1; c = in[ip++]; mt += c; } while (c == 255); }
        if (op + mt > ol) return -1;
        /* overlap-safe copy */
        for (size_t k = 0; k < mt; k++) out[op + k] = out[op - off + k];
        op += mt;
    }
    *produced = op; return 0;
}
/* simple hash-chain compressor; output always valid (may exceed input). */
static size_t lz4_compress(const uint8_t *in, size_t il, uint8_t *out) {
    static int tab[1 << 12];
    for (int i = 0; i < (1 << 12); i++) tab[i] = -1;
    size_t ip = 0, op = 0, anchor = 0;
    size_t iplimit = il > 12 ? il - 12 : 0;
    while (ip < iplimit) {
        uint32_t v = in[ip] | ((uint32_t)in[ip+1] << 8) |
                     ((uint32_t)in[ip+2] << 16) | ((uint32_t)in[ip+3] << 24);
        uint32_t h = (v * 2654435761u) >> 20;
        size_t ref = (size_t)tab[h & 0xFFF]; tab[h & 0xFFF] = (int)ip;
        size_t mlen = 0;
        if (ref < ip && ip - ref <= 65535 && ref + 4 <= il &&
            in[ref] == in[ip] && in[ref+1] == in[ip+1] &&
            in[ref+2] == in[ip+2] && in[ref+3] == in[ip+3]) {
            mlen = 4;
            while (ip + mlen < il && in[ref + mlen] == in[ip + mlen]) mlen++;
        }
        if (mlen >= 4) {
            size_t lit = ip - anchor, mt = mlen - 4, off = ip - ref;
            out[op++] = (uint8_t)((lit >= 15 ? 15 : lit) << 4 |
                                  (mt >= 15 ? 15 : mt));
            if (lit >= 15) {
                lit -= 15;
                while (lit >= 255) { out[op++] = 255; lit -= 255; }
                out[op++] = (uint8_t)lit;
            }
            memcpy(out + op, in + anchor, ip - anchor); op += ip - anchor;
            out[op++] = (uint8_t)off; out[op++] = (uint8_t)(off >> 8);
            if (mt >= 15) {
                mt -= 15;
                while (mt >= 255) { out[op++] = 255; mt -= 255; }
                out[op++] = (uint8_t)mt;
            }
            ip += mlen; anchor = ip;
        } else ip++;
    }
    { /* tail literals (also covers il<=12 whole-input path) */
        size_t lit = il - anchor;
        out[op++] = (uint8_t)((lit >= 15 ? 15 : lit) << 4);
        if (lit >= 15) {
            lit -= 15;
            while (lit >= 255) { out[op++] = 255; lit -= 255; }
            out[op++] = (uint8_t)lit;
        }
        memcpy(out + op, in + anchor, lit); op += lit;
    }
    return op;
}

/* ================= codecs ================= */
/* zlib (system libz; level 6 == Python zlib.compress default). */
static int z_comp(const uint8_t *in, size_t il, uint8_t **out, size_t *ol) {
    uLong bl = compressBound(il);
    uint8_t *b = malloc(bl);
    if (!b) return fail("out of memory");
    if (compress2(b, &bl, in, il, 6) != Z_OK) { free(b); return fail("zlib failed"); }
    *out = b; *ol = bl; return 0;
}
static int z_decomp(const uint8_t *in, size_t il, uint8_t **out, size_t *ol) {
    if (!il) return fail("zlib failed"); /* no progress possible */
    z_stream zs; memset(&zs, 0, sizeof zs);
    if (inflateInit(&zs) != Z_OK) return fail("zlib failed");
    buf b = {0}; uint8_t tmp[65536]; int zr;
    zs.next_in = (Bytef *)in; zs.avail_in = (uInt)il;
    /* NOTE: inflate input capped at 4G via uInt; AEA segments fit. */
    if ((size_t)zs.avail_in != il) { inflateEnd(&zs); return fail("zlib failed"); }
    do {
        zs.next_out = tmp; zs.avail_out = sizeof tmp;
        zr = inflate(&zs, Z_NO_FLUSH);
        if (zr != Z_OK && zr != Z_STREAM_END) {
            inflateEnd(&zs); bfree(&b); return fail("zlib failed");
        }
        if (bput(&b, tmp, sizeof tmp - zs.avail_out)) {
            inflateEnd(&zs); bfree(&b); return -1;
        }
    } while (zr != Z_STREAM_END);
    inflateEnd(&zs);
    *out = b.p; *ol = b.n; return 0; /* trailing input ignored, like Python */
}
/* lzma (pinned liblzma 5.8.4 direct link; preset 6 CRC64 == Python). */
static int x_comp(const uint8_t *in, size_t il, uint8_t **out, size_t *ol) {
    lzma_stream s = LZMA_STREAM_INIT;
    if (lzma_easy_encoder(&s, 6, LZMA_CHECK_CRC64) != LZMA_OK)
        return fail("lzma failed");
    buf b = {0}; uint8_t tmp[65536];
    s.next_in = in; s.avail_in = il;
    lzma_ret r;
    do {
        s.next_out = tmp; s.avail_out = sizeof tmp;
        r = lzma_code(&s, LZMA_FINISH);
        if (r != LZMA_OK && r != LZMA_STREAM_END) {
            lzma_end(&s); bfree(&b); return fail("lzma failed");
        }
        if (bput(&b, tmp, sizeof tmp - s.avail_out)) {
            lzma_end(&s); bfree(&b); return -1;
        }
    } while (r != LZMA_STREAM_END);
    lzma_end(&s); *out = b.p; *ol = b.n; return 0;
}
static int x_decomp(const uint8_t *in, size_t il, uint8_t **out, size_t *ol) {
    if (!il) return fail("lzma failed"); /* no progress possible */
    lzma_stream s = LZMA_STREAM_INIT;
    if (lzma_auto_decoder(&s, UINT64_MAX, 0) != LZMA_OK)
        return fail("lzma failed");
    buf b = {0}; uint8_t tmp[65536];
    s.next_in = in; s.avail_in = il;
    lzma_ret r;
    do {
        s.next_out = tmp; s.avail_out = sizeof tmp;
        r = lzma_code(&s, LZMA_FINISH);
        if (r != LZMA_OK && r != LZMA_STREAM_END) {
            lzma_end(&s); bfree(&b); return fail("lzma failed");
        }
        if (bput(&b, tmp, sizeof tmp - s.avail_out)) {
            lzma_end(&s); bfree(&b); return -1;
        }
        if (r == LZMA_STREAM_END && s.avail_in != 0) {
            /* Python lzma.decompress rejects trailing data. */
            lzma_end(&s); bfree(&b); return fail("lzma failed");
        }
    } while (r != LZMA_STREAM_END);
    lzma_end(&s); *out = b.p; *ol = b.n; return 0;
}
/* lzfse / lzbitmap / lzraven via macOS compression.h buffer API (no shims).
 * COMPRESSION_LZBITMAP/LZRAVEN are buffer-API-only (header: macOS 12+/27+). */
static int cap_decode(int alg, const char *ename,
                      const uint8_t *in, size_t il,
                      uint8_t *out, size_t ol) {
    if (ol == 0) return fail("%s failed", ename);
    size_t got = compression_decode_buffer(out, ol, in, il, NULL,
                                           (compression_algorithm)alg);
    if (got != ol) return fail("%s failed", ename);
    return 0;
}
static int cap_encode(int alg,
                      const uint8_t *in, size_t il,
                      uint8_t **out, size_t *ol) {
    size_t cap = il + il / 16 + 1024;
    uint8_t *b = malloc(cap ? cap : 64);
    if (!b) return fail("out of memory");
    size_t got = compression_encode_buffer(b, cap ? cap : 64, in, il, NULL,
                                           (compression_algorithm)alg);
    if (got == 0) { free(b); return fail("lzfse encode failed"); }
    *out = b; *ol = got; return 0;
}

/* ================= ver/enc + KD ================= */
static int dec_ver(const uint8_t key[/*32|80*/], size_t klen,
                   const uint8_t *data, size_t dn,
                   const uint8_t *salt, size_t sn, const uint8_t want[32],
                   uint8_t **plain, size_t *plen) {
    uint8_t m[32]; amac(key, data, dn, salt, sn, m);
    /* constant-time compare (fail-closed like hmac.compare_digest). */
    uint32_t d = 0; for (int i = 0; i < 32; i++) d |= m[i] ^ want[i];
    if (d) { memset(m, 0, 32); return fail("HMAC mismatch"); }
    if (klen == 80) {
        uint8_t *p = malloc(dn ? dn : 1);
        if (!p) return fail("out of memory");
        if (aes256ctr(key + 32, key + 64, data, p, dn)) { free(p); return -1; }
        *plain = p; *plen = dn; return 0;
    }
    uint8_t *p = malloc(dn ? dn : 1);
    if (!p) return fail("out of memory");
    memcpy(p, data, dn); *plain = p; *plen = dn; return 0;
}
static int enc_ver(const uint8_t key[/*32|80*/], size_t klen,
                   const uint8_t *data, size_t dn,
                   const uint8_t *salt, size_t sn,
                   uint8_t **stored, size_t *slen, uint8_t tag[32]) {
    uint8_t *st = malloc(dn ? dn : 1);
    if (!st) return fail("out of memory");
    if (klen == 80) {
        if (aes256ctr(key + 32, key + 64, data, st, dn)) { free(st); return -1; }
    } else memcpy(st, data, dn);
    amac(key, st, dn, salt, sn, tag);
    *stored = st; *slen = dn; return 0;
}
typedef struct { uint8_t main[32]; size_t ks; } KD;
static void kd_sigkey(const KD *k, uint8_t out[/*ks*/]) {
    uint8_t inner[32];
    hkdf(k->main, 32, (uint8_t *)"AEA_SEK", 7, NULL, 0, inner, 32);
    hkdf(inner, 32, (uint8_t *)"AEA_SEK2", 8, NULL, 0, out, k->ks);
    memset(inner, 0, 32);
}
static void kd_rootkey(const KD *k, uint8_t *out) {
    hkdf(k->main, 32, (uint8_t *)"AEA_RHEK", 8, NULL, 0, out, k->ks);
}
static void kd_clustkey(const KD *k, uint32_t i, uint8_t out[32]) {
    uint8_t info[10]; memcpy(info, "AEA_CK", 6); put32le(info + 6, i);
    hkdf(k->main, 32, info, 10, NULL, 0, out, 32);
}
static void kd_chek(const KD *k, const uint8_t ck[32], uint8_t *out) {
    hkdf(ck, 32, (uint8_t *)"AEA_CHEK", 8, NULL, 0, out, k->ks);
}
static void kd_segkey(const KD *k, const uint8_t ck[32], uint32_t i, uint8_t *out) {
    uint8_t info[10]; memcpy(info, "AEA_SK", 6); put32le(info + 6, i);
    hkdf(ck, 32, info, 10, NULL, 0, out, k->ks);
}

/* ================= decomp / comp dispatch ================= */
static int decomp(char alg, const uint8_t *data, size_t dn, size_t osz,
                  uint8_t **out, size_t *ol) {
    if (alg == '-') {
        uint8_t *p = malloc(dn ? dn : 1);
        if (!p) return fail("out of memory");
        memcpy(p, data, dn); *out = p; *ol = dn; return 0;
    }
    if (alg == 'z') {
        if (z_decomp(data, dn, out, ol)) return -1;
        return 0;
    }
    if (alg == 'x') {
        if (x_decomp(data, dn, out, ol)) return -1;
        return 0;
    }
    if (alg == '4') {
        uint8_t *p = malloc(osz ? osz : 1);
        if (!p) return fail("out of memory");
        size_t got = 0;
        if (lz4_decompress(data, dn, p, osz, &got) || got != osz) {
            free(p); return fail("lz4 failed");
        }
        *out = p; *ol = osz; return 0;
    }
    if (alg == 'e' || alg == 'b' || alg == 'm') {
        int ca = alg == 'e' ? COMPRESSION_LZFSE :
                 alg == 'b' ? COMPRESSION_LZBITMAP : COMPRESSION_LZRAVEN;
        uint8_t *p = malloc(osz ? osz : 1);
        if (!p) return fail("out of memory");
        const char *nm = alg == 'e' ? "lzfse" : alg == 'b' ? "lzbitmap" : "lzraven";
        if (cap_decode(ca, nm, data, dn, p, osz)) { free(p); return -1; }
        *out = p; *ol = osz; return 0;
    }
    return fail("codec '%c' unsupported", alg);
}
static int comp_enc(char alg, const uint8_t *data, size_t dn,
                    uint8_t **out, size_t *ol) {
    if (alg == '-') {
        uint8_t *p = malloc(dn ? dn : 1);
        if (!p) return fail("out of memory");
        memcpy(p, data, dn); *out = p; *ol = dn; return 0;
    }
    if (alg == 'z') return z_comp(data, dn, out, ol);
    if (alg == 'x') return x_comp(data, dn, out, ol);
    if (alg == '4') {
        size_t cap = dn + dn / 255 + 16;
        uint8_t *p = malloc(cap ? cap : 16);
        if (!p) return fail("out of memory");
        *ol = lz4_compress(data, dn, p); *out = p; return 0;
    }
    if (alg == 'e') return cap_encode(COMPRESSION_LZFSE, data, dn, out, ol);
    return fail("codec '%c' has no encoder in v1", alg);
}
static int cksum(int alg, const uint8_t *data, size_t dn,
                 uint8_t out[32], size_t *clen) {
    if (alg == 0) { *clen = 0; return 0; }
    if (alg == 1) { murmur64a(data, dn, out); *clen = 8; return 0; }
    if (alg == 2) { sha256(data, dn, out); *clen = 32; return 0; }
    return fail("checksum %d unsupported", alg);
}

/* ================= framing ================= */
static const size_t KSZ[6] = {32, 80, 80, 80, 80, 80};
static const size_t SSZ[6] = {128, 0, 160, 0, 160, 0};
static const size_t PSZ[6] = {32, 0, 0, 65, 65, 0};
static const size_t CSZ[3] = {0, 8, 32};
static const uint32_t SCRYPT_N[4] = {0x4000, 0x10000, 0x40000, 0x100000};

typedef struct { const uint8_t *p; size_t n, pos; } cur;
static int cread(cur *c, size_t n, const uint8_t **o) {
    if (c->pos + n > c->n || c->pos + n < c->pos) return -1;
    *o = c->p + c->pos; c->pos += n; return 0;
}

int aead_id(const uint8_t *blob, size_t len, uint8_t digest[32]) {
    if (len < 12 || memcmp(blob, "AEA1", 4)) return fail("bad magic");
    int prof = blob[4] | (blob[5] << 8) | (blob[6] << 16);
    if (prof < 0 || prof > 5) return fail("bad profile");
    uint32_t asz = get32le(blob + 8);
    size_t n = 12 + asz + SSZ[prof] + PSZ[prof] + 32 + 32 + 48 + 32;
    if (len < n) return fail("truncated prologue");
    sha256(blob, n, digest); return 0;
}

static int slice_range(const uint8_t *full, size_t fl,
                       int has_off, long off, int has_size, long size,
                       uint8_t **out, size_t *ol) {
    long start = 0, end = (long)fl;
    if (has_off) {
        start = off < 0 ? (long)fl + off : off;
        if (start < 0) start = 0; if (start > (long)fl) start = fl;
        end = start;
        if (!has_size) end = fl;
        else {
            long e = off + (size < 0 ? (long)fl + size - off : size);
            /* Python: full[off:off+size]; replicate via raw indices then clamp */
            e = off + size;
            if (off < 0) { long o2 = (long)fl + off; e = o2 + size; }
            if (size < 0 && !has_off) e = (long)fl + size;
            end = e;
            if (end < 0) end = 0; if (end > (long)fl) end = fl;
            if (end < start) end = start;
        }
    }
    size_t n = (size_t)(end - start);
    uint8_t *p = malloc(n ? n : 1);
    if (!p) return fail("out of memory");
    memcpy(p, full + start, n); *out = p; *ol = n; return 0;
}

static int check_password(const char *pw) {
    if (!pw || !*pw) {
        /* NOTE: Python `if password is None` -> "password required"; empty
         * string is falsy at CLI layer (never passed). Library: "" treated
         * as absent to match CLI. */
        return fail("password required");
    }
    if (strlen(pw) < 20) return fail("Password is too short");
    return 0;
}

int aead_decrypt(const uint8_t *blob, size_t blen, const aead_dec_opt *o,
                 uint8_t **out, size_t *out_len) {
    p256_init();
    cur c = {blob, blen, 0};
    const uint8_t *hdr, *auth, *sig, *pub, *salt, *rmac, *rdata, *cmac;
    if (cread(&c, 12, &hdr) || memcmp(hdr, "AEA1", 4))
        return fail("bad magic");
    int prof = hdr[4] | (hdr[5] << 8) | (hdr[6] << 16);
    int sstr = hdr[7];
    if (prof < 0 || prof > 5) return fail("bad profile");
    if (prof == 5 && (sstr < 0 || sstr > 3)) return fail("bad scrypt strength");
    uint32_t auth_sz = get32le(hdr + 8);
    if (cread(&c, auth_sz, &auth)) return fail("truncated prologue");
    size_t sig_start = c.pos;
    if (cread(&c, SSZ[prof], &sig)) return fail("truncated prologue");
    size_t sig_end = c.pos;
    if (cread(&c, PSZ[prof], &pub)) return fail("truncated prologue");
    if (cread(&c, 32, &salt)) return fail("truncated prologue");
    if (cread(&c, 32, &rmac)) return fail("truncated prologue");
    if (cread(&c, 48, &rdata)) return fail("truncated prologue");
    if (cread(&c, 32, &cmac)) return fail("truncated prologue");
    size_t prologue_end = c.pos;

    uint8_t symkey[80]; size_t symlen = 0;
    jpt sender, recip, spub;
    int has_sender = 0, has_recip = 0, has_spub = 0;
    uint8_t kdsalt[32];
    memcpy(kdsalt, salt, 32);
    if (prof == 0) {
        memcpy(symkey, pub, 32); symlen = 32;
    } else if (prof == 1 || prof == 2) {
        if (!o->symkey || o->symkey_len != 32)
            return fail("symmetric key required (32B)");
        memcpy(symkey, o->symkey, 32); symlen = 32;
    } else if (prof == 3 || prof == 4) {
        if (!o->recip_priv) return fail("recipient_priv required");
        u256 d;
        if (ec_parse(o->recip_priv, o->recip_priv_len, "recipient_priv", 1, &d, &recip))
            return -1;
        has_recip = 1;
        if (ec_peer(pub, &sender)) return fail("sender_pub invalid");
        has_sender = 1;
        if (ecdh(&d, &sender, symkey)) return -1;
        symlen = 32;
        memset(&d, 0, sizeof d);
    } else if (prof == 5) {
        if (check_password(o->password)) return -1;
        uint8_t ext[64];
        hkdf(salt, 32, (uint8_t *)"AEA_SCRYPT", 10, NULL, 0, ext, 64);
        memcpy(kdsalt, ext + 32, 32);
        if (scrypt((uint8_t *)o->password, strlen(o->password),
                   ext, 32, SCRYPT_N[sstr], symkey)) {
            memset(ext, 0, 64); return -1;
        }
        memset(ext, 0, 64); symlen = 32;
    }
    if (prof == 0 || prof == 2 || prof == 4) {
        if (!o->sign_pub) return fail("sign_pub required");
        u256 dummy;
        if (ec_parse(o->sign_pub, o->sign_pub_len, "sign_pub", 0, &dummy, &spub))
            return -1;
        has_spub = 1;
    }
    uint8_t info[7 + 4 + 65 * 3]; size_t il = 0;
    memcpy(info, "AEA_AMK", 7); il = 7;
    info[il++] = hdr[4]; info[il++] = hdr[5]; info[il++] = hdr[6];
    info[il++] = hdr[7];
    if (has_sender) { ec_x962(&sender, info + il); il += 65; }
    if (has_recip) { ec_x962(&recip, info + il); il += 65; }
    if (has_spub) { ec_x962(&spub, info + il); il += 65; }
    KD kd; kd.ks = KSZ[prof];
    hkdf(symkey, symlen, info, il, kdsalt, 32, kd.main, 32);

    if (prof == 0 || prof == 2 || prof == 4) {
        uint8_t s[128];
        if (prof != 0) {
            uint8_t sk[80]; kd_sigkey(&kd, sk);
            uint8_t *sp = NULL; size_t sl = 0;
            int rc = dec_ver(sk, 80, sig, 128, NULL, 0, sig + 128, &sp, &sl);
            memset(sk, 0, 80);
            if (rc) return -1;
            if (sl != 128) { free(sp); return fail("signature invalid"); }
            memcpy(s, sp, 128); free(sp);
        } else memcpy(s, sig, 128);
        size_t derlen = (size_t)s[1] + 2;
        if (derlen > 128) derlen = 128; /* Python slice truncates silently */
        /* pro = blob[:sig_start] + zeros + blob[sig_end:prologue_end] */
        buf pro = {0};
        if (bput(&pro, blob, sig_start)) return -1;
        uint8_t z[160]; memset(z, 0, SSZ[prof]);
        if (bput(&pro, z, SSZ[prof]) ||
            bput(&pro, blob + sig_end, prologue_end - sig_end)) {
            bfree(&pro); return -1;
        }
        uint8_t h[32]; sha256(pro.p, pro.n, h); bfree(&pro);
        if (ecdsa_verify(&spub, h, s, derlen)) return -1;
    }
    /* root */
    uint8_t rk[80]; kd_rootkey(&kd, rk);
    uint8_t csalt[64]; memcpy(csalt, cmac, 32); memcpy(csalt + 32, auth, auth_sz);
    uint8_t *rh = NULL; size_t rhl = 0;
    if (dec_ver(rk, kd.ks, rdata, 48, csalt, 32 + auth_sz, rmac, &rh, &rhl)) {
        memset(rk, 0, 80); return -1;
    }
    memset(rk, 0, 80);
    if (rhl < 26) { free(rh); return fail("HMAC mismatch"); }
    uint64_t orig = 0, arc = 0; uint32_t segper = 0;
    memcpy(&orig, rh, 8);
    /* LE loads */
    orig = (uint64_t)rh[0] | ((uint64_t)rh[1] << 8) | ((uint64_t)rh[2] << 16) |
           ((uint64_t)rh[3] << 24) | ((uint64_t)rh[4] << 32) |
           ((uint64_t)rh[5] << 40) | ((uint64_t)rh[6] << 48) |
           ((uint64_t)rh[7] << 56);
    arc = (uint64_t)rh[8] | ((uint64_t)rh[9] << 8) | ((uint64_t)rh[10] << 16) |
          ((uint64_t)rh[11] << 24) | ((uint64_t)rh[12] << 32) |
          ((uint64_t)rh[13] << 40) | ((uint64_t)rh[14] << 48) |
          ((uint64_t)rh[15] << 56);
    segper = get32le(rh + 20);
    char comp = (char)rh[24]; int ckalg = rh[25];
    free(rh);
    if (ckalg < 0 || ckalg > 2) return fail("bad checksum alg");
    if (blen < arc) return fail("truncated archive");
    uint8_t padkey[32];
    hkdf(kd.main, 32, (uint8_t *)"AEA_PAK", 7, NULL, 0, padkey, 32);
    if (orig == 0) {
        if (arc > prologue_end) {
            uint8_t m[32];
            /* HMAC(padkey, blob[pe:arc]) == cmac */
            buf b = {0};
            if (bput(&b, blob + prologue_end, arc - prologue_end)) return -1;
            hmac_sha256(padkey, 32, b.p, b.n, m); bfree(&b);
            uint32_t d = 0;
            for (int i = 0; i < 32; i++) d |= m[i] ^ cmac[i];
            if (d) return fail("padding auth failed");
        }
        return slice_range(blob, 0, o->has_range_off, o->range_off,
                           o->has_range_size, o->range_size, out, out_len);
    }
    size_t shsz = 8 + CSZ[ckalg];
    buf obuf = {0};
    int ci = 0;
    for (;;) {
        uint8_t ck[32]; kd_clustkey(&kd, ci, ck);
        uint8_t chk[80]; kd_chek(&kd, ck, chk);
        const uint8_t *shs, *nmac, *sms;
        if (cread(&c, shsz * segper, &shs) || cread(&c, 32, &nmac) ||
            cread(&c, 32 * (size_t)segper, &sms))
            { bfree(&obuf); return fail("truncated cluster header"); }
        size_t nsslen = 32 + 32 * (size_t)segper;
        uint8_t *nss = malloc(nsslen ? nsslen : 1);
        if (!nss) { bfree(&obuf); return fail("out of memory"); }
        memcpy(nss, nmac, 32); memcpy(nss + 32, sms, 32 * (size_t)segper);
        uint8_t *sh = NULL; size_t shl = 0;
        int dvr = dec_ver(chk, kd.ks, shs, shsz * segper, nss, nsslen,
                          cmac, &sh, &shl);
        free(nss);
        if (dvr) {
            bfree(&obuf); return -1;
        }
        memset(chk, 0, 80);
        (void)shl;
        for (uint32_t i = 0; i < segper; i++) {
            const uint8_t *e = sh + shsz * i;
            uint32_t osz = get32le(e), csz = get32le(e + 4);
            const uint8_t *want_ck = e + 8;
            const uint8_t *data;
            if (cread(&c, csz, &data)) {
                free(sh); bfree(&obuf); return fail("truncated segment");
            }
            uint8_t sk[80]; kd_segkey(&kd, ck, i, sk);
            uint8_t *seg = NULL; size_t segl = 0;
            int rc = dec_ver(sk, kd.ks, data, csz, NULL, 0,
                             sms + 32 * (size_t)i, &seg, &segl);
            memset(sk, 0, 80);
            if (rc) { free(sh); bfree(&obuf); return -1; }
            uint8_t *plain = seg; size_t plainl = segl;
            uint8_t *dp = NULL; size_t dpl = 0;
            if (osz > csz) {
                if (decomp(comp, seg, segl, osz, &dp, &dpl)) {
                    free(seg); free(sh); bfree(&obuf); return -1;
                }
                free(seg); plain = dp; plainl = dpl;
            }
            if (plainl != osz) {
                free(plain); free(sh); bfree(&obuf);
                return fail("segment size wrong");
            }
            uint8_t ckout[32]; size_t cklen = 0;
            if (cksum(ckalg, plain, plainl, ckout, &cklen)) {
                free(plain); free(sh); bfree(&obuf); return -1;
            }
            /* constant-time compare for stored checksums */
            uint32_t dfr = 0;
            for (size_t k = 0; k < cklen; k++) dfr |= ckout[k] ^ want_ck[k];
            if (dfr) {
                free(plain); free(sh); bfree(&obuf);
                return fail("checksum wrong");
            }
            if (bput(&obuf, plain, plainl)) {
                free(plain); free(sh); bfree(&obuf); return -1;
            }
            free(plain);
            if (obuf.n >= orig) {
                size_t padstart = c.pos;
                if (arc > padstart) {
                    uint8_t m[32]; hmac_sha256(padkey, 32, blob + padstart,
                                              arc - padstart, m);
                    uint32_t dd = 0;
                    for (int k = 0; k < 32; k++) dd |= m[k] ^ nmac[k];
                    if (dd) { free(sh); bfree(&obuf); return fail("padding auth failed"); }
                }
                uint8_t *full = obuf.p; size_t fulll = obuf.n;
                uint8_t *sl = NULL; size_t sll = 0;
                /* truncate to orig first (Python: getvalue()[:orig]) */
                int rc2 = slice_range(full, orig < fulll ? (size_t)orig : fulll,
                                      o->has_range_off, o->range_off,
                                      o->has_range_size, o->range_size,
                                      &sl, &sll);
                free(full); free(sh);
                if (rc2) return -1;
                *out = sl; *out_len = sll; return 0;
            }
        }
        free(sh);
        cmac = nmac; ci++;
        if (ci > 1000000) { bfree(&obuf); return fail("truncated archive"); }
    }
}

int aead_encrypt(const uint8_t *data, size_t data_len,
                 const aead_enc_opt *o, uint8_t **out, size_t *out_len) {
    p256_init();
    int profile = o->profile;
    if (profile < 0 || profile > 5) return fail("bad profile");
    if (o->block_size == 0) return fail("bad block size");
    char comp = o->comp;
    if (comp != '-' && comp != 'z' && comp != 'x' && comp != '4' && comp != 'e')
        return fail("bad algorithm");
    int ckalg = o->ckalg;
    if (ckalg < 0 || ckalg > 2) return fail("bad checksum");
    if (o->block_size == 0) return fail("bad block size");
    uint64_t padq = o->padq;
    if (padq != 0 && padq < 16) return fail("bad padding (must be 0/none or >= 16)");
    int sstr = 0; /* pinned (proto v1/v2: scrypt strength 0 on encrypt) */
    size_t ks = KSZ[profile];

    uint8_t symkey[80]; size_t symlen = 0;
    u256 epriv; int has_epriv = 0;
    jpt sender, recip, spub;
    int has_sender = 0, has_recip = 0, has_spub = 0;
    uint8_t pub[65]; size_t publen = 0;
    if (profile == 0) {
        if (!o->sign_priv) return fail("sign_priv required");
        u256 d;
        if (ec_parse(o->sign_priv, o->sign_priv_len, "sign_priv", 1, &d, &spub))
            return -1;
        has_spub = 1; memset(&d, 0, sizeof d);
        randbytes(symkey, 32); symlen = 32;
        memcpy(pub, symkey, 32); publen = 32;
    } else if (profile == 1 || profile == 2) {
        if (!o->symkey || o->symkey_len != 32)
            return fail("symmetric key required (32B)");
        memcpy(symkey, o->symkey, 32); symlen = 32;
        if (profile == 2) {
            if (!o->sign_priv) return fail("sign_priv required");
            u256 d;
            if (ec_parse(o->sign_priv, o->sign_priv_len, "sign_priv", 1, &d, &spub))
                return -1;
            has_spub = 1; memset(&d, 0, sizeof d);
        }
    } else if (profile == 3 || profile == 4) {
        if (!o->recip_pub) return fail("recipient_pub required");
        u256 dummy;
        if (ec_parse(o->recip_pub, o->recip_pub_len, "recipient_pub", 0, &dummy, &recip))
            return -1;
        has_recip = 1;
        if (o->eph_priv) {
            if (ec_parse(o->eph_priv, o->eph_priv_len, "eph_priv", 1, &epriv, &sender))
                return -1;
            has_epriv = 1;
        } else {
            uint8_t kb[32];
            do { randbytes(kb, 32); u256_frombytes_be(&epriv, kb); }
            while (u256_iszero(&epriv) || u256_cmp(&epriv, &P256_N) >= 0);
            jpt G; pt_set_aff(&G, &P256_GX, &P256_GY);
            pt_mul(&G, &epriv, &sender); has_epriv = 1;
        }
        has_sender = 1;
        uint8_t sx[65]; ec_x962(&sender, sx);
        memcpy(pub, sx, 65); publen = 65;
        if (ecdh(&epriv, &recip, symkey)) {
            memset(&epriv, 0, sizeof epriv); return -1;
        }
        memset(&epriv, 0, sizeof epriv);
        symlen = 32;
        if (profile == 4) {
            if (!o->sign_priv) return fail("sign_priv required");
            u256 d;
            if (ec_parse(o->sign_priv, o->sign_priv_len, "sign_priv", 1, &d, &spub))
                return -1;
            has_spub = 1; memset(&d, 0, sizeof d);
        }
    } else if (profile == 5) {
        if (check_password(o->password)) return -1;
        symlen = 32; /* filled below after salt */
    }
    (void)has_epriv;
    uint8_t salt[32];
    if (o->salt) {
        if (o->salt_len != 32) return fail("salt must be 32B");
        memcpy(salt, o->salt, 32);
    } else randbytes(salt, 32);
    uint8_t kdsalt[32]; memcpy(kdsalt, salt, 32);
    if (profile == 5) {
        uint8_t ext[64];
        hkdf(salt, 32, (uint8_t *)"AEA_SCRYPT", 10, NULL, 0, ext, 64);
        if (scrypt((uint8_t *)o->password, strlen(o->password),
                   ext, 32, SCRYPT_N[sstr], symkey)) {
            memset(ext, 0, 64); return -1;
        }
        memcpy(kdsalt, ext + 32, 32); memset(ext, 0, 64);
    }
    uint8_t info[7 + 4 + 65 * 3]; size_t il = 0;
    memcpy(info, "AEA_AMK", 7); il = 7;
    info[il++] = profile & 0xFF; info[il++] = (profile >> 8) & 0xFF;
    info[il++] = (profile >> 16) & 0xFF; info[il++] = sstr;
    if (has_sender) { ec_x962(&sender, info + il); il += 65; }
    if (has_recip) { ec_x962(&recip, info + il); il += 65; }
    if (has_spub) { ec_x962(&spub, info + il); il += 65; }
    KD kd; kd.ks = ks;
    hkdf(symkey, symlen, info, il, kdsalt, 32, kd.main, 32);

    if (o->nmacs && (o->nmacs_len % 32)) return fail("nmacs must be 32B multiples");
    if (o->smacs && (o->smacs_len % 32)) return fail("smacs must be 32B multiples");

    /* segment pre-compress */
    size_t bs = (size_t)o->block_size;
    size_t nseg = data_len ? (data_len + bs - 1) / bs : 0;
    uint8_t **stored = NULL; size_t *storedl = NULL;
    if (nseg) {
        stored = calloc(nseg, sizeof *stored);
        storedl = calloc(nseg, sizeof *storedl);
        if (!stored || !storedl) {
            free(stored); free(storedl); return fail("out of memory");
        }
        for (size_t gi = 0; gi < nseg; gi++) {
            size_t off = gi * bs, pl = data_len - off < bs ? data_len - off : bs;
            uint8_t *cd = NULL; size_t cdl = 0;
            if (comp_enc(comp, data + off, pl, &cd, &cdl)) {
                for (size_t k = 0; k < gi; k++) free(stored[k]);
                free(stored); free(storedl); return -1;
            }
            if (cdl < pl) { stored[gi] = cd; storedl[gi] = cdl; }
            else { free(cd); stored[gi] = NULL; storedl[gi] = pl; }
            /* NULL stored => plain (avoids a copy; handled at use) */
        }
    }
    size_t ncl = nseg ? (nseg + 255) / 256 : 0;
    const size_t segper = 256;
    size_t shsz = 8 + CSZ[ckalg];
    uint32_t asz = (uint32_t)o->auth_len;
    size_t siglen = SSZ[profile], publlen = publen;
    size_t prologue_end = 12 + asz + siglen + publlen + 32 + 32 + 48 + 32;
    size_t hdrlen = shsz * segper + 32 + 32 * segper;
    size_t segsum = 0;
    for (size_t gi = 0; gi < nseg; gi++)
        segsum += stored[gi] ? storedl[gi] :
            (data_len - gi * bs < bs ? data_len - gi * bs : bs);
    size_t padstart = prologue_end + ncl * hdrlen + segsum;
    /* padlen = (-(padstart % padq)) % padq (oracle-observed rule) */
    size_t padlen = padq ? (padq - (padstart % padq)) % padq : 0;
    size_t arc = padstart + padlen;
    uint8_t padkey[32];
    hkdf(kd.main, 32, (uint8_t *)"AEA_PAK", 7, NULL, 0, padkey, 32);
    uint8_t *pad = NULL;
    if (padlen) {
        pad = malloc(padlen);
        if (!pad) {
            for (size_t k = 0; k < nseg; k++) free(stored[k]);
            free(stored); free(storedl);
            return fail("out of memory");
        }
        randbytes(pad, padlen);
    }

    typedef struct {
        uint8_t *sh; uint8_t nmac[32]; uint8_t *sms;
        uint8_t **segp; size_t *segn; size_t nsegc;
        uint8_t *tab; /* cluster table; header tag computed in reverse pass */
    } cluster;
    cluster *cls = calloc(ncl ? ncl : 1, sizeof *cls);
    uint8_t cmacA[32]; int have_cmac = 0;
    int stage = 0; /* 0 ok, 1 oom, 2 crypto-fail, 3 smacs, 4 nmacs */
    size_t cix = 0;
    if (ncl && !cls) stage = 1;
    uint8_t *padB = pad; pad = NULL; /* cls cleanup owns padB below */
    for (cix = 0; stage == 0 && cix < ncl; cix++) {
        uint8_t ck[32]; kd_clustkey(&kd, (uint32_t)cix, ck);
        uint8_t chk[80]; kd_chek(&kd, ck, chk);
        uint8_t *tab = calloc(shsz * segper, 1);
        uint8_t *sms = malloc(32 * segper);
        size_t base = cix * segper;
        size_t nblobs = nseg > base ? (nseg - base < segper ? nseg - base : segper) : 0;
        uint8_t **segp = calloc(nblobs ? nblobs : 1, sizeof *segp);
        size_t *segn = calloc(nblobs ? nblobs : 1, sizeof *segn);
        if (!tab || !sms || (nblobs && (!segp || !segn))) {
            free(tab); free(sms); free(segp); free(segn);
            memset(chk, 0, 80); stage = 1; break;
        }
        if (o->smacs) {
            if (o->smacs_len < 32 * segper * (cix + 1)) {
                free(tab); free(sms); free(segp); free(segn);
                memset(chk, 0, 80); stage = 3; break;
            }
            memcpy(sms, o->smacs + 32 * segper * cix, 32 * segper);
        }
        size_t bj = 0; int bad = 0;
        for (size_t i = 0; i < segper; i++) {
            size_t gi = base + i;
            if (gi >= nseg) {
                uint8_t *e = tab + shsz * i;
                put32le(e, 0); put32le(e + 4, 0);
                memset(e + 8, 0, CSZ[ckalg]);
                if (!o->smacs) randbytes(sms + 32 * i, 32);
            } else {
                size_t off = gi * bs;
                size_t pl = data_len - off < bs ? data_len - off : bs;
                const uint8_t *plain = data + off;
                const uint8_t *stdp = stored[gi] ? stored[gi] : plain;
                size_t stdl = stored[gi] ? storedl[gi] : pl;
                uint8_t sk[80]; kd_segkey(&kd, ck, (uint32_t)i, sk);
                uint8_t ckout[32]; size_t cklen = 0;
                uint8_t *encd = NULL; size_t el = 0; uint8_t tag[32];
                if (cksum(ckalg, plain, pl, ckout, &cklen) ||
                    enc_ver(sk, kd.ks, stdp, stdl, NULL, 0, &encd, &el, tag)) {
                    memset(sk, 0, 80); bad = 1; break;
                }
                memset(sk, 0, 80);
                uint8_t *e = tab + shsz * i;
                put32le(e, (uint32_t)pl); put32le(e + 4, (uint32_t)stdl);
                memcpy(e + 8, ckout, cklen);
                if (!o->smacs) memcpy(sms + 32 * i, tag, 32);
                segp[bj] = encd; segn[bj] = el; bj++;
            }
        }
        if (bad) {
            for (size_t k = 0; k < bj; k++) free(segp[k]);
            free(segp); free(segn); free(tab); free(sms);
            memset(chk, 0, 80); stage = 2; break;
        }
        /* nmac: fixed values verbatim (proto parity); otherwise the header
         * tag is computed in the reverse pass below (oracle chaining:
         * nmac[i] = tag[i+1]; the reference proto emits random nmacs
         * forward, which NEITHER oracle NOR proto itself accepts for ncl>1). */
        uint8_t nmac[32];
        if (o->nmacs) {
            if (o->nmacs_len < 32 * (cix + 1)) {
                for (size_t k = 0; k < bj; k++) free(segp[k]);
                free(segp); free(segn); free(tab); free(sms);
                memset(chk, 0, 80); stage = 4; break;
            }
            memcpy(nmac, o->nmacs + 32 * cix, 32);
        } else memset(nmac, 0, 32); /* placeholder; reverse pass fills */
        memset(chk, 0, 80);
        cls[cix].sh = NULL; memcpy(cls[cix].nmac, nmac, 32);
        cls[cix].sms = sms; cls[cix].segp = segp; cls[cix].segn = segn;
        cls[cix].nsegc = nblobs; cls[cix].tab = tab;
    }
    /* reverse pass: cluster header tags + nmac chaining (oracle-observed:
     * nmac[i] = tag[i+1]; last nmac = pad-auth or random). Fixed nmacs stay
     * verbatim (proto parity; oracle-rejected for ncl>1, like the proto). */
    if (stage == 0 && ncl > 0) {
        uint8_t next[32];
        for (size_t r = ncl; r-- > 0;) {
            uint8_t ck[32]; kd_clustkey(&kd, (uint32_t)r, ck);
            uint8_t chk[80]; kd_chek(&kd, ck, chk);
            uint8_t nmac[32];
            if (o->nmacs) memcpy(nmac, cls[r].nmac, 32);
            else if (r == ncl - 1) {
                if (padlen) hmac_sha256(padkey, 32, padB, padlen, nmac);
                else randbytes(nmac, 32);
            } else memcpy(nmac, next, 32);
            uint8_t *shs = NULL; size_t shsl = 0; uint8_t want[32];
            size_t nsslen = 32 + 32 * segper;
            uint8_t *nss = malloc(nsslen ? nsslen : 1);
            int evr = -1;
            if (nss) {
                memcpy(nss, nmac, 32); memcpy(nss + 32, cls[r].sms, 32 * segper);
                evr = enc_ver(chk, kd.ks, cls[r].tab, shsz * segper, nss,
                              nsslen, &shs, &shsl, want);
                free(nss);
            }
            memset(chk, 0, 80);
            free(cls[r].tab); cls[r].tab = NULL;
            if (evr) {
                free(shs);
                for (size_t k = 0; k < ncl; k++) {
                    free(cls[k].sh); free(cls[k].sms); free(cls[k].tab);
                    for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                    free(cls[k].segp); free(cls[k].segn);
                }
                free(cls);
                for (size_t k = 0; k < nseg; k++) free(stored[k]);
                free(stored); free(storedl); free(padB);
                return -1;
            }
            cls[r].sh = shs; memcpy(cls[r].nmac, nmac, 32);
            if (r == 0) { memcpy(cmacA, want, 32); have_cmac = 1; }
            else memcpy(next, want, 32);
        }
    }
    if (stage == 0 && !have_cmac) { randbytes(cmacA, 32); have_cmac = 1; }
    if (stage) {
        for (size_t k = 0; k < cix; k++) {
            free(cls[k].sh); free(cls[k].sms); free(cls[k].tab);
            for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
            free(cls[k].segp); free(cls[k].segn);
        }
        free(cls);
        for (size_t k = 0; k < nseg; k++) free(stored[k]);
        free(stored); free(storedl); free(padB);
        if (stage == 3) return fail("smacs too short");
        if (stage == 4) return fail("nmacs too short");
        if (stage == 1) return fail("out of memory");
        return -1;
    }
    if (o->block_size > 0xFFFFFFFFull) {
        for (size_t k = 0; k < ncl; k++) {
            free(cls[k].sh); free(cls[k].sms); free(cls[k].tab);
            for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
            free(cls[k].segp); free(cls[k].segn);
        }
        free(cls);
        for (size_t k = 0; k < nseg; k++) free(stored[k]);
        free(stored); free(storedl); free(padB);
        return fail("bad block size");
    }
    uint8_t rh[48]; memset(rh, 0, 48);
    put64le(rh, data_len); put64le(rh + 8, arc);
    put32le(rh + 16, (uint32_t)bs); put32le(rh + 20, (uint32_t)segper);
    rh[24] = (uint8_t)comp; rh[25] = (uint8_t)ckalg;
    uint8_t rk[80]; kd_rootkey(&kd, rk);
    uint8_t *csalt = malloc(32 + o->auth_len);
    if (!csalt) {
        memset(rk, 0, 80);
        for (size_t k = 0; k < ncl; k++) {
            free(cls[k].sh); free(cls[k].sms); free(cls[k].tab);
            for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
            free(cls[k].segp); free(cls[k].segn);
        }
        free(cls);
        for (size_t k = 0; k < nseg; k++) free(stored[k]);
        free(stored); free(storedl); free(padB);
        return fail("out of memory");
    }
    memcpy(csalt, cmacA, 32);
    memcpy(csalt + 32, o->auth ? o->auth : (uint8_t *)"", o->auth_len);
    uint8_t *rdata_stored = NULL; size_t rdl = 0; uint8_t rmac[32];
    int rhrc = enc_ver(rk, kd.ks, rh, 48, csalt, 32 + o->auth_len,
                       &rdata_stored, &rdl, rmac);
    free(csalt);
    if (rhrc) {
        memset(rk, 0, 80);
        for (size_t k = 0; k < ncl; k++) {
            free(cls[k].sh); free(cls[k].sms); free(cls[k].tab);
            for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
            free(cls[k].segp); free(cls[k].segn);
        }
        free(cls);
        for (size_t k = 0; k < nseg; k++) free(stored[k]);
        free(stored); free(storedl); free(padB);
        return -1;
    }
    memset(rk, 0, 80);
    uint8_t sigB[160]; size_t sigBlen = 0;
    if (profile == 0 || profile == 2 || profile == 4) {
        u256 d;
        const uint8_t *sp = o->sign_priv; size_t spl = o->sign_priv_len;
        if (!sp) {
            free(rdata_stored);
            for (size_t k = 0; k < ncl; k++) {
                free(cls[k].sh); free(cls[k].sms);
                for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                free(cls[k].segp); free(cls[k].segn);
            }
            free(cls);
            for (size_t k = 0; k < nseg; k++) free(stored[k]);
            free(stored); free(storedl); free(padB);
            return fail("sign_priv required");
        }
        /* re-parse (earlier parse validated + derived spub already) */
        jpt dummy_pub;
        if (ec_parse(sp, spl, "sign_priv", 1, &d, &dummy_pub)) {
            free(rdata_stored);
            for (size_t k = 0; k < ncl; k++) {
                free(cls[k].sh); free(cls[k].sms);
                for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                free(cls[k].segp); free(cls[k].segn);
            }
            free(cls);
            for (size_t k = 0; k < nseg; k++) free(stored[k]);
            free(stored); free(storedl); free(padB);
            return -1;
        }
        buf pro = {0};
        uint8_t ph[12];
        memcpy(ph, "AEA1", 4);
        ph[4] = profile & 0xFF; ph[5] = (profile >> 8) & 0xFF;
        ph[6] = (profile >> 16) & 0xFF; ph[7] = (uint8_t)sstr;
        put32le(ph + 8, asz);
        int pror = 0;
        pror |= bput(&pro, ph, 12);
        pror |= bput(&pro, o->auth ? o->auth : (uint8_t *)"", o->auth_len);
        uint8_t zz[160]; memset(zz, 0, siglen);
        pror |= bput(&pro, zz, siglen);
        pror |= bput(&pro, pub, publlen);
        pror |= bput(&pro, salt, 32);
        pror |= bput(&pro, rmac, 32);
        pror |= bput(&pro, rdata_stored, 48);
        pror |= bput(&pro, cmacA, 32);
        uint8_t der[160]; size_t derlen = 0;
        if (!pror) {
            uint8_t h[32]; sha256(pro.p, pro.n, h);
            if (ecdsa_sign(&d, h, der, &derlen)) pror = 1;
        }
        memset(&d, 0, sizeof d);
        bfree(&pro);
        if (pror) {
            free(rdata_stored);
            for (size_t k = 0; k < ncl; k++) {
                free(cls[k].sh); free(cls[k].sms);
                for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                free(cls[k].segp); free(cls[k].segn);
            }
            free(cls);
            for (size_t k = 0; k < nseg; k++) free(stored[k]);
            free(stored); free(storedl); free(padB);
            return -1;
        }
        if (derlen > siglen - (profile != 0 ? 32 : 0)) {
            free(rdata_stored);
            for (size_t k = 0; k < ncl; k++) {
                free(cls[k].sh); free(cls[k].sms);
                for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                free(cls[k].segp); free(cls[k].segn);
            }
            free(cls);
            for (size_t k = 0; k < nseg; k++) free(stored[k]);
            free(stored); free(storedl); free(padB);
            return fail("signature too long");
        }
        uint8_t s128[128]; memset(s128, 0, 128);
        memcpy(s128, der, derlen);
        if (profile == 0) { memcpy(sigB, s128, 128); sigBlen = 128; }
        else {
            uint8_t sk[80]; kd_sigkey(&kd, sk);
            uint8_t *encs = NULL; size_t el = 0; uint8_t tag[32];
            int evr = enc_ver(sk, kd.ks, s128, 128, NULL, 0, &encs, &el, tag);
            memset(sk, 0, 80);
            if (evr) {
                free(rdata_stored);
                for (size_t k = 0; k < ncl; k++) {
                    free(cls[k].sh); free(cls[k].sms);
                    for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
                    free(cls[k].segp); free(cls[k].segn);
                }
                free(cls);
                for (size_t k = 0; k < nseg; k++) free(stored[k]);
                free(stored); free(storedl); free(padB);
                return -1;
            }
            memcpy(sigB, encs, el); memcpy(sigB + el, tag, 32);
            sigBlen = el + 32; free(encs);
        }
    }
    buf ob = {0};
    uint8_t ph2[12];
    memcpy(ph2, "AEA1", 4);
    ph2[4] = profile & 0xFF; ph2[5] = (profile >> 8) & 0xFF;
    ph2[6] = (profile >> 16) & 0xFF; ph2[7] = (uint8_t)sstr;
    put32le(ph2 + 8, asz);
    int owr = 0;
    owr |= bput(&ob, ph2, 12);
    owr |= bput(&ob, o->auth ? o->auth : (uint8_t *)"", o->auth_len);
    owr |= bput(&ob, sigB, sigBlen);
    owr |= bput(&ob, pub, publlen);
    owr |= bput(&ob, salt, 32);
    owr |= bput(&ob, rmac, 32);
    owr |= bput(&ob, rdata_stored, 48);
    owr |= bput(&ob, cmacA, 32);
    for (size_t k = 0; k < ncl && !owr; k++) {
        owr |= bput(&ob, cls[k].sh, shsz * segper);
        owr |= bput(&ob, cls[k].nmac, 32);
        owr |= bput(&ob, cls[k].sms, 32 * segper);
        for (size_t j = 0; j < cls[k].nsegc && !owr; j++)
            owr |= bput(&ob, cls[k].segp[j], cls[k].segn[j]);
    }
    if (padlen && !owr) owr |= bput(&ob, padB, padlen);
    free(rdata_stored);
    for (size_t k = 0; k < ncl; k++) {
        free(cls[k].sh); free(cls[k].sms);
        for (size_t j = 0; j < cls[k].nsegc; j++) free(cls[k].segp[j]);
        free(cls[k].segp); free(cls[k].segn);
    }
    free(cls);
    for (size_t k = 0; k < nseg; k++) free(stored[k]);
    free(stored); free(storedl); free(padB);
    if (owr || ob.n != arc) { bfree(&ob); return fail("internal error"); }
    *out = ob.p; *out_len = ob.n; return 0;
}

/* ================= CLI helpers (mirror proto/aead.py main) ============ */
static void rstrip_crnl(uint8_t *d, size_t *n) {
    while (*n && (d[*n-1] == '\r' || d[*n-1] == '\n')) (*n)--;
}
static int is_ascii(const uint8_t *d, size_t n) {
    for (size_t i = 0; i < n; i++) if (d[i] >= 128) return 0;
    return 1;
}
/* read_key_file: raw passthrough unless ascii hex:/base64: (proto parity). */
static int read_key_file(const char *path, uint8_t **out, size_t *olen) {
    uint8_t *raw = NULL; size_t n = 0;
    if (read_all(path, &raw, &n)) return -1;
    if (!is_ascii(raw, n)) { *out = raw; *olen = n; return 0; }
    size_t c = n;
    rstrip_crnl(raw, &c);
    if (c > 4 && !memcmp(raw, "hex:", 4)) {
        uint8_t *o = NULL; size_t ol = 0;
        int rc = unhex((char *)raw + 4, c - 4, &o, &ol);
        free(raw);
        if (rc) return fail("key invalid");
        *out = o; *olen = ol; return 0;
    }
    if (c > 7 && !memcmp(raw, "base64:", 7)) {
        uint8_t *o = NULL; size_t ol = 0;
        int rc = unb64((char *)raw + 7, c - 7, &o, &ol);
        free(raw);
        if (rc) return fail("key invalid");
        *out = o; *olen = ol; return 0;
    }
    *out = raw; *olen = n; return 0; /* raw incl. newline (err-key32nl) */
}
static int parse_key_value(const char *val, uint8_t **out, size_t *olen) {
    size_t n = strlen(val);
    if (n > 4 && !memcmp(val, "hex:", 4))
        return unhex(val + 4, n - 4, out, olen);
    if (n > 7 && !memcmp(val, "base64:", 7))
        return unb64(val + 7, n - 7, out, olen);
    return fail("key-value must be hex:... or base64:... (oracle rejects bare)");
}
static void pyrepr(const char *s, char *o, size_t cap) {
    /* Python repr() of short ascii strings: '...' with \\ and \' escapes. */
    size_t p = 0;
    if (p < cap) o[p++] = '\'';
    for (; *s && p + 2 < cap; s++) {
        if (*s == '\'' || *s == '\\') o[p++] = '\\';
        o[p++] = *s;
    }
    if (p < cap) o[p++] = '\'';
    o[p < cap ? p : cap - 1] = 0;
}
static int parse_size(const char *s, uint64_t *out) {
    if (!s) return fail("bad size");
    while (*s == ' ' || *s == '\t' || *s == '\n' || *s == '\r') s++;
    const char *e = s + strlen(s);
    while (e > s && (e[-1] == ' ' || e[-1] == '\t' || e[-1] == '\n' || e[-1] == '\r')) e--;
    size_t n = e - s;
    if (!n) return fail("bad size");
    char t[64];
    if (n >= sizeof t) return fail("bad size");
    memcpy(t, s, n); t[n] = 0;
    uint64_t mult = 1;
    char last = t[n-1];
    if (last == 'b' || last == 'B' || last == 'k' || last == 'K' ||
        last == 'm' || last == 'M' || last == 'g' || last == 'G') {
        switch (last == 'b' ? 'B' : last >= 'a' ? last - 32 : last) {
        case 'B': mult = 1; break;
        case 'K': mult = 1 << 10; break;
        case 'M': mult = 1 << 20; break;
        case 'G': mult = 1 << 30; break;
        }
        t[n-1] = 0;
        if (!t[0]) { char r[80]; pyrepr(t, r, sizeof r); return fail("bad size %s", r); }
    }
    /* Python int(): optional sign + digits */
    int neg = 0; const char *q = t;
    if (*q == '+' || *q == '-') { neg = *q == '-'; q++; }
    if (!*q) { char r[80]; pyrepr(t, r, sizeof r); return fail("bad size %s", r); }
    uint64_t v = 0;
    for (; *q; q++) {
        if (*q < '0' || *q > '9') {
            char r[80]; pyrepr(t, r, sizeof r); return fail("bad size %s", r);
        }
        v = v * 10 + (uint64_t)(*q - '0');
    }
    if (neg) *out = (uint64_t)(-(int64_t)(v * mult));
    else *out = v * mult;
    return 0;
}
static int utf8_valid(const uint8_t *d, size_t n) {
    size_t i = 0;
    while (i < n) {
        uint8_t c = d[i];
        size_t need = 0;
        if (c < 0x80) { i++; continue; }
        else if ((c & 0xE0) == 0xC0) need = 1;
        else if ((c & 0xF0) == 0xE0) need = 2;
        else if ((c & 0xF8) == 0xF0) need = 3;
        else return 0;
        if (i + need >= n) return 0;
        for (size_t k = 1; k <= need; k++)
            if ((d[i+k] & 0xC0) != 0x80) return 0;
        i += need + 1;
    }
    return 1;
}

/* ================= selftest (mirrors tests/test_aead_units.py logic) == */
static int st_n = 0, st_fail = 0;
#define ST(cond, name) do { st_n++; if (cond) printf("ST-PASS %s\n", name); \
    else { st_fail++; printf("ST-FAIL %s\n", name); } } while (0)

static void manual_hkdf(const uint8_t *ikm, size_t ikl, const uint8_t *info,
                        size_t infl, const uint8_t *salt, size_t sl,
                        uint8_t *okm, size_t L) {
    uint8_t zeros[32]; memset(zeros, 0, 32);
    if (sl == 0) { salt = zeros; sl = 32; }
    uint8_t prk[32]; hmac_sha256(salt, sl, ikm, ikl, prk);
    uint8_t prev[32]; size_t pl = 0; uint8_t c = 1; size_t pos = 0;
    uint8_t in[64 + 256];
    while (pos < L) {
        memcpy(in, prev, pl); memcpy(in + pl, info, infl); in[pl + infl] = c;
        hmac_sha256(prk, 32, in, pl + infl + 1, prev); pl = 32;
        size_t t = L - pos < 32 ? L - pos : 32;
        memcpy(okm + pos, prev, t); pos += t; c++;
    }
}

static const char ST_PRIV[] =
    "-----BEGIN EC PRIVATE KEY-----\n"
    "MHcCAQEEIPGSQqjbmnk9U22XnJfR1K3R5YmmpGPofBmtpOq4qfmRoAoGCCqGSM49\n"
    "AwEHoUQDQgAE1WgKoso3G+/L9xAvs1Ls50zBgby79pbE+7W9eC/qY43TCI6AfNgr\n"
    "ayAhjIIjwlT0xs4R0TgNA+c7dtINp2P1LA==\n"
    "-----END EC PRIVATE KEY-----\n"
;
static const char ST_PUB[] =
    "-----BEGIN PUBLIC KEY-----\n"
    "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE1WgKoso3G+/L9xAvs1Ls50zBgby7\n"
    "9pbE+7W9eC/qY43TCI6AfNgrayAhjIIjwlT0xs4R0TgNA+c7dtINp2P1LA==\n"
    "-----END PUBLIC KEY-----\n"
;
int aead_selftest(void) {
    p256_init();
    /* hkdf matches manual (RFC 5869 framing cross-check) */
    {
        struct { size_t L; const char *ikm, *info, *salt; } v[] = {
            {32, "k", "AEA_RHEK", "salt"},
            {80, "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "AEA_SK\x01\x00\x00\x00", ""},
            {64, "ssssssssssssssssssssssssssssssss", "AEA_SCRYPT", ""},
        };
        for (size_t i = 0; i < 3; i++) {
            uint8_t a[80], b[80];
            hkdf((uint8_t *)v[i].ikm, strlen(v[i].ikm),
                 (uint8_t *)v[i].info, strlen(v[i].info),
                 (uint8_t *)v[i].salt, strlen(v[i].salt), a, v[i].L);
            manual_hkdf((uint8_t *)v[i].ikm, strlen(v[i].ikm),
                        (uint8_t *)v[i].info, strlen(v[i].info),
                        (uint8_t *)v[i].salt, strlen(v[i].salt), b, v[i].L);
            ST(!memcmp(a, b, v[i].L), "hkdf-manual");
        }
    }
    /* HMAC-SHA256 primitive vs RFC 4231 test case 1 */
    {
        uint8_t key[20]; memset(key, 0x0b, 20);
        uint8_t d[32];
        hmac_sha256(key, 20, (uint8_t *)"Hi There", 8, d);
        /* RFC 4231 test case 1 (value confirmed via reference HMAC) */
        uint8_t want[32] = {0xb0,0x34,0x4c,0x61,0xd8,0xdb,0x38,0x53,
            0x5c,0xa8,0xaf,0xce,0xaf,0x0b,0xf1,0x2b,0x88,0x1d,0xc2,0x00,
            0xc9,0x83,0x3d,0xa7,0x26,0xe9,0x37,0x6c,0x2e,0x32,0xcf,0xf7};
        ST(!memcmp(d, want, 32), "hmac-rfc4231");
    }
    /* mac() framing: HMAC(key, salt+data+LE64(len salt)) */
    {
        uint8_t k[32]; memset(k, 'K', 32);
        uint8_t m[32], ref[32];
        amac(k, (uint8_t *)"data", 4, (uint8_t *)"salt", 4, m);
        uint8_t pre[4 + 4 + 8]; memcpy(pre, "saltdata", 8); put64le(pre + 8, 4);
        hmac_sha256(k, 32, pre, 16, ref);
        ST(!memcmp(m, ref, 32), "mac-shape");
    }
    /* archive_id shape + trunc boundary */
    {
        uint8_t b[156], d[32], e[32];
        memcpy(b, "AEA1", 4); b[4] = 5; b[5] = 0; b[6] = 0; b[7] = 0;
        put32le(b + 8, 0); memset(b + 12, 0, 144);
        ST(!aead_id(b, 156, d), "id-ok");
        sha256(b, 156, e); ST(!memcmp(d, e, 32), "id-shape");
        ST(aead_id(b, 155, d) && !strcmp(aead_err, "truncated prologue"), "id-trunc155");
        ST(!aead_id(b, 156, d), "id-156");
        uint8_t b2[160]; memcpy(b2, "AEA1", 4);
        b2[4] = 1; b2[5] = 0; b2[6] = 0; b2[7] = 0;
        put32le(b2 + 8, 4); memcpy(b2 + 12, "ABCD", 4); memset(b2 + 16, 0, 144);
        ST(!aead_id(b2, 160, d), "id-auth");
        sha256(b2, 160, e); ST(!memcmp(d, e, 32), "id-auth-shape");
        uint8_t bw[168]; memcpy(bw, "AEA1", 4);
        bw[4] = 5; bw[5] = 0; bw[6] = 0; bw[7] = 0; put32le(bw + 8, 12);
        memset(bw + 12, 0, 12 + 144);
        ST(aead_id(bw, 167, d) && !strcmp(aead_err, "truncated prologue"), "id-trunc167");
        ST(!aead_id(bw, 168, d), "id-168");
    }
    /* rejects */
    {
        uint8_t *o = NULL; size_t ol = 0;
        aead_dec_opt z; memset(&z, 0, sizeof z);
        ST(aead_decrypt((uint8_t *)"XXXX....", 8, &z, &o, &ol) &&
           !strcmp(aead_err, "bad magic"), "rej-magic");
        uint8_t b9[212]; memcpy(b9, "AEA1", 4);
        b9[4] = 9; memset(b9 + 5, 0, 207);
        ST(aead_decrypt(b9, sizeof b9, &z, &o, &ol) &&
           !strcmp(aead_err, "bad profile"), "rej-profile");
        uint8_t b5[112]; memcpy(b5, "AEA1", 4);
        b5[4] = 5; b5[5] = b5[6] = b5[7] = 0; put32le(b5 + 8, 0);
        memset(b5 + 12, 0, 100);
        ST(aead_decrypt(b5, sizeof b5, &z, &o, &ol) &&
           !strcmp(aead_err, "truncated prologue"), "rej-trunc");
        uint8_t sh[6] = "short";
        ST(aead_id(sh, 5, (uint8_t[32]){0}) &&
           !strcmp(aead_err, "bad magic"), "rej-id-short");
    }
    /* keyvalue forms */
    {
        uint8_t *kv = NULL; size_t kvl = 0;
        uint8_t raw32[32]; for (int i = 0; i < 32; i++) raw32[i] = i;
        char hx[70]; strcpy(hx, "hex:");
        for (int i = 0; i < 32; i++) snprintf(hx + 4 + 2 * i, 3, "%02x", i);
        ST(!parse_key_value(hx, &kv, &kvl) && kvl == 32 &&
           !memcmp(kv, raw32, 32), "kv-hex");
        free(kv);
        /* base64 of bytes(range(32)) */
        ST(!parse_key_value("base64:AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8", &kv, &kvl) &&
           kvl == 32 && !memcmp(kv, raw32, 32), "kv-b64");
        free(kv);
        uint8_t *bad = NULL; size_t bl = 0;
        char bare[65]; for (int i = 0; i < 32; i++) snprintf(bare + 2 * i, 3, "%02x", 0xab);
        ST(parse_key_value(bare, &bad, &bl) &&
           !strcmp(aead_err, "key-value must be hex:... or base64:... (oracle rejects bare)"),
           "kv-bare");
    }
    /* codec dispatch */
    {
        uint8_t *co = NULL; size_t col = 0;
        ST(!decomp('-', (uint8_t *)"q", 1, 1, &co, &col) && col == 1 &&
           co[0] == 'q', "codec-none");
        free(co);
        uint8_t *zb = NULL; size_t zl = 0;
        ST(!z_comp((uint8_t *)"hi", 2, &zb, &zl), "zlib-enc");
        ST(!decomp('z', zb, zl, 2, &co, &col) && col == 2 &&
           !memcmp(co, "hi", 2), "codec-zlib");
        free(zb); free(co);
        ST(decomp('Q', (uint8_t *)"q", 1, 1, &co, &col) &&
           !strcmp(aead_err, "codec 'Q' unsupported"), "codec-unsupported");
        ST(comp_enc('b', (uint8_t *)"q", 1, &co, &col) &&
           !strcmp(aead_err, "codec 'b' has no encoder in v1"), "codec-noenc");
        uint8_t c1[32], c2[32]; size_t l1 = 9, l2 = 9;
        ST(!cksum(0, (uint8_t *)"q", 1, c1, &l1) && l1 == 0, "cksum-none");
        ST(!cksum(1, (uint8_t *)"q", 1, c1, &l1) && l1 == 8, "cksum-mur-len");
        ST(!cksum(1, (uint8_t *)"q", 1, c2, &l2) && !memcmp(c1, c2, 8), "cksum-mur-det");
        ST(!cksum(1, (uint8_t *)"qq", 2, c2, &l2) && memcmp(c1, c2, 8), "cksum-mur-diff");
        ST(!cksum(2, (uint8_t *)"q", 1, c2, &l2) && l2 == 32, "cksum-sha");
        ST(cksum(9, (uint8_t *)"q", 1, c2, &l2) &&
           !strcmp(aead_err, "checksum 9 unsupported"), "cksum-bad");
        uint8_t m0a[8], m0b[8];
        murmur64a(NULL, 0, m0a); murmur64a((uint8_t *)"", 0, m0b);
        ST(!memcmp(m0a, m0b, 8), "murmur-empty");
    }
    /* dec_ver / enc_ver mirror */
    {
        uint8_t key[80]; for (int i = 0; i < 80; i++) key[i] = i;
        uint8_t tag[32]; amac(key, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5, tag);
        uint8_t *dec = NULL; size_t dl = 0;
        /* CTR decrypt of the raw bytes (== encrypt); must succeed + transform */
        ST(!dec_ver(key, 80, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5,
                    tag, &dec, &dl) && dl == 12 &&
           memcmp(dec, "payload-data", 12), "decver-80");
        uint8_t tag2[32]; amac(key, dec, dl, (uint8_t *)"salty", 5, tag2);
        uint8_t *enc = NULL; size_t el = 0;
        ST(!dec_ver(key, 80, dec, dl, (uint8_t *)"salty", 5, tag2, &enc, &el) &&
           el == 12 && !memcmp(enc, "payload-data", 12), "decver-80rt");
        free(dec); free(enc);
        ST(!dec_ver(key, 32, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5,
                    tag, &dec, &dl) && dl == 12, "decver-32");
        free(dec);
        uint8_t z32[32]; memset(z32, 0, 32);
        ST(dec_ver(key, 80, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5,
                   z32, &dec, &dl) && !strcmp(aead_err, "HMAC mismatch"), "decver-tampertag");
        uint8_t *dd = NULL; size_t ddl = 0;
        ST(dec_ver(key, 80, (uint8_t *)"payload-dataX", 13, (uint8_t *)"salty", 5,
                   tag, &dd, &ddl) && !strcmp(aead_err, "HMAC mismatch"), "decver-tamperdata");
        uint8_t *st = NULL; size_t sln = 0; uint8_t tg[32];
        ST(!enc_ver(key, 80, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5,
                    &st, &sln, tg), "encver-80");
        ST(!dec_ver(key, 80, st, sln, (uint8_t *)"salty", 5, tg, &dec, &dl) &&
           dl == 12 && !memcmp(dec, "payload-data", 12), "encver-mirror");
        ST(memcmp(st, "payload-data", 12), "encver-ctrapplied");
        free(st); free(dec);
        uint8_t *st32 = NULL; size_t s32l = 0; uint8_t tg32[32];
        ST(!enc_ver(key, 32, (uint8_t *)"payload-data", 12, (uint8_t *)"salty", 5,
                    &st32, &s32l, tg32) && s32l == 12 &&
           !memcmp(st32, "payload-data", 12), "encver-32");
        free(st32);
    }
    /* scrypt vs vectors observed from reference (hashlib.scrypt) */
    {
        uint8_t dk[32];
        uint8_t w1[32] = {0x56,0xd1,0x86,0x5f,0xe3,0x9b,0xed,0x79,0x1e,0x63,0x58,0x12,0xf1,0x1a,0xb4,0xc9,0x0a,0x25,0xf6,0x5c,0x47,0x98,0x42,0x53,0xca,0xb0,0x64,0x00,0x48,0x8c,0x43,0x51};
        ST(!scrypt((uint8_t *)"pw", 2, (uint8_t *)"salt1234", 8, 1024, dk) &&
           !memcmp(dk, w1, 32), "scrypt-1024");
        uint8_t w2[32] = {0x17,0x35,0xa7,0x6c,0xff,0x61,0x05,0xf2,0x7a,0x31,0xcb,0xf2,0xa5,0xbe,0xbb,0xf1,0x82,0x58,0x1b,0x6c,0x0f,0xbe,0x93,0x98,0x88,0xed,0xa8,0x9b,0x56,0x1a,0xf1,0x42};
        ST(!scrypt((uint8_t *)"pw", 2, (uint8_t *)"salt1234", 8, 16384, dk) &&
           !memcmp(dk, w2, 32), "scrypt-16384");
    }
    /* parse_size */
    {
        uint64_t v = 99;
        ST(!parse_size("1m", &v) && v == (1 << 20), "ps-1m");
        ST(!parse_size("64k", &v) && v == (64 << 10), "ps-64k");
        ST(!parse_size("16", &v) && v == 16, "ps-16");
        ST(!parse_size("0", &v) && v == 0, "ps-0");
        ST(parse_size("bogus", &v) && !strcmp(aead_err, "bad size 'bogus'"), "ps-bogus");
    }
    /* P-256: 1*G == G; ECDH(1,G) == x(G); sign/verify roundtrip */
    {
        u256 one; memset(&one, 0, sizeof one); one.v[0] = 1;
        jpt G; pt_set_aff(&G, &P256_GX, &P256_GY);
        jpt R; pt_mul(&G, &one, &R);
        u256 x, y; pt_to_aff(&R, &x, &y);
        ST(!u256_cmp(&x, &P256_GX) && !u256_cmp(&y, &P256_GY), "p256-1G");
        uint8_t ss[32];
        ST(!ecdh(&one, &G, ss), "ecdh-1G");
        uint8_t gx[32]; u256_tobytes_be(&P256_GX, gx);
        ST(!memcmp(ss, gx, 32), "ecdh-x");
        uint8_t h[32]; sha256((uint8_t *)"test", 4, h);
        uint8_t der[160]; size_t dl = 0;
        ST(!ecdsa_sign(&one, h, der, &dl), "ecdsa-sign");
        ST(!ecdsa_verify(&G, h, der, dl), "ecdsa-verify");
        der[dl - 1] ^= 1;
        ST(ecdsa_verify(&G, h, der, dl) &&
           !strcmp(aead_err, "signature invalid"), "ecdsa-tamper");
    }
    /* EC PEM parse (SEC1 priv + SPKI pub) + ECDH cross-consistency */
    {
        u256 d; jpt pub, pub2; u256 dummy;
        ST(!ec_parse((uint8_t *)ST_PRIV, strlen(ST_PRIV), "sign_priv", 1, &d, &pub),
           "pem-priv");
        ST(!ec_parse((uint8_t *)ST_PUB, strlen(ST_PUB), "sign_pub", 0, &dummy, &pub2),
           "pem-pub");
        u256 x1, y1, x2, y2; pt_to_aff(&pub, &x1, &y1); pt_to_aff(&pub2, &x2, &y2);
        ST(!u256_cmp(&x1, &x2) && !u256_cmp(&y1, &y2), "pem-privpub-match");
        uint8_t s1[32], s2[32];
        /* ecdh(d, G) == ecdh(1, pub): DH symmetry */
        u256 one; memset(&one, 0, sizeof one); one.v[0] = 1;
        jpt G; pt_set_aff(&G, &P256_GX, &P256_GY);
        ST(!ecdh(&d, &G, s1) && !ecdh(&one, &pub, s2) && !memcmp(s1, s2, 32),
           "ecdh-sym");
        uint8_t hx[32]; u256_tobytes_be(&x1, hx);
        ST(!memcmp(s2, hx, 32), "ecdh-xcoord");
        uint8_t h[32]; sha256((uint8_t *)"m", 1, h);
        uint8_t der[160]; size_t dl = 0;
        ST(!ecdsa_sign(&d, h, der, &dl) && !ecdsa_verify(&pub2, h, der, dl),
           "ecdsa-pem-roundtrip");
        memset(&d, 0, sizeof d);
    }
    /* LZ4 block micro-vector + roundtrips */
    {
        uint8_t *lo = NULL; size_t ll = 0;
        uint8_t blk[] = {0x50, 'h', 'e', 'l', 'l', 'o'};
        ST(!decomp('4', blk, sizeof blk, 5, &lo, &ll) && ll == 5 &&
           !memcmp(lo, "hello", 5), "lz4-micro");
        free(lo);
        const char *pats[] = {"", "a", "abcdefgh",
            "The quick brown fox jumps over the lazy dog. The quick brown fox. ",
            NULL};
        size_t pl3 = strlen(pats[3]);
        for (int i = 0; i < 4; i++) {
            size_t il = i == 3 ? 3000 : strlen(pats[i]);
            uint8_t *in = malloc(il ? il : 1);
            if (i == 3) { for (int k = 0; k < 3000; k++) in[k] = pats[3][k % pl3]; }
            else if (il) memcpy(in, pats[i], il);
            size_t cap = il + il / 255 + 16;
            uint8_t *cb = malloc(cap ? cap : 16);
            size_t cl = lz4_compress(in, il, cb);
            uint8_t *rt = NULL; size_t rl = 0;
            int ok = !decomp('4', cb, cl, il, &rt, &rl) && rl == il &&
                     (il == 0 || !memcmp(rt, in, il));
            char nm[32]; snprintf(nm, sizeof nm, "lz4-rt%d", i);
            ST(ok, nm);
            free(in); free(cb); free(rt);
        }
        /* incompressible */
        {
            uint8_t in[1024]; for (int k = 0; k < 1024; k++) in[k] = (k * 7919) & 0xFF;
            uint8_t *cb = malloc(2048); size_t cl = lz4_compress(in, 1024, cb);
            uint8_t *rt = NULL; size_t rl = 0;
            ST(!decomp('4', cb, cl, 1024, &rt, &rl) && rl == 1024 &&
               !memcmp(rt, in, 1024), "lz4-rt-inc");
            free(cb); free(rt);
        }
    }
    /* lzfse + zlib + lzma roundtrips */
    {
        uint8_t in[5000]; for (int k = 0; k < 5000; k++) in[k] = "abc"[k % 3];
        uint8_t *e = NULL, *z = NULL, *xb = NULL;
        size_t el = 0, zl = 0, xbl = 0;
        ST(!comp_enc('z', in, 5000, &z, &zl), "zl-enc");
        uint8_t *o = NULL; size_t ol = 0;
        ST(!decomp('z', z, zl, 5000, &o, &ol) && ol == 5000 &&
           !memcmp(o, in, 5000), "zl-rt");
        free(z); free(o);
        ST(!comp_enc('x', in, 5000, &xb, &xbl), "xz-enc");
        ST(!decomp('x', xb, xbl, 5000, &o, &ol) && ol == 5000 &&
           !memcmp(o, in, 5000), "xz-rt");
        free(xb); free(o);
        ST(!comp_enc('e', in, 5000, &e, &el), "e-enc");
        ST(!decomp('e', e, el, 5000, &o, &ol) && ol == 5000 &&
           !memcmp(o, in, 5000), "e-rt");
        free(e); free(o);
    }
    /* encrypt self roundtrips: p1 + p5 + empty + padded, fixed salt */
    {
        uint8_t key[32]; for (int i = 0; i < 32; i++) key[i] = i;
        uint8_t salt[32]; memset(salt, 0xAB, 32);
        aead_enc_opt e; memset(&e, 0, sizeof e);
        e.profile = 1; e.symkey = key; e.symkey_len = 32;
        e.comp = '-'; e.ckalg = 2; e.block_size = 1 << 20;
        e.salt = salt; e.salt_len = 32;
        uint8_t *b = NULL; size_t bl = 0;
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-p1");
        aead_dec_opt d; memset(&d, 0, sizeof d);
        d.symkey = key; d.symkey_len = 32;
        uint8_t *p = NULL; size_t pl = 0;
        ST(!aead_decrypt(b, bl, &d, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-p1-rt");
        free(b); free(p); b = p = NULL;
        e.profile = 5; e.symkey = NULL; e.symkey_len = 0;
        e.password = "pw-20-bytes-long-ok!!"; e.ckalg = 0;
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-p5");
        aead_dec_opt d5; memset(&d5, 0, sizeof d5);
        d5.password = "pw-20-bytes-long-ok!!";
        ST(!aead_decrypt(b, bl, &d5, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-p5-rt");
        free(b); free(p); b = p = NULL;
        e.profile = 1; e.symkey = key; e.symkey_len = 32;
        e.password = NULL; e.ckalg = 0;
        ST(!aead_encrypt(NULL, 0, &e, &b, &bl), "enc-empty");
        ST(!aead_decrypt(b, bl, &d, &p, &pl) && pl == 0, "enc-empty-rt");
        free(b); free(p); b = p = NULL;
        e.ckalg = 2; e.padq = 16;
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-pad");
        ST(!aead_decrypt(b, bl, &d, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-pad-rt");
        free(b); free(p); b = p = NULL;
        /* multi-cluster: force small blocks */
        e.padq = 0; e.block_size = 64; e.ckalg = 2;
        uint8_t *big = malloc(70000);
        for (int k = 0; k < 70000; k++) big[k] = (k * 31) & 0xFF;
        ST(!aead_encrypt(big, 70000, &e, &b, &bl), "enc-multi");
        ST(!aead_decrypt(b, bl, &d, &p, &pl) && pl == 70000 &&
           !memcmp(p, big, 70000), "enc-multi-rt");
        free(big); free(b); free(p); b = p = NULL;
        /* signed profile roundtrip (p2) */
        e.profile = 2; e.symkey = key; e.symkey_len = 32;
        e.sign_priv = (uint8_t *)ST_PRIV; e.sign_priv_len = strlen(ST_PRIV);
        e.block_size = 1 << 20;
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-p2");
        aead_dec_opt d2; memset(&d2, 0, sizeof d2);
        d2.symkey = key; d2.symkey_len = 32;
        d2.sign_pub = (uint8_t *)ST_PUB; d2.sign_pub_len = strlen(ST_PUB);
        ST(!aead_decrypt(b, bl, &d2, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-p2-rt");
        free(b); free(p); b = p = NULL;
        /* EC profiles (p3/p4) roundtrip */
        e.profile = 3;
        e.recip_pub = (uint8_t *)ST_PUB; e.recip_pub_len = strlen(ST_PUB);
        e.sign_priv = NULL; e.sign_priv_len = 0;
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-p3");
        aead_dec_opt d3; memset(&d3, 0, sizeof d3);
        d3.recip_priv = (uint8_t *)ST_PRIV; d3.recip_priv_len = strlen(ST_PRIV);
        ST(!aead_decrypt(b, bl, &d3, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-p3-rt");
        free(b); free(p); b = p = NULL;
        e.profile = 4;
        e.sign_priv = (uint8_t *)ST_PRIV; e.sign_priv_len = strlen(ST_PRIV);
        ST(!aead_encrypt((uint8_t *)"hello", 5, &e, &b, &bl), "enc-p4");
        aead_dec_opt d4; memset(&d4, 0, sizeof d4);
        d4.recip_priv = (uint8_t *)ST_PRIV; d4.recip_priv_len = strlen(ST_PRIV);
        d4.sign_pub = (uint8_t *)ST_PUB; d4.sign_pub_len = strlen(ST_PUB);
        ST(!aead_decrypt(b, bl, &d4, &p, &pl) && pl == 5 &&
           !memcmp(p, "hello", 5), "enc-p4-rt");
        free(b); free(p); b = p = NULL;
    }
    /* encrypt rejects (message parity) */
    {
        aead_enc_opt e; memset(&e, 0, sizeof e);
        uint8_t key[32]; memset(key, 0, 32);
        uint8_t *b = NULL; size_t bl = 0;
        e.comp = '-'; e.ckalg = 2; e.block_size = 1 << 20;
        e.profile = 9; e.symkey = key; e.symkey_len = 32;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "bad profile"), "rej-enc-prof");
        e.profile = 1; e.symkey = NULL; e.symkey_len = 0;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "symmetric key required (32B)"), "rej-enc-nokey");
        e.symkey = key; e.symkey_len = 32; e.comp = '?';
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "bad algorithm"), "rej-enc-alg");
        e.comp = '-'; e.ckalg = 9;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "bad checksum"), "rej-enc-ck");
        e.ckalg = 2; e.padq = 5;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "bad padding (must be 0/none or >= 16)"), "rej-enc-pad");
        e.padq = 0; e.profile = 2; e.sign_priv = NULL;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "sign_priv required"), "rej-enc-nosign");
        e.profile = 5; e.symkey = NULL; e.password = "short";
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "Password is too short"), "rej-enc-pwshort");
        e.password = NULL;
        ST(aead_encrypt((uint8_t *)"x", 1, &e, &b, &bl) &&
           !strcmp(aead_err, "password required"), "rej-enc-pwnone");
        aead_dec_opt d; memset(&d, 0, sizeof d);
        d.password = "short";
        uint8_t pb[200]; memcpy(pb, "AEA1", 4);
        pb[4] = 5; pb[5] = pb[6] = 0; pb[7] = 0; put32le(pb + 8, 0);
        memset(pb + 12, 0, 188);
        uint8_t *p = NULL; size_t pl = 0;
        ST(aead_decrypt(pb, sizeof pb, &d, &p, &pl) &&
           !strcmp(aead_err, "Password is too short"), "rej-dec-pwshort");
    }
    printf("SELFTEST %d/%d %s\n", st_n - st_fail, st_n,
           st_fail ? "FAIL" : "PASS");
    return st_fail ? 1 : 0;
}

/* ================= main CLI (flag parity with proto/aead.py) ========= */
static const char *g_prog = "aeadc";

static int usage_err(const char *msg) {
    fprintf(stderr, "%s: error: %s\n", g_prog, msg);
    return 2;
}
static int need_arg(int i, int argc, const char *flag) {
    if (i + 1 >= argc) {
        fprintf(stderr, "%s: error: argument %s: expected one argument\n",
                g_prog, flag);
        return -1;
    }
    return 0;
}
static uint8_t *read_stdin_all(size_t *n) {
    buf b = {0}; uint8_t tmp[65536]; size_t r;
    while ((r = fread(tmp, 1, sizeof tmp, stdin)) > 0)
        if (bput(&b, tmp, r)) { bfree(&b); return NULL; }
    *n = b.n; return b.p ? b.p : (uint8_t *)calloc(1, 1);
}
/* value of --flag (supports --flag=x and --flag x). Returns NULL if absent. */
static const char *opt_val(int *i, int argc, char **argv, const char *flag) {
    const char *a = argv[*i];
    size_t fl = strlen(flag);
    if (!strncmp(a, flag, fl) && a[fl] == '=') return a + fl + 1;
    if (strcmp(a, flag)) return NULL;
    if (*i + 1 >= argc) return (const char *)-1;
    (*i)++;
    return argv[*i];
}
static int parse_int_arg(const char *v, const char *flag, long *out) {
    if (!v || !*v) return usage_err("expected integer");
    char *e = NULL;
    /* Python int(): strip whitespace, optional sign, digits only. */
    while (*v == ' ' || *v == '\t' || *v == '\n') v++;
    long x = strtol(v, &e, 10);
    while (e && (*e == ' ' || *e == '\t' || *e == '\n')) e++;
    if (!e || *e) {
        char m[128]; snprintf(m, sizeof m, "argument %s: invalid int value", flag);
        return usage_err(m);
    }
    *out = x; return 0;
}

static int do_decrypt(int argc, char **argv) {
    const char *in = NULL, *outp = NULL;
    const char *key = NULL, *keyval = NULL, *pw = NULL, *pwfile = NULL;
    const char *recpriv = NULL, *signpub = NULL;
    const char *ro = NULL, *rs = NULL;
    for (int i = 0; i < argc; i++) {
        const char *v;
        if (!strcmp(argv[i], "-i")) { if (need_arg(i, argc, "-i")) return 2; in = argv[++i]; }
        else if (!strcmp(argv[i], "-o")) { if (need_arg(i, argc, "-o")) return 2; outp = argv[++i]; }
        else if ((v = opt_val(&i, argc, argv, "--key"))) { if (v == (void *)-1) return usage_err("argument --key: expected one argument"); key = v; }
        else if ((v = opt_val(&i, argc, argv, "--key-value"))) { if (v == (void *)-1) return usage_err("argument --key-value: expected one argument"); keyval = v; }
        else if ((v = opt_val(&i, argc, argv, "--password"))) { if (v == (void *)-1) return usage_err("argument --password: expected one argument"); pw = v; }
        else if ((v = opt_val(&i, argc, argv, "--password-file"))) { if (v == (void *)-1) return usage_err("argument --password-file: expected one argument"); pwfile = v; }
        else if ((v = opt_val(&i, argc, argv, "--recipient-priv"))) { if (v == (void *)-1) return usage_err("argument --recipient-priv: expected one argument"); recpriv = v; }
        else if ((v = opt_val(&i, argc, argv, "--sign-pub"))) { if (v == (void *)-1) return usage_err("argument --sign-pub: expected one argument"); signpub = v; }
        else if ((v = opt_val(&i, argc, argv, "--range-offset"))) { if (v == (void *)-1) return usage_err("argument --range-offset: expected one argument"); ro = v; }
        else if ((v = opt_val(&i, argc, argv, "--range-size"))) { if (v == (void *)-1) return usage_err("argument --range-size: expected one argument"); rs = v; }
        else { char m[160]; snprintf(m, sizeof m, "unrecognized arguments: %s", argv[i]); return usage_err(m); }
    }
    uint8_t *blob = NULL; size_t bl = 0;
    if (!in) { blob = read_stdin_all(&bl); if (!blob) { fprintf(stderr, "aead: cannot read stdin\n"); return 1; } }
    else if (read_all(in, &blob, &bl)) { fprintf(stderr, "aead: %s\n", aead_err); return 1; }
    aead_dec_opt o; memset(&o, 0, sizeof o);
    uint8_t *sk = NULL; size_t skl = 0;
    uint8_t *rpl = NULL; size_t rpln = 0;
    uint8_t *spl = NULL; size_t spln = 0;
    uint8_t *kvb = NULL; size_t kvn = 0;
    char *pwbuf = NULL;
    if (key && read_key_file(key, &sk, &skl)) { fprintf(stderr, "aead: %s\n", aead_err); free(blob); return 1; }
    if (keyval && parse_key_value(keyval, &kvb, &kvn)) { fprintf(stderr, "aead: %s\n", aead_err); free(blob); free(sk); return 1; }
    if (sk) { o.symkey = sk; o.symkey_len = skl; }
    if (kvb) { o.symkey = kvb; o.symkey_len = kvn; } /* key_value wins (proto order) */
    if (pw && pw[0]) o.password = pw;
    if (pwfile) {
        uint8_t *raw = NULL; size_t n = 0;
        if (read_all(pwfile, &raw, &n)) { fprintf(stderr, "aead: %s\n", aead_err); goto derr; }
        if (!utf8_valid(raw, n)) { free(raw); aead_err[0] = 0; fail("password file not text"); fprintf(stderr, "aead: %s\n", aead_err); goto derr; }
        rstrip_crnl(raw, &n);
        pwbuf = malloc(n + 1);
        if (!pwbuf) { free(raw); fprintf(stderr, "aead: out of memory\n"); goto derr; }
        memcpy(pwbuf, raw, n); pwbuf[n] = 0; free(raw);
        o.password = pwbuf; /* file wins (proto order); empty->absent via falsy */
        if (!pwbuf[0]) o.password = NULL;
    }
    if (recpriv) {
        if (read_all(recpriv, &rpl, &rpln)) { fprintf(stderr, "aead: %s\n", aead_err); goto derr; }
        o.recip_priv = rpl; o.recip_priv_len = rpln;
    }
    if (signpub) {
        if (read_all(signpub, &spl, &spln)) { fprintf(stderr, "aead: %s\n", aead_err); goto derr; }
        o.sign_pub = spl; o.sign_pub_len = spln;
    }
    if (ro) { long x; if (parse_int_arg(ro, "--range-offset", &x)) goto derr2; o.has_range_off = 1; o.range_off = x; }
    if (rs) { long x; if (parse_int_arg(rs, "--range-size", &x)) goto derr2; o.has_range_size = 1; o.range_size = x; }
    {
        uint8_t *p = NULL; size_t pl = 0;
        if (aead_decrypt(blob, bl, &o, &p, &pl)) {
            fprintf(stderr, "aead: %s\n", aead_err); goto derr;
        }
        int wr = 0;
        if (!outp) wr = write_all(NULL, p, pl);
        else wr = write_all(outp, p, pl);
        free(p);
        if (wr) { fprintf(stderr, "aead: %s\n", aead_err); goto derr; }
    }
    free(blob); free(sk); free(kvb); free(pwbuf); free(rpl); free(spl);
    return 0;
derr:
    free(blob); free(sk); free(kvb); free(pwbuf); free(rpl); free(spl);
    return 1;
derr2:
    free(blob); free(sk); free(kvb); free(pwbuf); free(rpl); free(spl);
    return 2;
}

static int do_encrypt(int argc, char **argv) {
    const char *in = NULL, *outp = NULL;
    const char *key = NULL, *keyval = NULL, *pw = NULL, *pwfile = NULL;
    const char *recpub = NULL, *signpriv = NULL;
    const char *prof = NULL, *alg = "none", *bs = "1m", *ck = "sha256",
               *pad = "none";
    const char *fsalt = NULL, *fnmac = NULL, *fsmacs = NULL;
    /* --auth-data/--auth-data-value/--auth-data-key (repeatable) */
    char **adF = NULL, **adV = NULL, **adK = NULL;
    size_t nF = 0, nV = 0, nK = 0;
    for (int i = 0; i < argc; i++) {
        const char *v;
        if (!strcmp(argv[i], "-i")) { if (need_arg(i, argc, "-i")) return 2; in = argv[++i]; }
        else if (!strcmp(argv[i], "-o")) { if (need_arg(i, argc, "-o")) return 2; outp = argv[++i]; }
        else if (!strcmp(argv[i], "-a")) { if (need_arg(i, argc, "-a")) return 2; alg = argv[++i]; }
        else if (!strcmp(argv[i], "-b")) { if (need_arg(i, argc, "-b")) return 2; bs = argv[++i]; }
        else if ((v = opt_val(&i, argc, argv, "--profile"))) { if (v == (void *)-1) return usage_err("argument --profile: expected one argument"); prof = v; }
        else if ((v = opt_val(&i, argc, argv, "--key"))) { if (v == (void *)-1) return usage_err("argument --key: expected one argument"); key = v; }
        else if ((v = opt_val(&i, argc, argv, "--key-value"))) { if (v == (void *)-1) return usage_err("argument --key-value: expected one argument"); keyval = v; }
        else if ((v = opt_val(&i, argc, argv, "--password"))) { if (v == (void *)-1) return usage_err("argument --password: expected one argument"); pw = v; }
        else if ((v = opt_val(&i, argc, argv, "--password-file"))) { if (v == (void *)-1) return usage_err("argument --password-file: expected one argument"); pwfile = v; }
        else if ((v = opt_val(&i, argc, argv, "--recipient-pub"))) { if (v == (void *)-1) return usage_err("argument --recipient-pub: expected one argument"); recpub = v; }
        else if ((v = opt_val(&i, argc, argv, "--sign-priv"))) { if (v == (void *)-1) return usage_err("argument --sign-priv: expected one argument"); signpriv = v; }
        else if ((v = opt_val(&i, argc, argv, "--checksum"))) { if (v == (void *)-1) return usage_err("argument --checksum: expected one argument"); ck = v; }
        else if ((v = opt_val(&i, argc, argv, "--padding"))) { if (v == (void *)-1) return usage_err("argument --padding: expected one argument"); pad = v; }
        else if ((v = opt_val(&i, argc, argv, "--auth-data"))) { if (v == (void *)-1) return usage_err("argument --auth-data: expected one argument"); adF = realloc((void *)adF, (nF + 1) * sizeof *adF); adF[nF++] = (char *)v; }
        else if ((v = opt_val(&i, argc, argv, "--auth-data-value"))) { if (v == (void *)-1) return usage_err("argument --auth-data-value: expected one argument"); adV = realloc((void *)adV, (nV + 1) * sizeof *adV); adV[nV++] = (char *)v; }
        else if ((v = opt_val(&i, argc, argv, "--auth-data-key"))) { if (v == (void *)-1) return usage_err("argument --auth-data-key: expected one argument"); adK = realloc((void *)adK, (nK + 1) * sizeof *adK); adK[nK++] = (char *)v; }
        else if ((v = opt_val(&i, argc, argv, "--fixed-salt"))) { if (v == (void *)-1) return usage_err("argument --fixed-salt: expected one argument"); fsalt = v; }
        else if ((v = opt_val(&i, argc, argv, "--fixed-nmac"))) { if (v == (void *)-1) return usage_err("argument --fixed-nmac: expected one argument"); fnmac = v; }
        else if ((v = opt_val(&i, argc, argv, "--fixed-smacs"))) { if (v == (void *)-1) return usage_err("argument --fixed-smacs: expected one argument"); fsmacs = v; }
        else { char m[160]; snprintf(m, sizeof m, "unrecognized arguments: %s", argv[i]); free(adF); free(adV); free(adK); return usage_err(m); }
    }
    if (!prof) { free(adF); free(adV); free(adK); return usage_err("the following arguments are required: --profile"); }
    long profl = -1;
    { char *e = NULL; profl = strtol(prof, &e, 10); if (e == prof || *e) { free(adF); free(adV); free(adK); return usage_err("argument --profile: invalid int value"); } }
    uint8_t *data = NULL; size_t dl = 0;
    if (!in) { data = read_stdin_all(&dl); if (!data) { free(adF); free(adV); free(adK); fprintf(stderr, "aead: cannot read stdin\n"); return 1; } }
    else if (read_all(in, &data, &dl)) { free(adF); free(adV); free(adK); fprintf(stderr, "aead: %s\n", aead_err); return 1; }
    aead_enc_opt o; memset(&o, 0, sizeof o);
    o.profile = (int)profl;
    char comp = '?';
    if (!strcmp(alg, "none")) comp = '-';
    else if (!strcmp(alg, "zlib")) comp = 'z';
    else if (!strcmp(alg, "lzma")) comp = 'x';
    else if (!strcmp(alg, "lz4")) comp = '4';
    else if (!strcmp(alg, "lzfse")) comp = 'e';
    o.comp = comp;
    if (!strcmp(ck, "none")) o.ckalg = 0;
    else if (!strcmp(ck, "murmur64")) o.ckalg = 1;
    else if (!strcmp(ck, "sha256")) o.ckalg = 2;
    else o.ckalg = -1; /* -> "bad checksum" */
    uint64_t bsz = 0;
    if (parse_size(bs, &bsz)) {
        fprintf(stderr, "aead: %s\n", aead_err);
        free(adF); free(adV); free(adK); free(data); return 1;
    }
    o.block_size = bsz; /* 0 -> "bad block size" in lib */
    if (!strcmp(pad, "none") || !strcmp(pad, "0")) o.padq = 0;
    else if (!strcmp(pad, "adaptive")) {
        fprintf(stderr, "aead: bad padding (adaptive unsupported in v1)\n");
        free(adF); free(adV); free(adK); free(data); return 1;
    } else {
        uint64_t pq = 0;
        if (parse_size(pad, &pq)) {
            fprintf(stderr, "aead: %s\n", aead_err);
            free(adF); free(adV); free(adK); free(data); return 1;
        }
        o.padq = pq;
    }
    uint8_t *sk = NULL; size_t skl = 0;
    uint8_t *kvb = NULL; size_t kvn = 0;
    char *pwbuf = NULL;
    uint8_t *rpb = NULL; size_t rpn = 0;
    uint8_t *spb = NULL; size_t spn = 0;
    uint8_t *fsb = NULL; size_t fsn = 0;
    uint8_t *fnb = NULL; size_t fnn = 0;
    uint8_t *fmb = NULL; size_t fmn = 0;
    buf auth = {0};
    int rc = 1;
    if (key && read_key_file(key, &sk, &skl)) goto efin;
    if (keyval && parse_key_value(keyval, &kvb, &kvn)) goto efin;
    if (sk) { o.symkey = sk; o.symkey_len = skl; }
    if (kvb) { o.symkey = kvb; o.symkey_len = kvn; }
    if (pw && pw[0]) o.password = pw;
    if (pwfile) {
        uint8_t *raw = NULL; size_t n = 0;
        if (read_all(pwfile, &raw, &n)) goto efin;
        if (!utf8_valid(raw, n)) { free(raw); fail("password file not text"); goto efin; }
        rstrip_crnl(raw, &n);
        pwbuf = malloc(n + 1);
        if (!pwbuf) { free(raw); fail("out of memory"); goto efin; }
        memcpy(pwbuf, raw, n); pwbuf[n] = 0; free(raw);
        o.password = pwbuf[0] ? pwbuf : NULL;
    }
    if (recpub && read_all(recpub, &rpb, &rpn)) goto efin;
    if (rpb) { o.recip_pub = rpb; o.recip_pub_len = rpn; }
    if (signpriv && read_all(signpriv, &spb, &spn)) goto efin;
    if (spb) { o.sign_priv = spb; o.sign_priv_len = spn; }
    for (size_t i = 0; i < nF; i++) {
        uint8_t *f = NULL; size_t fl = 0;
        if (read_all(adF[i], &f, &fl)) goto efin;
        if (bput(&auth, f, fl)) { free(f); fail("out of memory"); goto efin; }
        free(f);
    }
    {
        size_t vi = 0;
        for (size_t i = 0; i < nK; i++) {
            if (vi >= nV) { fail("auth-data-key without following value"); goto efin; }
            uint8_t *v = NULL; size_t vl = 0;
            if (parse_key_value(adV[vi], &v, &vl)) goto efin;
            size_t kl = strlen(adK[i]);
            uint8_t l4[4]; put32le(l4, (uint32_t)(4 + kl + 1 + vl));
            if (bput(&auth, l4, 4) || bput(&auth, adK[i], kl) ||
                bput(&auth, "\x00", 1) || bput(&auth, v, vl)) {
                free(v); fail("out of memory"); goto efin;
            }
            free(v); vi++;
        }
        for (; vi < nV; vi++) {
            uint8_t *v = NULL; size_t vl = 0;
            if (parse_key_value(adV[vi], &v, &vl)) goto efin;
            if (bput(&auth, v, vl)) { free(v); fail("out of memory"); goto efin; }
            free(v);
        }
    }
    o.auth = auth.p; o.auth_len = auth.n;
    if (fsalt && parse_key_value(fsalt, &fsb, &fsn)) goto efin;
    if (fsb) { o.salt = fsb; o.salt_len = fsn; }
    if (fnmac && parse_key_value(fnmac, &fnb, &fnn)) goto efin;
    if (fnb) { o.nmacs = fnb; o.nmacs_len = fnn; }
    if (fsmacs && parse_key_value(fsmacs, &fmb, &fmn)) goto efin;
    if (fmb) { o.smacs = fmb; o.smacs_len = fmn; }
    {
        uint8_t *b = NULL; size_t bl = 0;
        if (aead_encrypt(data, dl, &o, &b, &bl)) goto efin;
        int wr = outp ? write_all(outp, b, bl) : write_all(NULL, b, bl);
        free(b);
        if (wr) goto efin;
    }
    rc = 0;
efin:
    if (rc) fprintf(stderr, "aead: %s\n", aead_err);
    free(adF); free(adV); free(adK); free(data);
    free(sk); free(kvb); free(pwbuf); free(rpb); free(spb);
    free(fsb); free(fnb); free(fmb); bfree(&auth);
    return rc;
}

static int do_id(int argc, char **argv) {
    const char *in = NULL;
    for (int i = 0; i < argc; i++) {
        if (!strcmp(argv[i], "-i")) { if (need_arg(i, argc, "-i")) return 2; in = argv[++i]; }
        else { char m[160]; snprintf(m, sizeof m, "unrecognized arguments: %s", argv[i]); return usage_err(m); }
    }
    if (!in) return usage_err("the following arguments are required: -i");
    uint8_t *blob = NULL; size_t bl = 0;
    if (read_all(in, &blob, &bl)) { fprintf(stderr, "aead: %s\n", aead_err); return 1; }
    uint8_t d[32];
    if (aead_id(blob, bl, d)) { fprintf(stderr, "aead: %s\n", aead_err); free(blob); return 1; }
    free(blob);
    for (int i = 0; i < 32; i++) printf("%02x", d[i]);
    printf("\n");
    return 0;
}

int aead_main(int argc, char **argv) {
    if (argc > 0 && argv[0]) {
        const char *b = strrchr(argv[0], '/');
        g_prog = b ? b + 1 : argv[0];
    }
    if (argc < 2) {
        fprintf(stderr, "usage: %s {decrypt|encrypt|id|selftest} ...\n", g_prog);
        return 2;
    }
    if (!strcmp(argv[1], "decrypt")) return do_decrypt(argc - 2, argv + 2);
    if (!strcmp(argv[1], "encrypt")) return do_encrypt(argc - 2, argv + 2);
    if (!strcmp(argv[1], "id")) return do_id(argc - 2, argv + 2);
    if (!strcmp(argv[1], "selftest")) return aead_selftest();
    char m[160]; snprintf(m, sizeof m, "unrecognized arguments: %s", argv[1]);
    return usage_err(m);
}

/* Standalone entry (dropped from shipped build; kept for source parity).
 * The shipped binary (aae-cli) compiles with -DAAE_CLI_UNIFIED and calls
 * aead_main() in-process instead. */
#ifndef AAE_CLI_UNIFIED
int main(int argc, char **argv) { return aead_main(argc, argv); }
#endif
