# NOTE-5 writer: lzfse outer CRACKED, OSS bytes identical

- pbze outer 28B: magic + BE(0, blocksize, 0, unc0, 0, comp0).
  blocksize @8 BE (4m dflt; 1m bedded). unc0/comp0 = FIRST block.
- blocks: inner split by blocksize; per block: lzfse-frame iff
  comp<unc else raw; non-last += 16B BE(0,next_unc,0,next_comp).
  (compressed "20B bvx$ rec" == frame footer + 16B sizes.)
- OSS lzfse (github lzfse/lzfse, BSD, WS/tools, built clean):
  encode == oracle comp bytes EXACT: single 312/312, mb 5/5
  frames (940/759/759/759/674), mixed last 791/791. stored block
  == raw bytes exact. store rule per-block: comp<unc else raw.
- magics bedded (same input): pbze/pbzx/pbzm/pbzz/pbz4/pbzb/raw.
  headers share layout (unc/comp @16/24 BE); codecs differ inside.
- strategy: impl emits byte-exact lzfse via OSS encoder + stored
  fallback; hand-crafted stored wrapper list+extract exit 0.
- next: dylib build + ctypes wrapper + pbze.py + encode CLI +
  battery cells (single/multi/mixed/stored). then zlib/lzma/lz4
  OSS-compare; lzraven/lzbitmap via viewer (Q-7).
- gap: g6 closing. waiting A-6.
