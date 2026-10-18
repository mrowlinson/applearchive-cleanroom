# NOTE-003 encode-viewer: recon progress (heartbeat 1)

- provenance RE-VERIFIED first-hand: aa 823df81f.../527200B, aea 16bfbb1c.../337040B,
  3 archs (x86_64+arm64e+arm64e.x1), linkage matches L4 exactly (MATCH).
- nm arm64e: aa 226 lines (1 defined __TEXT,__text + 225 undef: 106 libAppleArchive,
  78 libSystem, 24 libParallelCompression, 11 CF, 6 Sec). aea 98 lines.
- encode entries (aa imports, dirty-side SYMBOL candidates):
  AAEncodeArchiveOutputStreamOpen, AAArchiveStreamWriteHeader/WriteBlob/WritePathList,
  AACompressionOutputStreamOpen(+Existing), AAHeaderGetEncodedSize/GetPayloadSize,
  ParallelArchiveWriterCreate(+Legacy)/WriteDirContents/WriteEntryHeader/WriteEntryData,
  ParallelCompressionOStreamCreate/Write/Destroy.
- segments arm64e: aa __text 71832B/__cstring 25820B; aea __text 36600B/__cstring 11686B.
  Thin CLIs; logic lives in dyld-cached libAppleArchive/libParallelCompression.
- cache: 79-file split dyld_shared_cache_arm64e (+.atlas/.map) present.
- tooling gap: no Ghidra in /Applications,/usr/local,~/Applications,/opt,WS/tools;
  no dsc_extractor/dyld-shared-cache-util in Xcode usr/bin head. Still hunting
  (sibling project tooling, deeper Xcode paths). No disassembly started.
- next: full symbol-file capture to WS + continued extractor hunt + positive controls.
