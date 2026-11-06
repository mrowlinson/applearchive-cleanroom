# Harness CLI contract (DRAFT, wave 1)

Goal: 1 interface runs oracle AND impl-under-test. Batteries swap backend, never rewrite checks.

## Backends

- `oracle`: vendor `/usr/bin/aa` + `/usr/bin/aea` via `oracle-adapter.sh`.
- `impl`: future cleanroom binary. Same argv, same exit codes, same bytes. UNRESOLVED until JOBS #1 decides goal.

## Commands (all exit 0 = ok, nonzero = fail; diagnostics to stderr, data to stdout/file only)

```
adapter probe
  Print provenance block (tool paths+sha256, OS, arch, date). No other output.

adapter aar-encode --alg ALG [--block SIZE] [--threads N] SRCDIR OUT.aar
  Vendor: aa archive -d SRCDIR -a ALG [-b SIZE] [-t N] -o OUT.aar
  NOTE: dir-in, not byte-pipe. Vendor limitation. Impl matches same shape.

adapter aar-decode IN.aar OUTDIR
  Vendor: aa extract -i IN.aar -d OUTDIR

adapter aar-list IN.aar
  Vendor: aa list -i IN.aar. Bytes-in, text-out. Text compared loosely (see BATTERY.md).

adapter aea-encrypt --profile P [profile opts] IN OUT
  Vendor: aea encrypt -profile P ... -i IN -o OUT. True byte pipe (IN/OUT may be - for stdio).

adapter aea-decrypt [key opts] IN OUT
  Vendor: aea decrypt -i IN -o OUT. True byte pipe.

adapter aea-id IN
  Vendor: aea id -i IN. Bytes-in, text-out.
```

## Observed oracle capabilities (macOS 27.0.1, arm64, `aa -h` / `aea -h`, 2026-10-07)

- aa algs: lzfse, lzma, lzraven, zlib, lz4, lzbitmap, raw. Defaults: archive `-a lzfse -b 4m`; others `-a lzfse -b 1m`.
- NEW vs RESEARCH.md: `lzraven` (no prior note). `lzbitmap` CONFIRMED present (was single-sourced; OS floor still UNRESOLVED).
- aa threads: default = ncpu (18 here). Byte-compare runs pin `-t 1` until parallel determinism measured (UNRESOLVED).
- aea profiles: 0 hkdf_sha256_hmac__none__ecdsa_p256, 1 hkdf_sha256_aesctr_hmac__symmetric__none, 2 ...__symmetric__ecdsa_p256, 3 ...__ecdhe_p256__none, 4 ...__ecdhe_p256__ecdsa_p256, 5 hkdf_sha256_aesctr_hmac__scrypt__none.
- aea algs: same 6 + none (no compression). Default lzfse, block 1m.

## Determinism rules

- Fixed threads, fixed block size, fixed profile per vector. Recorded in pin row.
- Timestamps/xattrs in test dirs: pinned inputs only (generator script committed, output hash-pinned).
- Nondeterminism observed => vector FAILS until cause filed (never re-pin silently).

## Out of scope (later lanes)

- `aa convert/manifest/verify/check-and-fix/append/patch` matrix (JOBS #8/#9). Adapter gains subcommands when batteries need them.
- Timing protocol. Correctness first; timing gate separate (needs quiet-box rules).

## Impl coverage + intentional differences (cli-wireup lane)

- Impl (`src/aae-cli`) now covers all 7 `aar-encode` algs and all 6
  `aea-encrypt` profiles. No parked subset remains.
- Honest refusals (INTENTIONAL difference, with reason): on inputs outside
  the proven-parity class — lzraven unclosed (`LzRavenUnclosed`, e.g. zeros
  runs past scope 820) and lzbitmap match-class (`LzBitmapMatchFound`) —
  the impl EXITS 2 with a marker on stderr (`lzraven unclosed` /
  `lzbitmap match-class`) instead of emitting bytes. The oracle exits 0
  there. Reason: emitting literal/stored bytes on those inputs would
  silently diverge from the oracle's globally-planned grammar; refusal is
  the contract (batteries assert exit 2 + marker, never byte parity).
  Exit-code parity therefore does NOT hold on refusal inputs by design.
- Refusal exit code is 2 at the CLI layer (usage/harness-level error),
  while direct `src/encode.py` exits 1 on the same inputs. Reason: the CLI
  reserves 1 for operation failures per this contract's exit-code rule.
- `aea-encrypt` parity rule is interop roundtrip (oracle decrypts CLI
  output to input bytes), NOT byte-compare. Reason: encrypt output is
  nondeterministic by design (random salts/MACs); deterministic
  transplant byte-compare lives in `tests/test_aea_enc.sh`.
