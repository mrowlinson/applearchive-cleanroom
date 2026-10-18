# A-5 framing verdicts (MEASURED, nest + xattr + ns + vol probes, macOS 27.0.1)

## (a) 'T' 12B = u64le sec + u32le nsec. CONFIRMED.
- bed: file utime(ns) forced mtime=1600000000.123456789 -> CTM and MTM both 'T',
  sec=1600000000 ns=123456789 EXACT (parser-verified, archive end-to-end EXACT).
- second confirm: root MTM ns=801965257 == stat st_mtime_ns ...801965257 EXACT.
- S-vs-T rule: nsec==0 -> 'S' (u64le sec, 8B, NO len prefix); nsec!=0 -> 'T' (12B).
  evidence: touch -t file (nsec 0) uses 'S' both stamps; all live-nsec entries use 'T'. 8/8.
- correction to your NOTE-2: 'S' has no u16 len (kind + 8B direct). 'P'/'A' take u16le len; '1' 1B; '2' u16le.

## (b) 'A' payload rule: per-entry headers-then-payloads, field order. CONFIRMED + BOUNDED.
- each entry: header (fields) then its own 'A' values in FIELD order, then next AA01.
  5/5 two-A entries: DAT payload first, XAT payload second (DAT field precedes XAT field).
- >2 'A' fields: NOT OBSERVED. only DAT + XAT exist as 'A' carriers; extra xattrs fold
  INTO the single XAT value (bed: 2 added xattrs -> XAT len 101 = 36 + 29 + 36, still one field).
- XAT value shape (bedded): provenance record 36B (u32 0x24 + name NUL + 11B blob) then per-xattr
  records (u32 total-len + name NUL + raw value). record lens VERIFIED: 0x1d=29, 0x24=36.

## (c) 11B blob `01 02 00 66 97 d0 7a bb 10 2c 73`: constant across 20+ entries.
- varied with NO change: content (0/5/16/20/2000B), mtime (2020 touch/live/ns-forced),
  name (5 names), entry kind (dir/file/symlink/subdir), xattr count (0/2), volume
  (internal SSD repo worktree vs external NVME), wrapper (raw inner == stored outer inner).
- OPEN: uid variation (single-user box; chown needs root), host variation (single box).
  verdict: treat as CONSTANT; writer emits these exact 11B. file Q if uid/host bed needed.

## (d) entry kinds: your M/X/P theory is WRONG. CORRECTED.
- byte after AA01 is u16le TOTAL HEADER SIZE (includes 6B magic+size prefix), not a kind.
  proof: 10/10 entries across 4 archives parse EXACT end-to-end with size rule
  (sizes 77/80/93/80/85/97/88/82/98/99 — vary with path/field content; two files in
  one archive got DIFFERENT bytes, impossible for a type marker).
- entry TYPE = TYP'1' 1-byte value (not 2B: the 'P' you read as second byte starts "PAT"):
  'D' dir, 'F' file, 'L' symlink (bedded: link1 -> TYP 'L' + NEW key LNK'P' carrying target "f.bin").
  full set beyond D/F/L: OPEN (need fifo/socket/device/char/block probes; man lists b c d f l m p s).
- PATH: PAT'P' carries path RELATIVE to archived root, "" for root ("sub/deep/g.txt" bedded).
- entry ORDER (observed, nest.aar): root, f.bin, link1, sub, deep, g.txt. ordering rule OPEN
  (readdir order suspected; NOT sorted: f.bin < link1 < sub alphabetically coincides — need adversarial names).
- LNK key: symlink target as 'P' string. symlink has NO DAT field (bedded).

## Parser cross-check
- throwaway dirty-side parser (WS tmp/aar-parse.py, never crosses): 5/5 archives end-to-end EXACT
  (nest 754, xattr 322, ns 244, hello-raw 2445, bed-empty 113) under: size rule + kinds 1/2/P/S/T/A.
