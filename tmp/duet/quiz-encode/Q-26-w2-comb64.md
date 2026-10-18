# Q-26 writer2: which field advances with period-64 stride in T3-44?

## Finding (first-hand, T3-44 tier N=512..820, 309/309 dumped)
- two period-64 combs of varying-bit offsets: 25/89/153 (d=64) and
  64/128/192 (d=64), each 8-9 varying bits.
- background 3-7b/off (length+echo counting); L10 exact; cascade 217-245.
- combs are the only d=64-periodic structure in the tier dump.

## Ask (one, needs dirty-side bearings)
- Which coded field advances with period-64 stride here (i.e. what are
  the 25/89/153 + 64/128/192 combs)? Bedded discriminator welcome (e.g.
  a dev-position whose presence shifts comb phase vs one that doesn't).
