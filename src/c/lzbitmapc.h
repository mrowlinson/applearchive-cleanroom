/* lzbitmap literal-class ZBM encoder. C port of ../lzbitmap.py.
 * Derived black-box from /usr/bin/aa I/O only. Covers the LITERAL class
 * only; every input outside refuses with the exact G1/G2/G3/G4 reason.
 * Refusal predicate is conservative: inputs inside the class are
 * oracle-literal (battery-proven), inputs outside refuse honestly.
 * No Python on this path. */
#ifndef AAE_LZBITMAPC_H
#define AAE_LZBITMAPC_H
#include <stddef.h>
#include <stdint.h>

#define ZBM_CHUNK 32768u
#define ZBM_WIN 65535u

/* 1 + reason set (exact G1/G2/G3/G4 string) if outside proven-parity
 * class, else 0. aae prefixes "lzbitmap match-class input: ". */
int lzbitmap_refuse(const uint8_t *d, size_t n, char *reason, size_t rcap);

/* Literal ZBM stream -> malloc'd bytes. NULL on refusal (reason set). */
uint8_t *zbm_encode_literal(const uint8_t *d, size_t n, size_t *on,
                            char *err, size_t errcap);

/* Outer pbzb framing (mirrors wrap_pbzb): per-block literal stream +
 * 15/16 store rule, independent per-block analysis. NULL on refusal. */
uint8_t *lzbitmap_wrap_pbzb(const uint8_t *inner, size_t ilen,
                            size_t blocksize, size_t *on,
                            char *err, size_t errcap);
#endif
