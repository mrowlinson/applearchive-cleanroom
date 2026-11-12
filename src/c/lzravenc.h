/* lzraven encoder. C port of ../lzraven.py (empty/stored/T0-T3 synth).
 * Derived black-box from compression_tool I/O only. Scope: single-frame
 * streams, zeros N<=820 synthesized, stored paths, honest refusal past
 * scope. STORED-GUESS on non-zero n>=64 kept AS-IS (proto gap, stays
 * loud): output equals oracle iff oracle stores this input.
 * No Python on this path; tables come from lzraventab.h only. */
#ifndef AAE_LZRAVENC_H
#define AAE_LZRAVENC_H
#include <stddef.h>
#include <stdint.h>

#define LZRAVEN_SCOPE_MAX 820

/* Encode one raw slice -> malloc'd raven stream (*on bytes). NULL on
 * refusal (n all-zeros past scope); err gets "zeros N=%zu beyond
 * proto scope 820". aae prefixes "lzraven unclosed input: ". */
uint8_t *lzraven_encode_stream(const uint8_t *d, size_t n, size_t *on,
                               char *err, size_t errcap);

/* Outer pbzm framing: per-block stream + 15/16 store rule (mirrors
 * lzraven.wrap_pbzm + rb2.frame). NULL on refusal (err set). */
uint8_t *lzraven_wrap_pbzm(const uint8_t *inner, size_t ilen,
                           size_t blocksize, size_t *on,
                           char *err, size_t errcap);
#endif
