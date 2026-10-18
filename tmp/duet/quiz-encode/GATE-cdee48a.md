# GATE-cdee48a (encode-writer2 tip): PASS, rgram T4G/H/I 280/280 (+1 flake)

- scope: cb301db (T4G) + c45da60 (T4H) + cdee48a (T4I).
  covers both within (same poll gap). +21 cells +42 pins.
  src purely additive (+114/-0). no tmp/, no pyc.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, RB2 47/47, RAVFRAME 181/181, RGRAM 280/280,
  PINS-RGRAM set-eq 280/280. OUTER2: 283/284 first run
  (a-nd-p3 char 15 vs pin 14) — FLAKE, see below.
- FLAKE (pre-existing, NOT this tip): a-nd-p3 nondet-char
  pin flipped 14->15->14 across two runs minutes apart on
  the IDENTICAL extract; tip chain doesn't touch outer2
  files; re-run exit 0 OUTER2-GREEN (all nd PASS). = the
  AEA p3 first-diff char varies run-to-run; pin char-14 is
  over-specific. remedy for writer (non-blocking): p0-
  treatment (verdict-only DIFF or char-set pin) for p3.
  filed NOTE-FLAKE-a-nd-p3.
- code read first-hand: 3 branches (T4G bands+tabs, T4H
  counters+carry, T4I H-regime cont) mirror NOTE-w2s7-20/
  21/22; literals OPEN-declared. old 238 cells CLOSED.
- verdict: PASS all three commits. no FLAG. w2 line clear.
- repro: gate-tip.sh cdee48a $WS/gate-w2-cdee48a-s2 (+ nd
  re-run work/outer2-rerun for flake proof).
