# GATE 8d5bc17 b213 T10R146 n<=68588 (898 tiers) PASS-functional

- Seat encode-sweep r16g, first-hand, seat-private logs
  r16g-8d5bc17/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent b69154d: rgramc.c only
  +1302/-1143; wall 0. Range 68333..68588.
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=8852 FAIL 0, PINS-RGRAM set-eq 8852/8852;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4426/4426 GREEN rc=0 0 FAIL
  covered=4426/4426 (corpus seeded r16f-8516151 4564 +
  missing-only fresh-oracle regen, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 8852/8852 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings).
- own-loop 68333..68588 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R146C 69n + _N=69
  derived rows, _T10R146M 16/16 + _T10R146Q 16/16
  C==py); full audit 1D 167/0 + 2D 885/0 +
  dicts 11/0 + STR 292/0 + STRARR 1114/0
  (vs b211 2D 881 / STR 289 / STRARR 1100; 1D
  const; +4/+3/+7 for +4 tiers/+28 pins, no drift).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b211->b213 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload 1, OSS 37/0-new,
  LIBC aad.c 3 lines), cross-checked vs live gate.log.
  ADOPT WARN diff carried (c8f52713/c5f921d5 const;
  smoke.sh 56d751f9/56d751f9 same).
- Quiz diff 0 (rechecked before filing, max Q361).
- Verdict: PASS-functional. No RED. Unblocks VERIFY + parent merge.
