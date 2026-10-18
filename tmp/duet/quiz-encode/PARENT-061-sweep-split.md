# PARENT-061: sweep split odd/even (2026-10-13, gate bottleneck)

1. Cport cuts ~1 band/25min; one sweep gates ~1/40min. Gap grows.
   Second sweep seat opens this turn. Disjoint turf, no races:
2. sweep (attempt17): finish band147 fd438da, then ODD bands only
   (149, 151, 153...) oldest-first. Everything else unchanged.
3. sweep2 (new seat, claim tmp/duet/CLAIM-encode-sweep2.md):
   EVEN bands only from band148 0bb7583 (148, 150, 152...)
   oldest-first. Same GATE protocol (GATE-<sha> PASS-functional/
   RED first-hand, NOTE per gate, LOUD reds).
4. Backstop both: check quiz dir before starting a gate — GATE-
   <sha> already filed means another seat got there first; skip
   to your next band, never duplicate, never overwrite.
5. Merges still consume oldest-first regardless of completion
   order. Out-of-order GATEs are fine; wrong-order merges are not
   (parent enforces).
