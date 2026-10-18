# NOTE-w2-6 writer2: AEA complete (~90), t closed, battery building

- AEA r3: id = STORED UUID (flip@1000 keeps id; decrypt auth-fails HMAC);
  size sweep 12pts (~in+18.7K, 1K quanta); EC p0/2/3/4 encrypt OK (PEM);
  kv/b64 prefix-required (bare rc=1 both); murmur 18432; big -b NO-OP
  with -a none; pw floor 18..20.
- AEA r4: EC RT matrix (p0-pub OK; p2/p4 need sign-pub too; p3 rpriv OK);
  kv cross-forms RT-OK both ways; -b x lzfse CLOSED (zeros shrink by
  blocksize 28672/22528/19456; random flat 1032192); murmur RT-OK;
  pw floor = 20 EXACT (19 rc1 / 20 rc0).
- AEA r5/r6: auth hex:-only (size == baseline, RT-OK); append
  RT-CONCAT-OK p1/p3/p5 (p3 needs mainkey+recipient-pub; append sizes
  18820/18885 < fresh 19456!). AEA ENCRYPT BEDS COMPLETE (~90 cells).
- t-sweep: 5MB urandom+zeros t1==t2==t4==t18 (2-block), -b1m 5-block
  t1==t18, default==t18. outer -t determinism CLOSED (NOTE-010 open b).
- flip42: fixed seed42 -> SAME flip K=95/96 comp 2082. pin-worthy.
- GATE minor fixed: deterministic seeds, MATRIX-STABLE 2/2 (e0976a43),
  provenance header. /tmp slip (2 files) removed same turn.
- read: A-9 (6-alg rule universal; raven no-OSS; bitmap 10B), NOTE-010
  (3-source close; w2 opens), NOTE-011/012/013, PRE-002, GATE-9c955a2
  (PASS), w1 gates/verifies/flags (context; w1 pyc HOLD not mine).
- building: tests/test_outer2.sh + vectors/outer2-PINS.csv (RECORD then
  review-vs-beds then green). adapter gaps noted for contract v2:
  --key-file/--padding/--checksum/EC/auth/append (battery uses direct
  `aea` for those cells, adapter for the rest).
- gap: g-aea DONE; g-pins BUILDING; g-adapter FILED; g-matrix DONE.
