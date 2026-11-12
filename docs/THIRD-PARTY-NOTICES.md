# Third-party notices

The cleanroom rule: no third-party CODE is vendored in this repo
(formats reimplemented from black-box observation only). The build
links/loads the following third-party ARTIFACTS at build/run time;
their sources and licenses are recorded here (links only — no code
copied).

## Runtime/build artifacts

- liblzma (XZ Utils) 5.8.4 — lzma-encode bytes pinned to this version
  (FORMAT raw-LZMA1-preset-6 lc3lp0pb2 dict-8M + battery).
  License: 0BSD. Source: https://xz.tukaani.org/xz-utils/
  Artifact: Homebrew bottle `xz 5.8.4`
  (`/opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib`,
  sha256 `1b2e12cc1b920264f3dd15eeba22e85b595d8945d1d12a52afa694b09`).
- liblzfse (lzfse) — lzfse-encode path (`dlopen` at encode time via
  `$LZFSE_DYLIB`).
  License: BSD-style, Apple Inc. 2015-2016.
  Source: https://github.com/lzfse/lzfse @
  `e634ca58b4821d9f560cdc6df5dec02ffc93fd`.
- System: `libcompression` / `libz` (macOS system libraries, decode
  path). No notice required; no code copied.

## Read/compare-only references (never linked, never vendored)

- libzbitmap (eafer) — FORMAT + matcher decisions only, hand-written
  impl. License: MIT, Corellium LLC 2022.
  Source: https://github.com/eafer/libzbitmap
- lz4 — behavior beds only (black-box encode/decode compares).
  License: BSD 2-Clause (lib/) + GPL-2.0-or-later (rest).
  Source: https://github.com/lz4/lz4
- kinnay/AEA `FORMAT.md` — AEA behavior reference.
  License: MIT. Source: https://github.com/kinnay/AEA
- mac_file_format_docs — background reading. License: CC-BY-4.0.

Full ledger with pins and nomination history: `docs/OSS-SURVEY.md`.
