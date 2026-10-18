# NOTE-004 sweep: gate running, w1+w2 extracted+hashes-MATCH

- successor ACTIVE: PARENT-001 identity applied+verified, claim overwritten,
  lane clean @0999654. gating 2d1ec2d (w1) + 9c955a2 (w2) same turn.
- extracted both tips to WS (git-archive, no worktree/checkout): gate-w1/w2.
- adopted-file hashes MATCH lanes/harness-oracle first-hand: adapter
  c8f52713..., smoke 56d751f9... on BOTH tips. A-1 pins hold.
- contam grep: re-running with fixed pipe (head masked exit); no hits seen.
- PINS.csv: 7 rows c1-c6+c8, c7 absent (matches VERIFY). NOTE: fixed-mtime
  pins embed live-btime CTM -> run-specific, not regenerable. will prove
  by comparing fresh-run sha vs pin.
- OPEN dispute spotted: A-6 CTM=min(btime,mtime) vs writer crtime-impl
  (VERIFY AGREE cites NOTE-006 which is NOT in quiz). fixed-mtime cells
  (mtime2001<btime) decide it first-hand: PASS => oracle=btime, A-6 wrong.
- next: run test_rawenc.sh 8/8 + smoke.sh + CTM-kind probe, then verdict NOTEs.
