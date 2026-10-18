# NOTE-w2s4-13 writer2: A-18/19/21 read, Q-20 filed, X80/Y20 counts

- A-18 (Q-17 raven tinybeds): cross-checks MY matrix on ALL
  shared points (magic/store+16/min-64/trailer/F2-1M). Q-17
  CLOSED. (Their 64B-distinct-STORED vs my 64B-periodic-
  COMPRESSED = content rule, consistent.)
- A-21 (Q-19): P-SHA + 5-seed INSHAs MATCH mine; my tables =
  theirs EXACT (odd keys pbc!=0-appended = my (pbc,val)-ASC
  class; nkeys<=12 -> trigger HOLDS all 5). L2750-INSHA DIFF
  (mine ae35 vs theirs 138c) but tables match EXACT ->
  likely stale hash on their side; noted, tables rule.
  B RECOUNT: 13 OP-keys (be/0 CUT) CONFIRMED -> A-21-Q2's
  "B: 12 (no cut)" is stale; pin-vs-cut hypothesis FALSIFIED
  by B (CUT + PINNED); PIN-FORK (B-vs-2750 slot0) REMAINS.
- X80/Y20 REPRODUCED table-exact [00,01,80,81,ff,00/1]:
  counts 00=84,80=13,00/1=3,01=2,ff=1,81=1 (A-19 NEED (a)
  answered; even-group variant, same table).
- 1M-ZERO CLOSES under my frame model (2 frames 100+76B,
  f2=0x40..): NO model gap; add multi-frame-compressed cells
  to battery (queued followup commit).
- MANY-TIE bed (20 keys): counts unequal (4-6, cross-match)
  but table kills count-primary ([27,4,5,6,...] ASC-triple
  slots 1-3). SCR-order parked for Q-20 (mechanism ask).
- Q-20 filed (structure/order/pre-pass/qsort derived ask).
  PV-009: d755fe2 MERGED. lane continues (no rebase; parent
  merges forward). claim HELD.
