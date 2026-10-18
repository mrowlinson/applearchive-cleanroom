# NOTE-scout-r1-07: TYP census + manifest key shape (round 8)

## TYP census (oracle-observed, `aa list -list-format json`, -a raw)
CONFIRMED (7): D dir (root + sub), F file (DAT=size), L symlink
(LNK=target), P fifo, B block-dev (DEV key; seen in committed
bdev-basic.aar: DEV 16777216), C char-dev (DEV 50331650; via
-d /dev -i null single-entry mode), S socket (bound unix socket).
All UPPERCASE wire form.
NOT OBSERVED: h hardlink (plain nlink=2 pair archived as TWO F
with duplicated DAT — no dedup, no h trigger found); m metadata
(plain `aa manifest` output has NO M entries — 4 plain D/F);
W/R/T whiteout/door/port (wiki-only; no local creation path —
UNPROBEABLE-locally, treat as foreign-parsed at most).
Score: binary `aa -h` 9-list leads 7-0 over wiki extras (0/3 WRT
observed); wiki table's W/R/T now DOWNGRADED to unconfirmed.

## Behavior edges (battery must-haves)
- fifo archive BLOCKS with no reader (aa opens fifo; hung run
  terminated, reproduced-safe via held RDWR fd). Battery fifo cells
  MUST hold a writer/reader fd or use prebuilt bytes.
- Single-entry mode (-d DIR -i PATH) emits NO root-D wrapper
  (devnull.aar = 1 entry). Framing code must not assume root entry.
- Manifest file-entry keys: CTM FLG GID MOD MTM PAT SH2 SIZ TYP UID
  XAT; DAT absent (alias honored). IDX/IDZ absent in verb-manifests
  (input-archive indexes — expect only in -omanifest convert pairs).

## Open for container lane
- h-trigger (cpio -i path? HLC synthesis?); M/YAF source (check-and-
  fix error-correcting manifests?); W/R/T parse-only acceptance.
