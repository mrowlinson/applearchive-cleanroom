# GATE ef0144b b193 T10R136 n<=65108 (858 tiers) PASS-functional

- Seat encode-sweep r14, first-hand, seat-private logs
  r14-ef0144b/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent ad52ea0: rgramc.c only
  +1233/-1074; wall 0. Range 64853..65108.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8304 FAIL 0, PINS-RGRAM set-eq 8304/8304;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4152/4152 GREEN rc=0 0 FAIL
  covered=4152/4152 (corpus seeded r14-b191 4127 +
  25 fresh-oracle regen for new N, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8304/8304 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 64853..65108 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R136C 66n + _N=66
  derived rows, _T10R136M 16/16 + _T10R136Q 16/16
  C==py); full audit 1D 167/0 + 2D 845/0 +
  dicts 11/0 + STR 263/0 + STRARR 1043/0
  (b192 baseline confirms exact +1 2D / +2
  STRARR delta).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b192->b193 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload raw 74/74 incl
  survivor proto/impl-adapter.sh ZBM_DYLIB
  known-FP, OSS 37/0-new, LIBC aad.c 3 lines),
  cross-checked vs live gate.log. ADOPT WARN diff
  carried (c8f52713/c5f921d5 const).
- Quiz diff 0 (rechecked before filing).
- Verdict: PASS-functional. No RED. Run cap 2/2.
