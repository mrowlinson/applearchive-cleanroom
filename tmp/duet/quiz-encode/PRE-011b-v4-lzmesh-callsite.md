# PRE-011b lzmesh callsite: NONE on any AppleArchive surface (PARENT-011/012)

## libcompression HAS lzmesh (0xE05, buffer API)
- full ID sweep 0x0-0xFFF: 339 working IDs; 0xE05 encodes (38B test vector)
  + roundtrip TRUE. bytes fingerprint as lzmesh per LZMESH shared spec
  (02-format-spec.md): tag 0x01 head, 0xFF end marker.
- families mapped by magic: 0x100 bv41/lz4, 0x101 lz4_raw, 0x200-0x209
  stored/zlib-ish, 0x306 xz/lzma, 0x500-0x509 zlib, 0x600-0x602 ?, 0x700
  ZBMv12, 0x701/0x702 ZBMv9, 0x801/0x802/0x891/0x8a1 lzfse, 0x900 ?, 0xa0x ?,
  0xddc-0xdff raven (2b00caec), 0xe00/0xe01/0xe05/0xe09 mesh (01140500).

## AppleArchive NEVER invokes it (4 negatives)
1. CLI -a/-A lists (aa/aea/ct --help): lzmesh absent everywhere.
2. -a lzmesh: aa rc=1, ct rc=1, ct -A rc=1 (all rejected).
3. strings aa/aea: 0 lzmesh hits (shas re-match CR-122/123).
4. /usr/lib dylibs are cache-stubs (no files); nm empty — static link
   audit impossible without cache tools (absent, cf CR-122); behavioral
   surfaces above are the complete CLI/API evidence.

## verdict + link plan
- NO callsite: nothing in this repo links lzmesh (nothing to link).
  revisit ONLY if a new AppleArchive surface appears (re-probe -a lists
  per OS bump). PARENT-012 pin (duet-land3 f56d181a) recorded, unused.
