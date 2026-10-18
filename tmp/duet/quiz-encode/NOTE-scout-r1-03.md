# NOTE-scout-r1-03: OSS container delta (re-verify + lzraven hunt)

L3 §1-6 stands; this is delta-only. No code read this round (existence
+ search-snippet level only, except man page below).

## A. Link re-verify (curl HEAD, 2026-10-15, all fetch-verified)
- 404 HOLDS: github.com/apple/apple-archive (wall posture unchanged;
  no Apple source drop; cleanroom derivation still the lane).
- 200: libNeoAppleArchive, apple-archive-rust, kinnay/AEA (+FORMAT.md
  blob URL), eafer/libzbitmap, blacktop/ipsw, mac_file_format_docs
  (+raw README), lzfse/lzfse, file.org/extension/aar.
- theapplewiki Apple_Archive 200 (full-read, NOTE-02). Eclectic Light
  deep-dive 200 (full-read, NOTE-02). Apple dev-docs AppleArchive 200
  but JS-shell (no citable content).

## B. lzraven: OPEN item now has leads (L3 found zero OSS trace)
- NEW (existence-verified 200, NOT read — see wall note):
  1. anat0m1a/liblzraven — self-described clean-room C11 LZRAVEN
     impl; search snippet claims COMPRESSION_LZRAVEN enum 0xD05,
     new in OS 27 cycle, pbzm OTA container use.
  2. retrowave3/apple-compressions — claims lzmesh + lzraven +
     lzbitmap .h/.c pairs "based on iOS 27.0", selector 0xD05.
- WALL FLAG (binding on all clean lanes): liblzraven's own SPEC
  snippet admits derivation via interop RE incl [disasm] evidence
  markers; apple-compressions provenance unaudited. Per FIREWALL +
  README posture, disasm/RE-derived sources are FORBIDDEN to
  implementers. These are DECOMPILE-SIDE/question-track leads ONLY:
  static claims must be confirmed against the running binary (aa /
  compression_tool black-box) before becoming spec clauses. No clean
  lane reads/clones/ports them without a viewer nomination + ruling.
- Corroboration available WITHOUT touching them: `aa -h` lists
  lzraven (already in CLI-CONTRACT); compression_tool -a includes
  lzraven (man, §C). Codec-framing probes via local binaries suffice
  for container needs; enum value 0xD05 stays UNVERIFIED (single
  second-hand source class) until a black-box probe shows it.
- ipsw "lzraven support" per snippet = cgo into Apple's closed lib
  (not open) — consistent with L3 §4 (LZ4/LZVN unsupported there).

## C. compression_tool man page (local, macOS 27.0 — NEW read)
- Exists (/usr/bin/compression_tool + man). NOTE: Compression-library
  surface, NOT the AAR container — adjacent, not container proper.
- Codec framings (man-stated, file for container DAT-payload work):
  zlib = raw DEFLATE (RFC 1951), encoder level 5; lzma = LZMA2
  preset 6 inside XZ container; lz4 = raw LZ4 in simple frame
  (compression.h) + lz4_raw variant; lzfse payload; lzraven payload.
- -A block-compression mode + -b block size + -t threads (default =
  logical threads; cf Eclectic Light -t-0-means-all claim, still
  UNVERIFIED). NO lzbitmap in -a list (man-vs-aa drift again).
- Container relevance: these framings are what DAT blobs carry per
  -a choice; container battery needs one vector per framing incl
  stored/raw default (L3 §2 gap) + sparse/clone (NOTE-02).

## D. Still OPEN (unchanged from L3 §10)
- libNeo AEA profile-1 contradiction; ipsw LZMA/LZVN quirk; CMP key
  single-sourced; theapplewiki framing claims UNVERIFIED vs bytes.
- Dev-forums XIP thread (L2 lead) still unread — low container value
  (XIP predecessor); deprioritized, not dropped.

## Carry-forward
- Next: NOTE-04 fixture inventory (vectors/ + WS batteries, hashes
  only), then NOTE-05 harness skeleton commit on lane.
