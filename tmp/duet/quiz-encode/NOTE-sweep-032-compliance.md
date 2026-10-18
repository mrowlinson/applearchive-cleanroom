# NOTE-sweep-032-compliance: inherited-hold conversion (all cport bands)

Ruling applied: PARENT-032 remedy (b) + PARENT-033 stop-refiling.
HYGIENE/CONTAM/LIBCOMPRESSION legs scope to lane-diff paths, NOT
inherited tree files. Inherited hits = OBSERVED-inherited +
master-hygiene backlog, never lane FAIL.

Converted (verdict RED-tree/HELD -> PASS-functional + OBSERVED-inherited;
evidence in each GATE stands, parent-confirmed sufficient):
- 0f57814 band1: FLAG-0f57814-hold CLEARED (band1 MERGED 4459536).
- ee8a9b5 band2, c12fcc6 band3, eb766e3 band4, 937c347 band5,
  e64e2da band6, ee40fd9 mk, 9d7d20c band7, b6a42aa band8,
  84c84e1 band9, a99d06a band10, a0adca4 band11: same-cause holds
  SUPERSEDED (single cause, single ruling). No new holds filed.
- Each GATE file carries a SUPERSEDED-VERDICT banner; each FLAG file
  carries a CLEARED/SUPERSEDED status line. History preserved.

New convention from here: cport GATEs record inherited legs as
OBSERVED-inherited (no FLAG, no HOLD). Merges: 920e187 lane-diff
gate REQUIRED per 032.14 (queued oldest-first next-after-R24);
later merges (2dbd144+) DEFERRED pending ruling — content =
already-gated w2 tips (032.18 No-action class); will gate on order.

Self-correction: missed PARENT-032/033 for ~2h (polled tips, not
PARENT-*). From here: explicit PARENT-* poll EVERY turn.
