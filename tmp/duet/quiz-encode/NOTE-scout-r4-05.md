# NOTE-scout-r4-05: T2 q8+q9 LANDED (@a13215e)

## Committed (lanes/encode-container@a13215e, LOCAL ONLY, 3 files)
- `tests/container/t2-seeded.sh`: +q8 (16 arch cells -b x
  {lzma,lz4,lzraven,lzbitmap} + framing/census/monotonicity +
  lz4_raw negative + 2 round-trip corners) + q9 (8 cells:
  verify clean/content/missing/added/meta + fix clean/meta-heal/
  data-residue). 28 -> 56 cells.
- `tests/container/README.md` + `vectors/FIXTURES.md` §9: cell
  counts, q8 magic map + geometry, q9 rc contract. G4 now FULLY
  closed (-b sweep full codec matrix + verify/file-corruption
  pairs) for the container battery.
- Hashes-not-bytes honored: code only, zero archive bytes.
  Nothing pushed; master untouched; no map-lane reads.

## First-hand GREEN (NVME r4 scratch, aa macOS 27.0.1)
- T2-SEED7 GREEN 56/56, T3-SEED8 GREEN 56/56 (x2 rerun),
  T0+T1 regression GREEN via test_container.sh gate.
- Two battery bugs caught by the battery itself (fixed before
  landing): cp -R mtime non-preservation (expect stats from
  pristine corpus) + pipe-rc artifact (fix-dirty rc is 1, a
  healed-check — NOTE-r4-04 corrected).

## Queue status
- (1a) kickoff plan filed (r4-03); (1b) wall brief filed (r4-02).
  (2) T2 extensions DONE + landed. (3) v1/v2 trivia: untouched
  (decode need never arrived). (4) CMP donor: none appeared.
- Entering stay-alive polls with claim HELD for r5.
