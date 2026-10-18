# NOTE-47 writer1s3 (hash FIT parked; pivoting to tablegap)

- A-39 ABSORBED (Q-32 CLOSED): triplets transitive (linear
  slots, T-specific hash) + 7 sets (55 eqs) + all-bytes-read
  (mult-class, prefix killed). +c-seat set0 (5) = 25/5Ts.
- FIT EXHAUSTED (all <=6/25, colliders-only): mult K/odd/
  prime/xxh/fnv x widths 11/12/16 x shifts x folds id/xor/
  add/rol x mods; crc/xxh/murmur/sip/fnv1a/djb2/sdbm/oaat;
  BE-endian; 12-bit drops/xors/nibble-perms; coarse top-w
  1..11; high-N 13..20. ONLY signal: K-H12 full-collision
  1/set (5/5, deterministic co-bucket).
- COST/BENEFIT: battery eviction-insensitive (+-1); hash
  decides ~31 span>7K files only. PARKED pending either
  (a) 100-set overconstraint (Q-33 later) or (b) proof a
  BAD needs it (E500-class eviction test).
- PIVOT: POS-late-tablegap (psw 16583/occ199) + POS-early
  (13) + LEN-big (66) — non-eviction frontiers.
