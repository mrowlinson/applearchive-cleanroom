# Gated recon: decode side (viewer, dirty)

Date: 2026-10-07. Lane: lanes/decode-viewer. Arch of record: arm64e.
Tools: nm/otool/lipo/size/dyld_info/strings/codesign (system). No decompiler installed (OPEN-1).

## 1. Provenance (re-verified own, MATCH L4)

| binary | bytes | sha256 | archs | mtime |
|---|---|---|---|---|
| /usr/bin/aa | 527200 | 823df81f1c4331d1e36eee38b20b71a76f016835a01c68d863ce5d8fcb280ef4 | x86_64 arm64e arm64e.x1 | Sep 24 03:10:37 2026 |
| /usr/bin/aea | 337040 | 16bfbb1c09b092ef0996191ba5e152485fad40be8b28736bf40f68f1628e6c10 | x86_64 arm64e arm64e.x1 | Sep 24 03:10:37 2026 |

Linkage (otool -L): both -> libAppleArchive 1.0.0, CoreFoundation 5027.0.69,
Security 62460.1.2, libSystem 1359.0.0. aa ONLY adds libParallelCompression 1.0.0.

## 2. Symbol inventory (nm -arch arm64e)

| binary | defined globals | undef (imports) | AA* | AEA* | Parallel* | system |
|---|---|---|---|---|---|---|
| aa | 0 (stripped) | 225 | 87 | 19 | 21 (14 Archive + 7 Compression) | 98 |
| aea | 0 (stripped) | 97 | 9 | 29 | 0 | 59 |

Binds (dyld_info -arch arm64e -fixups): aa 292 rows = 228 bind + 64 rebase;
aea 172 rows = 97 bind + 75 rebase. Unique bind syms: aa 225 (= undef, 3 dup rows),
aea 97 (= undef). Per-dylib rows: aa CF 11 / libAppleArchive 106 / libParallelCompression 24 /
libSystem 81 / Security 6; aea CF 7 / libAppleArchive 38 / libSystem 46 / Security 6.

Positive control: 0/106 aa + 0/38 aea AA/AEA imports missing from the 232-symbol
tbd list (API-SYMBOLS-L2.txt) -> every AppleArchive import is public API. PASS.

Decode entries imported (aa): AADecodeArchiveInputStreamOpen,
AADecompressionInputStreamOpen, AADecompressionRandomAccessInputStreamOpen,
AAArchiveStreamReadHeader, AAArchiveStreamReadBlob,
AAExtractArchiveOutputStreamOpen, AAExtractArchiveOutputStreamSetQuarantine,
AAConvertArchiveOutputStreamOpen, 5x AAAssetExtractor*, ParallelArchiveExtract,
ParallelArchiveRead, ParallelArchiveReadMetadata (+11 more Parallel*).
Decode entries imported (aea): AEADecryptInPlace, AEADecryptToFileChunk,
AEADecryptionInputStreamOpen, AEADecryptionRandomAccessInputStreamOpen +
9 AA byte-stream/file-stream/thread-ctx helpers.

## 3. Table inventory (bind tables; no defined-symbol tables — stripped)

| binary | table | addr (arm64e) | size | entries | entry width |
|---|---|---|---|---|---|
| aa | __auth_stubs | 0x100012068 | 0xd80 3456B | 216 | 16B |
| aa | __auth_got | 0x10001c218 | 0x6c0 1728B | 216 | 8B |
| aa | __got | 0x10001c8d8 | 0x40 64B | 8 | 8B |
| aa | __auth_ptr | 0x10001c918 | 0x20 32B | 4 | 8B |
| aa | __text | 0x100007d0 | 0x11898 71832B | — | — |
| aa | __cstring | 0x100012de8 | 0x64dc 25820B | 785 strings | — |
| aea | __auth_stubs | 0x100009548 | 0x5d0 1488B | 93 | 16B |
| aea | __auth_got | 0x100010258 | 0x2e8 744B | 93 | 8B |
| aea | __got | 0x100010540 | 0x20 32B | 4 | 8B |
| aea | __text | 0x10000650 | 0x8ef8 36600B | — | — |
| aea | __cstring | 0x100009b18 | 0x2da6 11686B | 401 strings | — |

Reconciliation: aa 216+8+4 = 228 bind rows EXACT; aea 93+4 = 97 EXACT.
Data tables live in the cache-resident dylibs (no standalone file) -> OPEN-2.

__cstring survey: aa 785 strings, 8 codec-token hits, 0 `pbz*` literals
(magics constructed, not literal, or lib-side). aea 401 strings, 18 AEA-token
hits, 5 hkdf profile-id prefixes embedded (profile table client-side).

## 4. Gate verdict: PASS (both vendor builds)

1. provenance MATCH (hash+size+arch+mtime+linkage) both. 2. symbol inventory
complete (0 defined, all undef enumerated + per-dylib). 3. positive controls
green (tbd cover 0-missing; bind rows reconcile to section sizes; unique syms
= nm undef). 4. running-binary confirmation: 9/9 decode probes green (see CR-001).

## 5. OPEN rows (decode recon)

| # | question | settling work | gates |
|---|---|---|---|
| OPEN-1 | decompiler install (Ghidra/Hopper/radare2)? | install + pin version on demand | disassembly transcripts |
| OPEN-2 | dylib tables (libAppleArchive in dyld cache)? | cache extraction tooling or decompiler-on-cache | table inventory (data) |
| OPEN-3 | aa 3 duplicate bind rows: which symbols? | 1 dyld_info pass, diff rows vs unique | CR-002 completeness (minor) |
