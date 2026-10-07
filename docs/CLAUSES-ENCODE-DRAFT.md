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
