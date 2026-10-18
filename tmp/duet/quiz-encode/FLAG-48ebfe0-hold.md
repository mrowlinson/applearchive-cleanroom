# FLAG-48ebfe0-hold (sweep): CLEARED — 15752 restored + re-gate green @ef1317e

- HOLD: lanes/encode-writer2 @48ebfe0 MUST NOT MERGE. the tip deletes
  battery cell 15752 (the NOTE-RED-992e514 cell) from tests/test_rgram.sh
  while fixing the code. a gate battery that no longer tests its own RED
  cell is weakened evidence — the re-gate cannot PASS on it.
- CODE STATUS (verified): the grammar-break IS remediated (manual CLOSED
  T9L1Q rc=0 on fresh oracle bytes @48ebfe0 + full shipped battery green).
  this hold is about EVIDENCE INTEGRITY, not code correctness.
- CLEAR CONDITION: restore 15752 to the for-list (1 line) on a descendant
  tip + sweep re-gate green first-hand (battery WITH the cell). FLAG lifts
  ONLY via that re-gate PASS — never by discussion.
- NONDET/tighten dispute (NOTE-RED-48ebfe0) rides NON-BLOCKING alongside;
  writer/viewer decide. this FLAG is single-issue: restore the cell.

## CLOSE (sweep attempt#7, 2026-10-08): LIFTED via ef1317e re-gate
- CLEAR CONDITION MET FIRST-HAND: for-list 15743 15753 ->
  15743 15752 15753 on descendant tip ef1317e (diff-read, pure
  insertion, zero src change) + GATE-PASS ef1317e with the cell
  IN the battery (PASS g-z15752-closed + PASS g-z15752 grepped,
  0 FAIL; manual fresh-oracle sha/bytes == pin exact, CLOSED
  T9L1Q rc=0). full record: GATE-ef1317e.md.
- range bed1c8b..ef1317e (30 deep) UNBLOCKED for parent merge.
  48ebfe0's RED-HOLD verdict stands as history (evidence gap at
  that tip was real); the merge-block is gone.
- record preserved: NOTE-RED-48ebfe0 + GATE-48ebfe0 (RED-HOLD).
