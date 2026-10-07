# DPROBE-02 bvx framing (writer black-box, oracle-generated inputs)

## Multi-block file layout (5MB zeros, lzfse, -b 4m default)
- file = outer28 + blk1 + [blk16hdr + blkN]*.
- blk1: outer unc=4194304 (==bsize), comp=2832.
- blk2 @2860: 16B hdr `00000000 000c4c2f 00000000 000002a2` =
  zeros + unc BE 806191 + zeros + comp BE 674. 16+674=690 tail EXACT.
- total unc 4194304+806191 = 5000495 (5000000B input + TLV).
- blk2 payload starts `bvx2` + le32 @4 = 806191 (== hdr unc).

## Block payload envelope (all lzfse/lz4 samples)
- starts: bvx magic (bvxn/bvx2/bv41) + le32 unc @4. ends: `bvx$` 4B trailer.
- bvxn hello: @8 le32 = 277 = chunks region incl trailer (293-16).
- magic rule: unc 2445/3237 -> bvxn; unc 5237+ -> bvx2. threshold open.

## bvxn chunk 1 (hello, verified vs hello-raw.aar bytes)
- `e0 25` + 37 raw bytes == raw[0:37] EXACT. e0 = raw-chunk flag (1 sample).
- chunk 2 @51 starts `ed 01 ...` (coded? OPEN).

## lz4 bv41 (hello)
- `bv41 8d09 0000 9001 0000 f72e AA01...`: same envelope, raw run after hdr.

## lzbitmap ZBM (hello, observed only)
- `5a42 4d09 4701 008d 0900 f800 0003 0100 1101 00 AA01...`; contains 8d09.

## lzraven (hello, observed only)
- `2b00 caec 0000 0000 0080 1100 1802 0000 1bd3 f2a0 5592 4c7e ...`
- no ASCII magic. OPEN (Q-007).

## xz (hello-lzma)
- payload[28:] = raw XZ stream, stdlib decodes to unc 2445 EXACT.
