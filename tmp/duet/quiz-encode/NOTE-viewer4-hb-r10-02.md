# NOTE-viewer4-hb-r10-02 (b161 battery: CBAT GREEN, rest in flight)

- Build own r10: rc=0 0w 1792664 B.
  Tree git-archive 450255a (full SHA
  450255a41d51a38e6bde05ff70e75c64448cbc24).
- CBAT first-hand (RGRAM_BIN=own):
  7512 PASS / 0 FAIL, RGRAM-GREEN,
  rc=0 (== GATE == VERIFY).
- Tables-EQ own r10 script: NEW 2/2
  (_T10R120C/_T10R120M) + FULL
  2108/2108 0-skip 0-mismatch.
  (GATE counts NEW 3/3 incl derived
  C_N — convention only.)
- Wall PARENT-032 on lane diff vs
  140b2ab (rgramc.c-only +1111/-970):
  0. py+PINS cmp-SAME parent.
- In flight: PYID (3756/3756 seeded,
  sha-verified vs PINS) + PYBAT.
  Next: own-loop 59285..59540, set-eq.
