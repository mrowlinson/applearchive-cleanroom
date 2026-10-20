# GATE cdfc644d b304 T10P196 pins 84945..85292 (1128 tiers) PASS-functional

Seat sweep2-r38, first-hand, WT tmp/wt-encode-sweep2 @cdfc644d,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep2/r38.
Band = 241a980a (py merge w2b@0da37af9 partial, +16 tiers +68 pins)
+ cdfc644d (C port). Base fc1d9af3 (b303 tip).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile,
  seat-private build304/bin/{aae,rgramc} (BUILDDIR= override),
  rc=0, 0 warnings. sha256 rgramc ce6518bf / aae d6e27c97
  (aae identical to b288-b302 builds: aae.c untouched).
- RGRAMC-PYID 5769/5769 covered=5769/5769 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary, ct-cache).
- RGRAM py 11538/11538 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, ct-cache).
- RGRAM C 11538/11538 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (diff 0 lines, 11538/11538).
- PINS-RGRAM cells set-eq 5769/5769 (diff 0, PINS base-N
  set vs for-list); PINS 11540 rows (2 hdr + 11538 =
  PASS lines). For-list union +34 (84945 84946 84947
  84954 84962 84963 84964 84965 84966 84967 84968
  84969 84970 84971 84972 84973 84980 84988 84989
  84991 84992 85004 85005 85012 85020 85021 85028
  85036 85037 85119 85120 85247 85248 85292),
  0 removed (`; do` stripped before tokenize). Each for-N
  yields 2 PASS lines (g-zN-closed + g-zN). The 34 ARE
  the DET34 set (B5-carry 84991/92 + T-ring edges
  85119/20 85247/48 incl).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Tables audit P196 C-vs-py, script-compared, all EXACT:
  S0/S1/S2/S3/S4/S5/S6/S7 1/1 each, AM 16/16, BM 2/2,
  AC 75/75, BC 72/72, ALTM 16/16, ALTC0/1/2/3 75/75
  each, P80 2/2, PC 81/81, RM 16/16, RQ 16/16,
  RC 68/68; C _N decls 75/72/75x4/81/68 match actual.
  M/QR/QT/QC absent BOTH sides (no Q tier in P196:
  16 tiers = PB0+PB1+PBA16+PBB2+7xSING+4xALT16+T-ring
  per A-421; tabc.py QC_N probe N/A, rc=1 on that
  probe only; tabc196.py covers S3-S7/ALT/P/R rc=0).
  Excl-consts 75/72/75x4/68 match A-421 exactly.
- Dispatch eye-verified both sides, 16 tiers in order:
  S0 n=84945 (PB0 sig 48030000 REPEAT P195), S1
  n=84946 (fat PB1 sig 79ad0500), A 84947-84962 PBA16
  (sig 97d75a00 NEW, mtab b6-8,76-79, b5 const 97,
  raw lencode), B 84963-84964 PBB2 (sig 34e50600 NEW,
  mtab b6,7,48-51,80-83, b5 const 97, raw lencode),
  SINGs 84965-84969 (9b720300/34e50600==PBB2/
  9e720300/9d720300/9e720300), PAIR 84970-84971
  (sig 9d720300, b80 tab + consts), SING 84972
  (9e720300), ALT0/1/2/3 84973-85036 (sigs 3e293700/
  3d293700/3e293700/3d293700, SHARED mtab b13-15,
  76-79 + own consts, B5-CARRY @84992 row1, raw
  lencode), R 85037-85292 T-ring TRANSPOSED+
  TAILS-SWAPPED sig ae937203 (M7 b20-22,72-75 by COL
  off&15, Q7 b13-15,76-79 by ROW off>>4, b4=
  (0x5b+2off)&FF, b5=0x98+(off>=83)+(off>=211)).
  C blocks carry T54218/223/228/243/259.../T54303/
  318/333/348/363 py-line mirrors. Insert position
  exact both sides: after T10P195R close, at dispatch
  tail (N-out-of-scope fallthrough follows). Matches
  A-421 geometry (VPOS A [4,6,7,8,76-79] / B b4+M10
  / ALT b4+M7 b13-15,76-79 / R 16, sigs, lencode
  92/92, const-diffs 11/11/11B, M-tails 16/16 NEW,
  T-ring edges 85119->85120 + 85247->85248 ff->01,
  flips {84992,85120,85248}, DET34 34 cells).
- C diff renumber-only + new: numstat 2588 add / 1484 del;
  raw grep 2572 add / 1484 del (16 blank-only `+` lines,
  verified; 0 blank `-`); normalized (_t/_i/_b/T numbers)
  del-subset-add 0 missing (del-uniq 1481, add-uniq
  1976). Pipeline validated: reproduces b302 del-uniq
  1466 / miss 0 (add-uniq 1849 vs r37 1848, +1 dedup
  edge, immaterial).
- Wall on band diff added lines (scope fc1d9af3..cdfc644d,
  3027 added lines): vendor/disasm 0 hits, depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load) 0 hits.
  Files touched: rgramc.c 2588/1484, rgram.py +370/+0
  purely additive, test_rgram.sh 1/1, PINS +68/+0.
- CONFIRM evidence (CONVERT-01 rule b): A-429-q428-t10p196
  verdict CONFIRM (45/45 checks, live; A-421-q427 45/45
  itemized, A-266 corroborates geometry/convention).
  No CONFIRM-P196.md file; A-429 suffices per rule.
  Agrees with cport commit msg (PYID 5769, RGRAM 11538).
- Quiz: no conflicting CLAIM/GATE/FLAG on b304. No new
  PARENT-* (newest PROSE-01, read at boot).
- Logs: NVME ws tmp/encode-sweep2/r38/ (build304.log,
  build304.sha, pyid304, rgram304py/c, cmp304.py/.c,
  for304-fc1d9af3/cdfc644d, for304-added, pins304.csv/
  .cells, seteq304, smoke304, tables304.log,
  tables304b.log, tabc.py, tabc196.py, cdiff304,
  cdiff304.del/.add, del/addnorm304, cdiff304.miss,
  banddiff304, added304, numstat304).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
