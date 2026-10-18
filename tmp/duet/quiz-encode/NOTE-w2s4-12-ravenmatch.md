# NOTE-w2s4-12 writer2: raven MID-value closed, match limits

- MID-VALUE CLOSED @40: V = ((LASTB-0x40)/2)<<4 | (B6/4).
  B6 = LO<<2 exact 16/16; LASTB = 0x40+HI<<1 7/7. 8/8 bits,
  2 fields (singleton, MID-regime).
- MIN-MATCH-LEN <= 2: L=2/3/4..32 adjacent-random-repeats
  all repeat==single (copies free). 2B-period (64 reps)
  costs same as zeros (long match, not per-rep tokens).
- OFFSETS: 32B-repeat matched at D=32..64000 (all tested).
  marginal cost varies (+4 in 128B-total, +0 in 1K/64K-total;
  restructure effect, needs hex-compare). max-offset TBD.
- PAIR-TOKENS refined: (0,1,2)->48 OK, 5-EARLY/5-MID->56 OK
  (+12 = 3 pair-tokens); (0,1,2,3)->48 MISS (pred 52, got
  +4 not +8: (2,3) pairs free with prefix context?).
  count-only insufficient (again); hex shows global resync
  (bitstream) -> need bit-level token tools.
- next: bit-level diff tools + D-max + early/MID token hex
  map. Q-17/18/19 open (Q-19 trigger-ask filed). claim HELD.
