# GATE-4365e9e sweep: PASS-individual (rgram 2272/2272; RANGE still HELD)

- tip: lanes/encode-writer2 @4365e9e (parent a2923bc gated PASS). rgram.py
  +204/-0, cells to 17084, pins 2222->2272 (+50/-0, append-only).
- code read (ALL 6 branches): DIP pair (16737-38, 68B lits) + A 16-row
  (16739-54, off0-15, AT 16) + BH 10-row dip-band (16755-64, off0-9, BHT
  10, paylen 68) + BQ 4x16 (16765-828, m0-15 BQT 16, q0-3 BQB 4, b5 rule)
  + B 16-row (16829-44, off0-15, BT 16) + Q 15x16 (16845-7084: m0-15,
  q0-14, QB5/QB1/QB4/QB41 len 15, blk=BQT[q+1]<=15 verb-skip, tab=BT[m]
  reuse). AST-verified all lens. contiguous throughout (each follows
  prior). no imports/OSS/disasm markers.
- battery: GATE-PASS shipped legs (outdir gate-w2-4365e9e-s4): HYGIENE/
  CONTAM clean, RGRAM n=2272, PINS-RGRAM set-eq 2272/2272, OSS none,
  LIBCOMP zero, ADOPT match. PLUS manual RED-cell re-verification @tip:
  N=15752 fresh bytes => CLOSED T9L1Q rc=0 (fix holds).
- verdict: PASS for THIS tip's code. FLAG-48ebfe0-hold STILL BLOCKS the
  range (15752 not restored — verified absent in this tip).
- NIT (no FAIL, persistent class): message "(2274 pins)" counts 2 csv
  comments; data rows 2272 (battery decisive).
- coverage: 149/150 PASS + 1 RED-held (48ebfe0; 992e514 RED-orphan).
