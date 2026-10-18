# VERIFY-0d64e0a T10P18 23001..23092: PASS

## first-hand (at-commit tree ver-0d64e0a, fresh oracle bytes)
- repo gate: `sh tests/test_rgram.sh` at-commit => RGRAM-GREEN
  (tail: PASS g-z23092-closed, PASS g-z23092).
- FULL battery 23001..23092 (92/92, own loop, fresh
  compression_tool bytes): pass=92 fail=0.
- independent oracle sha vs vectors/rgram-PINS.csv: 11 pin
  rows in range, 11/11 MATCH, 0 SHADIFF.
- boundary: 23000 CLOSED T10R16 off=255 (prev tier intact);
  23093 "N out of scope" rc=2.
- verdict labels: PI0 23001 / PI1 23002 / PIA 23003..23018 /
  PIB 23019..23028 / PIQ 23029..23092 (spot 23040 off=11,
  23077 off=48, 23092 off=63) — all correct tokens.
- consts non-vacuous (balanced-parse module tables):
  PI0C 71, PI1C 71, PIAC 69, PIBC 62, PIQC 54 — all
  0 oracle violations.
- NOTE: first battery attempt all-OPEN was MY invocation
  error (rgram.py needs FILE.rav N args); re-ran correctly.
  No w2 defect.

## verdict: PASS (T10P18 23001..23092 CLOSED 92/92)
