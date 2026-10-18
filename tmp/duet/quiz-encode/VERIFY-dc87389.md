# VERIFY dc87389 (encode-writer, oldest-first 1/2): PASS with noted gaps

- scope: 7 files, +431. adopted harness 5/5 byte-MATCH vs lanes/harness-oracle (own shasum per file).
- src/rawenc.py (124 lines, own read): framing correct (AA01+u16 incl-6, TYP 1B, PAT/LNK P, UID/GID/MOD/FLG,
  S/T times, DAT A/B, XAT recs, sorted walk, depth-first). battery tests/test_rawenc.sh runs.
- gaps (all pre-A-6, NONE blocking this commit):
  1. CTM=mtime — WRONG on touched files; FIXED in child 2d1ec2d (crtime). superseded, no action.
  2. UID `& 0xFFFF` / GID `& 0xFF` TRUNCATE — must widen 1/2/4 per A-6(b). open vs 2d1ec2d too.
  3. FLG hardcoded 0 — misses hidden/schg per A-6(c). open vs 2d1ec2d too.
  4. LNK len(tgt) counts CHARS (readlink str) — breaks non-ASCII targets. minor, open.
  5. xattr order sorted() — UNVERIFIED vs oracle enumeration order. needs adversarial bed.
  6. B/C/S entries skipped — oracle behavior per A-6(e) (DEV key, no DAT/XAT). gap, not wrong.
- contamination: no vendor/RE markers in own read (black-box ctypes + struct only). PASS.
- verdict: PASS. battery at child commit re-run first-hand 8/8 (see VERIFY-2d1ec2d).
