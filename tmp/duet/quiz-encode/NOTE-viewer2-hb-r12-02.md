# NOTE-viewer2-hb-r12-02 (battery staged, wall+diff green)

- r11 tree verified: fresh git archive of
  02c66ac diff-identical to staged tree
  (diff -r rc=0). HEAD intact on lane.
- Lane diff f8ad2af..02c66ac: rgramc.c
  only +1267/-1108; py+PINS+tests
  byte-identical to writer parent; wall
  (cpat|libcompression|depload|dlopen|
  dylib) 0 hits. PINS 8572.
- Quiz: Q max 361, qmiss=0, diff 0.
- r12 battery scripted (run-r12.sh:
  PYID/CBAT/PYBAT/set-eq/own-loop/
  tables); launching on fresh r12 build.
- GATE-02c66ac: sweep r16d claimed 02:33,
  battery running; VERIFY files on PASS.
