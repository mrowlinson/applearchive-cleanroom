# GATE-3ef1563 sweep: PASS-individual (rgram 2108/2108; RANGE still HELD)

- tip: lanes/encode-writer2 @3ef1563 (parent 48ebfe0 RED-held). rgram.py
  +44/-0, cells to 16040, pins 2088->2108 (+20/-0, append-only).
- code read (ALL): _T9M1QT 16 tabs (7B) + _T9M1B5 16 b5-vals + _T9M1QC
  consts (52 keys, unique; tab/word bytes excluded) + branch n<=16040
  (off=n-15785, m=off&15, q=off>>4): m<=15 (16 tabs), q<=15 (B5/L1Q24A/
  L1Q25A/L1QT-rot len 16 each), b5=B5[q]+(m>=7&q in 5,13), blk=L1QT[q],
  tab=QT[m]. contiguous after T9L1Q (15785 follows 15784), paylen 68.
- battery: GATE-PASS shipped legs (outdir gate-w2-3ef1563-s4): HYGIENE/
  CONTAM clean, RGRAM n=2108, PINS-RGRAM set-eq 2108/2108, OSS none,
  LIBCOMP zero, ADOPT match. PLUS manual RED-cell re-verification @this
  tip: N=15752 fresh oracle bytes => CLOSED T9L1Q rc=0 (fix holds).
- verdict: PASS for THIS tip's code. BUT FLAG-48ebfe0-hold STILL BLOCKS
  the range (15752 not restored to for-list in this tip — verified
  absent). parent: do not merge 48ebfe0..3ef1563 until a descendant
  restores the cell + re-gate greens (then FLAG-CLEARED-48ebfe0).
- NIT (no FAIL, persistent class): message "(2110 pins)" counts 2 csv
  comments; data rows 2108 (battery decisive).
- coverage: 143/144 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
