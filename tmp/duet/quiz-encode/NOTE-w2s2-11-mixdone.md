# NOTE-w2s2-11 writer2: 8327f34 mix cells 133/133, per-block decision proven

- commit 8327f34: MIX() + 3 cells (S/C pattern + sha), 127->133,
  verify 133/133 PASS exit 0 (log $WS/ver6.log). pattern CCCCCSSSSSS
  identical raven/bitmap/lzfse: zeros-half COMPRESS (80/94/153B),
  random-half STORE (10000/10000), tail [223/223S]. 15/16 applies
  PER-BLOCK (stream mixes freely) — impl architecture consequence.
- shift totals: 7 commits, battery 71->133, ~900 oracle cells. open:
  Q-13/Q-14, gates on fb9d88b/0661787/8327f34, parent calls. claim HELD.
- next: poll; remaining gaps are parent-held (impl sign) or
  viewer-held (Q answers). green-keeping as needed.
