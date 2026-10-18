# GATE d01a797 b207 T10R143 n<=67544 (886 tiers) PASS-functional

- Seat encode-sweep r16e, first-hand, seat-private logs
  r16e-d01a797/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent a86038d: rgramc.c only
  +1281/-1122; wall 0. Range 67289..67544.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8684 FAIL 0, PINS-RGRAM set-eq 8684/8684;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4342/4342 GREEN rc=0 0 FAIL
  covered=4342/4342 (corpus seeded r16e-b205 4396 +
  missing-only fresh-oracle regen, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8684/8684 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 67289..67544 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R143C 69n + _N=69
  derived rows, _T10R143M 16/16 + _T10R143Q 16/16
  C==py); full audit 1D 167/0 + 2D 873/0 +
  dicts 11/0 + STR 283/0 + STRARR 1093/0
  (vs b205 2D 869 / STR 279 / STRARR 1086; 1D
  const; +4/+4/+7 for +2 tiers/+28 pins, no drift).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b205->b207 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload 1, OSS 37/0-new,
  LIBC aad.c 3 lines), cross-checked vs live gate.log.
  ADOPT WARN diff carried (c8f52713/c5f921d5 const;
  smoke.sh 56d751f9/56d751f9 same).
- Quiz diff 0 (rechecked before filing, max Q361).
- Verdict: PASS-functional. No RED. Unblocks VERIFY + parent merge.
