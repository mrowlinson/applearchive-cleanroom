# NOTE-scout-r3-08: r3 REFILL HANDOFF (no joint DONE, seat held)

## r3 delivered (lanes/encode-container@9afdb12, LOCAL ONLY, 2 commits)
1. T2 generator+runner (b006ad4, 6 files): t2-gen.py (seeded,
   same-seed diff -r identical) + t2-seeded.sh (28 cells q0..q7:
   quota exit-3, -b sweep 12-arch + chunk-walk + corners, -t
   pairs incl lzbitmap, sparse dense/explode/holes, clone
   no-SLC, HLC+inode+ignore, omanifest-IDX chain, seed guard)
   + adapter --block/--omanifest + frame-cpio-convert + T2=1
   wiring + README + FIXTURES §9. T2-SEED7 GREEN, T3-SEED8
   GREEN, T0+T1 regression GREEN (9afdb12 adds q2-lzbitmap).
2. m/YAF emit-negative (NOTE-r3-04): no local path emits TYP m
   or YAF (archive±flags, convert, manifest, omanifest, cpio,
   verify, check-and-fix, patch); -include-type m -> 0 entries.
   Parse-acceptance OPEN (foreign bytes, kickoff coordination).
   Bycatch: yec/duz/cks/sh1 forceable (shapes measured), btm
   silent; check-and-fix puzzle filed (verify turf).
3. W/R/T+YAA1 spelling verdicts (NOTE-r3-05): type vocab =
   exactly {bcdfhlmps} case-insensitive (W/R/T rejected);
   field rule = exactly-3-alnum, membership unchecked (YAA1
   fails format; YAA form emits nothing — not aa-vocabulary).
   Foreign-bytes parse half = kickoff work.
4. lzbitmap path (NOTE-r3-06): same pbz* framing; ZBM-or-raw
   per chunk (c==u + magic agree); whole-archive convert
   oracle PROVEN (977-chunk + single-chunk treecmp clean);
   slice oracle REFUTED (stream-layer validation); OSS-decoder
   decision filed for wall ruling.
5. Gap-fills: APFS sparse threshold (16,20]MB (NOTE-r3-02);
   CMP all-codec negative + AFSC parked (NOTE-r3-07);
   append-time -omanifest WRITES, same IDX shape (hb-07).
6. Polls 1-10 (sleep-60 each): map-turf only, zero scout Qs
   (full Q grep each poll), DONE unchanged (sweep-r5 seat DONE
   only). Claim HELD for r4.

## Hygiene
- Nothing pushed; master untouched; no map-lane reads; TMPDIR on
  NVME (r3/); worktree clean @9afdb12. Heartbeats hb-r3-01..10
  filed ~every 10 calls (this run: 8 notes + 10 heartbeats +
  this handoff).

## r4 queue (oldest-first)
1. Container-kickoff coordination prep: foreign-bytes
   parse-acceptance session (TYP m/W/R/T/h stream bytes) with
   decode lane; OSS-libzbitmap wall-ruling brief.
2. T2 extensions if lane wants them: -b sweep x lzma/lz4/
   lzraven/lzbitmap (q1 covers raw/lzfse/zlib); verify/
   check-and-fix battery legs (rc semantics measured r3).
3. v1/v2 selector trivia (r2-06: threshold in (2445,4096]) —
   narrow only if decode lane needs it.
4. CMP re-test if a decmpfs donor appears (parked, NOTE-r3-07).
