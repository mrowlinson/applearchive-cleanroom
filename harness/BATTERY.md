# Battery sketch (DRAFT, wave 1)

## Tiers

- T0 smoke (`tests/smoke.sh`). No pins. 2 cells: AAR roundtrip (tiny dir, default alg) + AEA roundtrip (profile 5, fixed passphrase). Pass = exit 0 + payload byte-identical. Seconds.
- T1 pinned (`vectors/PINS.csv`, L5 owns rows). Fixed vector set: 1 minimal .aar per aa alg (7) + 1 .aea per profile (6). Each row: name, sha256, bytes, generator cmd, OS, backend. Drift on re-run = FAIL. Re-pin = committed event with reason, never silent.
- T2 full. Seeded corpus sweep: empty/nested/symlink/xattr/large/sparse/uncompressible dirs × algs. Encode->decode->compare (payload bytes + entry list). Sizes recorded per cell.
- T3 holdout. Disjoint seeds from T2. Same checks. Generalization guard. 0 NEW required at gates.
- T4 fresh. Further disjoint seeds. Ungated frontier. Failures filed, never gate-blocking.

## Result files

- 1 file per run: provenance header (adapter probe output + seed + date) + 1 row per cell (name, status, bytes, sha, ms).
- Verdicts by setdiff vs base run (full keys), never eyeball.

## Text-output cells (aar-list, aea-id)

- Compared normalized (sort lines, strip blank) OR exact once oracle text pinned. Starts normalized; exact pinning when stable.

## Exit codes

- 0 all green. 1 any cell FAIL. 2 harness error (missing tool, bad args). 3 gated-skip (corpus absent; T2+ only, never T0/T1).

## Gate sketch (gates owned by later phase; shape fixed here)

- Ship bar: T0 green + T1 0-drift + T2/T3 0 NEW + units green. T4 informational.
- Impl-vs-oracle: same battery, both backends, setdiff must be empty on bytes cells.
