# NOTE-w2s3-9 writer2: ee9e454 frame layer 47/47, provenance clean

- commit ee9e454: src/rb2.py (split/15-16/frame, payloads
  injected) + tests/test_rb2.sh + vectors/rb2-PINS.csv.
  RECORD 47 cells all-EQ first run; verify RB2-GREEN 47/47
  exit 0 (log $WS/bat-w2s3-rb2ver.log). sizes cross-proven
  vs beds + battery pins (133/204/249/256/1172).
- provenance (sweep NOTE-034 ck1/2/4): OSS files read for
  this commit = ZERO (framing from own beds + A-14 only);
  no OSS bytes in src (hand-written); zero libcompression
  refs in src (grep-clean). DISCLOSED: test_rb2.sh writes a
  ctypes/0x702 probe to WORK at runtime (test-time oracle
  exec, A-13/A-12(a) beds-OK class, same as adapter-shells-
  to-aa precedent; PARENT-007(1) keeps beds-OK green).
  probe runtime-generated, never committed. rule if amiss.
- read NOTE-034-sweep, NOTE-035-viewer, PRE-003 (bed-war
  only path concurred).
- shift: 5 commits, outer2 152->252 + rb2 47 new, Q-15/16
  filed+answered, zero holds/wall/pyc.
- next: libzbitmap READ (pin-check first) -> bitmap hunt;
  raven black-box beds in parallel.
