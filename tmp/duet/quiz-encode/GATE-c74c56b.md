# GATE c74c56b b201 T10R140 n<=66500 (874 tiers) PASS-functional

- Seat encode-sweep r16c, first-hand, seat-private logs
  r16-c74c56b/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent 1177b26: rgramc.c only
  +1260/-1101; wall 0. Range 66245..66500.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8516 FAIL 0, PINS-RGRAM set-eq 8516/8516;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4258/4258 GREEN rc=0 0 FAIL
  covered=4258/4258 (corpus seeded r16c-b199 4232 +
  26 fresh-oracle regen for new N, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8516/8516 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 66245..66500 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R140C 69n + _N=69
  derived rows, _T10R140M 16/16 + _T10R140Q 16/16
  C==py); full audit 1D 167/0 + 2D 861/0 +
  dicts 11/0 + STR 274/0 + STRARR 1072/0
  (vs b199 2D 857 / STR 271 / STRARR 1065; 1D
  const; +4/+3/+7 for +2 tiers/+24 pins, no drift).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b199->b201 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload raw 74/74 incl
  survivor proto/impl-adapter.sh ZBM_DYLIB
  known-FP, OSS 37/0-new, LIBC aad.c 3 lines),
  cross-checked vs live gate.log. ADOPT WARN diff
  carried (c8f52713/c5f921d5 const; smoke.sh
  56d751f9/56d751f9 same).
- Quiz diff 0 (rechecked before filing).
- Verdict: PASS-functional. No RED. Run cap 2/2.
