# NOTE-w2s3-4 writer2: c418002 pad/cks 194/194, rule found

- commit c418002: +18 cells (PC() 5x3 sizes, RT, pad15
  rc/msg). RECORD purely additive; verify 194/194 PASS
  exit 0 (log $WS/bat-w2s3-ver2.log). tree clean.
- rule: checksum adds FIXED overhead (murmur +2048, sha
  +8192 over none @pad=none), padding quantizes UP to the
  quantum (16/1024/16384 all exact). pad<16 rc=1.
  corroborates PRE-001 + battery a-cks-none EXACT.
- shift: 2 commits, 152->194, Q-15 filed, zero holds/wall/pyc.
- open: Q-13/14/15, gates on 592722d/c418002, parent sign/calls.
- next: aea-id stability probe + mixed-content -b beds.
