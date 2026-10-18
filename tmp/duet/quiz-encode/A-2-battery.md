# A-2 battery entry + tiers (encode side)

## Entry point
- `tests/smoke.sh [workdir]` (default mktemp under $TMPDIR). Backend swap: `BACKEND=<impl-adapter> sh tests/smoke.sh`
- exit 0 all green / 1 any FAIL / 2 harness error. T0 never gated-skips.
- file: lanes/harness-oracle @543bb13 `tests/smoke.sh` 2034B sha256 56d751f9a1b2ca27e3e2cd2c98382b4af454cfb33e3b3cd65b8f96468eff86a2 (own hash). contamination PASS per A-1.

## Tiers (per harness/BATTERY.md)
- T0 smoke: EXISTS. encode-side cells inside: `aar-encode` (lzfse -t1, 2-file toy) + `aea-encrypt` (profile 5, fixed 32-char pw `smoke-test-passphrase-32-chars-ok12`, alg none). expect `PASS aar-encode`, `PASS aea-encrypt`, `SMOKE-GREEN`.
- T1 pinned: DEFINED, NOT FILED. `vectors/PINS.csv` absent. interim pin: `vectors/selfgen/SHA256SUMS` (13 rows, fixtures lane @eeedef2; DRIFT-FAIL binding: shasum -c before every battery, mismatch = HARD FAIL).
- T2 full / T3 holdout / T4 fresh: DEFINED ONLY. no scripts, no corpus generator yet.
- units: named in gate sketch only. no suite yet.

## Encode-side invocation today
- `sh tests/smoke.sh` -> expect `PASS aar-encode`, `PASS aea-encrypt`, `SMOKE-GREEN`
- roll your own pins (gap g5): fixed `-a`, `-b`, `-t 1` per row; record generator cmd + OS + backend in pin row. AAR regen must match pins byte-for-byte; AEA regen compares by decrypt-vs-plaintext, never .aea-vs-.aea (nondet from byte 13, fixtures-lane verdict).
- provenance header = `oracle-adapter.sh probe` + seed + date; verdicts by setdiff vs base, full keys, never eyeball.
