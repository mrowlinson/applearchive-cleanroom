# GATE 5bfc21a b187 T10R133 n<=64064 (846 tiers) PASS-functional

- Seat encode-sweep r12, first-hand, seat-private logs
  r12-5bfc21a/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent 786f2a7: rgramc.c only
  +1195/-1054; wall 0. Range 63809..64064.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8152 FAIL 0, PINS-RGRAM set-eq 8152/8152;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4076/4076 GREEN rc=0 0 FAIL
  covered=4076/4076 (corpus seeded r11 4078 + 12
  fresh-oracle regen for new N, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8152/8152 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings, 1929512 B).
- own-loop 63809..64064 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 3/3 EQ (C 2D _T10R133C 70 rows = _N,
  _T10R133M 16/16 C==py); full audit 1D 166/0 +
  2D 833/0 + dicts 11/0 + STR 255/0 + STRARR
  1022/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; lane file
  0/0/0, HYG .aar 13 identical b186->b187, CONTAM
  CHIT 43/43 identical + depload raw 74/74
  identical (survivor proto/impl-adapter.sh
  ZBM_DYLIB known-FP), Mach-O empty both, LIBCOMP
  aad.c 3 lines identical. ADOPT WARN diff carried
  (c8f52713/c5f921d5 const).
- Verdict: PASS-functional. No RED. Run cap 1/2.
