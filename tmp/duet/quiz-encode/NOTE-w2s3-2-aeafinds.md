# NOTE-w2s3-2 writer2: tip GREEN first-hand + AEA codec finds

- tip battery first-hand: 152/152 PASS OUTER2-GREEN exit 0
  (log $WS/bat-w2s3-tip.log). ls-files tmp/ = 4 coord only. clean.
- Q-15 self-beds (WS bed-w2s3-aea/, oracle exec only):
  (a) help lists 7 (-a raw NOT listed) but `-a raw` rc=0,
  size==none (24576), RT-OK -> SILENT ALIAS for none. bogus/
  LZMA rc=1 "Invalid compression algorithm". default(no -a)
  size==lzfse (19456) per help.
  (b) hdr12 identical ALL algs (AEA1/profile/zeros); @12+
  nondet crypto -> NO plaintext seg-alg field in hdr32.
  BUT `decrypt -v` prints "compression: <alg> 1 MB" ->
  codec in encrypted/authenticated metadata, revealed
  post-decrypt. also reveals default checksum=sha256 (p1;
  closes PRE-001 OPEN), raw data size, id==`aea id`.
  (c) r5k ALL algs 24576==none -> store-fallback/pad rule
  (sizes pinnable; mechanism OPEN).
- next: -v matrix all algs (+raw/default/p5) -> cells commit.
  Q-15 stays open for viewer confirm of (b)/(c) mechanism.
