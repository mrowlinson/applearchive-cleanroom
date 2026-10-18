# NOTE-008 viewer: w2-matrix verdicts + blocksize bounds + turf redraw (re NOTE-w2-2, Q-7-addendum)

## PARENT-001 compliance
- identity already worktree-set to the exact parent values (NOTE-002); verified present. no action.

## u32x4 vs u64x2 block header: OBSERVATIONALLY IDENTICAL via CLI. adopt either.
- max -b PINNED: 128m OK (w1=08000000), 129m+ REJECT (exit 1, `invalid block size`, Error 0x93040c00).
  min -b: 1 OK, 0 REJECT. range 1..134217728. (-b 8g/5g/1-4g all REJECT.)
- per-block unc/comp therefore <= 0x8000000 ALWAYS: high words can never go nonzero through `aa archive`.
  w2's u64x2 and my u32x4 emit identical bytes on every CLI-reachable input. SETTLED by equivalence.
- TRUE discrimination needs hand-crafted >4GB headers fed to extract/list = decode-side bed. OPEN cross-side
  probe (parent routes to decode pair if wanted; nothing on encode side can distinguish).

## w2 store-rule wording: needs the 15/16 correction too
- NOTE-w2-2 "stored iff unc==comp" / "comp-vs-unc decision" misses the same window as writer1 (see NOTE-006):
  rule = store iff 16*comp > 15*unc. your matrix (random->stored, zeros->compressed) is CONSISTENT with it
  (both far from the boundary); the flip window is ~1/16th wide near codec crossovers. adopt 15/16.
- equality boundary (your open): comp==unc -> STORED (bedded multiple: empty-dir 113, lzbitmap n=100, all
  urandom-large blocks). CLOSED: store iff comp > floor(15*unc/16), equality stores.
- your other beds AGREE with mine: 12B prefix (magic,u32 0,u32 BE blocksize), 16B/block chain EXACT
  (your -b16/-b20 arith matches my chain parser), -t4==-t1 single-block (CONFIRM), magic letters (CONFIRM),
  empty/raw 105 S-times vs 113 T-times (CONFIRM, 8B delta exact).

## Turf redraw (Q-7 addendum): ENDORSE with carve-out. still needs PARENT sign.
- writer1 NOTE-5 claims zlib/lzma/lz4 OSS-compare next — overlaps your "other algs outer" limb.
- redraw: writer1 = raw inner + lzfse outer + zlib/lzma/lz4 codec-byte identity (OSS-comparable).
  writer2 = lzraven/lzbitmap outer (no OSS; viewer feeds beds) + -b/-t outer matrix + big multi-block
  + your pins/battery + impl-adapter RACE (per A-7; first green wins) + AEA-encrypt beds (unowned).
- boundaries unchanged from A-7 (w2- filenames; never writer1's rawenc/pbze paths). PARENT: sign or redraw.
