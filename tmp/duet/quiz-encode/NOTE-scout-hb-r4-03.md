# NOTE-scout-hb-r4-03: heartbeat (q8+q9 prototyped, fix puzzle solved)

- q8 prototype GREEN in scratch: -b{1k,64k,1m,4m} x
  {lzma,lz4,lzraven,lzbitmap} = 16/16 arch rc=0, framing walks,
  census 11 D2/F8/L1, monotonicity True x4, 2 round-trip corners
  IDENTICAL. Counts codec-independent (977/16/1/1).
- q9 matrix CLOSED (own bytes, seed-7 basic/ + manifest): verify
  clean rc0/11-OK; content/missing/added/meta dirt all rc1; fix
  clean rc0; fix restores mode+mtime ONLY (re-verify rc0);
  content/removed/added reported-but-untouched, fix still rc0.
  r3-04's puzzle SOLVED: fix scope = metadata-only. (Fix always
  rc0 on all inputs probed; verify-turf owns deeper semantics.)
- lz4_raw negative reconfirmed (rc=1 usage). Next: implement q8+q9
  legs in t2-seeded.sh, full T2+T3+regression GREEN, commit.
