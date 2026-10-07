# Spec clause drafts — ENCODE side (viewer, dirty/spec)

Status: DRAFT on lanes/encode-viewer. Numbers CR-101..199 reserved encode-side here;
parent renumbers at merge into spec/CLAUSES.md. Shape: CR-nnn + ONE tag + stage +
artifact + numbers + verdict vs prior hypotheses. Derived-only (beds+numbers+verdicts).

```
CR-101 [MEASURED] AAR entry = AA01 + u16le total header size + TLV fields + own A-payloads
stage: bitstream
artifact: WS tmp/aar-parse.py (dirty-side only) + probe .aar beds
numbers: 12/12 archives parse EXACT end-to-end; sizes observed 75..338 by content
verdict: CORRECT vs file.org "2-byte header size" (size INCLUDES 6B magic+size prefix);
  CORRECT vs writer M/X/P kind theory (byte is size, not kind)
body: entries chain: magic @0, u16le @4 = header length incl 6B prefix, fields @6..size,
  then this entry's 'A' values in field order, then next AA01. No global headers-first section.
```

```
CR-102 [MEASURED] Field kinds: 1/2/4 u8/u16le/u32le minimal-width; P inline; S u64le; T u64+u32; A/B out-of-line u16/u32
stage: bitstream
artifact: beds q5probe/q6probe + boundary chown beds (root)
numbers: boundaries 255->1, 256->2, 65535->2, 65536->4 (UID/GID/FLG/MOD/DEV all); DAT A->B at n>65535 (70000 bedded 'B')
verdict: CONFIRM writer kinds + EXTEND with '4' (FLG schg 0x20000, DEV, big uid) and 'B'
body: field = key3 + kind1 + kind-body. Int kinds take smallest width fitting value, never clamp/truncate.
  'S' = 8B direct (no len). 'T' = u64le sec + u32le nsec. 'P' = u16le len + inline bytes. 'A'/'B' = len + out-of-line value.
```

```
CR-103 [MEASURED] TYP 1-byte values D/F/L/B/C/S; LNK carries link target; DEV carries dev_t; DAT/XAT presence rules
stage: bitstream
artifact: nest/dev/socket/symlink beds
numbers: 6 TYP values bedded; DEV u32le matches mknod major/minor (0x01000001, 0x03000002)
verdict: CORRECT writer "TYP 2B DP/FP" (1B; P starts PAT); NEW: B/C/S + DEV key
body: D dir (no DAT), F file (+DAT), L symlink (+LNK'P' target, no DAT), B/C devices (+DEV'4', no DAT/XAT),
  S socket (no DAT/XAT). DEV field sits after PAT. XAT present iff xattrs listable (provenance always on files/dirs/links).
```

```
CR-104 [MEASURED] CTM=btime, MTM=mtime; S iff that stamp's nsec==0, per-stamp independent; OS keeps btime<=mtime
stage: probe
artifact: touch/utime/stat beds (ns + tm + fut + bt)
numbers: ns-exact matches (123456789 forced; 801965257 stat-exact; 5/5 writer getattrlist); mixed S/T bedded
verdict: CONFIRM writer crtime-impl; CORRECT viewer A-6 min() (withdrawn NOTE-006: touch/utime retrodate btime)
body: CTM reads file birth time, MTM reads mtime. Each stamp independently 'S' (nsec 0) or 'T'. OS clamps
  btime<=mtime on mtime-set, so CTM<=MTM in practice; no bed separates btime from min(btime,mtime).
```

```
CR-105 [MEASURED] Entries bytewise-sorted by path, dirs depth-first inline; PAT = root-relative path ("" root)
stage: probe
artifact: order.aar adversarial bed + writer p8 exhibits
numbers: 9-entry bed (L,M,a.txt,asub,asub/n.txt,b.txt,zsub,zsub/z.txt); '.' 0x2E sorts before 's'
verdict: CONFIRM writer order claim (writer settled, viewer independently bedded)
body: sibling order = unsigned bytewise on full relpath; a dir's subtree immediately follows it. Not readdir order.
```

```
CR-106 [MEASURED] XAT value = chained records (u32 self-incl len + name NUL + raw value); provenance first; 11B blob constant
stage: bitstream
artifact: xattr.aar (101B XAT = 36+29+36, lens verified) + 20+ entry constancy matrix
numbers: blob 01 02 00 66 97 d0 7a bb 10 2c 73 identical across content/mtime/name/kind/xattr-count/volume/wrapper/nsec variations
verdict: CONFIRM writer 36B shape + EXTEND multi-record chaining; uid/host variation OPEN (single-user/box)
body: one XAT field per entry; value chains records. First record always com.apple.provenance (u32 0x24 + 21B name+NUL + 11B blob).
```

```
CR-107 [MEASURED] Outer = 12B prefix (magic, u32 0, u32 BE blocksize) + 16B/block chain (0, BE unc, 0, BE comp) + payloads; -b range 1..128m
stage: bitstream
artifact: multi-block beds (10MB 3-block, mixed, -b 1m 10-block, -b16/20 micro)
numbers: chains EXACT (10000301, 5037269, 10000413, 400459, 360427); magics pbze/pbzx/pbzm/pbzz/pbz4/pbzb per alg; 129m+ and 0 REJECT (0x93040c00)
verdict: CONFIRM writer1/writer2 framing (three parses, identical bytes); u32x4-vs-u64x2 observationally identical (blocks <=128MB)
body: prefix w1 = blocksize (4m default archive). Inner split into blocksize chunks; each block independently stored-or-compressed.
  a/b words always 0. Widths BE u32; >4GB behavior unreachable via CLI (OPEN, decode-side hand-craft probe suggested).
```

```
CR-108 [MEASURED] Per-block store rule: compress iff 16*comp <= 15*unc (savings >= ceil(unc/16)); equality stores
stage: probe
artifact: 20-pt bisect + name ladder + ratio sweep + fresh re-verify + writer 100/100
numbers: flip pinned (847,793)->C vs (850,~797)->S; name ladder comp const 794, unc 849 C -> 850 S; fresh: (850,796)->C edge-inclusive; ratios 0.575..0.9264 C @937
verdict: CORRECT writer "comp<unc" (misses (15unc/16,unc) window); VERIFIED lzfse+zlib+lz4+lzma+lzraven (flip pairs),
  lzbitmap 3/3 consistent incl non-monotonic compress@300 (494<=503) between stores (rule-predicted all)
body: decision per block on that block's own comp. Exact tie 16c==15u never observed (OPEN micro-gap; <= assumed).
  lzbitmap stores tiny-incompressible where lzfse compresses (its comp misses the bar, same rule).
```

```
CR-109 [MEASURED] Encode selector: aa archive dir-in file-or-stdout-out (silent 0 / coded 1); aea encrypt stdin-ok, -o REQUIRED
stage: probe
artifact: E1-E11 beds
numbers: 11 probes; stdout-omission byte-identical (274B); '-' literal-file class both tools; determinism cmp-clean
verdict: CORRECT CLI-CONTRACT "- for stdio" (dash = literal filename); NEW: encrypt/stdout asymmetry (-o required, decrypt pipes)
body: aa archive: exit 0 silent both streams; missing -d/srcdir -> 1 + coded text; bad -a -> 1 + usage. Omit -o -> bytes on stdout.
  aea encrypt: omit -i reads stdin; omit -o -> exit 1 "-o required". Adapter gaps: no omit-flag stdio form yet.
```

```
CR-110 [SYMBOL] Encode API surface (dirty-side only; NEVER crosses to clean)
stage: recon
artifact: WS recon/exports-*.txt + aa-arm64e-symbols.txt
numbers: aa imports 106 libAppleArchive + 24 libParallelCompression; dylib exports 232 (= tbd count) + 930 rows
verdict: NEW (entry-point map for viewer-side RE targeting)
body: write path entries with cache-relative offsets: AAEncodeArchiveOutputStreamOpen 0x7332C,
  AAArchiveStreamWriteHeader/Blob/PathList, AACompressionOutputStreamOpen(+Existing),
  ParallelArchiveWriterCreate(+Legacy)/WriteDirContents/WriteEntryHeader/WriteEntryData,
  ParallelCompressionOStreamCreate/Write/Destroy. Imagebases: AA 0x2AB561000, PC 0x195721000.
```

```
CR-111 [MEASURED] fifo blocks archive (hang, 0B out); socket/device exit 0 with TYP S/B/C
stage: probe
artifact: watchdog-kill bed (12s) + socket + root-mknod beds
numbers: fifo 0B after 12s (2 independent hangs: writer + viewer); sock 188B TYP S; dev TYP B/C + DEV
verdict: CONFIRM writer hang (ruling-grade negative); NEW device/socket behavior
body: aa archive opens+reads fifos (blocks forever on empty fifo; watchdog discipline for batteries).
  Sockets/devices encode metadata-only. Hardlink encoding OPEN.
```

```
CR-112 [MEASURED] AAR encode deterministic (-t 1); -t4 == -t1 bytes single-block
stage: probe
artifact: E6 + writer d1a/d1b + writer2 reps + -t beds
numbers: byte-identical reruns (274B toy, multi-file, 82-cell matrix reps 2/2)
verdict: CONFIRM fixtures-lane AAR determinism; EXTEND thread-invariance (single-block only; multi-block -t OPEN)
body: fixed inputs+flags => identical bytes incl live-nsec stamps only when inputs fixed. Pins valid per DRIFT-FAIL.
```

```
CR-113 [MEASURED] Hardlink members (regular, nlink>1) carry trailing HLC'1' 00; DAT duplicated per member
stage: probe
artifact: hl/hl3 beds (2-link + 3-link + solo + dir controls)
numbers: 5/5 members HLC-last; solo + dirs HLC-absent; payloads full-size each (18Bx2, 6Bx3)
verdict: NEW (key unseen in prior surveys; convert NLINK/INO->HLC note now grounded)
body: HLC field = last field, kind '1', value 0 constant. Rule: emit iff S_ISREG && st_nlink>1.
  No encode-side dedup; link restoration is decode-side behavior.
```

```
CR-114 [MEASURED] DAT lengths widen A(u16)->B(u32)->C(u64) minimal-width; 4.5GB bedded 'C'
stage: probe
artifact: big5 sparse bed (deleted post-measure; numbers = record)
numbers: 4831838208 -> 'C' + u64le exact; total 4831838451; pbze 1153-block chain EXACT
verdict: EXTEND CR-102 width rule to data lengths; CLOSE Q-9(c)
body: same minimal-fit rule as int fields. pbze per-block u32 never stressed (blocks <= blocksize <= 128m).
  XAT widening past 'A' OPEN micro.
```

```
CR-115 [MEASURED] lzraven Apple-internal (no OSS; tool-bytes == block EXACT); lzbitmap OSS format-match, encode 10B off
stage: probe
artifact: zbm1 beds + libzbitmap @574abea black-box compare
numbers: raven tool==block 3228B; bitmap OSS 3268 vs oracle 3228 (scattered chunk decisions); OSS-decodes-oracle EXACT 4737B
verdict: NEW (hardest encode gaps scoped; writer1 path per A-9(a))
body: raven: iteration oracle = compression_tool bytes; no third-party encoder exists. bitmap: OSS nominatable
  for format/decode; byte-exact encode needs decision hunt. Both keep 15/16 store rule (NOTE-012).
```

```
CR-116 [MEASURED + VENDOR-DOC] lzma/lz4 encoders = Apple Compression framework (preset 6 / Compression-library frame)
stage: probe
artifact: WS scratch-viewer2/lzmabed/bed.py + AADefs.h (CLT 27.0 SDK)
numbers: aa -a lzma payload 476B == compression_tool -encode -a lzma(inner 1109B) EXACT; lz4 614B == tool EXACT;
  tool 135168B sha256 a8f4f8ca0d4a7096...; AADefs.h sha256 dc3181c690242b48...
verdict: NEW (explains writer 355-combo liblzma fail + Apple-denser 236<240; liblzma-grid CLOSED, bed-war retargeted)
body: AADefs.h: "constants match compression.h"; LZMA=0x306 "LZMA preset 6"; LZ4=0x100 "frame format used in
  the Compression library". Container/props preset-6-shaped (dict 8M lc3lp0pb2) but encoder is Apple-internal
  shared aa/compression_tool infra, not XZ Utils. Iteration oracle = compression_tool (beds-OK, not shippable).
```

```
CR-117 [MEASURED] lz4 bv41 framing CLOSED: [bv41 u32le-unc u32le-len block[len]]+ + terminal bv4$; 64KB chunks; stock dict-linked blocks; no flags
stage: probe
artifact: WS scratch-viewer2/lzmabed beds (1109B + 100239B inners) + OSS liblz4 @0774d05 black-box decode
numbers: bed1 4+4+4+598+4=614 exact; bed2 frames (65536,582)+(34703,264), consumed 870/870, usum 100239==outer unc;
  OSS LZ4_decompress_safe exact (1109, 65536) + usingDict exact (34703 w/ 64K prefix); concat==inner byte-EXACT
verdict: NEW (framing fully closed; CORRECT w2 NOTE-w2-9 "flags" mis-split — zero bytes unaccounted)
body: blocks are stock LZ4 (decoder-compatible, encoder-hunt not format-war). Frame N>0 references prior output
  (1-deep prefix proven; deeper chains same mechanism presumed). OSS encoder NONE-FOUND 30 settings
  (writer 26 + viewer default/HC1/HC9/HC12 all 477B vs oracle 598B); lead = faster-than-default axis.
```

```
CR-118 [MEASURED] libcompression is dyld-cache-resident (no on-disk file); provenance = OS build pin only, sha-pin impossible
stage: probe
artifact: find + ctypes CDLL resolution test
numbers: find /usr/lib -maxdepth 2 '*compression*' = EMPTY; CDLL absolute + basename both OK (cache-resolved);
  OS build 26A434
verdict: NEW (beds-OK measurement class confirmed; src-use unpinnable — supports A-12 refuse-recommendation)
body: same provenance class as libAppleArchive (VENDOR-BINARIES §2). Record OS build per bed; re-pin on any OS
  bump (oracle-gate rule). A "pinned sha256" dependency on it is unstatable.
```

## Derivation appendix (this file, session 2026-10-07)

inputs (fresh sha256 where file):
- lanes/target-research@8a5e83e, vendor-docs@67527c5, oss-survey@6056a80, vendor-binaries@111024a,
  fixtures@eeedef2, harness-oracle@543bb13, spec-acquire@ebff5cf, setup-scaffold@3519129 (all read first-hand; see NOTE-002)
- /usr/bin/aa 823df81f... /usr/bin/aea 16bfbb1c... (own hashes MATCH)
- own probe beds: WS tmp/encprobe.bEXeI3, q5probe.jFF4Rl, q6probe.FT9V0Q + worktree tmp/scratch-verify/
- writer exhibits cited as CONFIRM/CORRECT targets only (NOTE-2/3/4/5/6, NOTE-w2-2), never as evidence
not-consulted: decompiler output (none produced; no disassembly run), SDK header contents, port/reference
  sources, decode-side A-answers for encode claims (A-001/002 read for adapter-hash consistency only),
  other-lane branches beyond the 8 intake lanes + writer lanes (verify duty)
outputs: 12 clause drafts (11 MEASURED + 1 SYMBOL), 0 clauses promoted (parent renumbers)
findings: framing/size/rule/store-rule/CTM/btime-invariant/blocksize-bounds/u32-u64-equivalence/fifo-negative
base: 0999654 + lane commit b6b9026

## Derivation appendix (this file, session 2026-10-07 attempt#2)

inputs (fresh sha256 where file):
- /usr/bin/compression_tool 135168B sha256 a8f4f8ca0d4a7096...e178 (own)
- AADefs.h (CLT 27.0 SDK) sha256 dc3181c690242b48...9daf (own)
- WS/tools/lz4 @0774d05537f9762f838f7ab541b7765f1a729cb5 (own rev-parse, tree clean) + liblz4 bytes
  sha256 2ec9fac7...2dad (own, black-box decode/encode only)
- WS/tools/libzbitmap @574abeae25b25c3319b9b6a9225cc7464e08ae88 (own rev-parse; +1 untracked build dylib noted)
- /usr/bin/aa sha + OS build 26A434: aa bytes trusted-from-prior VENDOR-BINARIES.md:9 (not re-hashed this
  session); OS build own sw_vers
- own probe beds: WS scratch-viewer2/lzmabed/bed.py + inline parses (1109B + 100239B inners, 64KB chunk bed)
- writer exhibits as CONFIRM/CORRECT targets only (CODEC-FINDINGS.md lzma/lz4 rows, NOTE-8 grids, NOTE-w2-9
  framing gloss CORRECTED by A-11, RESULTS-rb/rb2 rows cross-checked), never as evidence
not-consulted: decompiler output (none produced; no disassembly run), port/reference sources, vendor
  framework implementations, decode-side answers, other-lane branches beyond intake + writer lanes (verify duty)
outputs: 3 clause drafts (CR-116 MEASURED+VENDOR-DOC, CR-117/118 MEASURED), 0 promoted (parent renumbers)
findings: lzma/lz4-Apple-Compression-identity, bv41-framing-closed, libcompression-cache-provenance
base: lane commit d3c7512

```
CR-119 [MEASURED] raven/bitmap encoders = Apple Compression framework; compression_tool reproduces raven EXACT, rejects bitmap; libcompression one-shot reproduces BOTH EXACT
stage: probe
artifact: WS scratch-viewer3/bed.py + bed2.py (own, sha e5fdf5cb... / 2f1768f8...)
numbers: inner 1109B fixed input. aa -a lzraven payload 508B == compression_tool -encode -a lzraven(inner)
  EXACT; == libcompression COMPRESSION_LZRAVEN(0xD05) buffer call EXACT. aa -a lzbitmap payload 540B ==
  libcompression COMPRESSION_LZBITMAP(0x702) buffer call EXACT. compression_tool -a/-A lzbitmap -> rc=1
  usage error (algo list has no bitmap). compression.h (CLT 27.0 SDK, sha 62485df0...): 0x702 "buffer API
  only", 0xD05 "buffer API only, macOS 27.0+". tool 135168B sha a8f4f8ca...e178 (own MATCH)
verdict: NEW (raven joins lzma/lz4 with a compression_tool iteration oracle; bitmap oracle is
  libcompression-only, beds-OK class per A-12(a)/CR-118; closes w2 Q-13)
body: same shared-infra story as CR-116 for 2 more codecs: aa outer payload bytes are exactly what
  Apple's Compression stack emits for the raw inner. No wasted bitmap hunt: iterate vs one-shot.
```

```
CR-120 [MEASURED] outer blocks partition raw.aar WHOLE: sum(unc)==len(raw.aar) exact, last unc == tail slice; no +28/+30 anywhere
stage: probe
artifact: WS scratch-viewer3/bed.py + bed2.py + filename-vary bed (own runs)
numbers: raven b10k zeros-100k x3 filenames: inners 100239/100239/100235, lasts 239/239/235, sum==rawlen
  3/3; bitmap b10k 100239 EQ (11 frames); raven random-50k all-STORED 6/6 sum 50237 EQ; single-block
  raven+bitmap 1109 EQ both. 10/10 EQ total (8 distinct configs + bitmap/random fresh re-runs).
  chain closes byte-exact every case (12+sum(16+comp)==file)
verdict: CORRECTS w2 NOTE-w2s2-5 (+30) and NOTE-w2s2-6 (+28 last-block rule): both are artifacts of w2's
  UNC() defining inner=len(raw)-28. Their pinned verdict (su-28==len-28 ⟺ su==len) stays TRUE — record-only
  fix, no battery change. raw.aar incl AA01 magic IS the blocked input (confirms A-10/CR-116 framing parses)
body: the outer layer is a plain partitioner: 12B prefix (magic+0+BE blocksize) + blocks[16B hdr
  (0,BE unc,0,BE comp) + comp bytes], stored ⟺ comp==unc with payload = raw slice.
```

```
CR-121 [MEASURED] AEA -a accepts 8 values (7 + raw=none alias); codec choice has NO plaintext envelope field; bogus = rc1 hard error
stage: probe
artifact: WS scratch-viewer3/bed.py + bed2.py (own, profile 1, fixed key bytes 0x00..0x1F)
numbers: none/lzfse/lzma/lz4/zlib/lzraven/lzbitmap + raw ALL rc=0 (help lists the 7; raw undocumented).
  zeros-100k sizes: none/raw 118784, all 6 codecs 19456; urandom-5k: all-7 24576. hdr first-12B IDENTICAL
  all 8 (AEA1 01 00000000 00000000). same-alg rerun agrees 127/24576 (~chance). -a bogus: rc=1
  "Invalid compression algorithm: bogus" + usage, no fallback. decrypt -v prints "compression: <name>"
  (own: none/lzma/lzbitmap) — tool-reported signal, not envelope bytes; both decrypts RT-clean
verdict: NEW (AEA codec leg pinned for w2 battery; PRE-001 "seg-alg IDs on encode" answered: inside the
  encrypted envelope, unbeddable from ciphertext — decode-side territory if ever needed; closes w2 Q-15)
body: the AAR-outer 7 ⟷ AEA 7 codec correspondence holds. Observable encode-side codec effects = output
  size on compressible input + decrypt -v echo only.
```

## Derivation appendix (this file, session 2026-10-07 attempt#3)

inputs (fresh sha256 where file):
- /usr/bin/aa 823df81f1c4331d10ef4 (own re-hash, MATCHES attempt#1 appendix prefix 823df81f...)
- /usr/bin/aea 16bfbb1c09b092ef6c10 (own re-hash, MATCHES attempt#1 prefix 16bfbb1c...)
- /usr/bin/compression_tool 135168B sha a8f4f8ca0d4a7096e178 (own re-hash, MATCHES CR-116)
- compression.h (CLT 27.0 SDK) sha 62485df0c0bc5c9a (own; constant values read first-hand)
- OS build 26A434 (own sw_vers, same as CR-118)
- own probe beds: WS scratch-viewer3/bed.py (sha e5fdf5cb5661e578) + bed2.py (sha 2f1768f8b82a2860),
  each run TWICE (initial + fresh re-run before writing; identities hold within-run both runs;
  payload-size drift 504->508 across runs = input mtime, not behavior)
- libcompression via ctypes CDLL("libcompression.dylib") (cache-resolved per CR-118; beds-OK A-12(a))
- writer exhibits as CONFIRM/CORRECT targets only (NOTE-w2s2-5/6 trailer claims CORRECTED by CR-120,
  NOTE-w2s3-2 codec-meta + GATE-592722d raw-alias/bogus independently AGREE with CR-121), never as evidence
not-consulted: decompiler output (none produced; no disassembly run), port/reference sources, vendor
  framework implementations, decode-side answers, other-lane branches beyond intake + writer lanes (verify duty)
outputs: 3 clause drafts (CR-119/120/121 all MEASURED), 0 promoted (parent renumbers)
findings: raven-bitmap-oracle-identity, outer-partition-rule-correction, AEA-codec-matrix
base: lane commit c056286

```
CR-122 [MEASURED] lz4 matchfinder = hash table with count-based eviction (50% ~8.5K distinct inserts,
0% by ~11.5K); distance/window ruled OUT; no-start tail zone ~121-128; plain dups future-independent
stage: probe
artifact: WS scratch-viewer3/lz4probe.py (sha aee4c9ea...) + bed3.py (sha 50e86d99...), oracle
  compression_tool -a lz4 (CR-116-identical to aa payloads), own bv41/LZ4-sequence parser
numbers: decisive pair (retest@12108): zeros-12K fill -> CHECK (len 1884, off 12008); distinct-12K ->
  SKIP (literal, covering=[]). survival/6 seeds: 7250: 6/6; 8000: 5/6; 9000: 2/6; 10000/11000: 1/6;
  >=11500: 0/6 (0/24 combined). phase: candpos 5000 + 8K/9K -> 5/6 + 3/6 (same as candpos 100).
  tail: run60@1900/chunk2000 MISSED; run40@1123/chunk4163 CHECK (off 1021); zeros2000 tail 123 literal.
  futures: 9 variants (5 seeds + 4 flip-distances) -> identical match (8,681). all numbers re-run fresh
  (bed3.py) reproducing inline-bed values EXACTLY (deterministic oracle)
verdict: NEW (eviction mechanism + table-size class for w1 hunt; CORRECTS any distance/window theory;
  tail-zone CONFIRMS chunklen-relative ~121-128, REJECTS absolute-position limit; one-pass BOUNDED to
  clear cases — w1 HOLE1 future-shape not replicated, needs their minimal-pair bytes)
body: zeros fill (1 distinct 4-gram) never evicts over 12K; distinct fill evicts by count with a cliff
  STEEPER than any single uniform table (no one S fits 6/6 @7.25K with 0/24 @11.5K+) — second mechanism
  OPEN (segmented/capped/multi-slot/adaptive candidates). last-pos re-confirmed (offs track most recent).
  metadata hash lead NONE-FOUND: compression_tool = 54-string thin driver (no encoder constants), no
  dyld-shared-cache-util, SDK headers API-only, Ghidra absent. behavioral size: ~8-16K-slot CLASS (rough).
```

## Derivation appendix (this file, session 2026-10-07 attempt#3 entry-4)

inputs (fresh sha256 where file):
- /usr/bin/compression_tool sha a8f4f8ca0d4a7096e178 (re-MATCHES CR-116; oracle path for all beds)
- own apparatus: WS scratch-viewer3/lz4probe.py (sha aee4c9ea56de1659; self-tests: zeros match@1,
  rand stored-path, wall781 exact-start off-tracking) + bed3.py (sha 50e86d996e2d4954; fresh re-run
  reproduces ALL headline numbers exactly)
- own metadata sweep: strings -a (54 strings) + nm (thin driver, ParallelCompression imports) +
  SDK compression.h grep (empty) + tool-absence checks (dyld-shared-cache-util, Ghidra per NOTE-035)
- writer exhibits as CONFIRM/CORRECT targets only (NOTE-15/16/17/18 hunt state, misnumbered w1s2 Q-13
  answered as A-17; TAILS5/SL1123 shapes bedded independently — same verdict class, own inputs),
  never as evidence
not-consulted: decompiler output (none produced; no disassembly run), port/reference sources, vendor
  framework implementations, decode-side answers, other-lane branches beyond intake + writer lanes (verify duty)
outputs: 1 clause draft (CR-122 MEASURED), 0 promoted (parent renumbers)
findings: lz4-table-eviction-curve, tail-zone-confirm, future-independence-bound, metadata-none-found
base: lane commit bda1f61
