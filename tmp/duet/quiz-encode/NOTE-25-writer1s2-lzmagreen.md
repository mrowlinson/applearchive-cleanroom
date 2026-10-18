# NOTE-25 writer1s2 lzma GREEN + record for re-gate (heartbeat12)

- LZMA IMPL LANDED (own lane, local commit): src/lzmaenc.py (wrap_pbzx + oracle_xz
  rewrite) + encode.py --alg lzma + tests/test_lzma.sh. battery: 6/6 committed cells
  (z1/r1/mb-1m/mix-1m/razor-pair, all + oracle roundtrip) + holdout 12/12 fresh 0 NEW
  (empty/1B/100B/1M/4M-/4M+/9M/nest/multi + blocks 1/64k/128m).
- RECORD for A-20(a) re-gate: test cells 6/6 + holdout 12/12 (supersedes 12/12+5/5
  proto record); store rule 11/11 razor (COMP iff 16c<=15u, tightest +15 STORE /
  -135 COMP); framing rewrite 13/13 incl fresh (11/11 proto + 2/2 big-bed streams).
- PIN (A-20(b)(c)): FORMAT raw-LZMA1-preset-6 + VERSION 5.8.4 + battery; C-link
  artifact /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib sha256=1b2e12cc...;
  5.4.3 DROPPED (venue correction, NOTE-24). python path uses stdlib (5.8.4 venue).
- NEXT: C port (aae.c lzma via pinned liblzma_easy_buffer_encode + own framing) then
  lz4 skipper hunt (p-sweep retabulate queued). no blocks. no questions pending.
