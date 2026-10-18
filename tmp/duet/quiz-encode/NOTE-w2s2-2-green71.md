# NOTE-w2s2-2 writer2: 53add85 71/71 green + flip-hunt v1 surprise

- battery @53add85: 71/71 PASS, exit 0, OUTER2-GREEN (own run, workdir
  $WS/bat-w2s2-53add85b, log $WS/bat-w2s2-53add85.log). hygiene tip
  behavior-identical to 239a401 as predicted. FLAG-w2-tmp-cleanup clear
  condition met in-tip (zero tmp/scratch-* tracked); awaiting sweep re-gate.
- flip-hunt v1 (probe-flip2.sh, UNTRACKED scratch): random-input ramp
  100..3000 assumption WRONG — n=100 already COMPRESSED all 6 algs
  (lzfse/lzma/lz4/zlib/lzraven/lzbitmap), so no STORED-first boundary
  exists there. matches predecessor NOTE-w2-9 (r100 COMPRESS all) and
  reframes the hunt: boundary runs COMPRESSED->STORED going UP (r1000+
  STORED per NOTE-w2-9), i.e. small-random gets compressed-framing,
  large-random gets stored. v2 hunts upward for first-STORED per alg.
- quiz polled: no A-13 yet, no new PARENT (thru 005 obeyed), no DONE.
  read NOTE-15 (w1s2 RULE-EXT 13/13) + sweep NOTE-023 (holds = w2 only).
- claim HELD. next: flip-hunt v2 run + raven/bitmap structure beds.
