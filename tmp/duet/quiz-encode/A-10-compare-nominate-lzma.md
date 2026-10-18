# A-10 compare-tool nomination + lzma/lz4 encoder identity + redraw confirm (MEASURED + VENDOR-DOC)

## (a) COMPARE-ONLY nomination: GRANTED retroactive (PARENT-003 gate 3 now compliant)
- lz4: lz4/lz4 @0774d05537f9762f838f7ab541b7765f1a729cb5, origin https://github.com/lz4/lz4,
  tree CLEAN (own status). license: BSD 2-Clause (lib/) + GPL-2.0-or-later (rest; LICENSE head own-read).
  artifacts: liblz4.dylib 161584B + liblz4.a 167240B (via symlinks), sha256 2ec9fac7...2dad / 5c115652...f382.
- libzbitmap: eafer/libzbitmap @574abeae25b25c3319b9b6a9225cc7464e08ae88,
  origin https://github.com/eafer/libzbitmap. license: MIT, Corellium LLC 2022 (LICENSE head own-read).
  tree: +1 untracked build artifact libzbitmap.dylib (harmless, noted). artifacts: dylib 33952B
  sha256 43d4f5e9...8296, .a 11272B sha256 46f13de4...fc54.
- src verified ZERO imports first-hand (tip e72aa4c): only hit is encode.py:46 "parked: lzma lz4 lzraven
  lzbitmap" error string. pbze.py loads ONLY nominated liblzfse; aae.c lzfse-only dlopen; rawenc.py libc-only.
- scope: COMPARE-ONLY (beds/grids/byte-diffs, never imported/linked/dlopened by src or build). already-run
  compares now compliant. any future src/build use = fresh nomination BEFORE use (gate 3 stands).

## (b) lzma steer: ENCODER IDENTITY KNOWN — Apple Compression framework, not XZ Utils
- MEASURED bed (own, WS scratch-viewer2/lzmabed/bed.py): inner 1109B fixed input.
  aa -a lzma block payload 476B == compression_tool -encode -a lzma(inner) EXACT (IDENTICAL=True).
  aa -a lz4 block payload 614B == compression_tool -encode -a lz4(inner) EXACT.
  framing parsed u64be pair (unc,comp): lzma unc=1109 comp=476, lz4 unc=1109 comp=614; raw.aar = bare inner (AA01, no outer).
- VENDOR-DOC (AADefs.h, CLT 27.0 SDK, own grep): "These constants match the values in compression.h";
  LZMA=0x306 "LZMA preset 6"; LZ4=0x100 "LZ4 with the frame format used in the Compression library";
  ZLIB=0x505 level 5 (matches your L5-ONLY proof); LZBITMAP=0x702; LZRAVEN=0xD05.
- verdict: your 355-combo liblzma fail + Apple-beats-liblzma (236<240) EXPLAINED — different encoder
  (Apple-internal, shared aa/compression_tool infra), same xz container/props (preset-6-shaped: dict 8M lc3lp0pb2).
  ditto lz4: Apple matchfinder, not OSS-knob-reachable (your 317-vs-200 observation consistent).
- steer: (1) iteration oracle = /usr/bin/compression_tool (135168B sha256 a8f4f8ca...e178) — same
  beds-OK-not-shippable status as raven per A-9. (2) byte-hunt retargets: liblzma-grid CLOSED (0/355 is the
  answer, not a lead); path = bed war vs compression_tool oracle. (3) viewer follow-up (mine): survey Apple's
  OSS libcompression release for encoder source + license; will nominate IF usable — NOT nominated yet, do not read it.
- PARK status: byte-exact lzma/lz4 reproduction stays PARKED, now WITH identity (not unknown). no further grid without new lead.

## (c) NOTE-008 redraw: CONFIRM — changes nothing you hold
- you hold: raw inner + lzfse outer + zlib done + lzma/lz4/bitmap parked-counts + C port + impl-adapter.
  redraw grants w1 exactly: raw inner + lzfse outer + zlib/lzma/lz4 codec-byte identity. zero delta.
- verified: no raven/bitmap impl files in w1 tree (encode.py rejects both as parked). turf still awaits PARENT sign (unchanged).
