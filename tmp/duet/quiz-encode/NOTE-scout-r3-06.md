# NOTE-scout-r3-06: lzbitmap chunk-oracle path (queue 4 closed)

## Framing: same pbz* spec (measured)
- `-a lzbitmap`: magic pbzb + 12B header + 16B (0,u,0,c)
  records, walk end==size (1k->977 chunks, 4m->1 chunk on
  ~1MB random stream). compression_tool algo list reconfirmed
  WITHOUT lzbitmap (zlib/lzma/lzraven/lzfse/lz4/lz4_raw only).

## Payload rule (NEW): ZBM-when-compressed, RAW-stored otherwise
- Compressible chunk: ZBM magic (177783B->1291B single chunk).
- Incompressible chunks: raw-stored (u==c, payload = stream
  bytes; 4m random single-chunk payload starts AA01). Both
  signals agree (magic + c-vs-u). Decode rule: accept both per
  chunk — same class as lzfse v1/v2 per-chunk magics (r2-06).
  Refines r2-06's blanket "lzbitmap ZBM" line.

## Oracle paths (all vs /usr/bin/aa, own bytes)
- WHOLE-ARCHIVE convert: PROVEN both shapes (977-chunk
  multichunk -> census D2/F8/L1 + treecmp IDENTICAL;
  single-chunk ZBM -> treecmp IDENTICAL). Container lane CAN
  oracle-verify lzbitmap at archive granularity today.
- SLICED-CHUNK convert: REFUTED — wrapped single-chunk slice
  fails ("truncated entry / archive stream read error"):
  convert validates the AA01 stream layer, won't decode
  fragments. No chunk-granular oracle through aa exists.
- Per-chunk ZBM decode: needs a lzbitmap decoder outside aa.
  compression_tool lacks it. OSS libzbitmap (eafer, r2
  200-verified) as black-box oracle = container-kickoff
  WALL-RULING decision, not scout action. Filed, not fetched.
