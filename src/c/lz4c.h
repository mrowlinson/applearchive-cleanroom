/* lz4 (pbz4) encoder. C port of ../lz4enc.py (V0+K+A33).
 * Derived black-box from /usr/bin/aa I/O only.
 * Hash fn abstracted (LZ4_BKT macro) for A-33 swap when true
 * bucket-hash formula lands; current = H12>>1 (shift). */
#ifndef AAE_LZ4C_H
#define AAE_LZ4C_H
#include <stddef.h>
#include <stdint.h>

#define LZ4_CHUNK 65536u
#define LZ4_NEVER_K 127u
#define LZ4_BUCKETS 2048u
#define LZ4_SLOTS 5u
#define LZ4_K 2654435761u

/* bucket hash of 4 bytes at p (swap-ready). */
static inline uint32_t LZ4_BKT(const uint8_t *p) {
    uint32_t v = (uint32_t)p[0] | ((uint32_t)p[1] << 8) |
                 ((uint32_t)p[2] << 16) | ((uint32_t)p[3] << 24);
    return (uint32_t)(((v * LZ4_K) & 0xFFFFFFFFu) >> 20) >> 1;
}

/* one 64KB-chunk code result (malloc'd block, caller frees). */
typedef struct {
    size_t unc;
    uint8_t *blk;
    size_t blen;
} lz4_chunk;

/* encode full inner -> malloc'd chunk array (count in *nch, free via
 * lz4_free_chunks). mirrors lz4enc.lz4_encode(inner,2048,5,'shift'). */
lz4_chunk *lz4_encode_all(const uint8_t *inner, size_t ilen, size_t *nch);
void lz4_free_chunks(lz4_chunk *chs, size_t nch);

/* pbz4 outer wrap (mirrors wrap_pbz4). malloc'd, len in *olen. */
uint8_t *lz4_wrap_pbz4(const uint8_t *inner, size_t ilen,
                       const lz4_chunk *chs, size_t nch, size_t blocksize,
                       size_t *olen);
#endif
