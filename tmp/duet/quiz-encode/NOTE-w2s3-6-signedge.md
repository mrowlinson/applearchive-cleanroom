# NOTE-w2s3-6 writer2: sign/edge finds, 33 cells queued

- beds (WS bed-w2s3-aea/): nondet first-diff p0=c14 p2=c13
  p3=c14 p4=c13 (p1=c13 known); AEA -b 0/bogus/129m + -t 0
  ALL rc=0 silent + RT-OK (LENIENT vs AAR strict NOTE-008);
  -v block echo floors sub-MB ("0 MB" for 16b/64k, exact
  1/128 MB); sign matrix p1 rc1/msg/SAME, p0 rc0/silent/
  MOD/RT-OK, p2/p4 need priv+sigkey pair; deferred flow
  (pub-only enc -> dec rc1 "Failed to unlock container"
  -> sign rc0 MOD -> RT-OK) CLOSED.
- next: commit ND()+EDGE()+VB()+SIGN() ~33 cells (->252).
- open: Q-13/14/15, gates 592722d/c418002/c81821f, parent.
