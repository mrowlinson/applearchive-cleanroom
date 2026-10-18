# GATE 2205fa1 b173 T10R126 n<=61628 (818 tiers) PASS-functional

- Seat encode-sweep r5, first-hand, seat-private logs
  r5-2205fa1* under NVME encode-sweep.
- Lane-diff vs P126 cport base: rgramc.c only
  +1167/-1006; wall 0. Range 61373..61628.
- gate-tip: RGRAM py PASS n=7804 FAIL 0,
  PINS-RGRAM set-eq 7804/7804; RAWENC 13/13,
  PBZE 10/10, LZMA 6/6, LZ4 4/4 (+ -C legs),
  SMOKE 6/6, OUTER2 284/284, RB2 47/47,
  RAVFRAME 181/181, UNITS 22, LZ4C 5,
  OSS nominated-only, C-BUILD warnings=0.
- RGRAMC-PYID 3902/3902 GREEN.
- C-batt 7804/0 GREEN.
- own-loop 61373..61628 fresh-oracle 256/0,
  pins 24/24, py-agree 256/256.
- Added 4/4 EQ (M str n=16, QH str n=16,
  C 2D n=68, C_N=68 derived-consistent);
  audit 1D 166/0 + 2D 805/0 + dicts 11/0 +
  STR 235/0 + STRARR 978/0.
- Scoped OBSERVED-inherited (PARENT-032 shape):
  HYGIENE/CONTAM/LIBCOMPRESSION FAIL; lane file
  0/0/0, HYG 13 identical 171->173, CONTAM fileset
  identical r2 (docs/spec prose + known depload FP),
  LIBCOMP aad.c only. ADOPT WARN diff carried
  (oracle-adapter lane/tip const).
- Verdict: PASS-functional. No RED.
