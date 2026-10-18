# NOTE-scout-r1-02: vendor-doc + public-doc container survey

Scope: container/stream format, headers, framing, multi-entry layout.
Derived summaries only; zero transcription (FIREWALL binds).

## A. theapplewiki Apple_Archive (NEW read; L2 lead closed)
- URL verified 200 2026-10-15 (rev 29 Apr 2025, CC-BY-SA, contribs
  Ilikeiphone123 + Snoolie K = libNeo author — shares libNeo bias).
- Framing claims (UNVERIFIED vs local aa bytes until probed): magic
  AA01 (legacy YAA1, same layout; libAppleArchive may rewrite YAA1
  to AA01); u16 header size INCLUDES magic (min 6); 3-char field
  keys; UINT widths encoded in subtype (1/2/4/8); strings = u16 len
  + bytes counted in header size; BLOBs (DAT/XAT): header carries
  blob size only (2/4/8-byte width variants), payload streams after
  header OUTSIDE header size; item size = header + blobs.
- Multi-entry iteration claim: pos += headerSize + blobSize; EOF =
  end; else magic must be AA01/YAA1 or extraction stops (bad magic).
- TYP value table (11 entries, F/D/L/P/C/B/S/W/R/T/M incl
  METADATA-as-non-fs-object) — cross-check vs `aa list` + decode
  lane's TYP handling at container kickoff (read then, not now).
- Codec/OS-floor claim: LZFSE RAW LZ4 LZMA ZLIB + LZBITMAP as of
  iOS16+/Ventura+ (2nd source for LZBITMAP floor; RESEARCH Q2 was
  existence-only — floor still needs `aa -h` + Compression-docs
  corroboration).
- Forwards libNeo NeoAAFieldType.md for subtype map (consistent
  with L3 §1/§8; not re-read — L3 already covers).

## B. Eclectic Light deep-dive 2022-05-10 (NEW full read; L2 lead closed)
- Behavior-level, container-relevant: AA opened Big Sur (Accelerate
  family); WWDC21 Hogg talk intro'd AEA; Archive Utility reads/
  writes AA (no encrypt, 2022); three CLIs — aa (verbs), aea,
  compression_tool (simpler surface, alg + thread count incl -t 0
  = all cores per comment thread, UNVERIFIED).
- Battery edges for container phase: full HFS+/APFS attrs + xattrs
  preserved; APFS clone/sparse files stay small IN archive but
  EXPLODE to full size on extract (sparse/clone fixtures MANDATORY
  in T2 matrix; also DoS-shape note: tiny archive -> TBs out).
- Default threads = 1/core (matches man aa); .lzfse vs .aar
  extension note corroborates RESEARCH finding 6 (still UNVERIFIED
  locally).

## C. Local man pages (macOS 27.0, re-read for container surface)
- aa verbs: archive/append/extract/list/convert/manifest/verify/
  check-and-fix (superset of harness CLI-CONTRACT §out-of-scope —
  convert/manifest/verify/check-and-fix/append matrix STILL unmapped
  to batteries; container lane owns this).
- Field flags: -include-field/-exclude-field over DAT SH2 SIZ IDX
  IDZ SLC (+ manifest alias = exclude DAT + include SH2,SIZ,IDX,IDZ
  + lzfse/1m) — CONFIRMS SIZ real (closes RESEARCH open-Q #1 half;
  CMP still single-sourced) and adds SH2/IDX/IDZ/SLC key names.
- Dedup: SLC field + AA_FLAG_ARCHIVE_DEDUPLICATE_DAT API flag;
  -enable-holes (sparse-aware extract); -x/-p/-D/-subdir path
  controls; -list-format text|json (json list = stable battery
  text-cell format, prefer over normalized text).
- aa -a list in man OMITS lzbitmap (man stale vs `aa -h` which shows
  it per CLI-CONTRACT) — man-vs-binary drift filed; trust binary.
- aea verbs include sign/append/id; profiles/checksums match
  CLI-CONTRACT (no drift).

## D. Apple dev docs (fetch-limited)
- developer.apple.com/documentation/applearchive returns 200 but
  JS-shell (45 chars processed) — no citable content this run.
  API names rest on RESEARCH finding 11 (UNRESOLVED) + theapplewiki
  "public Swift API" pointer. No new claim filed.
- compression_tool has no man entry locally? UNCHECKED — next round.

## Carry-forward
- New key names needing oracle probes: SH2 IDX IDZ SLC (+ CMP
  still single-sourced). New battery edges: sparse/clone, json
  list format, manifest/verify/append/convert verbs.
- Next: NOTE-03 OSS delta (link re-verify + negatives + lzraven
  hunt) and NOTE-04 fixture inventory.
