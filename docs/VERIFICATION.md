# Verification (headline numbers + exact reruns)

Machine: macOS 27.2 arm64. Oracle: `/usr/bin/aa` + `/usr/bin/aea`.
Every battery requires `TMPDIR` set to NVME scratch
(`export TMPDIR=/Volumes/NVME/<proj>-ws/tmp/<lane>`); `: "${TMPDIR:?...}"`
legs refuse `/tmp` and repo `tmp/`.

## Headline numbers (fix-sweep-PTD gate, 2026-11-12)

| suite | result | rerun |
|---|---|---|
| c-battery | 1073/1073 GREEN | `sh tests/c-battery.sh` |
| smoke | 6/6 GREEN | `sh tests/smoke.sh` |
| test_cli py | 96/96 GREEN | `sh tests/test_cli.sh` |
| test_cli C | 117/117 GREEN (+5 SKIP absent-C-surface, +1 KNOWN-DIFF cli.c:1130) | `CLI_BIN=$NVME/aae-build/aae-cli sh tests/test_cli.sh` |
| test_aea_enc proto | 54/54 GREEN | `sh tests/test_aea_enc.sh` |
| test_aea_enc via C shim | 49/49 GREEN (5 det cells SKIP: no --fixed-* in C aeadc) | `CLI=... AEAD_PY=tests/aeadc-shim.sh sh tests/test_aea_enc.sh` |
| aea-battery | 187/187 GREEN | `sh tests/aea-battery.sh` |
| test_aead_c | 106/106 GREEN (incl. 4 lz4-tail roundtrips) | `CLI=... sh tests/test_aead_c.sh` |
| test_lz4 | GREEN incl. 100k odd-block oracle byte-compare | `sh tests/test_lz4.sh` |
| test_lzraven (+_c) | GREEN | `sh tests/test_lzraven.sh` |
| test_rb2 | GREEN (gate RB2 n=50) | `sh tests/test_rb2.sh` |
| test_ravframe | GREEN (gate RAVFRAME n=183) | `sh tests/test_ravframe.sh` |
| raw-trunc | 143/143 GREEN (full-size + strict rc<=1) | `sh tests/raw-trunc.sh` |
| sweep-decode | pins 18/18 (full verdict pending long run) | `sh tests/sweep-decode.sh` |
| aea-sweep | 320/320 GREEN, hang=0 | `sh tests/aea-sweep.sh` |
| test_units | GREEN | `python3 tests/test_units.py` |
| test_aead_units | 14/14 OK | `$AEAD_PY tests/test_aead_units.py` |
| test_rgramc_fast | RED (pre-existing py/C divergence, 35249 cells; floor 46745/55272 recorded) | `python3 tests/test_rgramc_fast.py` |
| test_rgram | partial, 0 fail at handoff (full sweep is hours-long) | `sh tests/test_rgram.sh` |
| gate-tip | see legs below | `sh tests/gate-tip.sh <rev> <nvme-outdir>` |

Build the C binary first (all C legs):
`make OUTDIR=$NVME/aae-build` (repo `Makefile`, in-tree `build/` never used).

## 27.2 provenance (D3 re-gate)

- 2026-11-04 re-gate (lane T40a): decode batteries re-ran on macOS 27.2,
  `vectors/rgram-PINS.csv` `os` column uniform `27.2` (verified
  `cut -d, -f6 | sort -u` = `os,27.2`); all other pins held byte-identical.
- This sweep re-verified on 27.2 (`sw_vers` 27.2): c-battery 1073/1073,
  oracle byte-compares green across lz4/lzma/rb2/ravframe/rawenc/pbze.
- New pin rows added this sweep carry `os=27.2`
  (`r-err-*` in rb2-PINS, `e12-*` in ravframe-PINS).

## gate-tip legs (rev-gated; pre-existing reds stay red)

- PASS: HYGIENE (vectors/*.aar exempt as intentional pins), GITIGNORE,
  C-BUILD, RAWENC/PBZE/LZMA/SMOKE/OUTER2/RB2/RAVFRAME batteries + C
  variants, PINS file+attestation (FULL-sha), PINSET set-eq, OSS, UNITS.
- PENDING (by design): SMOKE-IMPL2 (no impl2 backend — documented, not resurrected).
- FAIL pre-existing (not this lane; C-lane/quiz-owned):
  CONTAM (spec/ viewer docs trip the marker grep),
  LIBCOMPRESSION (src C + lzbitmap `compression_*` use vs A-12 REFUSE —
  needs quiz grant; none of the hits are this lane's files),
  ADOPT WARN (lane diff), AEA-BIN WARN (committed .aea fixtures by design).
- FAIL fixed this lane, verified on final gate run: PINS-RB2/PINS-RAVFRAME
  set-eq (new cells now pinned: 50/50, 183/183), C-BUILD TMPDIR wipe race
  (export moved after `rm -rf $OUT`), RAWENC-C/PBZE-C (gate now exports
  LZFSE_DYLIB; PBZE-C 10/10, PINS-PBZE-C 10/10).

## Canonical strings (cross-language, byte-compared in test_cli.sh)

- `aae-cli: aar-encode --alg <alg>: invalid block size: <raw>` exit 2 —
  all invalid blocks (unparsable incl. uppercase, out-of-range, overflow),
  Python `src/encode.py` and C `cli.c` emit identical bytes (C via
  `die_msg` prefix).
- Refusals: exit 2 + marker (`lzraven unclosed`, `lzbitmap match-class`).
