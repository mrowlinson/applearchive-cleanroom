# GATE fac36c9 b189 T10R134 n<=64412 (850 tiers) PASS-functional

- Seat encode-sweep r13, first-hand, seat-private logs
  r13-fac36c9/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent d335153: rgramc.c only
  +1220/-1061; wall 0. Range 64157..64412.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8202 FAIL 0, PINS-RGRAM set-eq 8202/8202;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4101/4101 GREEN rc=0 0 FAIL
  covered=4101/4101 (corpus seeded r12 4076 + 11
  fresh-oracle regen for new N, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8202/8202 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 64157..64412 fresh-oracle 256/256
  py-agree, pins 22/22, rc=0.
- Added 4/4 EQ (C 2D _T10R134C 134n + _N=67
  derived rows, _T10R134M 16/16 + _T10R134Q 16/16
  C==py); full audit 1D 166/0 + 2D 837/0 +
  dicts 11/0 + STR 258/0 + STRARR 1029/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all sets
  IDENTICAL b188->b189 first-hand (HYG .aar 13,
  CHIT 42, Mach-O 0, depload raw 74/74 incl
  survivor proto/impl-adapter.sh ZBM_DYLIB
  known-FP, OSS 37, LIBC aad.c 3 lines). ADOPT
  WARN diff carried (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED. Run cap 1/2.
