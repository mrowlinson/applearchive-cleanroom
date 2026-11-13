# Fixtures / vectors / corpora (L5, wave 1)

Status: SEEDED. 19 files, 116KB, all black-box self-generated. Zero vendor bytes committed (own outputs only).

## 1. Local oracle provenance (generators)

- `aa`: /usr/bin/aa, `aea`: /usr/bin/aea, shipped with macOS 27.0.1 (build 26A434), Apple Silicon.
- Binary hashes = L4 owns (vendor-binaries lane). This note pins OUTPUT hashes only.
- Generated: 2026-10-07. All commands below run from repo root unless noted.

## 2. Committed set: vectors/selfgen/

Inputs (regeneration source of truth):
- `input/hello/greet.txt` (58B, text) + `input/hello/repeat.txt` (2000B, `A` x2000).

AAR (13 files):
- `aar/hello-{lzfse,lzma,lzraven,zlib,lz4,lzbitmap,raw}.aar` — same input dir, one per `-a` codec.
- `aar/empty-lzfse.aar` (141B) — empty dir edge case.
- `aar/bdev-basic.aar` (2453B) — block/char device entries.
- `aar/fifo-mixed.aar` (246B) — fifo entry mixed with a regular file
  (oracle HANGS extracting this; decode batteries drain-guard it).
- `aar/hlink-basic.aar` (2467B) + `aar/hlink-missing.aar` (2465B) —
  hardlink pairs, present vs missing target.
- `aar/mix-fail.aar` (2501B) — mixed failure classes for error-shape pins.
- Generator: `aa archive -d <input-parent> -subdir hello -a <codec> -o <out>` (defaults: `-b 4m`, threads default).
- Empty: `aa archive -d <empty-dir> -a lzfse -o empty-lzfse.aar`.

AEA (3 files):
- `aea/hello-p1-nopad.aea` (21065B) — profile 1 symmetric, `-padding none -a none -b 1k`, key = `aea/testkey.bin` (32B: bytes 0x00..0x1F, TEST KEY, committed intentionally).
- `aea/hello-p5.aea` (21065B) — profile 5 scrypt, password `test-password-fixture`, same flags. Plaintext = `aar/hello-raw.aar` in both.
- Generators:
  - `aea encrypt -i vectors/selfgen/aar/hello-raw.aar -o <out> -profile 1 -key vectors/selfgen/aea/testkey.bin -padding none -a none -b 1k`
  - `aea encrypt -i vectors/selfgen/aar/hello-raw.aar -o <out> -profile 5 -password-value 'test-password-fixture' -padding none -a none -b 1k`
- Gotcha (observed): `-key-value <hex>` REJECTED bare 64-hex ("Error parsing key"); `-key <file>` works. External corroboration: aeota README uses `-key-value 'base64:<...>'` (prefixed form). Prefer `-key` files in harness.

Manifest: `vectors/selfgen/SHA256SUMS` (`shasum -a 256`, verify with `shasum -c` from that dir).

## 3. Determinism verdicts (measured, this box)

- AAR: DETERMINISTIC. Regen of hello-lzfse.aar byte-identical (`cmp` clean). Harness regen MUST match pins byte-for-byte.
- AEA: NONDETERMINISTIC from byte 13. Two identical profile-1 runs differ at char 13+ (random salt/IV/nonce region). First 12B stable (`AEA1` + profile LE int + flags?). Pinned .aea bytes = ONE instance. Harness regen rule: decrypt output must equal pinned plaintext; never byte-compare regenerated .aea vs pins.
- Round-trips verified: `aa extract` diff-clean vs input; `aea decrypt` output `cmp`-clean vs hello-raw.aar (profiles 1 + 5).

## 4. Black-box byte observations (feeds JOBS #2/#15, oracle-confirmed)

- Compressed AARs do NOT start with `AA01`. Observed magic per codec: lz4=`pbz4`, lzbitmap=`pbzb`, lzfse=`pbze`, lzma=`pbzx`, lzraven=`pbzm`, zlib=`pbzz`, each followed by 4 zero bytes. Only `-a raw` starts `41 41 30 31` (`AA01`).
- `lzraven` codec exists in `aa -h` (absent from prior research notes). NEW name, oracle-confirmed present.
- AEA: `AEA1` @0, profile as LE u32 @4 (`01 00 00 00` / `05 00 00 00` observed). Bytes 8..11 stable across runs here, 13+ random.
- Sizes (hello input): raw 2445, lz4 444, lzbitmap 365, lzfse 321, lzma 332, lzraven 324, zlib 290. AEA overhead ~19KB fixed at this scale (`-b 1k` vs default identical size: overhead not per-block here).

## 5. External fixture survey (no goldens exist publicly)

1. python-aea `tests/test_aea.py` (fetched 2026-10-07, MIT): 10+ round-trip tests, RANDOM keys/IVs per run, ZERO pinned vectors. One pinned datum: empty SIGNED encode length == 0x13C (their impl, not oracle — do not adopt as oracle pin).
2. lzfse repo `tests/` (API-listed 2026-10-07): single `round-trip.cmake`, no golden vectors. Codec-level only, no AAR container coverage.
3. ipsw (blacktop): pure-Go AEA fallback exists (behavioral corroboration only, wall: never port); no testdata/vectors located. Consumes real OTAs (multi-GB, key-gated) — not fixtures.
4. Apple sample `EncryptingAndDecryptingDirectories` (WWDC21, per dev forums): generates archives at runtime, ships no vectors; download portal-gated. Acquisition candidate for L7 (behavior reference, not bytes).
5. No public AEA/AAR conformance suite found (web search 2026-10-07). Corpus seed = this selfgen set + oracle regen.

## 6. DRIFT-FAIL note (binding on harness, L6)

- `vectors/selfgen/SHA256SUMS` is the pin. Harness MUST `shasum -c` before every battery; ANY mismatch = HARD FAIL, abort run, file incident. No silent re-baseline, ever.
- Oracle moves (OS bump, `aa` update): AAR regen differing from pins = EVENT. Procedure: confirm new oracle version, record old+new pins side by side, owner-visible note, only then re-pin. AEA pins never "re-pinned" by regen (nondeterministic) — decrypt-compare only.
- Growth: new vectors append rows + hashes in the same commit as the bytes. >1MB stays out (link + hash instead, per vectors/README.md).

## 7. Gaps (for L7 acquisition list)

- G1. Real-world `.aar` samples (Xcode-produced, Archive Utility) — breadth beyond synthetic hello/. Owner/acquire.
- G2. Real-world `.aea` with known keys (Simulator OTA small file?) — currently key-gated giants only.
- G3. Apple sample code archive (WWDC21) — portal download, behavior reference.
- G4. Multi-thread/`-b` sweep vectors, manifest/verify corruption pairs (need JOBS #9 scope; harness lane may grow these).
- G5. `aa convert`/`append`/`patch` outputs — UNPROBED, no vectors yet.

Inputs recorded per vectors/README.md: generator command + OS version, above.
