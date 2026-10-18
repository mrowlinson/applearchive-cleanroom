# NOTE-scout-r4-06: r4 REFILL HANDOFF (no joint DONE, seat held)

## r4 delivered (lanes/encode-container@a13215e, LOCAL ONLY, 1 commit)
1. T2 q8+q9 legs (a13215e, 3 files): q8 -b sweep x
   {lzma,lz4,lzraven,lzbitmap} (16 arch + framing/census/
   monotonicity + lz4_raw negative + 2 corners) + q9
   verify/check-and-fix rc + residue contract (8 cells). 28 ->
   56 cells. T2-SEED7 GREEN, T3-SEED8 GREEN (x2), T0+T1
   regression GREEN, all first-hand. G4 FULLY closed.
2. Codec->pbz* map payload-confirmed (r4-04): lzma->pbzx,
   lz4->pbz4, lzraven->pbzm, lzbitmap->pbzb (mnemonic NOT
   codec-initial). Raw-store rule generalizes to all codecs;
   chunk geometry codec-independent (977/16/1/1).
3. check-and-fix verdict (r4-04, closes r3-04 puzzle): fix scope
   = metadata-only; fix rc = healed-check (0 clean/healed,
   1 residue); data dirt reported-but-untouched. Pipe-rc
   artifact documented + corrected.
4. Kickoff session plan (r4-03): extract column census-closed
   (DPROBE-04 256/256, m/W/R/T in silent-248); residual = 18
   cells (list/verify x 7 TYPS + 4 extract re-confirms) + YAA1-
   magic question — decode lane owns method.
5. OSS-libzbitmap wall brief (r4-02): asks COMPARE-ONLY tier
   (A-10 precedent), fallback = archive-granularity legs only.
6. Polls 1-10 (sleep-60 each): inbox frozen, zero scout Qs
   (full Q grep each poll), DONE unchanged (w2s9 + writer1s3).
   Claim HELD for r5.

## Hygiene
- Nothing pushed; master untouched; no map-lane reads; TMPDIR on
  NVME (r4/); worktree clean @a13215e. Heartbeats hb-r4-01..06
  filed ~every 10 calls (this run: 6 notes + 6 heartbeats +
  this handoff).

## r5 queue (oldest-first)
1. Wall-ruling response (r4-02): if GRANTED, add per-chunk ZBM
   payload asserts to q8 lzbitmap cells (compare-only, hash-pin
   the dylib); if DENIED, mark DEFERRED-to-decode in FIXTURES.
2. Kickoff session: run r4-03's 18-cell matrix with decode lane
   (their craft harness); file verdicts.
3. v1/v2 selector trivia (r2-06: threshold in (2445,4096]) —
   narrow only if decode lane needs it.
4. CMP re-test if a decmpfs donor appears (parked, NOTE-r3-07).
