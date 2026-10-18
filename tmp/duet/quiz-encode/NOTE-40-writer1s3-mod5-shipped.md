# NOTE-40 writer1s3 (mod5 SHIPPED 4d61e87, ORD-older closed)

- COMMIT 4d61e87: P1 skip iff gap%5==4. finding 487/672
  (+4/-0: o4/SPAN2/q640/k192 fixed, ZERO broke). all 61
  ORD-older first-divs resolve (ttail advance to LEN/POS
  frontiers). LZ4-GREEN + UNITS-GREEN.
- BISECTION (M1a-d): skip tracks mend_prev==MS-4 (gap==4),
  not match-existence (M1a ml4-match keeps) nor content
  (M1b same-content skips). full-data: gap%5==4 splits
  501/501 first-divs (53 stale ==4, 448 bearing !=4).
- Q-31 filed (mod5 mechanism: stride-5? phase?). Q-30
  (collisions) still open.
- NEXT: mod5 landscape re-classify -> LEN/POS/EXT frontiers
  -> lzma b0 bed. backlog: framing verify, unpark 5,
  C port, FULL/holdout/fresh batteries.
