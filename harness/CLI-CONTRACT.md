# Harness CLI contract

Goal: 1 interface runs oracle AND impl-under-test. Batteries swap backend, never rewrite checks.

## Backends

- `oracle`: vendor `/usr/bin/aa` + `/usr/bin/aea` via `oracle-adapter.sh`.
- `impl`: shipped cleanroom binary `./build/aae-cli` (unified C) or
  `src/aae-cli` (Python reference; byte-identical contract). Same argv,
  same exit codes, same bytes — except the honest refusals below.

## Commands (all exit 0 = ok, 1 = operation failure, 2 = usage/harness/unsupported; diagnostics to stderr, data to stdout/file only)

```
adapter probe
  Print provenance block (tool paths+sha256, OS, arch, date). No other output.

adapter aar-encode --alg ALG [--block SIZE] [--threads N] SRCDIR OUT.aar
  Vendor: aa archive -d SRCDIR -a ALG [-b SIZE] [-t N] -o OUT.aar
  NOTE: dir-in, not byte-pipe. Vendor limitation. Impl matches same shape.
  SIZE: integer + optional b/k/m/g suffix (aa CLI shape); impl
  lowercase-only (aar-encode/rb2 paths). aea --block keeps its own
  case-insensitive shape (documented, not unified).

adapter aar-decode IN.aar OUTDIR
  Vendor: aa extract -i IN.aar -d OUTDIR

adapter aar-list IN.aar
  Vendor: aa list -i IN.aar. Bytes-in, text-out. Text compared loosely (see BATTERY.md).

adapter aea-encrypt --profile P [profile opts] IN OUT
  Vendor: aea encrypt -profile P ... -i IN -o OUT. True byte pipe (IN/OUT may be - for stdio).
  Flag forwarding (verified wiring): -a/--alg, -b/--block, --checksum,
  --padding, --password/--password-file, --key/--key-value/--key-file,
  --recipient-pub, --sign-priv, --auth-data/--auth-data-value/--auth-data-key.
  --threads accepted, single-threaded (validated int > 0, else exit 2).

adapter aea-decrypt [--password PW|--key HEX|...] [--range-offset N --range-size M] IN OUT
  Vendor: aea decrypt -i IN -o OUT. True byte pipe. Key material must be
  hex:... or base64:... prefixed (oracle rejects bare values in
  -key-value). The Python reference rejects bare values; the C binary
  still auto-prefixes bare hex (known diff, test-gated KNOWN-DIFF,
  patch pending with the C lane).

adapter aea-id IN
  Vendor: aea id -i IN. Bytes-in, text-out. IN may be - (stdin spool via
  TMPDIR temp file; test-only shape, not an oracle argv).
```

## Observed oracle capabilities (macOS 27.2, arm64, `aa -h` / `aea -h`)

- aa algs: lzfse, lzma, lzraven, zlib, lz4, lzbitmap, raw. Defaults: archive `-a lzfse -b 4m`; others `-a lzfse -b 1m`.
- `lzraven` (no prior note). `lzbitmap` CONFIRMED present. OS floor: 27.x
  (pins uniform 27.2 after the A-19 re-pin; see docs/VERIFICATION.md).
- aa threads: default = ncpu. Byte-compare runs pin `-t 1` until parallel determinism measured.
- aea profiles: 0 hkdf_sha256_hmac__none__ecdsa_p256, 1 hkdf_sha256_aesctr_hmac__symmetric__none, 2 ...__symmetric__ecdsa_p256, 3 ...__ecdhe_p256__none, 4 ...__ecdhe_p256__ecdsa_p256, 5 hkdf_sha256_aesctr_hmac__scrypt__none.
- aea algs: same 6 + none (no compression). Default lzfse, block 1m.

## Determinism rules

- Fixed threads, fixed block size, fixed profile per vector. Recorded in pin row.
- Timestamps/xattrs in test dirs: pinned inputs only (generator script committed, output hash-pinned).
- Nondeterminism observed => vector FAILS until cause filed (never re-pin silently).
- AEA encrypt is nondeterministic by design (random salts/MACs).
  Interop parity = oracle decrypts CLI output. Deterministic
  byte-compare lives in `tests/test_aea_enc.sh` via `--fixed-*`
  transplant flags (test-only, no oracle equivalents) — including the
  hidden `aeadc` passthrough used by `tests/test_aead_c.sh`, which
  forwards verbatim to the C `aead_main` so fixed-salt/nmac/smacs,
  stdio positionals and selftest keep byte-identical behavior.

## Out of scope (later lanes)

- `aa convert/manifest/verify/check-and-fix/append/patch` matrix. Adapter gains subcommands when batteries need them.
- Timing protocol. Correctness first; timing gate separate (needs quiet-box rules).

## Impl coverage + intentional differences (landed)

- Impl covers all 7 `aar-encode` algs and all 6 `aea-encrypt` profiles. No parked subset remains.
- Honest refusals (INTENTIONAL difference, with reason): on inputs outside
  the proven-parity class — lzraven unclosed (`LzRavenUnclosed`, e.g. zeros
  runs past scope 820) and lzbitmap match-class (`LzBitmapMatchFound`) —
  the impl EXITS 2 with a marker on stderr (`lzraven unclosed` /
  `lzbitmap match-class`) instead of emitting bytes. The oracle exits 0
  there. Reason: emitting literal/stored bytes on those inputs would
  silently diverge from the oracle's globally-planned grammar; refusal is
  the contract (batteries assert exit 2 + marker, never byte parity).
- Exit-code parity therefore does NOT hold on refusal inputs by design.
- Refusal exit code is 2 at the CLI layer (usage/harness-level error),
  while direct `src/encode.py` exits 1 on the same inputs. Reason: the CLI
  reserves 1 for operation failures per this contract's exit-code rule.
- `aea-encrypt` parity rule is interop roundtrip (oracle decrypts CLI
  output to the input bytes), NOT byte-compare. Reason: encrypt output is
  nondeterministic by design (random salts/MACs); deterministic
  transplant byte-compare lives in `tests/test_aea_enc.sh`.
