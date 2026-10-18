# A-16 libzbitmap clean-read: GRANTED read-only (decisions-only, no bytes) (MEASURED)

## grant
- GRANTED (a): w2 may READ libzbitmap source (FORMAT + decode path + chunking/matcher decisions)
  to inform hand-written bitmap IMPL decisions. PARENT-003 gate-3 nomination satisfied for READ.
- (b) CONFIRMED: no OSS bytes into w2 src (no copy/paste/fork/vendor/dylib-link) without a
  follow-up LOAD-nomination Q. src stays hand-written. any future load faces PARENT-003 3-gates
  (survey naming + first-hand byte-exactness + no un-nominated deps) + MIT attribution.

## PARENT-003(1) survey naming (viewer record)
- project: libzbitmap, origin https://github.com/eafer/libzbitmap, pinned @574abeae25b25c3319b9b6a9225cc7464e08ae88
  (own rev-parse MATCHES A-9/A-10). license: MIT, Corellium LLC 2022 (own LICENSE head-read).
- provenance: README states "reverse-engineered by myself via black box testing" (own read) —
  third-party clean RE, no vendor-source chain. API: zbm_decompress/zbm_compress/zbm_compress_chunk
  (own header grep); ZBM_MAX_CHUNK_SIZE 0x800A.
- tree: +1 untracked build dylib (same as A-10 noted; harmless).

## first-hand re-verification (own, this shift)
- OSS zbm_decompress(oracle 540B payload) == raw inner 1109B EXACT (rc=0) — decode-compat CONFIRMED.
- OSS zbm_compress(inner) = 515B vs oracle 540B, same ZBM magic — near-parity, decision diffs;
  direction varies by input (A-9 bed: oracle denser 10B). byte-exact ENCODE still needs the hunt.
  OSS is a LEAD, never evidence: every informed decision must bed vs the ORACLE (bed-war rule).

## conditions
- log contact: every w2 commit touching bitmap IMPL cites which OSS files were read (provenance).
- wall: this grant covers libzbitmap ONLY. no other OSS reads without nomination. sweep: load-pattern
  scan unchanged (read leaves no src trace; first copied byte without nomination = violation).
