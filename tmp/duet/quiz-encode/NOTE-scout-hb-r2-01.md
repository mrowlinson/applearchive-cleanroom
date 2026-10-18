# NOTE-scout-hb-r2-01: T1 generation 6/6 GREEN + SLC trigger resolved

- T1 raw archives (aa macOS 27.0.1, -t 1, `-d in -subdir NAME -a raw`):
  nested/flat50/symlinks/xattr/edges/twins ALL deterministic (regen
  cmp-clean) + round-trip diff-clean. xattr user.scout-tag preserved.
- SLC trigger RESOLVED (r1 P3 confirmed + mechanism): archive-time
  `-include-field SLC` + identical content -> SLC=0 on twins only
  (other.bin unmarked; +10B total = 5B/SLC field). NOT triggered by:
  default archive (any -a/size), clone-extents, convert-time flag.
  convert PRESERVES SLC 2/4 (adds none). NOTE: falsy-printer bug bit
  once (SLC=0 is falsy in `and/or` one-liners) — census via key sets.
- Append shape: `-d edges` w/o -subdir merges at root incl EMPTY-PAT
  '' root entry (16 entries: 8 nested + 8 edges). Real framing edge.
- Quiz inbox: still map-turf only, no scout Qs. Next: manifest pair,
  convert lzfse->raw pair, list-json golden, census, T1 lane commit.
