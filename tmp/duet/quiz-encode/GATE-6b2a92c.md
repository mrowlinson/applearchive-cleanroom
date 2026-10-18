# GATE 6b2a92c b215 T10R147 n<=68936 (902 tiers) PASS-functional

- Seat encode-sweep r16g, first-hand, seat-private logs
  r16g-6b2a92c/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent 8bed83b: rgramc.c only
  +1308/-1149; wall 0. Range 68681..68936.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8908 FAIL 0, PINS-RGRAM set-eq 8908/8908;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4454/4454 GREEN rc=0 0 FAIL
  covered=4454/4454 (corpus seeded r16g-b213 4620 +
  missing-only fresh-oracle regen, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8908/8908 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 68681..68936 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R147C 67n + _N=67
  derived rows, _T10R147M 16/16 + _T10R147Q 16/16
  C==py); full audit 1D 167/0 + 2D 889/0 +
  dicts 11/0 + STR 294/0 + STRARR 1121/0
  (vs b213 2D 885 / STR 292 / STRARR 1114; 1D
  const; +4/+2/+7 for +4 tiers/+28 pins, no drift).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b213->b215 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload 1, OSS 37/0-new,
  LIBC aad.c 3 lines), cross-checked vs live gate.log.
  ADOPT WARN diff carried (c8f52713/c5f921d5 const;
  smoke.sh 56d751f9/56d751f9 same).
- Quiz diff 0 (rechecked before filing, max Q361).
- Verdict: PASS-functional. No RED. Unblocks VERIFY + parent merge.
