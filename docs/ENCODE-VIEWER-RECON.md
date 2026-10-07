# Encode-viewer recon record (lanes/encode-viewer)

Viewer (dirty/spec), side ENCODE. First-hand recon 2026-10-07, macOS 27.0.1 arm64.
Bulky captures: /Volumes/NVME/applearchive-cleanroom-ws/recon/ (symbols, exports).
Probes: WS tmp/encprobe.* q5probe.* q6probe.* + worktree tmp/scratch-verify/.

## 1. Provenance (re-verified first-hand, MATCH L4)

/usr/bin/aa 527200B sha256 823df81f1c4331d1e36eee38b20b71a76f016835a01c68d863ce5d8fcb280ef4
/usr/bin/aea 337040B sha256 16bfbb1c09b092ef0996191ba5e152485fad40be8b28736bf40f68f1628e6c10
Both: Mach-O universal x86_64 + arm64e + arm64e.x1. aa UUID 64F1159D-DC30-38B1-A5D3-C993715FD7C3,
aea UUID 647DA924-84DF-3788-A9A0-2141DD1D04F2. aa links libAppleArchive + libParallelCompression
+ CF 5027.0.69 + Security 62460.1.2 + libSystem 1359.0.0; aea same minus libParallelCompression.

## 2. Symbol inventory (nm -m, arm64e)

aa: 226 lines = 1 defined (__TEXT,__text) + 225 undef: 106 libAppleArchive, 78 libSystem,
24 libParallelCompression, 11 CoreFoundation, 6 Security.
aea: 98 lines (all undef imports).
x86_64 vs arm64e aa: identical except libSystem shims (chkstk/bzero, $INODE64 stat family,
dyld_stub_binder). All 106+24 framework imports cross-arch identical.
Segments arm64e: aa __text 71832B __cstring 25820B; aea __text 36600B __cstring 11686B.
Verdict: thin CLIs; encode logic in dyld-cached dylibs.

## 3. Encode entries (aa imports; offsets = dyld export table, cache-relative)

libAppleArchive __TEXT base 0x2AB561000 (from .map): AAEncodeArchiveOutputStreamOpen 0x7332C,
AAArchiveStreamWriteHeader 0x5EE4, WriteBlob 0x5EFC, WritePathList 0x70B0,
AACompressionOutputStreamOpen 0x7B2F8 / OpenExisting 0x7BCFC, AAHeaderGetEncodedSize 0x68B40,
GetPayloadSize 0x68B38.
libParallelCompression __TEXT base 0x195721000: ParallelArchiveWriterCreate 0x9B1C /
CreateLegacy 0x9B9C / Destroy 0x9BC0, WriteDirContents 0x229C, WriteEntryHeader 0x9CA0,
WriteEntryData 0x9E9C, OStreamCreate 0x44F6C / Write 0x44FD4 / Destroy 0x44FDC.
libAppleArchive exports: 232 rows = L2 tbd 232 count MATCH. libParallelCompression: 930 rows,
430 with offsets >1MB (re-exported/objc aliases); 72 match archive/compress/diff/patch families.

## 4. Behavior beds closed (see quiz A-1..A-6 for numbers)

Encode selector contract (11 probes), battery entry, clean-read ruling, first beds (empty/one x raw/lzfse),
framing (size rule, kinds 1/2/4/P/S/T/A, CTM=btime, MTM=mtime, order bytewise+depth-first, payloads per-entry
field-order), edges (widening boundaries, FLG=st_flags, DEV key, TYP D/F/L/B/C/S, fifo HANG, names verbatim,
15/16 store rule, multi-block chain, blocksize word). Parser 12/12 archives EXACT (WS tmp/aar-parse.py, dirty-side only).

## 5. Tooling gaps

Ghidra: absent (no /Applications, brew cellar, /opt, WS/tools; sibling path stale). No dsc_extractor/
dyld-shared-cache-util. RE so far via nm/otool/dyld_info/strings + running-binary probes. Disassembly
stage NOT started; table inventory from export offsets is next-best without extraction.

## 6. Wall log

No clean-side contact beyond quiz A-/NOTE-/VERIFY-. No vendor expression crossed (beds+numbers+verdicts
only; symbol names above stay on dirty side / this lane). LNK-bytes + xattr-order + per-alg flips + hardlink
beds queued as writer/viewer follow-ups.
