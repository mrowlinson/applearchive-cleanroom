# harness

L6 wave-1 deliverables. Scaffolding only; no decoder code (JOBS #1 still OPEN).

- `CLI-CONTRACT.md`: 1 interface for oracle + impl. Backends, commands, observed oracle caps, determinism rules.
- `BATTERY.md`: T0 smoke / T1 pinned / T2 full / T3 holdout / T4 fresh. Result files, exit codes, gate sketch.
- `oracle-adapter.sh`: working vendor backend. Wraps `/usr/bin/aa` + `/usr/bin/aea`.
- `../tests/smoke.sh`: T0 skeleton. 2 cells, no pins.

Run: `sh tests/smoke.sh`. Backend swap: `BACKEND=<impl-adapter> sh tests/smoke.sh`.
