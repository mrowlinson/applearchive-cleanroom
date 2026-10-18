# NOTE-scout-r2-09: r2 REFILL HANDOFF (no joint DONE, seat held)

## r2 delivered (lanes/encode-container@4be6d90, LOCAL ONLY, 3 commits)
1. T1 fixture set (75726e7, 83 paths): 6 raw + slc + convert/append/
   manifest pairs + list-json golden + FIXTURES §8. Reproducibility
   law proven (CTM=MTM=mtime; recipe-regen byte-identical from
   simulated checkout 6/6). shasum ALL-ROWS-OK.
2. T1 battery (3fd9f68 + 4be6d90 T0 fix): frame-archive verb +
   t1-pinned.sh 27 cells + treecmp.py. Fresh-clone proof: T0 5/5 +
   T1 27/27 GREEN, 3 runs, no flakes.
3. Survey (NOTE-r2-04..08): HLC closed (cpio-only, extract restores
   hardlinks); h-verdict (parse-only, never emitted); pbz* DERIVED
   SPEC (12B + 16B chunks, all codecs, multichunk concat MATCH,
   zlib-wrap + lz4-tool + v1/v2 nuances); Apple-404 holds + OSS 200s;
   omanifest archive-writes; IDX/IDZ = stream (offset,length)
   chain-verified; CMP binary-accepted; -t deterministic; sparse
   mapped (dense archive, holes only with flag, content-equal).
4. Polls 1-8 (sleep-60 each): map-turf only, zero scout Qs (full Q
   grep), DONE markers unchanged. Claim HELD for r3.

## Hygiene
- Nothing pushed; master untouched; no map-lane reads (oss-survey
  docs read-only for URL recovery); TMPDIR on NVME; worktree clean.
- Heartbeats hb-r2-01..08 filed ~every 10 calls (this run: 8 notes
  + 8 heartbeats).

## r3 queue (oldest-first)
1. T2 seeded-corpus generators + runner legs (sparse/clone/-b/-t/
   HLC/cpio-convert/omanifest-IDX cells) — measurements done, code
   remains. 2. m/YAF hunt (every manifest path negative so far —
   try check-and-fix on corrupted inputs? container lane may own).
3. W/R/T + YAA1 parse-acceptance (needs foreign/hand-crafted bytes
   — decode-lane coordination at kickoff, not scout solo).
4. lzbitmap chunk-oracle path (no compression_tool coverage).
