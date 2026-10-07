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

Status of every clause: UNPROVEN until an implementation written ONLY from
this spec handles vendor real output.
