# VERIFY-956cb83: PASS (stored-verbatim check + 4 cells, additive, honest)

- scope first-hand: ravframe.py +50/-12 (--raw flag + verbatim assert + matched verdict),
  tests +22 (SCELL + 4 cells), pins +16 rows. full read of added lines.
- code: --raw asserts concat(stored payloads)==raw bytes EXACT, skipped-if-compressed (framing
  level, honest conditional); SCELL = CT + CLOSED + f2 + sha + rawmatch pins. seed-random inputs
  (incompressible -> stored expected). stdlib-only, zero oracle/OSS/libcompression in src.
- wall: 0 hits (P009 patterns). /tmp slip self-reported + removed same turn (no lane impact).
  no GATE yet; code PASS, no FLAG.
