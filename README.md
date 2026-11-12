# applearchive-cleanroom

A from-scratch, byte-identical replacement for Apple's `aa` and `aea`
command-line tools. Create, read, and list AppleArchive (`.aar`)
archives and encrypt/decrypt AEA blobs — with output bit-for-bit
identical to Apple's own tools. No Apple code inside: written purely
from observing what the tools do.

## Features

- **Archive and extract** directories as `.aar` with all 7 AppleArchive
  algorithms: lzfse, lzma, lzraven, zlib, lz4, lzbitmap, raw.
- **List** archive contents without extracting.
- **Encrypt and decrypt** AEA blobs with all 6 profiles
  (password, key, and asymmetric profiles).
- **Identify** AEA blobs (`aea-id`).
- **Byte-identical output**: for every supported operation, our bytes
  match Apple's bytes exactly — verified cell-by-cell against the real
  tools (see Verification below).
- **Honest failures**: operations outside the supported envelope exit
  with a clear error instead of wrong bytes, always.

## Install

Prereqs: macOS with Xcode command-line tools (`cc`), Homebrew `xz`
(pinned liblzma for lzma encode), and `python3` (batteries only).
Apple's `/usr/bin/aa` and `/usr/bin/aea` are only needed to run the
verification batteries, not to use the tools.

```sh
git clone https://github.com/mrowlinson/applearchive-cleanroom.git
cd applearchive-cleanroom
make                        # builds ./build: aad aae aae-cli aeadc rgramc
make OUTDIR=$HOME/aa-build  # or pick your own dir; all 5 land together
```

No runtime dependencies beyond macOS system libraries: no Python, no
pip packages, no environment variables. The CLI finds its backends
beside itself (`AAD_BIN`/`AAE_C`/`AEAD_C` override when set).

## Usage

One entry point, `build/aae-cli`:

```sh
CLI=build/aae-cli
# archive a directory (pick any of the 7 algorithms)
$CLI aar-encode --alg lzfse [--block 4m] [--threads 4] SRCDIR OUT.aar

# extract an archive
$CLI aar-decode IN.aar OUTDIR

# list contents
$CLI aar-list IN.aar

# encrypt (all 6 profiles)
$CLI aea-encrypt --profile 5 [--alg A] [--block S] IN OUT

# decrypt (password, hex key, or profile-appropriate key material)
$CLI aea-decrypt --password PW IN OUT

# identify a blob
$CLI aea-id IN
```

Exit codes: 0 ok, 1 operation failure, 2 usage error or unsupported
operation. Full contract: [harness/CLI-CONTRACT.md](harness/CLI-CONTRACT.md).

## How it works

Pure C top to bottom: the CLI dispatcher, all 7 encode paths, all 7
decode paths, and all 6 AEA profiles. Beside it sits the Python
reference implementation it was ported from — every C port had to
prove byte-parity (port == prototype == Apple oracle) before it
counted. The lzraven codec grammar alone is 110,000+ pinned behavior
cells covering every input length 0..390836.

Everything was derived black-box: feed Apple's tools inputs, record
outputs, implement to the observations. See
[docs/FIREWALL.md](docs/FIREWALL.md) for the cleanroom rules.

## Compatibility notes

- Output is byte-identical to Apple tools on macOS 27.x for all
  covered operations.
- lzraven general compressible inputs: supported through the closed
  grammar; anything outside it errors cleanly.
- lzbitmap: narrow parity class (empty + pure-random inputs); all other
  inputs are refused with a clear error rather than approximated.
- AEA encryption is salted (nondeterministic like Apple's): decrypts
  anywhere Apple's blobs decrypt; byte-compare applies to pinned
  vectors only.

## Layout

```
src/c/cli.c          unified CLI (C; `src/aae-cli` = Python reference)
src/aad.c            decode (C)
src/c/               encode + codec ports (C)
src/*.py             encode reference (Python)
proto/               decode mirror + AEA (Python)
harness/             CLI contract + test adapters
tests/               batteries (see Verification)
vectors/             pinned behavior cells + self-generated vectors
spec/ notes/ docs/   derived behavior clauses, experiment records, research
```

## Verification

Every claim above is gated by a battery that diffs our bytes against
Apple's tools on this machine (macOS 27.2). Current master HEAD:

| Battery | Result |
|---|---|
| every input length 0..390836, oracle + impl | 390837/390837 CLOSED, 0 bad |
| behavior pins (`test_rgram_fast.py`) | 110544/110544 |
| decode (`c-battery.sh`) | 1069/1069 |
| AEA (`aea-battery.sh`) | 187/187 |
| AEA encrypt + units | 49/49, 14/14 |
| CLI, C (`test_cli.sh` + `CLI_BIN`) | 104/104 |
| CLI, Python reference (`test_cli.sh`) | 78/78 |
| AEA C (`test_aead_c.sh`) | 102/102 |
| lzraven / lzbitmap C (`test_lzraven_c.sh`, `test_lzbitmap_c.sh`) | 64/64, 32/32 |
| lzraven / lzbitmap / lz4 (+full, +C parity) | 64/64, 32/32, 8/8 + 60x3 + 11/11 |
| smoke / units / pbze / rawenc / rb2 / ravframe / outer2 / lzma | all green |

Run them yourself:

```sh
sh tests/c-battery.sh
sh tests/aea-battery.sh
sh tests/test_cli.sh
python3 tests/test_rgram_fast.py <workdir>
```

## Cleanroom note

This repo contains no Apple code, headers, binaries, or transcribed spec text.

Spec sources: [AppleArchive docs](https://developer.apple.com/documentation/applearchive),
[Compression docs](https://developer.apple.com/documentation/compression),
local `aa(1)`/`aea(1)` man pages,
[AEA FORMAT.md](https://github.com/kinnay/AEA/blob/HEAD/FORMAT.md) (MIT),
[lzfse](https://github.com/lzfse/lzfse) (BSD),
[Eclectic Light intro](https://eclecticlight.co/2020/11/24/compress-and-decompress-files-using-applearchive/),
[mac_file_format_docs](https://raw.githubusercontent.com/dgelessus/mac_file_format_docs/HEAD/README.md) (CC-BY-4.0).

Prior art: [python-aea](https://github.com/kinnay/AEA) (MIT),
[lzfse](https://github.com/lzfse/lzfse) (BSD), Archive Utility, `aa`/`aea`.

## License

0BSD (BSD Zero Clause License) — see LICENSE. Public-domain-equivalent:
use, copy, modify, and distribute for any purpose with or without fee,
no attribution required.
