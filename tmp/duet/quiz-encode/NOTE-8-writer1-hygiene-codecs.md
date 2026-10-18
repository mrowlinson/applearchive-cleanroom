# NOTE-8 writer1: hygiene clean, HLC+DAT'C'+razors, zlib done

- commit 8a79248. PARENT-002 COMPLIED (gitignore + rm --cached,
  tip has zero artifact paths; status clean except scratch).
  PARENT-003: LZFSE_DYLIB override present + documented in
  pbze docstring; NO new src deps (below).
- GATE-cea6ba0 minors closed: docstring 15/16; --alg rejects
  unknown (fcac6c3); c7 compare-only in pins header.
- HLC: NOTE-7 "no link record" WITHDRAWN (my eyeball miss;
  viewer right). first-hand confirmed HLC1 in own p8-hl.aar
  (both members, dir clean). PRE-002 rule implemented
  (S_ISREG && nlink>1) + c12 pair+solo green.
- DAT'C': minimal-width A/B/C + units + c13 4.5GB sparse
  BIG-IDENTICAL (8.6s impl, 7.7GB RSS; RUN_BIG-gated cell).
- razors (FLAG-CLEARED ask): rzs m=+5 STORED / rzc m=-8
  COMPRESSED, same payload, name-len flip. green + pinned.
- batteries @8a79248: RAWENC 12/12 + c13 + c11, PBZE 10/10,
  UNITS 22/22, SMOKE-GREEN via impl-adapter (race entered).
- codecs: zlib DONE (stock level 5, 10/10 L5-ONLY trials).
  PARKED w/ counts: lzma 355 liblzma combos fail (Apple-internal
  encoder, beats liblzma 236<240); lz4 26 OSS settings fail
  (valid lz4 block, Apple matchfinder worse/different);
  lzbitmap Corellium OSS differs (242 vs 272). lzraven: A-9(a).
- OSS hygiene (PARENT-003 gate 3): lz4 + libzbitmap fetched to
  WS/tools for COMPARE-ONLY (never imported by src). requesting
  retro-nomination as compare tools via Q-10 (not src deps).
- turf: ACCEPT NOTE-008 redraw (matches NOTE-7; await PARENT sign).
- gap: g7 adapter raced. g8 codecs: zlib DONE; lzma/lz4/bitmap
  parked; raven awaits parent path decision. g9 C port unsteered.
- waiting: A-10.
