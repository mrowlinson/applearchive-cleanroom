# NOTE-w2-2 writer2: outer matrix 82/82, framing derived

- commit 9c955a2: adapter+smoke adopted (hashes MATCH, GREP-CLEAN, SMOKE-GREEN).
- matrix: 7 algs x 11 inputs + 2 rep + 3 b/t = 82 cells, all exit 0.
  fixed-mtime inputs (nsec=0); empty/raw=105B (A-4 113 - 8 S-time delta EXACT).
- OUTER MAGIC per alg: raw=AA01 none, lzfse=pbze, lzma=pbzx, lz4=pbz4,
  zlib=pbzz, lzraven=pbzm, lzbitmap=pbzb ("pbz"+letter).
- file hdr 12B: magic + u32BE 0 + u32BE BLOCKSIZE (default 0x400000=4MB).
  -b N sets blocksize N BYTES (16->16, 20->20, exact).
- block: u64BE unc + u64BE comp + comp-bytes. stored iff unc==comp
  (inner slice verbatim; R1000/EMPTY inner cmp-EQ raw @skip28).
  compressed payload = codec stream bytes (lzfse "bvx?..." lead, "bvx$" tail).
- stored rule (all 6 algs): random inputs stored (size=raw+28 exact);
  zeros compressed. small-in lz4/lzbitmap store where lzfse compresses
  (z0-lz4 249=221+28) -> per-block comp-vs-unc decision, same rule all algs.
- micro-block proof: -b16 z200k: 12+12513*32+31=400459 EXACT;
  -b20: 12+10011*36+19=360427 EXACT. inner contiguous across blocks (own cmp).
- determinism: 2/2 reps sha-MATCH. -t4 == -t1 bytes (single-block, sha-MATCH).
- read NOTE-4 (writer1 RAWENC-GREEN 8/8, g6=pbze stored+boundary+multiblock).
  OVERLAP with Q-7 proposal flagged in Q-7 addendum; alt split offered.
  writer2 steers: all-alg magics, -b/-t effects, big-multiblock, codec bytes.
- open: equality-boundary (comp==unc -> stored?), default-bs multiblock
  (>4MB inner), -t on multiblock, per-alg codec-bytes identity, -b edges.
- gap: g0 wait A-7; g1/g2 DONE; g3 open->boundary+MB probes; g4 pins next.
