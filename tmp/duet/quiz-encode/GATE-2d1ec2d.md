# GATE-2d1ec2d (encode-writer tip): PASS, 8/8 + pins 7/7 first-hand

- battery: sh tests/test_rawenc.sh $WS/gate-w1-work @2d1ec2d (WS extract,
  no checkout): PASS c1..c8 (105/221/233/956/70225/131408/616/455B),
  RAWENC-GREEN. shas MATCH vectors/rawenc-PINS.csv 7/7 pinned (c7 unpinned
  by nature: live-mtime compare-only).
- adopted files: adapter c8f52713... + smoke 56d751f9... MATCH
  lanes/harness-oracle first-hand. contam grep on full show: 0 hits.
- CTM=btime CORROBORATED 3-way (writer NOTE-4 / viewer NOTE-006 / this
  gate): touch -m, touch -d, cp -p, os.utime(ns) ALL retodate btime on
  BOTH volumes (first-hand: birth==mtime==981191106 universal). battery
  cells degenerate btime==mtime by construction; no live counterexample
  exists to btime-rule. A-6 min() withdrawn by viewer, correctly.
- carried OPEN gaps (out of battery scope, tracked by viewer, no action
  on this tip): UID/GID fixed-width truncate (A-6b: widen 1/2/4), FLG=0
  const (A-6c), LNK len() counts chars, xattr sorted()-order unverified,
  B/C/S skipped (A-6e DEV rule). none falsifies a claim IN this tip.
- verdict: PASS. no FLAG on this tip. merge-blocking hold for writer1's
  NEXT (pbze) commit filed separately (FLAG-w1-pbze-store-rule).
- repro: git -C REPO archive 2d1ec2d | tar -x -C $WS/gate-w1; sh
  $WS/gate-w1/tests/test_rawenc.sh $WS/gate-w1-work
