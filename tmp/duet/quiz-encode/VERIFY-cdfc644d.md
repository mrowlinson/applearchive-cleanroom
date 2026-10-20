# VERIFY-cdfc644d b304 T10P196 pins 84945..85292 (1128 tiers): PASS

viewer-r33, first-hand, detached tree NVME tmp/encode-viewer/r33/
tree-cdfc644d @cdfc644d (base fc1d9af3 = b303 tip), seat build
build304/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2613624 B, sha256 rgramc ce6518bf / aae d6e27c97
  (BOTH == GATE).
- RGRAMC-PYID 5769/5769 covered=5769/5769 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11538/11538 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11538/11538 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11538/11538).
- PINS-RGRAM cell set-eq 11538/11538 (cmp-identical).
  PINS N-set == for-list 5769/5769 (== GATE).
- PINS 11540 rows = 2 hdr + 11538, +68 vs base (11472).
  For-list +34 exactly: 84945 84946 84947 84954 84962 84963
  84964 84965 84966 84967 84968 84969 84970 84971 84972
  84973 84980 84988 84989 84991 84992 85004 85005 85012
  85020 85021 85028 85036 85037 85119 85120 85247 85248
  85292. 0 removed (== GATE; `; do` stripped before
  tokenize). 5769x2 = 11538 PASS lines (== GATE).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 84945..85292 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P196 C-vs-py mechanical, ALL EXACT: S0-S7
  168-hex-char singletons 1/1 each; AM 16/16, BM 2/2,
  ALTM 16/16, RM 16/16, RQ 16/16; P80 2/2 (py hex ints
  vs C longs, vals 136/190); AC 75/75, BC 72/72,
  ALTC0/1/2/3 75/75 each, PC 81/81, RC 68/68 (py-hex vs
  C-decimal normalized); C _N decls 75/72/75x4/81/68
  match actual rows (== GATE). M/QR/QT/QC absent BOTH
  sides (grep-0 both files; == GATE). Sigs first-hand:
  S0=48030000 (REPEAT P195) S1=79ad0500 S2=9b720300
  S3=34e50600 (==PBB2) S4=9e720300 S5=9d720300 S6=
  9e720300 S7=9e720300; A=97d75a00 B=34e50600 ALT=
  3e293700/3d293700/3e293700/3d293700 PAIR=9d720300
  R=ae937203 (== GATE).
- Dispatch by eye both impls, 16 tiers in order: S0
  n=84945 / S1 n=84946 singletons; A 84947-84962
  off=n-84947, mtab 7B b6-8/76-79, b5 const 97 (=0x97,
  codebase hex-shorthand convention as b303); B 84963-
  84964 off=n-84963, mtab 10B b6,7/48-51/80-83;
  S2-S6 n=84965-84969 singletons; PAIR 84970-84971
  off=n-84970, b80 tab + consts; S7 n=84972 (off 27);
  ALT0/1/2/3 84973-85036 off=n-rowbase, SHARED mtab
  7B b13-15/76-79 + own ALTC0-3, B5-CARRY @84992 row1
  (84991 ff/97 -> 84992 01/98, lencode arith-ok); R
  85037-85292 off=n-85037 c=off&15 r=off>>4
  TRANSPOSED+TAILS-SWAPPED, b4=(0x5b+2off)&FF b5=0x98+
  (off>=83)+(off>=211), M7 b20-22/72-75 by COL, Q7
  b13-15/76-79 by ROW; A/B/PAIR/ALT raw lencode, all
  paylen 84. Ring edges arith-ok: 85119->85120 +
  85247->85248 ff->01 at off 82->83 / 210->211;
  flips {84992,85120,85248} (== GATE). C blocks carry
  T54218/223/228/243/259/264/269/274/279/284/298/303/
  318/333/348/363 py-line mirrors (16/16 exact ==
  GATE). Insert position exact both sides: after
  T10P195R close, before dispatch-tail fallthrough
  ("N out of scope" + return 2). (== GATE.)
- py diff pure addition: rgram.py +370/-0 in 2 hunks
  (tables after _T10P195RC, dispatch in main()),
  test_rgram.sh +1/-1, PINS +68/+0.
- C diff renumber-only + new: numstat 2588 add / 1484 del;
  raw grep 2572 add / 1484 del + 16 blank-only `+` / 0
  blank-only `-` (all == GATE; 2572+16=2588 consistent).
  Fine-norm (_t/_i/_b/T) del-uniq 1481 / add-uniq 1976 /
  0 missing (== GATE exact; 1976 counts the blank-plus
  uniq-empty — blanks-excluded variant is 1975, miss 0
  either way, noted for provenance). (BSD sed: bare
  T[0-9]+ used, `\b` is a no-op.)
- Wall on band diff added lines (fc1d9af3..cdfc644d, 3027
  added lines == GATE scope): vendor/disasm/depload/
  libcompression/CT-shim/shebang//usr/bin/aa 0 hits.
  Files: rgramc.c 2588/1484, rgram.py +370/+0 purely
  additive, test_rgram.sh 1/1, PINS +68/+0.
- CONFIRM evidence: A-429-q428-t10p196 verdict CONFIRM
  45/45 (20+13+12, live re-derive; == GATE), A-421-q427
  45/45 itemized (20/20+13/13+12/12; == GATE), A-266
  corroborates geometry + const convention (== GATE),
  no DISSENT (CONVERT-01 rule b). No CONFIRM-P196.md
  file (== GATE; A-429 suffices per rule). GATE's A-421
  cites (VPOS A list, B b4+M10, ALT b4+M7, R 16, sigs,
  lencode 92/92, const-diffs 11/11/11B, M-tails 16/16
  NEW, edges, flips, DET34) all verbatim in file.
  For-list +34 carries B5-carry 84991/92 + ring edges
  85119/20 + 85247/48 (== GATE DET34 note). Memo excl
  75/72/75x4/68 == code tables; PC 81 consistent (PAIR
  VPOS [4,80] + const b5).
- GATE prose CORRECT throughout (build incl both shas,
  counts, for-list + tokenize note, tables incl P80 2/2
  + ALTC 75x4 + absence note, _N decls, sigs incl
  S3==PBB2, mtab byte lists, carry/edge arithmetic,
  T-mirrors, insert position, blank-line accounting,
  fine renumber counts, A-429/A-421/A-266 recon). No
  slips.

Agrees with GATE-cdfc644d (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r33/
(*304* files).

Verdict: PASS. Ready for parent PV + merge.
