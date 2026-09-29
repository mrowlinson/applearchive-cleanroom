# applearchive-cleanroom

Docs + dirs only. Zero decoder code. Scaffold date: 2026-09-29.

## Goal

UNRESOLVED (see Open questions). Candidate: independent AAR/AEA tooling.
JOBS item 1 tracks the decision. Nothing decided here.

## Non-goals

- No decoder/encoder code in this repo until goal set.
- No pasted spec text, SDK headers, reference code, binaries.
- No vectors over 1MB in-repo.
- No claims without fetch-verified sources.

## Cleanroom firewall

Wall = public specs + black-box only. Questions behavior-only.
Answers derived (beds + numbers), never transcribed.
Full rules: [docs/FIREWALL.md](docs/FIREWALL.md).

Firewall posture note: Apple has NOT open-sourced AppleArchive.
`github.com/apple/apple-archive` returns 404 (verified 2026-09-29).
Only the LZFSE codec is open (BSD). Wall stays strict.
If an Apple source drop appears later, posture changes; re-survey first.

## Spec inventory (verified links)

Every URL below fetch-verified 2026-09-29. Unfetched = uncited.

1. Apple Archive dev docs — <https://developer.apple.com/documentation/applearchive>
   200, JS shell. Title verified. Body needs browser read. UNRESOLVED content.
2. Compression dev docs — <https://developer.apple.com/documentation/compression>
   200, JS shell. Title verified. Body needs browser read. UNRESOLVED content.
3. `aa(1)` + `aea(1)` man pages — local. Observed on macOS 27.0.
   `/usr/bin/aa`, `/usr/bin/aea` present. Commands: aa archive/extract/list/
   convert/manifest/verify; aea encrypt/decrypt/sign/append/id.
4. AEA format doc — <https://github.com/kinnay/AEA/blob/HEAD/FORMAT.md>
   200, full text verified. Magic `AEA1`, LE ints, profiles, scrypt KDF,
   ECDSA P-256 sig, AES-CTR, X9.62 pubkeys. MIT repo (LICENSE verified,
   (c) 2024 Yannik Marchand). Summarize + link; never transcribe.
5. LZFSE reference impl — <https://github.com/lzfse/lzfse>
   200. LICENSE = BSD-3-Clause, (c) Apple 2015-2016. Reusable w/ attribution.
6. Eclectic Light intro — <https://eclecticlight.co/2020/11/24/compress-and-decompress-files-using-applearchive/>
   200, full text. 4 codecs: LZ4, LZMA, zlib, LZFSE. LZFSE ~= zlib-5,
   faster, Apple-proprietary, avoid for cross-platform archives.
7. Format-docs collection — <https://raw.githubusercontent.com/dgelessus/mac_file_format_docs/HEAD/README.md>
   200. CC-BY-4.0. Corroborates python-aea MIT claim.

Negative result: <https://github.com/apple/apple-archive> = 404.
No Apple AppleArchive source drop. Do not cite as source.

## Prior art

- python-aea (<https://github.com/kinnay/AEA>) — MIT. Py lib + FORMAT.md.
  AEA side covered. AAR side: UNRESOLVED coverage.
- lzfse ref impl (<https://github.com/lzfse/lzfse>) — BSD. Codec only.
- Archive Utility — ships w/ macOS. Decompresses LZFSE .aar (per #6).
  Compression support incomplete. UNRESOLVED current state.
- `aa` / `aea` CLIs — ship w/ macOS. Black-box oracles.

## Layout

```
README.md            this file
docs/FIREWALL.md     wall rules
spec/README.md       format notes go here (derived only)
vectors/README.md    test vectors (<1MB; big ones stay out)
tests/README.md      harness notes
tmp/queries/         mailbox: QUESTION-<lane>-<n>.md + JOBS.md
tmp/hints/answers/   ANSWER-<lane>-<n>.md
tmp/scratch/         throwaway; .gitkeep only at rest
```

No `src/`. No code files. By design.

## Test vectors

None yet. Rules: <1MB in-repo, larger stay out (link instead).
Sources: generate via local `aa`/`aea` (black-box), never vendor
binaries from elsewhere. Record generator command + OS version per vector.

## Next steps

1. Owner answers goal question (JOBS #1).
2. Browser-read Apple dev docs (#1, #2 above); file findings as answers.
3. Black-box `aa`/`aea` probes; first vectors.
4. AAR header survey (magic? container? codec IDs?) — all UNRESOLVED.

## Open questions

1. Goal: port vs independent impl vs format docs? OPEN. Never decided here.
2. Is AEA payload an embedded AAR? UNRESOLVED.
3. AAR magic bytes / header layout? UNRESOLVED.
4. AAR codec IDs for LZ4/LZMA/zlib/LZFSE? UNRESOLVED.
5. AppleArchive.framework API surface (stable? SPI?) UNRESOLVED.
6. Does `aa convert` bridge AAR<->other formats? UNRESOLVED.
7. xip relation to AAR/AEA? UNRESOLVED.
