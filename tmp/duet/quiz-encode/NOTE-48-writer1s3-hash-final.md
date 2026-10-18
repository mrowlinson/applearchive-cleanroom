# NOTE-48 writer1s3 (hash PARKED-final, Q-33 filed; back to POS/LEN)

- HASH EXHAUSTED (25 eqs): +mid-slices (mid13/14/16 tie
  488, identical sets) + fmix/murmur/splitmix (488,
  identical) + rol-scatter + avalanche (all scatter PSW-6
  but overflow 199 elsewhere). every partition ~=488
  (eviction-insensitive confirmed 6 ways).
- PSW-199 needs sparse-199-bucket; any single-bed win =
  lottery (whack-a-mole). TRUE hash needs overconstraint.
- Q-33 filed (100+ mate-sets (500 eqs, table-fit) OR 20
  same-T4 sets (bucket census)). hash parked until A-33.
- NEXT (non-hash): POS-early x13 (lookup gate: mine
  matches where oracle literals) + LEN-big x66 + EXT
  (parked) + P1 (parked). then C lz4 port scoping.
