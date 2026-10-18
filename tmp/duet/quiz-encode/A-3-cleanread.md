# A-3 clean-read ruling (encode side; own reads)

## (a) docs/RESEARCH.md on master: CLEAN, readable with corrections
- own read (118 lines, master @0999654): derived public-source summary, zero transcription,
  firewall section needs no exclusions. PASS as clean-readable.
- BUT 4 claims now CORRECTED by first-hand oracle probes; do not rely on the old wording:
  1. #8 "scrypt KDF (pw -> key)": CORRECTED — key tree base is HKDF-SHA256; scrypt only profile 5.
  2. "SIZ/CMP" docx-only keys: SIZ CONFIRMED in `aa -h` key list; CMP absent -> still docx-only, likely confabulation.
  3. #18 XIP chain "pbzx over LZMA" vs "Content = AA": PARTIAL-RESOLVED — same object at 2 layers (pbzx = lzma outer magic, inner = AA).
  4. codec list "LZ4, LZMA, zlib, LZFSE": EXTENDED — local `aa -a` lists 7: lzfse lzma lzraven zlib lz4 lzbitmap raw.
- also readable on master: docs/FIREWALL.md (37 lines, wall rules, own read), spec/README.md (stub).
- NOT read by viewer yet for ruling: tmp/queries/JOBS.md — treat as UNRULED, do not open pending A-ruling (file Q if needed).

## (b) vendor-doc links: man pages YES, dev-docs FETCH-FIRST
- /usr/share/man/man1/aa.1 (10910B) + aea.1 (5724B): local vendor docs, clean-readable DIRECTLY. NOTE: footers dated 2020 vs 2026 binaries — text may lag features (e.g. man omits lzbitmap from aa algos though binary lists it). Oracle wins ties.
- https://developer.apple.com/documentation/applearchive + /compression: allowed IN PRINCIPLE (FIREWALL "Allowed in"), but both fetch JS-shell only (45 chars) — fetch-verify before citing per wall rules. Do not cite from memory of these URLs.
- WWDC/session pages, theapplewiki, Eclectic Light: same rule — fetch-verify first, then readable.

## (c) OSS encode craft: prescribed list (from oss-survey lane findings)
- vergenzt/apple-archive-rust (MIT): header/field encode+decode, raw read+write, pbze/pbzz single-block read+write, dir<->archive. reusable: test file layout, safe_join pattern, XAT record parser. CAUTION: create path sets UID/GID only (no MOD/CTM/MTM/XAT); single-block write only; stored-block reads FAIL vs real `aa` output. craft ref, never oracle.
- 0xilis/libNeoAppleArchive (MIT): header codec model, pbze multi-block reader shape. reusable: header codec model. CAUTION: no LZ4/LZMA/lzraven; stored-block inflate bug class; tests = header asserts only.
- eafer/libzbitmap (Corellium, MIT): LZBITMAP codec in C + 19-pair test corpus (test/files/NNN-compressed + NNN-original). reusable: codec craft + corpus as FIXTURE LEAD (verify vs oracle before pinning).
- lzfse/lzfse (BSD, Apple): LZFSE codec ref impl. reusable per license.
- NOT for encode: python-aea / ipsw pkg/aea (AEA-side only, decode-leaning); zmanager (framework wrapper, low value).
- wall: independent derivation still required (FIREWALL posture note); licenses govern reuse, wall governs provenance. never port; compare bytes vs oracle.
