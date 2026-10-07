# Spec clauses: decode side (viewer lane working copy)

Viewer-authored clauses. Parent folds into spec/CLAUSES.md at merge.
Shape: CR-nnn + ONE tag + stage + artifact + numbers + verdict. Untagged = inadmissible.

```
CR-001 [MEASURED] oracle decode selector contract (aa extract / aea decrypt)
stage: probe
artifact: vectors/selfgen (fixtures@eeedef2, shasum -c 13/13 OK re-verified)
numbers: 9 probes green; exits 0 ok / 1 fail; aa err 0x9106b002 (missing/corrupt input); aea err 0xde108400 HMAC (wrong pw)
verdict: CONFIRM vs OPEN-2/OPEN-4 (decode path exists, AEA plaintext == hello-raw.aar cmp-clean); CORRECT vs CLI-CONTRACT stdio claim (see CR-004)
body: aa extract -i IN -d OUT = dir-out (stdout empty, files under OUTDIR, cmp-clean P1); omit -i reads stdin (P9). aea decrypt [-password-value|-key-value] -i IN -o OUT = byte pipe (P4 cmp-clean); omit -i/-o = stdio (P7/P8). stderr silent on success, diagnostics on fail. probe logs: WS tmp/decode-viewer-probes (P1..P9, this shift).
```

```
CR-002 [SYMBOL] aa decode-entry import inventory (arm64e)
stage: recon
artifact: /usr/bin/aa (527200B, sha256 823df81f..., 3 archs)
numbers: 225 undef (0 defined, stripped); 106 libAppleArchive (87 AA* + 19 AEA*); 24 libParallelCompression binds; 228 bind rows / 225 unique; __text 71832B @0x100007d0; bind tables __auth_stubs 216x16B @0x100012068, __auth_got 216x8B @0x10001c218, __got 8 @0x10001c8d8, __auth_ptr 4 @0x10001c918 (216+8+4=228 EXACT)
verdict: CONFIRM vs OPEN-6 partial (decode half of API surface now enumerated client-side); OPEN vs OPEN-3 (3 dup bind rows unidentified, minor)
body: decode entries: AADecodeArchiveInputStreamOpen, AADecompression{,RandomAccess}InputStreamOpen, AAArchiveStreamRead{Header,Blob}, AAExtractArchiveOutputStream{Open,SetQuarantine}, AAConvertArchiveOutputStreamOpen, 5x AAAssetExtractor*, ParallelArchive{Extract,Read,ReadMetadata} (+11 Parallel*). tbd cover: 0/106 missing from 232-symbol list -> all public API.
```

```
CR-003 [SYMBOL] aea decode-entry import inventory (arm64e)
stage: recon
artifact: /usr/bin/aea (337040B, sha256 16bfbb1c..., 3 archs)
numbers: 97 undef (0 defined, stripped); 38 libAppleArchive (9 AA* + 29 AEA*); 97 bind rows / 97 unique EXACT; __text 36600B @0x10000650; __auth_stubs 93x16B @0x100009548, __auth_got 93x8B @0x100010258, __got 4 @0x100010540 (93+4=97 EXACT); __cstring 401 strings, 5 hkdf profile-id prefixes embedded
verdict: CONFIRM vs OPEN-5 partial (profile ids client-side corroborate 0..5); OPEN vs OPEN-4 remainder (encrypt-side entries out of decode scope)
body: decode entries: AEADecryptInPlace, AEADecryptToFileChunk, AEADecryption{,RandomAccess}InputStreamOpen + 9 AA helpers (5 byte-stream, 2 file-stream, 2 thread-ctx). tbd cover: 0/38 missing -> all public API. no libParallelCompression linkage (CONFIRMS L4).
```

```
CR-004 [MEASURED] stdio selection rule: omit-flag, never dash
stage: probe
artifact: /usr/bin/aa + /usr/bin/aea (same provenance as CR-002/CR-003)
numbers: 4 probes (P3/P6 dash-fail + P7/P8/P9 omit-ok); dash -> exit 1 `open: -` + 0x9106b002; omit -> exit 0 BYTES-MATCH x3
verdict: CORRECT vs CLI-CONTRACT.md ("IN/OUT may be - for stdio", harness-oracle@543bb13:27,30) — dash is a literal filename to both tools
body: stdio contract: omit -i to read stdin, omit -o to write stdout. adapter gap: oracle-adapter.sh cannot express stdio today (passes - through -> oracle fails 1). writer/sweep use real paths until adapter gains omit-flag form.
```

```
CR-005 [INFERRED:MODERATE] decode logic lives in dylibs, CLIs are thin shims
stage: recon
artifact: /usr/bin/aa + /usr/bin/aea section tables
numbers: __text aa 71832B / aea 36600B; imports aa 225 / aea 97; cstrings aa 785 (0 pbz literals) / aea 401
body chain: small __text + large bound-import surface (106/38 lib calls) + zero embedded pbz magics (aa) => container/codec machinery is lib-side (cache-resident, no standalone file). MODERATE: static only, no dynamic trace yet; disassembly or cache extraction raises to STRONG.
verdict: OPEN vs OPEN-2 (dylib tables); gates deep behavior clauses (bitstream stage)
```

```
CR-006 [MEASURED] outer single-block layout (all pbz*)
stage: bitstream
artifact: vectors/selfgen 8 AAR (fixtures@eeedef2) + 3 own-gen probes (WS tmp/decode-viewer-probes: hello-b1m, tiny, rnd)
numbers: 10/10 samples; 28B header; magic ASCII @0; zeros @4/@12/@20; blocksize BE u32 @8 (0x400000 @-b 4m, 0x100000 @-b 1m CONFIRMED own); uncSize BE u32 @16; compSize BE u32 @24; fileSize = 28 + compSize EXACT 10/10
verdict: CONFIRM vs OSS-SURVEY §1 pbze note (BE sizes @+4/+12 of 16B block hdr: matches @16/@24 relative to @12); CONFIRM vs TARGET-L1 §A inner-off-0 (inner AA01 @28+ when stored, @0x2a lzfse/lz4 compressed)
body: per-codec comp (unc 2445): lzfse 293, zlib 262, lzma 304, lz4 416, lzbitmap 337, lzraven 296. payload prefixes: bvxn/bv41 (lzfse/lz4, AA01 @0x2a), XZ magic (lzma), ZBM framing (lzbitmap, AA01 @0x2f), 2b00caec (lzraven), 06785e (zlib). inner hdr u16LE after AA01 (0x52 hello, 0x4d empty).
```

```
CR-007 [MEASURED] stored-block rule (comp==unc, raw inner, no codec framing)
stage: bitstream
artifact: vectors/selfgen/aar/empty-lzfse.aar (141B, committed fixture, pin OK)
numbers: 1 positive (empty: unc=comp=0x71=113, AA01 @28, 28+113=141 EXACT); 2 negatives (3B tiny comp 186<249, 100B random comp 284<344 — still framed bvxn)
verdict: CONFIRM vs OSS-SURVEY §8 stored-block layout (comp==unc raw payload); PARTIAL vs trigger rule (empty triggers, tiny/random don't — trigger predicate OPEN)
body: stored payload starts AA01 directly (no bv/codec bytes). writer MUST implement stored path: it is reachable from stock `aa` output (empty dir case) and breaks naive inflate-always readers (survey §2 failure class).
```

```
CR-008 [INFERRED:STRONG] inner TLV field parse (key + subtype + len + LE value)
stage: bitstream
artifact: vectors/selfgen/aar/hello-raw.aar (2445B, pin OK)
numbers: 7 fields read @6..~60: TYP/1/'D', PAT/P/0005/"hello", UID/2/f501, GID/1/14, MOD/2/ed01, FLG/1/00, CTM/T/12B
verdict: OPEN vs CR-005 (deep: full TLV grammar incl long-form lens, all 23 -h keys); CONFIRM vs VENDOR-DOCS-L2 field list (typ/pat/uid/gid/mod/flg/ctm all in man list)
body chain: UID f501 LE u16 = 501 (own uid) + GID 14 = 20 (staff) + MOD ed01 LE = 0x1ed = 493 = 0755 (own umask default) = 3 independent corroborations -> STRONG for (subtype byte, LE value) reading of short int fields. string field PAT carries u16LE len. CTM 12B timestamp shape unparsed (bytes recorded, no claim).
```

```
CR-009 [MEASURED] multi-block chain (12B prefix + N x (16B hdr + payload), EOF-exact)
stage: bitstream
artifact: own-gen big/ (3MB zeros + 500KB random; inner 3500382B via -a raw) @ -b 1m/-b 256k/-b 4m (WS tmp/decode-viewer-probes)
numbers: 3/3 walks EOF-exact; unc sums 3500382 EXACT x3; b1m 4 blocks (505811/759/759/408 comp); b256k 14 blocks (blk0 stored 262144==262144, blk1 240628, blk2..12 300 each, blk13 92510/254); b4m single (3500382/507323)
verdict: CONFIRM vs CR-006 (single-block = 1-iteration special case); CONFIRM vs CR-007 (stored mixes per-block in chains)
body: walk rule: off=12; loop {16B hdr zeros+uncBE+zeros+compBE; payload comp bytes; stored iff comp==unc} until off==EOF. zeros MUST be 0; off>EOF or pad = corrupt. blk BE field @8 = blocksize in all 3 (0x100000/0x40000/0x400000 CONFIRMED).
```

```
CR-010 [MEASURED] outer payload = complete codec frame (oracle-decodable whole)
stage: probe
artifact: vectors/selfgen 4 AAR payloads (lz4/lzraven/lzfse/lzma) + compression_tool (macOS 27.0.1)
numbers: 4 decoding rules verified: lz4 full-payload -a lz4 MATCH; lzraven full-payload -a lzraven MATCH (6/6 off>0 slices fail); lzfse full-payload -a lzfse MATCH; lzma payload = raw XZ magic (no frame). all MATCH = cmp vs hello-raw.aar
verdict: CONFIRM vs compression_tool man digest (per-alg decode exists); OPEN sub-parse: lz4 inner XLE32 = comp-16 unexplained; lzraven size fields unlocated (3-sample bed filed, A-007); lzbitmap framing unprobed (writer has OSS path)
body: writer oracle cross-check per codec: slice @28..28+comp, compression_tool -decode -a <alg>, cmp vs raw. lz4 sub-frame bytes: bv41 + uncLE32 + XLE32 + stream@12 (f7 2e + literals); raw-LZ4 reading of stream INFERRED:MODERATE (lz4_raw slice fails = quirk OPEN).
```

```
CR-011 [MEASURED] codec sub-frame rules (lzfse magic @4096 unc; lz4 64KB frames; stored trigger)
stage: bitstream
artifact: own-gen magic sweep (20 archives: zeros/text/random x sizes, -b 4m single-block) + fixtures (WS tmp/decode-viewer-probes)
numbers: lzfse n<4096 (max 3998) / 2>=4096 (min 4098), 100B bracket, comp-overlap kills comp-theory; lz4 @4 = min(unc,65536) bracket (31738,102650], frames EOF-exact x2, usum exact x2 (102650, 600244); stored: random 10K-600K 4/4 stored, small random framed iff comp<unc; tails bvx$ 12/12 lzfse, bv4$ 3/3 lz4
verdict: CONFIRM vs CR-007 (stored trigger refined to comp>=unc); CONFIRM vs CR-010 (payload = frame(s) + $-terminator); OPEN: lz4 stream raw-LZ4 confirm (writer-side lib), bvx2 @8+ stream parse (OSS-readable), exact stored comparison, lzraven internals
body: lzfse frame = magic + uncLE32 + (n: XLE32=comp-16 5/5 | 2: stream bytes) + stream + bvx$. lz4 frame = bv41 + uncLE + compLE + raw-block stream; multi-frame concatenated + bv4$; per-block rule (multi-block blk1 -> bvx2). writer1's 4MB flip = unc-driven, not multi-block-driven.
```

## Clause index

| ID | Tag | Claim | Verdict |
|----|-----|-------|---------|
| CR-001 | MEASURED | decode selector contract | CONFIRM/CORRECT, see body |
| CR-002 | SYMBOL | aa decode-entry imports | CONFIRM (OPEN-3 SETTLED: ___chkstk_darwin x4) |
| CR-003 | SYMBOL | aea decode-entry imports | CONFIRM |
| CR-004 | MEASURED | omit-flag stdio rule | CORRECT vs CLI-CONTRACT |
| CR-005 | INFERRED:MODERATE | thin-shim, logic in dylibs | OPEN vs OPEN-2 |
| CR-006 | MEASURED | outer single-block layout | CONFIRM |
| CR-007 | MEASURED | stored-block rule | CONFIRM + trigger OPEN |
| CR-008 | INFERRED:STRONG | inner TLV field parse | CONFIRM + grammar OPEN |
| CR-009 | MEASURED | multi-block chain | CONFIRM |
| CR-010 | MEASURED | payload = codec frame | CONFIRM + sub-parse OPEN |
| CR-011 | MEASURED | sub-frame rules (4096/64K/stored) | CONFIRM + 4 OPENs |
| CR-012 | MEASURED | lzraven stream framing (hdr/blocks/params/terminator) | CONFIRM + 2 OPENs |
| CR-013 | MEASURED | AAR outer magic per codec (pbz* table) | CONFIRM |
| CR-014 | MEASURED | entry-kind census (11 TYPs + behaviors) | CORRECTED by CR-015 (was 11, is 12) |
| CR-015 | MEASURED | TYP H hardlink-by-path (12th kind) | CORRECT vs CR-014 |
| CR-016 | MEASURED | lzraven bit0 raw emission rule | CONFIRM vs CR-012 |
| CR-017 | MEASURED | AEA cluster-chain walk (offsets/repeat/N-global) | CONFIRM vs writer2 split rule |
| CR-018 | MEASURED | AEA pad-auth verified ranges ([padstart,arc)) | CONFIRM ranges; construction OPEN |
| CR-019 | MEASURED | W/R/T/M silent-skip exit 0 | CORRECT vs A-013; dispute CLOSED |
| CR-020 | MEASURED | AEA pad-tag = last-nmac HMAC rule | CONFIRM (closes CR-018 OPEN) |
| CR-021 | SYMBOL | libAppleArchive public-export inventory (232) | CONFIRM vs CR-002/003 + vendor list |
| CR-022 | MEASURED | AEA empty-archive shape (156B bare / cmac pad-tag) | CONFIRM vs writer2 empty rows |
| CR-023 | MEASURED | lzraven flag alphabet + raw exclusivity (0x3 negative, 0x402 wild) | CONFIRM alphabet; OPEN narrowed |

```
CR-012 [MEASURED] lzraven stream framing (8B hdr + u32 block-hdrs + u32-0 terminator)
stage: bitstream
artifact: own-gen lrv-ladder (18 aa-emitted -a lzraven -b 4m -t 1, unc 337..1048815) + 3 compression_tool -encode streams + 3 A-007 re-parsed (WS tmp/decode-viewer-probes/lrv-ladder)
numbers: walks end-exact 20/20; nblocks == ceil(unc/524288) 20/20; params size(i) smallest>=src 24/24 (2 exact 239B-margin fits); oracle full-stream MATCH 18/18 framed + 2/2 outer-stored; surgery 12/12 structural-FAIL; sweep 67 (62 FAIL / 1 MATCH-explained-reserved-bit / 4 DIFF); leniency MATCH 3/3 (params-high/reserved-flags/trailing); corruption-localization 3/3 last-32B of block range; third-party lzraven_dec 16/16 MATCH + 2/2 correct-reject
verdict: CONFIRM vs CR-010 (payload = frame(s) + terminator, sub-parse now closed); CONFIRM vs third-party SPEC [test] framing (anat0m1a/liblzraven@700b88c, corroborated first-hand, NOT used as evidence); CORRECT vs A-007 (size fields LOCATED: @8/@10 are u32 block-hdr halves (size>>12, flags&0xFFF); @4 is params u32, not zeros); OPEN: stream-internals implementation (writer turf via nominated SPEC), BCJ/raw flags unobserved (0x000 24/24)
body: layout: u32 magic 0xECCA002B (LE 2b00caec) + u32 params (bits[31:26] dict index, decoder validates low26==0 then ignores) + N x [u32 (size<<12|flags) + size payload] + u32 0 mandatory. unc ABSENT from stream (0 pattern hits); output length emergent; outer uncBE is the check. no stream checksum (4 silent-corrupt DIFFs). decoder stops at terminator, ignores trailing.
```

```
CR-013 [MEASURED] AAR outer magic encodes the codec (per-codec pbz* table)
stage: bitstream
artifact: vectors/selfgen/aar 8 fixtures (fixtures@eeedef2, pins OK) + ladder AARs
numbers: 8/8 fixtures: lzfse->pbze lz4->pbz4 lzbitmap->pbzb lzma->pbzx lzraven->pbzm zlib->pbzz raw->AA01-bare (no outer); ladder lzraven AARs 18/18 pbzm
verdict: CONFIRM vs CR-006 (magic ASCII @0, now tabulated); CONFIRM vs writer aad.c dispatch (independent agreement); NOTE: magic family shared with OTA pbzx/pbzm containers, DIFFERENT layouts (ours 28B+BE-u32 per CR-006/009 vs theirs 12B+BE-u64) — never apply third-party §10 container doc to AAR outer
body: raw = bare inner (AA01 @0, file IS the inner). all other codecs = outer-framed with codec magic.
```

```
CR-014 [MEASURED] entry-kind census: 11 TYPs, 8 sampled with record bytes + fs effects
stage: probe
artifact: own-gen kindbed (reg/symlink/hardlink/fifo/socket/xattr/sub, feeder-guarded) + dev2.aar (crafted-cpio convert) + SDK AADefs.h enum (VENDOR-DOC corroboration) (WS tmp/decode-viewer-probes/kindbed)
numbers: TYP bytes: F/D/L/P/S/C/B sampled (record hex + list-json + extract); H = F+HLC:0 (same-ino nlink=2 post-extract); fifo archive-hang w/o feeder + extract-hang post-create (25s+ timeout); socket/device extract exit-1 0xc8055000 "not implemented yet"; device archive 6/6 FAIL "Archive encoding failed"; /dev scan aborts (fd); M trigger 0/5 probes; whiteout 0 vendor mentions outside header enum
verdict: CONFIRM vs CR-008 (TLV shape; entry u16 = keys-region offset, value blobs appended); CONFIRM vs VENDOR-DOCS-L2 types (CORRECTED: 11 not 8 — h is HLC pseudo-filter, W/R/T exist in enum); CONFIRM vs writer HLC semantics (NOTE-015, exact agreement); OPEN: W/R/T/M triggers + samples (parse rule safe-by-construction: TYP always 1-char UINT)
body: TYP1<char> for all kinds; LNK/P+u16; HLC1/u8 group; DAT/A+u16 reg-only; DEV4/u32LE st_rdev (3,2/1,0 exact); XAT blob u32-records; MTM S-short(8B)/T-long(12B). xattr-only is NOT a kind (field on F). R/T unreachable on macOS (Solaris bits). M = parse + skip (no fs object).
```

```
CR-015 [MEASURED] TYP H hardlink-by-path: 12th on-disk kind (decode-side real, encode-side unobserved)
stage: probe
artifact: writer1 fixture hlink-basic.aar (99db53e, pin 46239d23... verified own) + `aa list` parse + DPROBE-04 rules
numbers: TYP1'H' + LNK/P ("hello/repeat.txt") + DAT:58 + XAT:36 parsed by oracle JSON; H behaviors writer-measured (LNK-path link, no-LNK abort, LNK-must-be-regular, forward refs, symlink-reject, fifo-hang-consistent)
verdict: CORRECT vs CR-014 (census was 11, is 12: F D L P C B S H W R T M); CORRECT vs A-012/A-013 (CLI 'h' = TYP H filter, not HLC pseudo-filter); SDK header enum (11, no H) covers encoder-produced types only
body: H entries carry LNK path + full DAT; extract links by path (deferred pass). no natural encode vector (encoder emits HLC groups); evidence writer-crafted + oracle-measured. census: 9 known-behavior (F D L P S C B H + M-skip) + 3 open (W/R/T).
```

```
CR-016 [MEASURED] lzraven bit0 raw emission rule (incompressible block -> verbatim payload)
stage: bitstream
artifact: own-gen bit0/ (zr/rz/r600k/r2m aa -a lzraven + ct2-r/ct2-zr/ct2-r10k pure-stream; seeded) (WS tmp/decode-viewer-probes/bit0)
numbers: 6 raw blocks: rz-blk0 524288, zr-blk1 90351 (== last-out EXACT), ct2-r 524288+90112, ct2-zr-blk1 90112, ct2-r10k 10240 (single-block); raw size == block output 6/6; roundtrips MATCH 5/5; pure-random aa inners OUTER-stored 2/2 (no stream); mixed aa inners per-block raw 2/2
verdict: CONFIRM vs CR-012 (extends: raw-flag semantics + emission conditions); mutual-CONFIRM vs writer2 e7a9249 (independently derived same rule + AEA-seg firing); OPEN: raw+BCJ combos (0x003) unobserved
body: rule: block incompressible -> flags bit0, payload = verbatim block bytes. aa path absorbs fully-random inners at outer level; pure-stream path has no outer so random always goes raw per-block. decoder: bit0 -> memcpy size bytes, skip entropy decode (SPEC §2.3 driver rule, behavior-confirmed).
```

```
CR-017 [MEASURED] AEA cluster-chain walk (2-cluster offsets, repeat/continue, global seg-N)
stage: probe
artifact: own-gen c2-sha.aea (256MiB+1 zeros, p5/-a none/sha256/pad-none, 268472541B) + walk.py + 6 flip probes (WS tmp/decode-viewer-probes/cluster2)
numbers: OVH 37084 = 18620+18464; C0 hdr@156 (sh[156,10396)/nmac/smacs), C0 data 256x(1M,1M), C1 hdr@268454076 (sh/nmac/smacs), C1 seg0 (1,1), tail 255x(0,0); EOF-exact; root orig/arc(=filesize 2/2)/segsz=1M/segper=256/comp='-'/ckalg=2; 6/6 flips exit 1 (seg-N GLOBAL: C0seg0->0, C1seg0->256; C0-hdr faults route via seg-0 worker tail, C1-hdr via next-cluster unlock without tail; smac faults surface at cluster level)
verdict: CONFIRM vs writer2 split rule ceil(IN/256MiB) (boundary mutual-CONFIRM); bed A-015
body: ONCE: prologue 156B + root fields. REPEAT per cluster: sh-table (256 entries, zero tail) + nmac32 + smacs. CONTINUE: cluster index, cmac chain (C1 verify consumes C0 nmac), output concat, seg-error N. size equation OUT = IN + 156 + N*clustersz(ck) (sha256 18464 measured 1+2cl; none 10272 writer 1..3cl; murmur64 12320 writer 2cl).
```

```
CR-018 [MEASURED] AEA pad-auth verified ranges ([padstart,arc), arc-ignored, read-vs-auth classes)
stage: probe
artifact: own-gen p-18.aea (18B/default-pad 19456B) + p16-18.aea (pad 2B) + c2p-sha.aea (256MiB+1/default-pad 276824064B) + flip/append/trunc matrix (WS tmp/decode-viewer-probes/padauth)
numbers: range [padstart,arc) EXACT 3 shapes (padstart = last-seg-data-end: 18638 / 18638 / 268472541); arc==filesize 4/4; bytes>=arc IGNORED 2/2 (exit 0 MATCH); short pad -> 0x9e040400 `reading padding`; corrupt -> 0x9e041c00 ST / 0x9e05cc00+`authenticating padding` MT; 2-byte pad both bytes authenticated; pad = randomized ciphertext (815/818 nonzero, 2 encryptions differ), OUTSIDE seg table (sh lists real segs only)
verdict: CONFIRM ranges; OPEN construction (tag slot + MAC inputs); bed A-016 partial
body: ONE trailing region all shapes (no per-cluster pads). tag is OUTSIDE pad (2B-pad proof); NOT rdata spare (22 zeros x4) NOR sh tail (255/255 zero x2); mechanism (own binary read): streaming digest <=1MB chunks, HKDF info label len7 "AEA_PAK", constant-time compare vs stored tag, wantlen [8,256]. candidates remain: nmac/smacs/cmac/rmac/salt.
```

```
CR-019 [MEASURED] TYP W/R/T/M extract = silent-skip exit 0 (DAT + DAT-less)
stage: probe
artifact: own-gen raw single-file archive (D@6/F@119) + 8 TYP-flip extracts (WS tmp/decode-viewer-probes/q018)
numbers: W/R/T/M DAT-carrying 4/4 exit 0 EMPTY-stderr SKIPPED; DAT-less W exit 0 skipped + sibling `hello` MATCH; Z control silent-skip; S controls 2/2 exit 1 loud stanza (`Error 0xc8055000 / not implemented yet / creating fs object: <pat> / N entries failed to extract`) + sibling extracted (continue)
verdict: CORRECT vs A-013 (loud-for-W/R/T prescription, was unmeasured); CONFIRM vs writer1 256-TYP census; bed A-018; dispute CLOSED
body: unknown-kind policy = skip-and-continue exit 0 regardless of DAT carriage; S-class = loud-skip-and-continue exit 1 with count line. no revisit unless a loud W/R/T vector fires.
```

```
CR-020 [MEASURED] AEA pad-tag construction (last-nmac = HMAC(padkey, [padstart,arc)))
stage: bitstream
artifact: padsearch2.py v2 search + padconfirm.py (6 shapes) + unpadded negatives (WS tmp/decode-viewer-probes/padauth)
numbers: HIT 3/3 seed files (pad 818/818/2B) + 7/7 generality (2-cluster last-nmac 8MB pad, p1/zlib 932B pad, cksum-none 4228B pad, p2-signed 658B pad, p0-signed-padded 4068B pad, p3-ecdhe 61507B pad, p4-ecdhe-signed 61347B pad) + 3/3 unpadded negatives (nmac random iff padlen 0); rule: padkey = HKDF-SHA256(main, "AEA_PAK"), tag = HMAC-SHA256(padkey, file[padstart:arc)) vs last nmac
verdict: CONFIRM (closes CR-018 construction-OPEN); bed A-016B
body: non-last nmacs keep chain role; padlen 0 skips auth; mismatch -> pad-auth fail, len<arc -> read class. universal across all 6 profiles (p0..p5 first-hand)/checksums/codecs/clusters/padlens 2B..8MB; p0 default emits no pad (roundtrip OK, skip holds). streaming-verify mechanism (init/update/final, const-time compare) corroborates.
```

```
CR-021 [SYMBOL] libAppleArchive public-export inventory (232 exports, decode surface enumerated)
stage: recon
artifact: dyld_info -all_dyld_cache -exports (macOS 27.0.1, arm64e) -> WS aa-exports.txt (232 names) + aa-block.txt (offsets); full-cache dump deleted post-extract
numbers: 232 exports = 185 AA* + 47 AEA* + 0 other; setdiff vs vendor-docs API-SYMBOLS-L2.txt 232-list EMPTY both ways; all CR-002 (106) + CR-003 (38) bound imports resolve incl every named decode entry; 18 Decrypt/Decode symbols exported, CLIs bind a subset (ToStream/AndExtract/RandomAccess families unbound by either CLI)
verdict: CONFIRM vs CR-002/CR-003 (dylib side of the client import inventory); CONFIRM vs vendor-docs symbol list (exact mutual); PARTIAL vs CR-005 (public surface closed; stripped internals stay behavior-only by design)
body: the dylib's public API surface is fully enumerated and cross-checked three ways (cache exports, vendor list, CLI binds). decode entries live here as public symbols; no hidden public decode API exists outside this table.
```

```
CR-022 [MEASURED] AEA empty-archive shape (prologue-only bare, cmac pad-tag when padded)
stage: probe
artifact: own-gen e-nopad.aea (156B) + e-pad2.aea (160B, p5/-a none) + flip + HMAC confirm (WS tmp/decode-viewer-probes/padauth)
numbers: empty/-padding none = 156B exactly (prologue, zero cluster headers), decrypt exit 0, 0 bytes out; empty/default-pad = 160B (156 + 4 pad, arc 160), pad flip -> 0x9e041c00 exit 1, HMAC(padkey,[156,160)) == cmac True
verdict: CONFIRM vs writer2 empty rows (size + decrypt); cmac-slot rule mutual-CONFIRM (writer2 found, viewer independently confirmed)
body: orig==0 short-circuits cluster parsing entirely; pad (if any) starts at prologue_end and verifies against the cmac slot (no nmac exists). extends CR-020 with the degenerate case.
```

```
CR-023 [MEASURED] lzraven block-flag alphabet {0,1,2,4,6,0x402} + raw-bit exclusivity (0x3/5/7 unobserved)
stage: probe
artifact: 7 own compression_tool -encode -a lzraven inputs (Mach-O /bin/ls, true-random 600K, code+random mix, /bin/zsh 2MB, 64K-alternating, BCJ-bait sea, xz-output) + block-flag walks + wild big-lrv.aar (2MB Mach-O via aa -a lzraven, stream flags [0x4,0x402x3]) + oracle/proto dual-decode (WS tmp/decode-viewer-probes/lrv003)
numbers: 15 blocks: 0x0 x2, 0x1 x4, 0x2 x3, 0x4 x2 (zsh blk0 + big blk0), 0x6 x2, 0x402 x3 (big blk1-3, NEW bit10, content-driven per amend); raw (0x1) blocks 4/4 carry no other bits; combos 0x3/0x5/0x7 0/15 blocks; wild-0x402 archive: oracle exit 0 MATCH + writer1 proto exit 0 TREE-MATCH (decoder-covered, no gap); trigger-map: 9 pos-vectors (A/B/C/D/E/F/G/H/I) all roundtrip-clean + end-exact, 19 blocks: code<->0x4 follows content thru position swap (A/B), zeros 4/4 0x0, zsh 8/8 0x4, ls-bytes 4/4 carry bit1 (E/C1/H 0x6, I-hi pure 0x2), size ruled out (G); bit10-hunt 5 vectors: same-bytes aa-vs-ct IDENTICAL 2/2 (big3m 6x0x4 both paths; dir-inner [0x4,0x402x3] both paths exact sizes), wild replicated (repdir unc 2045677 flags MATCH), full-zsh pure [0x4,0x2x3] vs dir-inner [0x4,0x402x3], big3m-dir 6x0x4 (no bit1-content, no bit10); 0x402 x6 total; nblocks==ceil(unc/512K) 38/38 (recount: 20 ladder + 9 pos + 7 hunt + 2 quarters incl inner-payload streams; entry-14's 26/26 undercounted); bit1 non-monotonic: ls-q3 (H=3.53) 0x2 vs ls-q4 (H=1.36, 88% zero) 0x0 (J/K roundtrip-clean) — ladder 0x0/0x2/0x6/0x4 by chunk character, exact thresholds encoder-side
verdict: CONFIRM alphabet {0,1,2,4,6,0x402}; CR-012/016 raw+BCJ OPEN narrowed to bounded negative (encoder not observed emitting raw+transform after targeted hunt; decoder fail-closed on unseen combos stands)
body: bit0 = raw verbatim (incompressible/high-entropy chunks); bit1/bit2/bit10 = INDEPENDENTLY-triggered content features (bit2 on zsh-like code slices, bit1 on ls-like/zsh-late slices, joint 0x6 on mixed; bit10 rides bit1-content slices under shifted alignment; position/size/path ALL ruled out — tree-mode-bit hypothesis REFUTED first-hand); bit0 never co-occurs with transform bits in 15/15 blocks. exact per-feature predicates stay encoder-side (decode-covered regardless).
```

Status of every clause: UNPROVEN until an implementation written ONLY from
this spec handles vendor real output.
