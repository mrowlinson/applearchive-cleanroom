# A-25 ff-slot: DP-TIE-LOTTERY model (parse-identity, not statistics) + 4 predictions (Q-22)

## reproduction + fragile-point discovery (own beds)
- tag30/tag80 reproduced EXACT from Q-22 recipe (ff@0 / ff@2; B80 size 19653).
- 49 single-byte flips on tag80: 48 = table IDENTICAL (size ±1B); ONE (pos18500) = SAME-SET
  GLOBAL REORDER ([f8,03/2,ff,...] -> [c0,ff,e0,fe,...]: c0 9->0! f8 0->7! ff 2->1!), size +1B.
- fragile window NARROW (<50B: 18475/18525 quiet). Robust landscape + razor tie-points.

## mechanism: table records WHICH OPTIMAL PARSE won (tie-lottery)
- size-neutral reorders (parse changes, size ±1B) + ff count-stable (2103/2109 per w2) yet slot
  flips (0/2) + narrow fragile points = DP TIES: 1 byte flips a tie-break -> different optimal
  parse (same size!) -> different op multiset -> different table. No static quantity decides the
  slot (counts/runs/positions all killed: same-yet-flip).
- Q-22#1: ff's slot = TIE OUTCOME. Bedded knob = flips at fragile points (pos18500-class).
  Counts/runs/first-seen do NOT decide (all same-yet-flip across tag30/80).
- Q-22#2: head = TIE-VOLATILE keys (large-count ⟺ ops span tie regions — correlation, not rule!);
  tail = TIE-IMMUNE keys (small-count ops never in ties -> count-exact). Membership = tie-EXPOSURE.
  TEST (either seat): find a flip moving a TAIL key with counts fixed -> confirms exposure model.

## 4 falsifiable predictions (w2's parser decides — P2 is the crux)
- P1: base80 vs flip@18500 have DIFFERENT op sequences (same size ±1B, same key set).
- P2: ff's op-count SAME (±10) in both (slot moves WITHOUT count move — kills residual count-drive).
- P3: parses DIVERGE at/after pos18500 (tie region; traceback diff localizes there).
- P4: tag30 vs tag80 = different parses (not just different counts).
- If P2 FAILS (ff counts differ >>10) -> back to count-driven (joint-fit revived). If P1 FAILS
  (same ops, different table!) -> pure write-path dynamics (insertion/hash) independent of parse.
