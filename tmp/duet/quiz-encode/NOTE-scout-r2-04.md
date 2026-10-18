# NOTE-scout-r2-04: survey leg — HLC closed, h-verdict, links, omanifest

## HLC synthesis CLOSED (cpio path, all black-box, macOS 27.0.1)
- `aa convert -i hardlink.cpio -o h.aar` (rc=0): nlink=2 pair ->
  two TYP F entries carrying HLC=0 (shared cluster id) + INO (shared
  source inode) + NLK=2, plus IDX (per-entry offsets 250/599) +
  IDZ=99 shared. cpio entries lack CTM/FLG/XAT (no such source
  metadata); MTM present. Pax AppleDouble `._` sidecars archived as
  plain F (no HLC).
- `-ignore-cpio-hlc` honored: HLC 0/4 (flag does what help claims).
- Extract RESTORES hardlinks (both paths, same inode) — full loop:
  cpio NLINK -> HLC cluster -> disk hardlinks. Container battery
  needs a cpio-convert HLC vector + inode-equality leg (T2).
- HLC is convert-sticky (F+HLC survives convert->raw, TYP stays F)
  but NOT archive-forceable: `archive -include-field HLC` on a live
  nlink=2 pair emits NO HLC (unlike SLC). HLC synthesis lives ONLY
  on the cpio-convert path. r1's "nlink=2 -> two F + dup DAT"
  reconfirmed (this is hl-arch.aar, no-hlc).

## TYP h VERDICT: parse-vocabulary, never locally emitted
- h unobserved via EVERY local path: archive nlink=2 (plain +
  -include-field HLC), cpio convert (+- ignore flag), convert of
  F+HLC archives. Hardlink clusters encode as F+HLC, never TYP h.
- Verdict: `h` is in aa's PARSEABLE type vocabulary (`-h` list) but
  no local ENCODE path emits it. Container decode MUST parse TYP h
  (foreign/hand-crafted acceptance probe still open); container
  encode never emits it. h half of TYP 9-vs-11 CLOSED as
  emit-negative; m half still open (no M in verb-manifests per r1;
  -omanifest probe below found no M either — no omanifest at all).

## -omanifest: accepted-but-silent (OPEN, container lane owns)
- `aa convert -a {raw,lzfse} -omanifest PATH ...` rc=0 but WRITES NO
  FILE either time. Trigger unknown (stdin-input? append-path?
  compressed-input?). No IDX/IDZ-via-omanifest pair obtainable this
  run; IDX/IDZ observed instead on the cpio-convert path (above).

## Link re-verify (curl, 2026-10-15)
- Apple-404 HOLDS (github.com/apple/apple-archive HEAD 404 — wall
  posture unchanged; cleanroom derivation still the lane).
- 200: 0xilis/libNeoAppleArchive, kinnay/AEA, eafer/libzbitmap.
- theapplewiki Apple_Archive: 403 via curl HEAD+GET (was 200 in r1
  via fetch) — bot-guard fluctuation, NOT a dead-link claim.
- Self-correction: an early guessed owner URL for libNeo 404'd; that
  was my malformed guess, not evidence — real URL recovered from L3
  (0xilis, read-only) and re-verified 200 above.

## Still open in survey leg
- compression_tool framing vs pbz* outer: NOT bare codec (decode of
  payload-after-magic FAILED; `bvxn` block magic at offset 28,
  header = pbze + u64 0x4000 + more framing). Slice-decode probes
  (20/24/27/28) queued — shell backpressure stalled this run.
- m/YAF source; W/R/T parse-only acceptance; CMP key still
  single-sourced; YAA1 handling.
