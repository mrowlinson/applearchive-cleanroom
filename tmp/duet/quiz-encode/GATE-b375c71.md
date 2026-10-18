# GATE-b375c71 sweep: PASS-individual x2 (rgram 2166/2166; RANGE still HELD)

- chain: lanes/encode-writer2 da93c06->20d3042(O1Q 7x16 16133-244)->
  b375c71(O2Q 8x16+11 16245-383). rgram.py +63/-0, pins 2148->2158->2166
  (+18/-0, append-only).
- code read (ALL). (a) O1Q: _T9O1QT 16 tabs (7B) + _T9O1QC consts (53 keys,
  unique) + branch (off=n-16133, m&q): tab=O1QT[m] (b5,6,7,56-59),
  blk=N1QT[q] (q0-6, len 16). (b) O2Q: NO new tables (O1QT/O1QC/N1QT
  reuse) + branch (off=n-16245, m&q): b5=int(_o[0:2],16)+((q>=1)|(m>=11)),
  tab=_o[2:] (b6,7,56-59), blk=N1QT[q+7] (q<=8 => idx<=15). q=8 m0-10 =
  +11 rows. all indices in-range, contiguous (16133/16245 follow priors).
  no imports/OSS/disasm markers.
- battery: GATE-PASS shipped legs (outdir gate-w2-b375c71-s4): HYGIENE/
  CONTAM clean, RGRAM n=2166, PINS-RGRAM set-eq 2166/2166, OSS none,
  LIBCOMP zero, ADOPT match. PLUS manual RED-cell re-verification @tip:
  N=15752 fresh bytes => CLOSED T9L1Q rc=0 (fix holds).
- verdict: PASS both tips' code. FLAG-48ebfe0-hold STILL BLOCKS the range
  (15752 not restored — verified absent in this tip).
- NIT (no FAIL, persistent class): messages "(2160/2168 pins)" count 2 csv
  comments; data rows 2158/2166 (battery decisive).
- coverage: 146/147 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
