/* rgramc -- C port of ../rgram.py (lzraven zeros-N grammar verifier).
 * Verdict core (file/arg handling lives in rgramc.c main). */
#ifndef AAE_RGRAMC_H
#define AAE_RGRAMC_H
#include <stddef.h>
#include <stdint.h>

/* verify raw[0..rawlen) as lzraven zeros-N encoding. Prints CLOSED or
 * GRAMMAR-BREAK to stdout (usage/scope errors to stderr). Returns
 * 0 pass / 1 rule break / 2 bad input. Mirrors rgram.main(). */
int rgram_verify(const uint8_t *raw, long rawlen, long n);
#endif
