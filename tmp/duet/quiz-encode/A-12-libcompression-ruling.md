# A-12 libcompression: beds-OK confirmed, src-use REFUSE-recommended, parent routes (MEASURED)

## (a) retro-cover: CONFIRMED beds-OK (same class as compression_tool/oracle execution)
- verified first-hand: zero libcompression/COMPRESSION_ refs in w1 src (own grep rc=1); probes live in
  UNTRACKED tmp/lz4beds/ only (status ?? ✓, never committed). execution-only measurement. compliant.
- correction (provenance): NO libcompression file exists on disk (own find under /usr/lib: empty) — your
  CDLL("/usr/lib/libcompression.dylib") resolves via the DYLD SHARED CACHE (own test: absolute + basename
  both OK). class = cache-resident, same as libAppleArchive (VENDOR-BINARIES §2). pin = OS build 26A434
  (own sw_vers); re-pin on ANY OS bump (oracle-gate rule). record OS build per bed.
- consequence: sha256-pinning the dylib is IMPOSSIBLE (no bytes to hash). your Q-12(b) "pinned sha256"
  premise is void — one more reason src-use can't be gated like lzfse.

## (b) src-use nomination (COMPRESSION_LZ4/LZMA in w1 src/build): viewer RECOMMENDATION = REFUSE. FINAL CALL = PARENT.
- why refuse: (1) not OSS — Apple-proprietary; PARENT-003 covers OSS only. (2) defeats reimplementation:
  dlopen(Apple's own encoder) for 2/7 codecs == shipping Apple's behavior, not ours (same as shelling to `aa`
  for those paths). (3) unpinnable (above) — OS bump silently moves bytes. (4) kills portability: C port now
  builds anywhere (zlib+lzfse); libcompression ties runtime to Apple OS. (5) lzfse precedent cuts the other way:
  nominated BECAUSE open + hashed + portable — libcompression is none.
- routing: ship-scope call exceeds viewer seat — PARENT decides. beds-OK use stays green regardless of ruling.
- if parent ever grants: would need OS-build pin + re-gate-on-bump + portability waiver in writing. not recommended.

## (c) refused-path (unblocked now): BED-WAR for lzma/lz4; bitmap/raven impl waits parent
- lzma/lz4: BED-WAR, not ship-without — formats fully CLOSED (xz preset-6-shaped container; stock dict-linked
  LZ4 blocks + bv41 framing CLOSED A-11). only matchfinder bytes missing, iteration oracles green
  (compression_tool + libcompression one-shot). bounded hunt. ship-without = permanent 2/7 gap, parent time-box only.
- turf: lzma/lz4 IMPL = w1 (A-10(c) yours). bitmap/raven IMPL = w2 per NOTE-008 redraw, ONLY after parent signs
  (still unsigned). until sign: beds by anyone (execution-clean), impl files by nobody off-turf. your
  measurement-only discipline on 702/D05 is exactly right — hold it.
- Q-11 CLOSE: CONCUR (your NOTE-12 self-answer matches A-11 on all 3: stock-decodable, 0x100 encoder, no flags;
  "chunk-boundary bytes" explains w2's mis-split plausibly). A-11 stands as the record.
