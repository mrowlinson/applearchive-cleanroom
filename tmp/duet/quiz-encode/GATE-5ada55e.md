# GATE-5ada55e (encode-writer2 tip): PASS, outer2 big-matrix 284/284

- scope: TCMP() t1-vs-t18 (8 cells) + BECHO() block echo (4)
  + BIG() chain+sha (4); pins +32 rows. purely additive.
  no tmp/, no pyc, no impl.
- legs (pristine, ce9006b): HYGIENE/CONTAM(P009)/OSS clean,
  SMOKE 6/6, OUTER2 284/284, RB2 47/47, RAVFRAME 181/181,
  RGRAM 104/104, PINS set-eq all five.
- code read first-hand: TCMP cmp-EQ + sha (threads don't
  change bytes); BECHO asserts zero-fields + walks chain
  (bs:nb echo); BIG chain-close + unc-sum + sha. honest.
  internal consistency: tt shas == bg shas same inputs;
  bb-4k 1221 blocks = 5MB/4K ✓.
- minor (non-blocking): comments cite NOTE-w2s7-8 beds but
  no such file in quiz — provenance wart; pins verified
  first-hand regardless.
- verdict: PASS. no FLAG. w2 line clear.
- repro: gate-tip.sh 5ada55e $WS/gate-w2-5ada55e-s2
