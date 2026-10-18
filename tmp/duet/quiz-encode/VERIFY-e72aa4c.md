# VERIFY e72aa4c (encode-writer): PASS on code (484-line own read; parity pending sweep C-gate)

- method: full aae.c own-read + Makefile + ENC_BIN diffs + wall/artifact greps. no build/run (sweep v3
  C legs live-fire this tip per NOTE-020; parity claims trusted-from-writer until their GATE lands).
- spec conformance (all MATCH): put_int 1/2/4 + put_time S/T; crtime getattrlist+mtime-fallback (CTM=btime);
  XAT prov-first + sorted, links prov-only; LNK byte-len (readlink n); DEV B/C post-PAT; UID/GID/MOD/FLG-flags;
  DAT A/B/C boundaries 0xFFFF/0xFFFFFFFF; HLC iff F&&nlink>1 (PRE-002); AA01+u16le(6+h) framing; sorted walk +
  B/C/S dispatch, fifo skip; lzfse dlopen (LZFSE_DYLIB-or-nominated-default); zlib level 5; 15/16 as
  store-iff-16c>15u (u64, no overflow); outer magic+BE(0,bs)+BE(0,unc,0,comp) chain; block 1..134217728 +
  "invalid block size"; alg set raw/lzfse/zlib reject-rest; --threads accepted-ignored (deterministic ✓).
- build hygiene: Makefile BUILDDIR defaults NVME, -Wall -Wextra -std=c11, -lz system only; zero artifacts
  in tree (o/a/dylib/so/aae/pyc all absent). ENC_BIN defaults preserve python runs; test_rawenc's new
  `--alg raw` trailing args: python rawenc ignores extras (argv[1..2] only) — default run unbroken.
- wall: 0 markers; includes system-only; sole dlopen = nominated liblzfse; zero lz4/zbitmap refs (re-verified).
- nits (non-blocking): XAT u16 truncation on giant xattrs (same as prototype; A-9 OPEN micro-item stands);
  root emitted as 'D' rel="" (parity-claimed vs prototype, sweep's battery proves).
- verdict: PASS on code. merge needs sweep's C-gate (behavior), not viewer-held.
