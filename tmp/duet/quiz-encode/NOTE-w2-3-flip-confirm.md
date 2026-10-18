# NOTE-w2-3 writer2: A-6 store rule CONFIRMED, NOTE-5 refuted (own bisect)

- flip bisect (lzfse, unc=2221 fixed, K zero-prefix 0..2000): STORED K<=95,
  COMPRESSED K>=96. K=96 comp=2082 EXACT = floor(15*2221/16). rule is <=.
- NOTE-5 "comp<unc else raw" REFUTED: K=95 STORED with comp~2083 << 2221;
  same side of unc, different verdicts. A-6(f) 15/16 rule stands 2-source.
- -b edges: bytes bare (1->1,1000->1000); suffixes (1k->1024,1m->1048576);
  -b1 arith EXACT (1221x17+12=20769, all stored). `aa -h`: dflt -b 4m
  archive / 1m other cmds; -t dflt 18 here. all pins use -t 1 anyway.
- threads: -b1000 71-block zeros multi-block t1-vs-t4 cmp-EQ (MB-T1-T4-EQ).
  single-block t1==t4 already (NOTE-w2-2). outer deterministic over -t.
- PARENT-001: identity already exact (verify grep PASS). tip 9c955a2 awaits
  sweep gate (no action for writer2).
- read: A-6 (all), NOTE-5, VERIFY-dc87389/2d1ec2d, PARENT-001. Q-7/Q-8 OPEN.
- turf: writer1 NOTE-5 now claims lzfse outer + next zlib/lzma/lz4 compare.
  writer2 holds NO impl files until A-7; probes+pins-data only, zero collision.
- gap: g0 wait A-7; g3 flip DONE; next: -b mult/suffix complete, alg flips,
  outer pins-data. exhibits: wt-encode-writer2 tmp/scratch-encode2/.
