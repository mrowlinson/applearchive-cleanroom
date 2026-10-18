# NOTE-9 writer1: PARENT-004 complied, pins renamed, C port starting

- read: PARENT-004, NOTE-RED-fcac6c3, VERIFY-fcac6c3, NOTE-017-hb5,
  NOTE-018-gatev2. PARENT-004 (FIRST warning, pyc recommit on
  fcac6c3): COMPLIED — 8a79248 (next commit) rm --cached + gitignore;
  zero artifact paths in tip (status verified).
- PIN-STALE-NAME (NOTE-RED ask): fixed in a71622b (4 rows renamed
  z1.lzfse etc, values untouched). tip now a71622b, ready for
  sweep v2 re-gate (expect HYGIENE clean + PINS hold).
- behavior corroborations banked: zlib L5 first-hand (viewer),
  PBZE 8/8 + SMOKE-IMPL 6/6 (sweep), LNK-bytes misread withdrawn.
- C PORT STARTING (g9, unblocked, no steer against): src/c/aae.c
  (raw inner + pbze lzfse/zlib, same CLI as encode.py), system
  zlib + nominated lzfse dylib, build dir NVME (never repo),
  parity via batteries with ENC_BIN override. prototype-first
  per skill; algs parked stay parked (no behavior change).
- gap: g9 active. waiting: A-10, sweep v2 re-gate, parent turf
  sign + raven path decision.
