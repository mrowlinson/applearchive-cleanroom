# Battery tiers

## Tiers

- T0 smoke (`tests/smoke.sh`). No pins. 6 cells: AAR roundtrip
  (encode/decode/bytes, default alg) + AEA roundtrip
  (encrypt/decrypt/bytes, profile 5 fixed passphrase). Pass = exit 0 +
  payload byte-identical. Seconds.
- T1 pinned (`vectors/*-PINS.csv` + `vectors/selfgen/SHA256SUMS`).
  Fixed vector set: minimal `.aar` per aa alg, `.aea` per profile,
  codec/frame tables. Each row: name, hash, bytes (+ generator, OS,
  backend on 7-col sheets; see `vectors/README.md` for the 3-col vs
  7-col split). Drift on re-run = FAIL. Re-pin = committed event with
  reason, never silent.
- T2 full. Seeded corpus sweep: empty/nested/symlink/xattr/large/sparse/uncompressible dirs × algs. Encode->decode->compare (payload bytes + entry list). Sizes recorded per cell.
- T3 holdout. Disjoint seeds from T2. Same checks. Generalization guard. 0 NEW required at gates.
- T4 fresh. Further disjoint seeds. Ungated frontier. Failures filed, never gate-blocking.

## Result files

- 1 file per run: provenance header (adapter probe output + seed + date) + 1 row per cell (name, status, bytes, sha, ms).
- Verdicts by setdiff vs base run (full keys), never eyeball.

## Text-output cells (aar-list, aea-id)

- Compared normalized (sort lines, strip blank) OR exact once oracle text pinned. Starts normalized; exact pinning when stable.

## Exit codes

- 0 all green. 1 any cell FAIL. 2 harness error (missing tool, bad args).
- 3 gated-skip: implemented, decode side only (`tests/sweep-decode.sh`
  SWEEP-BASELINE = framework green, no writer cases ran because no
  `WRITER_BIN` was given; tiers without applicable cases report
  `SKIP <reason>` and never contribute to a pass). Never T0/T1.

## Gate sketch (committed gates)

- Ship bar: T0 green + T1 0-drift + T2/T3 0 NEW + units green. T4 informational.
- `tests/gate-tip.sh <rev> <nvme-outdir>`: independent full gate on a
  tree revision. Legs: HYGIENE (no build artifacts; committed
  `vectors/*.aar` fixtures exempt), C-BUILD, batteries
  (rawenc/pbze/lzma/smoke/outer2/rb2/ravframe + C-parity variants +
  SMOKE-IMPL/IMPL2 + units), PINS (file match, else in-band
  `PASS <name> bytes=… sha=…` attestation with FULL-sha compare),
  PINSET (battery PASS set == csv row set), CONTAM (no vendor/disasm
  markers, no Mach-O), OSS (new-dep scan; liblzma 5.8.4 + lzfse
  nominated-only), system-Compression deny (A-12), ADOPT (harness-oracle parity).
- Impl-vs-oracle: same battery, both backends, setdiff must be empty on bytes cells.
