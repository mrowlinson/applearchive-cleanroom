# NOTE-20-writer1s2-storerule (heartbeat9)

## store-rule CLOSED (single-stream): store iff 16c > 15u
- 60+ beds: flip s84(c/u .9305,C)/s85(S); bracket g85010(c93976,C)/g85020(S); exact-scan w84991..99
  NON-MONOTONIC near boundary (w84996 S, w84997 c93972 C) -> decision on exact c, content-specific.
- c-quantum 4B (XZ pad); strictness >/>= unobservable at quantum (93975 unhittable); adopt 16c>15u.
- Models c>u-u//16 vs 16c>15u differ only at c=floor(15u/16)+1 (rare; revisit if battery hits).
- zr/rz order-independent (same c 50976) -> whole-stream decision.

## per-stream independence CONFIRMED (5MB mixed beds, 4 streams each)
- z4r1/r1z4/r4z1/z1r4: zeros-streams compress, random-streams store (c==u, raw slice, gap [u,u]).
- (beds used 4.0MB regions vs 4MiB streams; arithmetic reconciled, no format surprise.)

## lzma framing COMPLETE (packet encoder still open)
- F1 streams 4MB + gap[u64,u64]; F2 per-stream XZ-or-store; F3 chunks <=2MB @packet-end;
  F4 dict 0x16 lc/lp/pb 3/0/2 check NONE; b0 fields11->+4 (2 samples).
- Next: liblzma preset-compare (raw-output inners -> xz -6 --check=none vs oracle) + viewer debts (X=0/HOLE1 bytes).
