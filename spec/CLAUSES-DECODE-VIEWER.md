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

## Clause index

| ID | Tag | Claim | Verdict |
|----|-----|-------|---------|
| CR-001 | MEASURED | decode selector contract | CONFIRM/CORRECT, see body |
| CR-002 | SYMBOL | aa decode-entry imports | CONFIRM + OPEN-3 minor |
| CR-003 | SYMBOL | aea decode-entry imports | CONFIRM |
| CR-004 | MEASURED | omit-flag stdio rule | CORRECT vs CLI-CONTRACT |
| CR-005 | INFERRED:MODERATE | thin-shim, logic in dylibs | OPEN vs OPEN-2 |

Status of every clause: UNPROVEN until an implementation written ONLY from
this spec handles vendor real output.
