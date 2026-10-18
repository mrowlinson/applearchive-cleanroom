# NOTE-sweep-243 — relaunch hb, tip gated, polling b132+

- State: b102-b131 gated (b131 5db2d64 PASS-functional).
  cport tip 5db2d64 (03:58) = gated; nothing newer.
  wt-encode-cport dirty (rgram.py/test/pins) = b132 prep
  in flight.
- Pending writer tiers: 11 (T10P108..T10P113,
  54321..56152). Expect b132 = T10P108 first.
- Next: poll lanes/encode-cport; gate oldest-first per
  seat protocol (gate-tip + ownbuild/pyid/cbatt/ownloop/
  tables/wall).
