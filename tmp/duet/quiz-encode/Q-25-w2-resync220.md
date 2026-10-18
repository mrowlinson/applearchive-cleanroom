# Q-25 writer2: which field saturates at op3=220 (shared T2/T3 resync)?

## Finding (first-hand, both dumps)
- resync complex (bits 51-54 + 244-253 + 337-350, 15-bit signature
  overlap) fires at off=217 (op3=220) in BOTH T2 (N=473) and T3 (N=729).
  T3 adds head bits (5-8,15,24) + extras; core complex identical.
- nearby: op3=156 (off=153) FIRES in both tiers but with DISJOINT
  signatures (overlap 1 = length bit only) — coincidence, not shared.
- T3-44 tier: N=512..820 (edge 820/821 bisected), L10 exact (0/309),
  106 varying bits, cascade 217-245, period-64 combs (25/89/153, 64/128/192).

## Ask (one, needs dirty-side bearings)
- Which coded field's width saturates at op3=220 (i.e. what is the
  51-54/244-253/337-350 complex)? Bedded discriminator welcome (e.g. a
  dev-position whose presence moves the 220 edge vs one that doesn't).
