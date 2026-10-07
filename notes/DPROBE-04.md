# DPROBE-04 special file types + oracle fifo quirks (writer-measured)

All black-box: oracle executed via harness adapter, I/O observed.
No binaries opened, no disassembly. 2026-10-07.

## TYP values (uint-w1, ASCII letters)

| TYP | kind | oracle encode | oracle extract |
|-----|------|---------------|----------------|
| D 68 | dir | records | mkdir + deferred meta |
| F 70 | reg | records + DAT | write + meta |
| L 76 | symlink | records + LNK | symlink + meta |
| P 80 | fifo | records, NO DAT (never reads content) | mkfifo + meta, then HANGS (quirk Q1) |
| S 83 | socket | records, NO DAT | LOUD SKIP exit 1, continue ("not implemented yet...N entries failed") |
| B 66 | block dev | n/a (needs root) | B-no-DEV: LOUD ABORT exit 1, STOPS ("YAA device entry has no DEV field") |
| Z/Q/NUL/FF | unknown | n/a (crafted) | SILENT SKIP exit 0, continue (4/4 measured) |

## Quirk Q1: `aa extract` hangs on fifo-bearing archives

2/2 runs: tree COMPLETE (fifo 0644 + siblings), process never exits
(killed at 50s, 15s). Decoder mirrors tree + meta, exits 0, no hang.
Documented divergence: exit/hang behavior only, never tree bytes.

## Quirk Q2: `aa archive` opens fifos blocking

fifo-only tree: encode hangs >60s (2/2). Control (reg-only): 0.0s.
With feeder thread supplying a writer, encode completes fast and
records metadata-only P entry (content discarded; EPIPE observed =
reader closed w/o reading). Battery pins fifo fixture bytes
(vectors/selfgen/aar/fifo-mixed.aar) instead of live-regenerating.

## HLC hardlink groups (see NOTE-014/015)

HLC = uint group id (0,1..; solo files lack key); all members carry
full DAT; oracle links post-extract. Decoder: first member writes,
rest link(2) to first; meta applied per member (idempotent).

## Open (viewer Q-012/Q-013)

B/C-with-DEV shape + behavior (needs root); whiteout kind (if any);
device-restore parity. Decoder fail-closed on DEV-present (exit 1).
