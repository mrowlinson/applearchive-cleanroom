# NOTE-scout-hb-r7-02 (round 4/10)

- Regression GREEN filed (r7-02: T0+T1+T2-SEED7+T3-SEED8 @7b3226e).
- Census DONE (24 cells, NVME r7/census/): same pbz* framing
  all codecs; stream magics pbze/pbzx/pbz4/pbzm/pbzz/pbzb;
  payload m8: lzfse bvxn, lzma xz fd377a58, lz4 bv41 (new),
  lzraven 2b00caec, zlib 78.., lzbitmap ZBM\\t. Stream layout
  codec-independent (N=100->u344, N=2000->1024+1024+196 all).
- Next: coarse benefit sweeps per codec (tail u 1..320) to
  bracket each RAW->coded step, then fine step-1 + 4k anchors.
