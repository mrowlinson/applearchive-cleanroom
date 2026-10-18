# NOTE-scout-r4-04: T2 extension measurements (q8 codec sweep + q9 rc battery)

## q8: -b sweep x {lzma, lz4, lzraven, lzbitmap} (seed-7 basic/)
- 16/16 `frame-archive` rc=0. Framing: every file walks clean per
  NOTE-r2-06 derived spec (12B header + (0,u,0,c) records,
  end==size). Magic map holds at every -b: lzma->pbzx, lz4->pbz4,
  lzraven->pbzm, lzbitmap->pbzb (payload-confirmed, hb-r4-02).
- Census 16/16: 11 entries D2/F8/L1 via frame-list json.
- Chunk counts codec-independent: 977/16/1/1 for 1k/64k/1m/4m —
  same geometry as q1's lzfse/zlib. Monotonicity
  (1k>64k>=1m>=4m) True on all 4 codecs.
- Round-trip corners: lzma-1k + lzraven-4m extract + treecmp
  IDENTICAL. (Scratch typo produced one TREES-DIFFER on a wrong
  path mid-probe — re-run on the right path IDENTICAL, no signal.)
- lz4_raw: rc=1 usage error reconfirmed (stays a negative cell).

## q9: verify / check-and-fix rc + residue semantics (aa 27.0.1)
Corpus: seed-7 basic/ (11 entries) + frame-xmanifest; verify scope
must match manifest scope (`-d DIR` bare when manifest built on
DIR — a -D split mismatch yields all-REMOVED/ADDED noise, probe
artifact, not a verdict).
- verify clean: rc=0, "11 common, OK".
- verify dirty: content-flip rc=1; removed-file rc=1; added-file
  rc=1; meta-only (mtime+mode) rc=1. Verdict lines name the class:
  DIFFER f (DAT), REMOVED f, ADDED f.
- check-and-fix clean: rc=0, "11 common, OK".
- check-and-fix meta-only dirt: rc=0 AND heals (mtime+mode
  restored to manifest values; re-verify rc=0). Isolated cleanly:
  touch+chmod -> fix -> stat matches -> re-verify green.
- check-and-fix data dirt: rc=1 and does NOT heal — content
  flip still differs, removed file still absent, added file still
  present; re-verify rc=1. Fix rc IS a healed-check: 0 iff the
  post-fix tree matches (clean/meta-healed), 1 iff residue
  remains. (CORRECTION: an early probe read rc=0 through a
  `| tail` pipe — tail's rc, not aa's. Battery pins genuine rcs.)
- RULE (closes r3-04 puzzle): fix scope = metadata-only restore;
  data presence/content/additions are report-only. Battery asserts
  rc + stat + re-verify only — never fix's healing of data.
- Turf note: deeper fix semantics (which meta fields, ignore-field
  interplay) belong to verify lane; q9 pins only the rc + residue
  contract the container battery needs.

## Leg shape (implementing)
- q8 mirrors q1: 16 arch cells + framing/census/monotonicity cell
  + lz4_raw negative + 2 round-trip corners (19 cells).
- q9: verify-clean, verify-content, verify-missing, verify-added,
  fix-meta-heals, fix-data-residue (6 cells). Meta asserts are
  self-relativizing (record -> dirt -> fix -> compare), no
  umask/TZ dependence.
