# GATE 171e45a b221 T10R150 n<=69980 (914 tiers) PASS-functional

- Seat encode-sweep r16i, first-hand, seat-private logs
  r16i-171e45a/* under NVME encode-sweep.
- Lane-diff vs writer-merge parent 3d13ec3: rgramc.c only
  +1328/-1169; wall 0. Range 69725..69980 (lo =
  b220 ceiling 69724 + 1, verified vs filed
  GATE-f1b8d9f; 256 n; matches writer +24 pins).
- gate-tip (wt-encode-sweep harness @ d56ce19): RGRAM py
  PASS n=9076 FAIL 0, PINS-RGRAM set-eq 9076/9076;
  RAWENC 13/13, PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C
  legs all PASS), SMOKE 6/6, SMOKE-IMPL 6/6, OUTER2
  284/284, RB2 47/47, RAVFRAME 181/181, UNITS 22,
  LZ4C 5, PINS-RAWENC 11/11 (+C), PINS-PBZE 10/10
  (+C), PINSET OUTER2/RB2/RAVFRAME set-eq, OSS
  nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 4538/4538 GREEN rc=0 0 FAIL
  covered=4538/4538 (corpus seeded r16h-b219 4788 +
  missing-only fresh-oracle regen, py+C freshly
  executed per pin).
- C-batt RGRAM-GREEN rc=0 9076/9076 0 FAIL
  (RGRAM_BIN=seat-private -O2 -Wall -Wextra -std=c11
  build, 0 warnings, 2117400 B).
- own-loop 69725..69980 fresh-oracle 256/256
  py-agree, pins 24/24, rc=0.
- Added 4/4 EQ (C 2D _T10R150C 71n + _N=71
  derived rows, _T10R150M 16/16 + _T10R150Q 16/16
  C==py); full audit 1D 167/0 + 2D 901/0 +
  dicts 11/0 + STR 302/0 + STRARR 1142/0
  (vs b219 2D 897 / STR 299 / STRARR 1135; 1D
  const; +4/+3/+7 for +2 tiers/+24 pins, no drift).
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL raw; all 9 sets
  IDENTICAL b219->b221 first-hand (HYG .aar 13,
  AEA 2, CHIT 42, Mach-O 0, depload 1, OSS 37/0-new,
  LIBC aad.c 3 lines), cross-checked vs live gate.log.
  ADOPT WARN diff carried (c8f52713/c5f921d5 const;
  smoke.sh 56d751f9/56d751f9 same).
- Quiz diff 0 (rechecked before filing, max Q361).
- Verdict: PASS-functional. No RED. Unblocks VERIFY + parent merge.
