# DPROBE-06 oracle extract phase model (writer-measured, 20 probes)

All black-box: oracle executed via harness adapter, I/O observed.
No binaries opened, no disassembly. 2026-10-07 (successor shift).

## Phase order (print order; all probed)

1. create, FORWARD. Aborts (no-TYP wrapper, L-no-LNK, B-no-DEV,
   bad path, mkdir/open/write fail) stop creation ONLY; H-pass,
   meta, flushes, summary still run (P4/HAB/SAB).
   - F without DAT key: skip + continue, recorded, flushed
     later (nodat craft; "final state" line, NO count).
   - F open EISDIR (incl PAT-empty F vs outdir): immediate
     3-line shape (header 0xc305ac15 + L1 basename + L2 abs +
     opening-line), COUNTED, continue (epf2 + arg variants).
   - S / B-with-DEV: recorded (forward), NO print yet.
   - D PAT-empty = ROOT item (real; encoder emits): meta
     target = outdir (marker/MOD/MTM all applied).
   - L/P PAT-empty, PAT-missing items: skipped (UNPROBED).
2. files meta, strict REVERSE (bad2 print; Q1 kill-state:
   archive-last mtime applied, fifo pending). Per entry:
   xattr -> chmod -> chown -> MTM -> CTM (xattr-first forced
   by MOD566+marker: oracle HAS marker+566).
   - XAT fail: header 0xe8012000 + "invalid XAT blob" x2 +
     "applyEntryAttributes failed: <pat>", COUNTED, rest
     SKIPPED (mx: mode stays default), continue.
   - XAT strict incl trailing bytes (mk566a accident).
3. S-flush, FORWARD (S2). Bare iff header already printed.
4. F-no-DAT flush, FORWARD (nh2: after S, before H).
   Header 0xc8039000 first-wins.
5. H pass, forward (runs even on abort per HAB). Fail detail
   lines uncounted; header 0xc8104800 first-wins; trailer
   "process hlinks" IFF any H-fail (valid silent).
6. dirs meta, REVERSE = children-first (root item0 lands
   last). XAT fail: triple + "applyEntryAttributes failed"
   (NO path), UNCOUNTED, continue (2-bad-dirs), dirfail=1.
7. "process dirs" trailer IFF dirfail (after H, before count).
8. "N entries failed to extract" IFF sfails (S + XAT-file +
   EISDIR share ONE counter; E4 "2"; H/nodat/dirXAT excluded).

## Headers: first "Error 0x" wins globally per run

0xbd03ac00 no-TYP (inside 5-line wrapper, byte-stable 8/8) /
0xc8055000 S / 0xe8012000 XAT / 0xc8039000 final-state /
0xc8104800 H / 0xc305ac15 EISDIR. Later classes print bare.

## Oracle's own races (unmatchable byte-wise; SET parity only)

- Multi-XAT-error print order races (bad2: 2/5 vs 3/5 runs).
- Multi-S stanzas can interleave mid-stanza (threads share
  stderr). Exit + tree + token-SET + count stay deterministic.

## Corrections to prior notes

- DPROBE-04 "xattr pass runs in ARCHIVE ORDER": REFUTED
  (kill-state + archived values force reverse; its FIRSTTAG
  archive must have had fifo-first order).
- DPROBE-04 skipped "process hlinks"/"process dirs" trailers:
  now mirrored (iff-fail rule) + cells.
- com.apple.provenance is AMBIENT (mkdir has it): presence
  asserts require markers (xo/rootm cells use markers).

## Open assumptions (documented; fuzz judges)

- L-no-LNK/B-no-DEV/bad-path/mkdir/open(non-EISDIR) aborts
  set header-flag (only no-TYP proven via SAB).
- Dirs-phase continues past failures (print order within
  unobservable: no paths; 2-fail proven).
- Unknown-TYP/S/B-with-DEV XAT never validated (E1/E2:
  skipped, no object).
- H entries' own XAT never validated (no meta per DPROBE-04).
- EISDIR immediate (not collected); non-root EISDIR paths
  follow the same basename/abs rule (root-case pinned).
- Rest-after-XAT-fail skipped for DIRS too (files pinned
  by mx; dirs assumed uniform).
