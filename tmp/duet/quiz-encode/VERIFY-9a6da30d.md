# VERIFY 9a6da30d b332 T10P224 pins 94689..95036 (1328 tiers) PASS

Seat viewer-r41, first-hand, fresh detached worktree tree-9a6da30d
(HEAD 9a6da30d, clean), TMPDIR /Volumes/NVME/applearchive-cleanroom-ws/
tmp/encode-viewer/r41. Base 6be444ff (b331 tip). CT shim on all
batteries (CT + CT_CACHE_DIR set; fast tests throughout).

- Build: make BUILDDIR=r41/build332/bin, rc=0, 0 warnings. aae
  sha256-8 d6e27c97 (== GATE), rgramc sha256-8 4652e61d (== GATE).
- RGRAMC-PYID 6524/6524 covered=6524/6524 GREEN rc=0 (own binary,
  tests/test_rgramc_fast.py, NVME workdir).
- RGRAM py 13048 PASS 0 FAIL RGRAM-GREEN rc=0 (fast, ct-cache).
- RGRAM C 13048 PASS 0 FAIL RGRAM-GREEN rc=0 (RGRAM_BIN=own binary).
- C-py PASS-set cmp-equal (13048/13048, diff 0).
- PINS 13050 rows (2 hdr + 13048 = 6524 sha + 6524 closed).
  Base-N set vs for-list set-eq 6524/6524 (diff -q clean).
- For-list union +26, 0 removed (old 6498 -> new 6524):
  94689 94690 94691 94698 94706 94707 94711 94716 94717 94719
  94720 94732 94733 94741 94748 94749 94757 94764 94765 94780
  94781 94847 94848 94975 94976 95036 (== GATE list verbatim).
- SMOKE-GREEN rc=0 (6/6, default oracle backend).
- Tables audit P224 C-vs-py, own script tables332.py rc=0 ALL-EXACT:
  S0/S1 len 168/168 eq, sigs 1f120000/fe042600, b4b5 c3e3/c5e3
  == lencode first-hand; AM16 BM10 M16 QR4 QT4 RM16 RQ16 all eq;
  AC75 BC71 QC65 RC69 all eq; _N decls 75/71/65/69 match; sigs
  fe044602/fe044e00/fe048604/409dff48; varsets exact (A 9: 4,5+
  32-34,76-79; B 13: 4,5+22,23,30,31,36-38,80-83; Q 19; R 15);
  cover84 x4 0-overlap; b4/b5 in no A/B const set (-1 bookkeeping,
  via lencode); QR r0==r1+r2==r3 DOUBLE-PAIRED 2/4 distinct
  01aae8f8749ec7 x2 / 89b8ccf914329a x2; QT verbatim 70ec9d9c/
  9cec9d9c/09ee0259/38ee0259, r0/r1 share ec9d9c + r2/r3 share
  ee0259; widths AM7/BM11/M6/QR7/RM7/RQ6; B-mtab 11-pos exact;
  B10M/QR11 share 8/11 {22,23,30,31,80-83}, B-only 36-38,
  Q-only 32-34; QM-heads==RQ-heads 16-set + full rows set-equal
  (M==RQ row-for-row); RM224-vs-RM223 shared 0/16 + QT224-vs-QT223
  shared 0/4 (M-tails ALL NEW first-hand); no PT/PC/CM/CC/FM/FC/
  FS/FO/H/TC syms either side; no extra P224 syms py/c.
- Dispatch eye-verified both sides, 6 blocks in order at dispatch
  tail after T10P223R close (N-out-of-scope fallthrough follows):
  S0 n=94689 PB0 1f120000 NEW, S1 n=94690 PB1 fe042600 NEW,
  A 94691-94706 PBA16 fe044602 (m-tab b32-34,76-79, b5 lencode),
  B 94707-94716 PBB10 fe044e00 single-sig (m-tab b22,23,30,31,
  36-38,80-83, b5 lencode), Q 94717-94780 QUAD fe048604 (m=off&15
  M6 b36,37,76-79, q=off>>4 R7 b22,23,30-34 + tails b80-83,
  b5-carry raw lencode), R 94781-95036 T-ring 409dff48 STANDARD
  (c=off&15 M7 b35,42,43,76-79, r=off>>4 R6 b36,37,72-75,
  b4=(0x7b+2off)&FF b5=0xe4+(off>=67)+(off>=195)).
  C T-mirrors 6/6: T61855/61860/61865/61880/61896/61919, py lines
  + bounds + comments exact; C guards/offs exact; C R-counter
  ((123+2*off)&255, (228+(off>=67))+(off>=195)) exact mirror.
- Edges recomputed first-hand from code formulas (all edge pins
  PASS): quad 94719 (off2, ff/e3) -> 94720 (off3, 01/e4) via
  l16=((n<<1)|1)&FFFF; ring 94847 (off66, ff/e4) -> 94848 (off67,
  01/e5); 94975 (off194, ff/e5) -> 94976 (off195, 01/e6) via
  counter formula. (== GATE.)
- C diff purely additive: numstat 606/0 + 237/0 + 1/1 + 52/0
  (== GATE); raw 606 add / 0 del (excl +++/--- headers); band
  added 896 total / 5 bare-`+` / 891 non-blank (== GATE 891).
  sh 1/1 = for-list line rewrite (+26/0rem verified above).
  Number-norms: plain ([0-9]+->N) add-uniq 156; own fine
  (_t/_i/_b/T61xxx, empty-excluding) add-uniq 379; del-uniq 0
  under every norm -> del-subset-add miss 0. GATE fine 377:
  same verdict (miss 0); absolute differs by 2 under their
  unspecified seds (method-relative, not rechecked further).
- Wall on band added lines (891): vendor/disasm/depload(7)/
  libcompression/CT-cache/CT_REAL/compression_tool/shebang/^+#!
  /usr/bin/aa/nominat 0 hits throughout (13 patterns).
- Tiers: merge-msg +6, code 6 blocks, dispatch-guards singletons
  480->482 +2 / ranges +4 (own count 344->348; GATE stated-method
  322->326; delta +4 agrees both ways), seal 1322->1328 +6
  (commit msgs): all agree.
- Band comp: 4c741ebb (py merge w2b@21b18db2 partial, +6 tiers,
  +52 pins) + 9a6da30d (C port). Matches GATE.
- CONFIRM: A-502-q616-t10p224 CONFIRM 28/28 (14/14 shape + 10/10
  quad/ring + 4/4 counters, own bed, read in full). Citation
  "A-502-q616" CORRECT (file A-502-q616-t10p224-geometry.md).
  No CONFIRM-P224.md file; rule-b satisfied. A-294 recon: sigs
  6/6, VPOS sets, double-pair + tails verbatim, B10M/QR 8/11 +
  B-only/Q-only, M-tails 16/16 NEW, R6 UNPAIRED 16/16, lencode
  348/348, ring formulas + edges, consts 76/72/65/69 with -1
  bookkeeping resolved, NO D dips: all consistent first-hand.
- Own-loop ownloop332b.py (cache-path-direct, zero-write):
  348/348 ok, 0 bad, rc=0. (322 non-pin Ns fetched via the
  tool-identical -encode -a lzraven invocation; 26 pins
  pre-cached. No truncated entries seen.)
- Quiz: no conflicting CLAIM/GATE/FLAG on b332. Newest PARENT-*
  QNUM-08..12 (writer Q-blocks only, read, no gate impact).

Verdict: PASS. GATE CORRECT, 0 slips (prose + code).
Logs: NVME ws tmp/encode-viewer/r41/ (tree-9a6da30d detached;
build332.log, pyid332.log, rgram332py/c.log, pass332py/c.txt,
for332-old/new.nums, pins332-base.nums, smoke332.log, tables332.py/
.log, cadd332.txt, addnorm332-GATE/fine.txt, delnorm332-GATE.txt,
added332.txt, numstat332.txt, ownloop332b.py/.log, populate332.py/
.log, ownloop-work332/, smoke332work/, scratch332py/c/, pyid332work/).
