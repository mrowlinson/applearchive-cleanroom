# applearchive-cleanroom

Independent cleanroom reimplementation of AppleArchive (AAR archives,
AEA encrypted blobs): behavior-identical to Apple's `aa(1)`/`aea(1)`
from black-box observation only. No Apple code, headers, binaries, or
transcribed spec text in this repo.

Status date: 2026-11-06. Everything below is master HEAD. **Finished:
all batteries green, CONTIG-390836 proven.**

## What it is

- `src/aae-cli` — unified impl-only CLI: `aar-encode`, `aar-decode`,
  `aar-list`, `aea-encrypt`, `aea-decrypt`, `aea-id`. Zero oracle
  passthrough (contract: [harness/CLI-CONTRACT.md](harness/CLI-CONTRACT.md)).
- Decode: C (`src/aad.c`) + Python mirror (`proto/aad.py`), all 7
  algorithms, thread-shape + writer TIPs.
- Encode: Python reference (`src/encode.py` + codec modules) + C port
  (`src/c/aae.c`, `lz4c`), PBZE/RAWENC/OUTER2/RB2/RAVFRAME framing.
- AEA: all 6 profiles, encrypt + decrypt + archive-id (`proto/aead.py`).
- lzraven zeros-N grammar (`src/rgram.py`): contiguous CLOSED coverage
  N 0..390836, proved by exhaustive first-hand sweep.

## Verification (master HEAD, this machine)

| Battery | Result |
|---|---|
| rgram CONTIG sweep (every N 0..390836, oracle + impl) | 390837/390837 CLOSED, 0 bad |
| rgram pins (`test_rgram_fast.py`) | 110544/110544 RGRAM-GREEN |
| decode C battery (`c-battery.sh`) | 1069/1069 |
| AEA battery (`aea-battery.sh`) | 187/187 |
| AEA encrypt (`test_aea_enc.sh`) + aead units | 49/49, 14/14 |
| CLI (`test_cli.sh`) | 74/74 |
| lzraven-enc / lzbitmap / lz4 (+full, +C parity) | 64/64, 32/32, 8/8 + 60x3 + 11/11 |
| smoke / units / pbze / rawenc / rb2 / ravframe / outer2 / lzma | all GREEN |
| encode proto gates | 9/9 |

GREEN = every cell byte-matched against the Apple oracle; pins held
(`vectors/rgram-PINS.csv`: 110544 rows, uniform macOS 27.2).

## Quickstart

Prereqs: macOS with `/usr/bin/aa`, `/usr/bin/aea`,
`/usr/bin/compression_tool` (black-box oracles), `cc`, `python3`.
AEA paths need `cryptography` + `lz4` (`uv run --with lz4
--with cryptography ...`). LZFSE encode cells use OSS liblzfse via
`$LZFSE_DYLIB`. Keep scratch on fast local disk
(`export TMPDIR=<workspace>/tmp`), never in the repo.

```sh
# decode battery + AEA battery + CLI battery
sh tests/c-battery.sh
sh tests/aea-battery.sh
sh tests/test_cli.sh

# rgram grammar battery (fast gate; .sh form is the same cells, slower)
python3 tests/test_rgram_fast.py <workdir>

# per-codec encode batteries
sh tests/test_pbze.sh <workdir>
sh tests/test_rawenc.sh <workdir>
sh tests/test_lzraven.sh

# C ports (see src/c/Makefile for output dir)
make -C src/c OUTDIR=<workspace>/build

# unified CLI (impl only, no oracle)
python3 src/aae-cli probe
python3 src/aae-cli aar-list <archive.aar>
```

## Layout

```
src/aae-cli          unified CLI (python3 entry point)
src/aad.c            decode C deliverable
src/c/               encode C port (aae.c, lz4c, rgramc)
src/*.py             encode reference: rgram/pbze/rawenc/rb2/ravframe/
                     lzraven/lzbitmap/lz4enc/lzmaenc/encode
proto/               decode mirror (aad.py) + aead (aead.py) + adapters
harness/             oracle adapter, impl adapter, CLI contract
tests/               smoke + per-codec batteries + c/aea/cli batteries
vectors/             pins + self-generated vectors (generator+OS recorded)
spec/                derived behavior clauses (CR-nnn) + derivation log
notes/               DPROBE-nn experiment records (decode)
docs/                firewall, recon notes, research
```

Python is the reference prototype; C is the deliverable. Ports prove
byte-parity (port == proto == oracle) before they count.

## Known limits (honest, by design)

- lzraven: zeros-N grammar fully closed; general compressible inputs
  and zeros N>820 surface honest errors, not silent divergence.
- lzbitmap: parity class is narrow (empty + pure-random); everything
  else is an exact, tested refusal.
- CLI propagates all refusals as errors (exit 2), never silent output.
- AEA encrypt is nondeterministic (salt): interop round-trip, not
  byte-compare, except pinned p1/p5 vectors.
- AEA 0-7B `Invalid password` KDF layer: documented divergence.

## Cleanroom firewall

Wall = vendor-published docs + black-box execution only. Questions
behavior-only (what does it output for X). Answers derived (beds +
numbers + verdicts), never transcribed. Disassembly, teardowns, and
patents were forbidden to implementers. Full rules:
[docs/FIREWALL.md](docs/FIREWALL.md).

Posture note: Apple has NOT open-sourced AppleArchive.
`github.com/apple/apple-archive` returns 404 (verified 2026-09-29).
Only the LZFSE codec is open (BSD). If an Apple source drop appears
later, posture changes; re-survey first.

## Spec inventory (links fetch-verified 2026-09-29)

1. Apple Archive dev docs — <https://developer.apple.com/documentation/applearchive>
2. Compression dev docs — <https://developer.apple.com/documentation/compression>
3. `aa(1)` + `aea(1)` man pages — local, macOS 27.x
4. AEA format doc — <https://github.com/kinnay/AEA/blob/HEAD/FORMAT.md> (MIT)
5. LZFSE reference impl — <https://github.com/lzfse/lzfse> (BSD-3-Clause, (c) Apple 2015-2016)
6. Eclectic Light intro — <https://eclecticlight.co/2020/11/24/compress-and-decompress-files-using-applearchive/>
7. Format-docs collection — <https://raw.githubusercontent.com/dgelessus/mac_file_format_docs/HEAD/README.md> (CC-BY-4.0)

Negative result: `github.com/apple/apple-archive` = 404. Do not cite.

## Prior art

- python-aea (<https://github.com/kinnay/AEA>) — MIT. AEA covered; AAR partial.
- lzfse ref impl (<https://github.com/lzfse/lzfse>) — BSD. Codec only.
- Archive Utility — ships w/ macOS. Partial support.
- `aa` / `aea` CLIs — ship w/ macOS. Black-box oracles.

## Test vectors

In-repo vectors are self-generated via local `aa`/`aea` (black-box)
with generator + OS recorded. Larger corpora stay out (link instead).
Never commit vendor binaries from elsewhere.

## License

0BSD (BSD Zero Clause License) — see LICENSE. Public-domain-equivalent:
use, copy, modify, and distribute for any purpose with or without fee,
no attribution required.
