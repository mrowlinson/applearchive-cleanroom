# harness

Shipped contract + batteries for the finished `aae-cli` deliverable
(single unified C binary, `./build/aae-cli`).

- `CLI-CONTRACT.md`: the one interface oracle + impl share. Backends,
  commands, observed oracle caps, determinism rules, honest-refusal
  policy (exit 2 + marker where the impl subset ends).
- `BATTERY.md`: T0 smoke / T1 pinned / T2 full / T3 holdout / T4 fresh.
  Result files, exit codes, gate sketch.
- `oracle-adapter.sh`: vendor backend. Wraps `/usr/bin/aa` + `/usr/bin/aea`.
- `impl-adapter.sh`: legacy encode-side shim (writer1 era). Now only
  historical: `aar-encode` for raw/lzfse/zlib via `src/encode.py`,
  everything else passes through to the oracle adapter. The shipped
  impl path is `src/aae-cli` (Python reference) and `./build/aae-cli`
  (unified C binary), exercised directly by `tests/test_cli.sh`.

Run: `sh tests/smoke.sh`. Backend swap: `BACKEND=<impl-adapter> sh tests/smoke.sh`.
Full gate: `sh tests/gate-tip.sh <rev> <nvme-outdir>`.
All batteries require `TMPDIR` set to NVME scratch (never `/tmp`).
