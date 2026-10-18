# GATE-a2923bc sweep: PASS-individual (rgram 2222/2222; RANGE still HELD)

- tip: lanes/encode-writer2 @a2923bc (parent b25a422 gated PASS). rgram.py
  +50/-1, cells to 16736, pins 2206->2222 (+16/-0, append-only).
- code read (ALL): _T10HT 16 tabs (5B) + _T10HB5 16 b5-vals + _T10HB 16
  block-words (7B) + _T10HC consts (56 keys, unique; tab/block bytes
  excluded) + branch n<=16736 (off=n-16481, m=off&15, q=off>>4): m<=15
  (16 tabs), q<=15 (B5/HB len 16 each), b5=B5[q]+(m==15&q in 1,9),
  blk=HB[q], tab=HT[m]. paylen gate +72 (the ONE modified line, explained:
  72B tier opens — same class as +64/+68). contiguous after T9P1Q (16481
  follows 16480), paylen 72. no imports/OSS/disasm markers.
- battery: GATE-PASS shipped legs (outdir gate-w2-a2923bc-s4): HYGIENE/
  CONTAM clean, RGRAM n=2222, PINS-RGRAM set-eq 2222/2222, OSS none,
  LIBCOMP zero, ADOPT match. PLUS manual RED-cell re-verification @tip:
  N=15752 fresh bytes => CLOSED T9L1Q rc=0 (fix holds).
- verdict: PASS for THIS tip's code. FLAG-48ebfe0-hold STILL BLOCKS the
  range (15752 not restored — verified absent in this tip).
- NIT (no FAIL, persistent class): message "(2224 pins)" counts 2 csv
  comments; data rows 2222 (battery decisive).
- coverage: 148/149 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
