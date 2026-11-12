/* aeadc.h -- AEA encrypt/decrypt/id C port (proto/aead.py v1).
 * Clean-room port from behavior beds + public specs only. No third-party
 * implementation code is copied. Crypto provenance:
 *  - SHA-256 / HMAC-SHA-256 / AES-256-CTR: macOS system CommonCrypto
 *    (headers verified: SDK usr/include/CommonCrypto/; CTR-BE per
 *    NIST SP 800-38A section 6.5).
 *  - HKDF-SHA256: own, from RFC 5869 section 2.2/2.3.
 *  - scrypt: own, from RFC 7914 (PBKDF2-HMAC-SHA256 + ROMix/BlockMix;
 *    Salsa20/8 core per Bernstein Salsa20 spec, public domain, as invoked
 *    by RFC 7914 section 5).
 *  - P-256 ECDH/ECDSA/keys: own field+curve arithmetic from SEC1 v2.0
 *    section 2 (domain parameters) / section 3.3 (ECDH) and FIPS 186-4
 *    section 6.4 (sign) / appendix D.1.2.3 (P-256). Chosen over
 *    Security.framework SecKeyCopyKeyExchangeResult after a live probe:
 *    SecKeyCreateWithData rejects raw 32B scalar import (paramErr,
 *    requires X9.63 04||X||Y[||K] which needs the public point at import
 *    time -- circular for PEM-only private keys).
 *  - zlib: system libz (level 6 == Python zlib.compress default).
 *  - lzma: pinned liblzma 5.8.4 direct link (in-repo precedent, preset 6
 *    CRC64 == Python lzma.compress defaults).
 *  - lzfse/lzbitmap/lzraven decode+lzfse encode: macOS compression.h
 *    buffer API (COMPRESSION_LZFSE/LZBITMAP/LZRAVEN; headers verified;
 *    LZRAVEN needs macOS 27+; this host is 27.x). No LZFSE_BIN/ZBM_BIN/
 *    LZR_BIN subprocess shims (killed by design).
 *  - LZ4 block: own, from the public LZ4 Block Format Description
 *    (literal/match token framing). No third-party code.
 *  - murmur64a: line-port of own proto (behavior bed).
 *  - base64: RFC 4648 section 4 (own); PEM/DER walk: own parser.
 */
#ifndef AAE_AEADC_H
#define AAE_AEADC_H
#include <stddef.h>
#include <stdint.h>

extern char aead_err[256]; /* last FmtErr text (no "aead: " prefix) */

/* decrypt/encrypt operate on whole buffers; plaintext/ciphertext malloc'd.
 * Return 0 ok / -1 FmtErr (aead_err set). All refusal strings are identical
 * to proto/aead.py FmtErr texts. */
typedef struct {
    const uint8_t *symkey; size_t symkey_len; /* 32B or absent */
    const uint8_t *recip_priv; size_t recip_priv_len;   /* PEM bytes */
    const uint8_t *sign_pub; size_t sign_pub_len;        /* PEM bytes */
    const char *password;   /* NULL = absent; "" treated as absent (falsy) */
    int has_range_off; long range_off;
    int has_range_size; long range_size;
} aead_dec_opt;

typedef struct {
    int profile;
    const uint8_t *symkey; size_t symkey_len;
    const char *password;   /* NULL absent; "" absent (falsy) */
    const uint8_t *recip_pub; size_t recip_pub_len;      /* PEM bytes */
    const uint8_t *sign_priv; size_t sign_priv_len;      /* PEM bytes */
    const uint8_t *eph_priv; size_t eph_priv_len;        /* PEM bytes or NULL */
    char comp;              /* '-','z','x','4','e' */
    int ckalg;              /* 0,1,2 */
    uint64_t block_size;
    uint64_t padq;          /* 0 or >=16 */
    const uint8_t *auth; size_t auth_len;
    const uint8_t *salt; size_t salt_len;  /* 32B or NULL */
    const uint8_t *nmacs; size_t nmacs_len;   /* multiples of 32 or NULL */
    const uint8_t *smacs; size_t smacs_len;
} aead_enc_opt;

int aead_decrypt(const uint8_t *blob, size_t blob_len,
                 const aead_dec_opt *o,
                 uint8_t **out, size_t *out_len);
int aead_encrypt(const uint8_t *data, size_t data_len,
                 const aead_enc_opt *o,
                 uint8_t **out, size_t *out_len);
int aead_id(const uint8_t *blob, size_t blob_len,
            uint8_t digest[32]);

int aead_selftest(void); /* 0 all-pass; prints SELFTEST lines */
#endif
