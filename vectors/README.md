# vectors

Test vectors live here. Over 1MB stays out (link instead) — with one
recorded exception: `rgram-PINS.csv` (10MB, 55k rows) is committed
intentionally. It pins the full lzraven zeros-N grammar (every N in
scope); regenerating it costs a full compression_tool sweep, so the
file itself is the pin baseline. Do not split or trim it without a
reviewed re-pin commit.

Record generator command + OS version per vector.

## CSV schemas (two shapes, both current — do NOT reformat)

- 3-col (`name,sha256,bytes`): `rawenc-PINS.csv`, `pbze-PINS.csv`.
  One row per battery cell; `name` matches the battery's `PASS <name>`
  line and the `<name>.got.aar` artifact (or the in-band attestation
  log for cells the battery cleans, e.g. `c13`).
- 7-col (`name,check,expect,bytes,generator,os,backend`):
  `ravframe-PINS.csv`, `lzraven-PINS.csv`, `rb2-PINS.csv`,
  `outer2-PINS.csv`, `lzbitmap-PINS.csv`, `rgram-PINS.csv`.
  `check` is `sha` (artifact hash), `str` (verdict string) or `rc`
  (exit code); `expect` is the pinned value. The `os` col is uniform
  `27.2` after the A-19 re-pin (see `docs/VERIFICATION.md`).

`gate-tip.sh` `pinleg` handles both: file match first
(`<name>.got.aar`/`.got.aea` full-sha + bytes), else in-band
`PASS <name> bytes=… sha=…` log attestation with FULL-sha compare.
