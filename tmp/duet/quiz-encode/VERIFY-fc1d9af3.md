# VERIFY-fc1d9af3 b303 T10P195 pins 84597..84944 (1112 tiers): PASS

viewer-r33, first-hand, detached tree NVME tmp/encode-viewer/r33/
tree-fc1d9af3 @fc1d9af3 (base de815ae0 = b302 tip), seat build
build303/ rgramc, env CT shim + CT_CACHE_DIR (CT-CACHE-01),
fast batteries (FASTBAT-01).

- Build: cc -O2 -Wall -Wextra -std=c11 via src/c/Makefile, rc=0,
  0 warnings, 2596472 B, sha256 rgramc 5da7da91 / aae d6e27c97
  (GATE cites aae sha only == match; rgramc sha first-hand).
- RGRAMC-PYID 5735/5735 covered=5735/5735 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary).
- RGRAM C 11470/11470 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary, tests/test_rgram_fast.py).
- RGRAM py 11470/11470 PASS 0 FAIL RGRAM-GREEN rc=0.
- C-py PASS-set cmp-identical (11470/11470).
- PINS-RGRAM cell set-eq 11470/11470 (cmp-identical; == GATE).
  PINS N-set == for-list 5735/5735 (== GATE).
- PINS 11472 rows = 2 hdr + 11470, +46 vs base (11426).
  For-list +23 exactly: 84597 84598 84599 84607 84608 84615
  84616 84617 84618 84621 84624 84625 84640 84641 84657
  84673 84688 84689 84735 84736 84863 84864 84944.
  0 removed (== GATE).
- SMOKE-GREEN rc=0 (6/6: aar+aea encode/decode/bytes PASS).
- Own-loop 84597..84944 every N (own script, fresh C+py
  subprocesses per N, oracle via ct-cache/miss=real tool):
  348 ok / 0 bad, rc=0, C-stdout==py-stdout, CLOSED all.
- Tables P195 C-vs-py mechanical, ALL 15 EXACT: S0/S1/S2
  168-hex-char singletons 1/1 each; AM 16/16, BM 9/9,
  M 16/16, QR 4/4, QT 4/4, RM 16/16, RQ 16/16; B42 16/16
  (py hex ints vs C longs); AC 76/76, BC 70/70, QC 65/65,
  RC 67/67 (py-hex vs C-decimal normalized); C _N decls
  76/70/65/67 match actual rows (== GATE). Excl-b5
  accounting confirmed in-table: no (5,v) entry in any of
  the 4 const tables (== GATE). Sigs first-hand: S0=
  48030000 (REPEAT P194: _T10P194S0 head 48030000), S1=
  79ad0500, S2=d3dd0300 (NEW); A=79ad6900, B=79ad0500
  (== PB1/S1), Q=79ad7900, R=79ad9906 (== GATE).
- Dispatch by eye both impls, 7 tiers in order: S0
  n=84597 / S1 n=84598 singletons (offs 0/1); A 84599-
  84614 off=n-84599, mtab 6B b36,37/76-79; B arm1
  84615-84616 off=n-84615 + arm2 84618-84624 off=n-84616,
  mtab 12B b32,33/37-42/80-83; S2 n=84617 (off 20);
  Q 84625-84688 off=n-84625 m=off&15 q=off>>4, M 5B
  b43/76-79, B42 row-rule (q<2 id, q==2 |1, else ^2),
  b34 col-half (0x17 m<8 else 0x1f), QR b36-41, QT
  b80-83; R 84689-84944 off=n-84689 c=off&15 r=off>>4
  TRANSPOSED, b4=(0xa3+2off)&FF b5=0x95+(off>=47)+
  (off>=175), RM b48-51/72-75 by COL, RQ b34/42/43/
  76-79 by ROW; A/B/Q raw lencode, all paylen 84.
  Step arithmetic first-hand: lencode @84608 ff/94->
  01/95 (carry), ring b4 edges 84735->84736 + 84863->
  84864 ff->01 at off 46->47 / 174->175 (== GATE).
  C blocks carry T53902/907/912/927/943/948/964/993
  py-line mirrors (8/8 exact line numbers == GATE).
  Insert position exact both sides: after T10P194R close,
  before dispatch-tail fallthrough (py "N out of scope"
  + return 2 / C L147118 identical). (== GATE.)
- py diff pure addition: rgram.py +268/-0 in 2 hunks
  (tables after _T10P194RC, dispatch in main()),
  test_rgram.sh +1/-1, PINS +46/+0.
- C diff renumber-only + new: numstat 2145 add / 1476 del;
  raw grep 2137 add / 1476 del + 8 blank-only `+` / 0
  blank-only `-` (all == GATE; 2137+8=2145 consistent).
  Coarse-norm ([0-9]+ -> N, cut-c2) del-uniq 949 /
  add-uniq 1125 / 0 missing (== GATE exact). Fine-norm
  (r31 recipe) del-uniq 1473 / add-uniq 1857 / 0 missing.
  (BSD sed gotcha: `\b` is a no-op — used bare T[0-9]+.)
- Wall on band diff added lines (de815ae0..fc1d9af3, 2460
  added lines == GATE scope): vendor/disasm/depload
  (dylib/CDLL/dlopen/ctypes/LoadLibrary/System.load)/
  libcompression/CT-shim/shebang//usr/bin/aa 0 hits.
  Files: rgramc.c, rgram.py, test_rgram.sh (for-line),
  PINS (+46/+0). Py side purely additive.
- CONFIRM evidence: A-420-q426-t10p195 verdict CONFIRM
  84/84 (23+14+5+42 section headers == GATE), no
  DISSENT (CONVERT-01 rule b); A-265 corroborates PBB
  2+7 split, b34 COLUMNS axis, consts 76/71/66/67 incl
  (== GATE). GATE's A-420 geometry cites (VPOS A list,
  top-paired r0==r1, TRANSPOSED+TAILS-SWAPPED, step,
  edges, flips {84608,84736,84864}) all verbatim in
  file. Memo incl-b5 76/71/66/67 consistent with
  excl-b5 code tables (b5 const only in B/Q zones).
- GATE prose CORRECT throughout (build, counts, for-list,
  tables incl BM 9/9 + B42 row-rule, _N decls, excl-b5
  note, sigs, mtab byte lists, counter formulas, step
  arithmetic, T-mirrors, insert position, blank-line
  accounting, coarse renumber counts, A-420/A-265 recon).
  No slips. (GATE omits rgramc sha; recorded first-hand
  above. Not a slip — no claim made.)

Agrees with GATE-fc1d9af3 (PASS-functional) on every
verdict-relevant leg. Logs: NVME ws tmp/encode-viewer/r33/
(*303* files).

Verdict: PASS. Ready for parent PV + merge.
