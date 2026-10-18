# GATE-da93c06 sweep: PASS-individual (rgram 2148/2148; OUTER2 flake; RANGE HELD)

- tip: lanes/encode-writer2 @da93c06 (parent 3ef1563 gated PASS). rgram.py
  +118/-0, cells to 16132, pins 2108->2148 (+40/-0, append-only).
- code read (ALL): N1 branch (singles {16041,16042,16043,16059,16060} 68B
  each + A 16044-58 15-row + B fall-through 16061-68 8-row, 9B tab) + Q
  branch (m=off&15, q=off>>4, b5=0x3d+(m>=11&q==3), blk=QB[q] 8B,
  tab=QT[m] 6B). AST: S1-S5 68B, AT/BT 15/8, QT/QB 16/4. all indices
  in-range, contiguous after T9M1Q (16041 follows 16040). no imports/OSS/
  disasm markers.
- battery: RGRAM n=2148 + PINS-RGRAM set-eq 2148/2148 + HYGIENE/CONTAM/OSS/
  LIBCOMP/ADOPT all PASS. manual RED-cell re-verification @this tip:
  N=15752 fresh bytes => CLOSED T9L1Q rc=0 (fix holds).
- FLAKE (NOT writer regression): first OUTER2 run hit a-nd-p4 `got char 14
  want char 13` (p4 = ECIES+ECDSA nondet profile; exact first-diff-char
  pin on nondeterministic output flakes ~1/256/run by construction — same
  class as the conceded p0/p3 NOTE-FLAKE). 3/3 fresh re-runs GREEN first-
  hand (exit 0, PASS a-nd-p4). TIP EXONERATED. RECOMMEND (writer, non-
  blocking): relax p4 to verdict-only DIFF like p0/p3 (NOTE-FLAKE-da93c06
  has the analysis).
- verdict: PASS for THIS tip's code. FLAG-48ebfe0-hold STILL BLOCKS the
  range (15752 not restored — verified absent in this tip).
- coverage: 144/145 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
