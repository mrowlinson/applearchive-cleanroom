# GATE f539e0c8 b413 T10P305 pins 122877..123224 (348 pins) PASS-functional

Seat sweep-r65, first-hand, WT tmp/wt-encode-sweep @f539e0c8,
TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-sweep/r65.
Band = e53a773d (py merge w2b@c942f03b partial, +6 tiers
+62 pins) + f539e0c8 (C port). Base 05055220 (b412 tip,
1812 tiers sealed).

- Build: make -C src/c BUILDDIR=r65/build413 aae rgramc
  (BUILDDIR absolute NVME path, flags -O2 -Wall -Wextra
  -std=c11 per Makefile), rc=0, 0 warnings (log = 4
  mkdir/cc command echoes only), build413/{aae,rgramc}.
  aae sha1 7d8dd3a2 / sha256 d6e27c97 (pinned stable
  continues: sha1 r39-r65, sha256 matches b354-b413
  pinned value; band touches no aae sources), rgramc
  sha1 3b8cd518 / sha256 ad486bdf.
- RGRAMC-PYID 9029/9029 covered=9029/9029 GREEN rc=0
  (tests/test_rgramc_fast.py, RGRAMC=seat binary,
  CT_CACHE_DIR set).
- RGRAM py 18058/18058 PASS 0 FAIL RGRAM-GREEN rc=0
  (tests/test_rgram_fast.py, CT_CACHE_DIR set).
- RGRAM C 18058/18058 PASS 0 FAIL RGRAM-GREEN rc=0
  (RGRAM_BIN=seat binary); C-py PASS-set cmp-equal
  (18058/18058, sorted).
- PINS-RGRAM cells set-eq 9029/9029 (xor 0 all 4 ways:
  for^pass-py for^pass-C py^C for^pins).
  PINS 18060 rows (2 hdr + 18058, +62 vs base 17998).
  For-list union 8998->9029 +31/-0 (python sets,
  trailing-';' stripped, never comm).
  31 = 2 sing (122877 122878) +
  A 6 (head 122879 + 122880 + 122886 + 122887 +
  122893 + tail 122894; offs 0,1,7,8,14,15) +
  C 6 (head 122895 + 122896 + 122899 + 122900 +
  122903 + tail 122904; offs 0,1,4,5,8,9; offs
  2,3,6,7 unsampled: 122897, 122898, 122901,
  122902) +
  Q 10 (head 122905 + off8 122913 + off16 122921 +
  off24 122929 + off32 122937 + off40 122945 +
  off48 122953 + off56 122961 + tail pair
  122967/122968; offs 0,8,16,24,32,40,48,56,
  62,63) +
  R 7 (head 122969 + edge pair 123007/123008 +
  mid 123097 + edge pair 123135/123136 + tail
  123224; offs 0,38/39,128,166/167,255).
  PINS adds = same 31 tier pins (2 rows each).
  Each for-N yields 2 PASS lines; 31x2 = 62
  = 18058-17996.
- SMOKE-GREEN rc=0 (6/6: aar encode/decode/bytes + aea
  encrypt/decrypt/bytes PASS, default oracle backend, no
  BACKEND var; workdir on NVME TMPDIR).
- Tables audit P305 C-vs-py, 12-table A-PBA88-STEP/
  C10-1SIG/QUAD88-2SIG+T88-RING-STANDARD layout, all EXACT:
  S0/S1 const strings EXACT (168 hex chars each,
  sigs db1b7900 NEW / 80299f81 NEW ==own-C10-sig;
  S0 diff vs P304S0 38/84 @ b0-2,4,5,11,19-39,
  52-55,72,74-79 NOT byte-equal + S1 diff vs P304S1
  62/84 @ b0-5,11-19,21-55,72-83 NOT byte-equal +
  S1 diff vs own C10 cells [22,22,22,22,22,22,22,
  21,21,23] NON-uniform (cell0 22 @ b4,5,34,35,
  42-51,56-59,80-83), NOT byte-equal);
  AM 16/16 (9B), CM 10/10 (11B), M 16/16 (7B),
  QR 4/4 (12B), RM 16/16 (7B), RQ 16/16 (7B)
  EXACT;
  AC 77/77, CC 71/71, QC 67/67, RC 72/72 EXACT
  (py-hex vs C-decimal normalized);
  C _N decls 77/71/67/72 match actual;
  TABAUDIT-GREEN rc=0 (tabaudit413.py 89 PASS 0 FAIL).
  No F/F0/F1 (no frags), no BM/BC (C10, not B10),
  no M19/X19, no M42/X42/H42/L42, no QB/PT/FM,
  no RT/TT (ring, not ROWTAIL), no QT (R12 carries
  b84-87 inside QR); table inventory exactly the 12.
  Missing-sets first-hand EXACT: AC-11 [4,5,51,52,
  53,54,55,80,81,82,83] = b4,b5+M9 (b51-55,
  80-83);
  CC-13 [4,5,15,46,47,48,49,50,51,80,81,82,83] =
  b4,b5+M11 (b15,46-51,80-83, full sig b0-3 in
  CC = 80,29,9f,81 -> 80299f81 x10);
  QC-21 [0,4,5,6,7,12,19,50,51,52,53,54,55,80,
  81,82,83,84,85,86,87] = b4,b5+QM7
  (b6,7,12,80-83)+R12 (b0,19,50-55,84-87);
  RC-16 [4,5,6,7,9,13,14,15,76,77,78,79,80,
  81,82,83] = b4,b5+TR7 (b6,7,9,76-79)+TM7
  (b13-15,80-83).
  STEP first-hand: AC b0..b3 = 09,00,00,00 ->
  sig 09000000 x16, b0 const 09; AM 16/16
  distinct; b5 0xbf+(o>=1) step o0->1 (earliest
  PBA step: 2nd cell).
  1SIG first-hand: CC b0-3 full sig 80299f81 x10
  SAME-as-PB1-sig (S1 sig-eq own C10); CM 10/10
  diverge; b5 const c0, NO step; 10/10 diverge.
  Code AC77/CC71/QC67/RC72; incl = +0/+1/+1/+0
  (A b5-step, C b5 const c0, Q b5 const c0, T
  counter) = 77/72/68/72; lane consts =
  A-779 INCL EXACT (deduct-b5-only-when-b5vary
  rule holds; PBA-step +0 like Q-step P303).
  Dispatch verified by eye both sides, all 6 blocks
  (2 sing + A/C/Q/R): P3050 n==122877 / P3051
  n==122878 singleton-const (offs 0/1);
  P305A 122879..122894 off=n-122879 PBA88-STEP
  (m-tab 9B b51-55,80-83, sig 09000000, b0
  const 09, b5 0xbf+(o>=1) step o0->1);
  P305C 122895..122904 off=n-122895 C10-1SIG
  (m-tab 11B b15,46-51,80-83 M11, full sig b0-3
  in CC = 80299f81, b5 const c0, NO step);
  P305Q 122905..122968 off=n-122905 m=off&15
  q=off>>4 QUAD88-2SIG row0 04000000 x16 +
  rows1-3 08000000 x48 (M 7B b6,7,12,80-83
  QM7 shared across sig boundary NO frags + R12
  b0,19,50-55,84-87 r0 04fa935e distinct +
  r123 share 8B 0808120e51f14f82, tails b84-87
  4 distinct 6435c2fa/eeaf4f2a/13b04f2a/
  d4ed1b48, r1r2 pair-only 2B 4f2a, r0 lcs 0
  vs all AND r3 lcs 0 vs all, r123 lcpre 8,
  full-row lcsuf r1r2=2 else 0, b5 const c0
  NO step, b4 0x33..0xb1 base 0x33 step2
  NO edge);
  P305R(T88-ring) 122969..123224 off=n-122969
  c=off&15 r=off>>4 STANDARD sig 84000000 (TM
  7B b13-15,80-83 by COL + TR 7B b6,7,9,76-79
  by ROW SPLIT tails UNPAIRED 16/16,
  b84-87 const c3/72/80/2f);
  A paylen 88 / C paylen 84 / Q paylen 88 + raw
  lencode l16=((n<<1)|1) &0xFFFF pay4=l16&0xFF
  pay5=l16>>8 (b5-step/const emerges from raw
  lencode);
  R paylen 88 +
  counter b4=(0xb3+2off)&FF b5=0xc0+(off>=39)+
  (off>=167).
  C blocks carry T82309/82314/82319/82334/82350/
  82371 py-line mirrors (exact); guards
  `if ((n) == (122877))` / `if ((n) == (122878))`
  + 4 ranges `if ((lo) <= (n) && (n) <= (hi))`
  exact; counter 179+2*off + 192+(off>=39)+
  (off>=167); temps _t6309.._t6324 appended
  (base max _t6308, no reuse); _i band 3825,
  3827,3830,3833 (base max _i3823), _b band
  3824,3826,3828,3829,3831,3832 (base max
  _b3822), no reuse; C byte-index lists match py
  per block (A 9B, C 11B, Q 7B/12B, R 7B/7B);
  insert position exact (P304R block precedes, N
  out-of-scope follows; C has 2 scope hits; py
  has 2 scope hits).
  Value checks first-hand: AM 16/16 distinct;
  CM 10/10 diverge; M 16/16 distinct;
  QR 4/4 distinct UNPAIRED (r0
  04fa935e...6435c2fa; r1
  0808120e...eeaf4f2a; r2
  0808120e...13b04f2a; r3
  0808120e...d4ed1b48);
  QR full-row lcsuf: r1r2 2, all other pairs 0;
  r123 lcpre 8B 0808120e51f14f82;
  RQ==M DIAG6 (M 7B vs RQ 7B: agree (0,0),
  (1,1),(3,3),(4,4),(5,5),(6,6) 16/16 each,
  RQ[2] isolated maxagree 0/16 2-distinct
  f4/f5, RQ[0] maxagree 16 distinct 15, RQ[1]
  maxagree 16 distinct 5, zero off-pattern
  incidentals) -- HEAD2+TAILS degree (heads b6,
  b7 + full tails agree; mid byte b9-vs-b12
  differs; NEW variant, joins neither prior
  group);
  24th odd-band RQ==M instance;
  tails STANDARD-SPLIT (RM b80-83 by COL c=off&15,
  RQ b76-79 by ROW r=off>>4, 16/16 distinct each,
  0 overlap UNPAIRED);
  M-tails 16/16 ALL NEW vs P304T RM col-led tails
  (overlap 0); RM-tails (b80-83) ALL NEW vs P304T
  RM col-led tails (overlap 0); RQ-tails (b76-79)
  ALL NEW vs P304T RQ row-led tails (overlap 0);
  cross overlaps 0 (P304T widths RM 7B/RQ 7B
  first-hand);
  S0 NEW string (38/84 differ vs P304S0 @ b0-2,4,
  5,11,19-39,52-55,72,74-79) + S1 NEW string
  (62/84 differ vs P304S1 @ b0-5,11-19,21-55,
  72-83; [22,22,22,22,22,22,22,21,21,23]
  NON-uniform vs own C10, cell0 22 @ b4,5,34,
  35,42-51,56-59,80-83);
  P305 actuals (S0 db1b7900/S1 80299f81/PBA88
  09000000/C10-1SIG 80299f81 x10 SAME-as-PB1-sig
  + PB1-vs-C10 22/84) == A-777 predicted next
  EXACT.
  Counter/lencode edges computed first-hand (never
  trusted from comments): A head ff/bf (122879)
  edge o0->1 (122879->122880) ff/bf->01/c0
  tail 1d/c0 (122894), b5set {bf,c0}; C head
  1f/c0 (122895) tail 31/c0 (122904), b5set
  {c0};
  Q head 33/c0 (122905) tail b1/c0 (122968)
  b5set {c0};
  quad b4=(0x33+2off) 64/64;
  T head b3/c0 (122969) + off38/39 (123007->
  123008) ff/c0->01/c1 + mid off128 b3/c1
  (123097) + off166/167 (123135->123136)
  ff/c1->01/c2 + tail off255 b1/c2 (123224).
  All edge pins in for-list + PASS (batteries
  GREEN); 123224 tail pinned + in for-list +
  PASS (direct first-hand: cache-hit rav sha
  ccac87af1ba01cb4... matches PINS rawlen 104,
  py+C CLOSED T10P305R off=255 agree).
  Ring counter==raw-lencode 256/256 mismatches 0;
  odd-lencode 348/348 first-hand (346 + S0/S1
  embedded b4/b5 fb/bf + fd/bf).
  Matches A-779 geometry (12x84B+336x88B framing
  PINS-confirmed 100x16+104x46, PB0 db1b7900 NEW
  + PB1 80299f81 NEW sig-eq own-C10 22/84,
  PBA88-STEP VPOS 11 b5-step o0->1 NO pair,
  C10-1SIG VPOS 12 b5 const c0 10/10 diverge,
  QUAD88-2SIG VPOS 20 QM7+R12 + R12 4/4 UNPAIRED
  + tails b84-87 4 distinct r1r2-pair-2B r0+r3
  isolated + M-tails ALL NEW 16/16, T88-RING
  STANDARD sig 84000000 TM7 by COL + TR7 by ROW
  UNPAIRED 16/16 + SPLIT tails + b84-87 const
  c372802f, ring edges + thresholds 39/167,
  NO D dips).
- C diff pure-add: numstat 604/0 rgramc.c + 230/0
  rgram.py (+1/-1 for-line, +62/0 PINS); raw C 604
  content + 5 blank-only `+` lines / 0 del; raw py
  230 content / 0 del;
  normalized ([0-9]+ -> N, diff-sign strip,
  trailing-';' strip, python sets) del-subset-add
  0 missing (C del-uniq 0 add-uniq 161, py del-uniq
  0 add-uniq 179). Band-level sole del = old
  for-line churn (for-line 1/1).
- Wall on band diff added lines (scope 05055220..
  f539e0c8, 897 added lines): vendor/disasm 0
  hits, depload (dylib/CDLL/dlopen/ctypes/
  LoadLibrary/System.load) 0 hits, libcompression/
  /usr/bin/aa 0 hits, shebang 0 hits. Files
  touched: rgramc.c 604/0, rgram.py 230/0,
  test_rgram.sh 1/1, PINS 62/0.
- Tiers: merge-msg +6, code 6 blocks,
  tier-comments `# T10P` 1718->1724 +6, singletons
  `if n == ` 642->644 +2, range-guards `<= n <=`
  672->676 +4, CLOSED T10P prints
  1718->1724 +6, seal 1812->1818
  +6 (cport msgs; offset +94 vs CLOSED-T10P stable
  b401-b413): all agree (stated literal methods,
  first-hand).
  C guards: singleton `if ((n) == (` 637->639 +2,
  range 672->676 +4; 5-count C-vs-py singleton
  offset pre-existing (same C-only dip guards as
  b357-b411 odds), unchanged by band.
- CONFIRM evidence (CONVERT-01 rule b): A-779-q897
  memo CONFIRM 58/58 CLEAN (section heads shape
  27/27 + quad+T-ring 16/16 + counters 15/15
  quoted verbatim; ZERO section-F; tier cut SAFE;
  w2b-r25 [6/8]; Port verdict: 2nd straight fully
  clean w2b sheet).
  Viewer: NO P305 geometry answer on file at gate
  time (memo-only recon; viewer VERIFY lands
  post-gate per pipeline order).
  No DISSENT on P305. Agrees with cport commit msg
  (py/C 18058, PYID 9029).
- Quiz: no conflicting CLAIM/GATE/FLAG on b413/
  f539e0c8. b412/b414 EVEN = sweep2 turf, used b412
  tip as diff-base only, NOT gated. Newest PARENT-*
  is QNUM-22 (w2e Q-block refill only, read, no gate
  impact); PROSE-01 re-read before filing.
- Logs: NVME ws tmp/encode-sweep/r65/ (build413.log,
  b413-pyid.log, b413-py/c.log, pass413py/c.txt,
  seteq413.py/log, b413-smoke.log, tables413.log,
  tabaudit413.py, edges413.py, edges413.log,
  cdiff413.txt, pydiff413.txt, banddiff413.txt,
  added413.txt, numstat413.txt, diffwall413.py/log,
  build413/ binaries,
  tail-123224.rav).

Verdict: PASS-functional. No RED. Ready for viewer VERIFY.
