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

5/5 runs: tree COMPLETE, process never exits (killed 15-50s).
Hang point mapped: data+mode+mtime applied for ALL entries (2020
mtime honored on reg file); xattr pass runs in ARCHIVE ORDER and
blocks AT the fifo (open-based apply): pre-fifo entries HAVE xattrs
(FIRSTTAG verified), fifo + later entries LACK them (FIFOTAG/DIRTAG
absent at kill). Archive DOES carry fifo XAT (XATlen 64 measured).
Decoder = completed behavior: all xattrs applied, exit 0, no hang.
PRINCIPLED divergence: never bake kill-truncated state into the
deliverable (matches oracle on every archive where oracle exits).

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

## Full TYP census (256/256 crafted flips, oracle decode)

248 values: silent skip, exit 0, continue. Non-baseline only:
B/C device-no-DEV abort; D-on-file creates dir; F normal; H link
(see below); L-no-LNK aborts ("link entry has no LNK field");
P-with-DAT hangs (same as real fifo); S loud-skip exit 1.
Decoder mirrors all 8 classes (verified matrix + battery cells).

## H hardlink-by-path (TYP 72, LNK key)

H + LNK=archive-relative-path -> link(2) to that path; entry's own
DAT IGNORED; meta NOT applied (mode600 probe: target mode kept).
Forward refs work: oracle runs "process hlinks" post-pass after all
entries, before deferred dir-meta (dir mtime = archived MTM).
H-no-LNK: loud ABORT exit 1, stop (like B). H failures in post-pass:
exit 1, others already extracted. LNK must be archive-relative +
existing REGULAR file, else exit 1 ("invalid 'H' LNK" for abs/escape;
"'H' LNK not a regular file" for missing/dir). H-target matrix
closed: reg ok; symlink rejected (lstat-based, exit 1, tree MATCH);
fifo: oracle hangs (Q1) with h-to-fifo ABSENT at kill = consistent
with reg-only rule. Minimal TYP/PAT/LNK-only items parse + extract
on oracle (L verified). No natural H vector observed (encoder emits
HLC groups); all H evidence crafted.

## PAT escape parity

PAT `../evil-...`: oracle exit 1 "Invalid entry path...stream
cancelled", aborts (later entries skipped), no escape artifact.
Decoder safe_join abort exit 1, same partial tree. MATCH.

## Open (viewer Q-012/Q-013)

B/C-with-DEV shape + behavior (needs root); whiteout kind (if any);
device-restore parity. Decoder fail-closed on DEV-present (exit 1).
