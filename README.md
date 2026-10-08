# applearchive-cleanroom

Independent cleanroom reimplementation of AppleArchive (AAR archives,
AEA encrypted blobs): behavior-identical to Apple's `aa(1)`/`aea(1)`
from black-box observation only. No Apple code, headers, binaries, or
transcribed spec text in this repo. Private, early, moving fast.

Status date: 2026-10-07. Everything below is master HEAD.

## Status

Encode (master): raw + pbze byte-exact vs oracle in Python prototype
and C port (`src/c/aae.c`) — PBZE-GREEN + RAWENC-GREEN batteries,
15/16 store rule, razor flip coverage. zlib level-5 byte-exact.
Decode (master): spec clauses CR-001..011 (outer block, stored rule,
TLV, multi-block chain, sub-frames). Decode implementation (C +
prototype: chain/TLV/zlib, lzraven/murmur MATCH) is green on lanes,
merging as gates pass.
Frontier (in-flight on lanes): full-corpus byte-identity gates,
holdout/fresh slices, AEA encrypt/sign paths, timing work. Nothing
here claims 100% until the gates say so.

## Quickstart

Prereqs: macOS with `/usr/bin/aa`, `/usr/bin/aea` (black-box oracles),
`cc`, `python3`. LZFSE cells use OSS liblzfse via `$LZFSE_DYLIB`
(default: this project's NVME tools path).

```sh
sh tests/smoke.sh <workdir>       # T0 oracle round-trip smoke
sh tests/test_pbze.sh <workdir>   # pbze byte-exact battery
sh tests/test_rawenc.sh <workdir> # rawenc byte-exact battery
make -C src/c                     # C port (see Makefile for out dir)
```

`<workdir>` is scratch the script may fill (use NVME, not the repo).
Batteries compare implementation bytes vs oracle bytes; GREEN means
every cell matched, pins held.

## Layout

```
README.md            this file
src/                 our code: encode.py/pbze.py/rawenc.py (proto), c/aae.c (C port)
harness/             oracle adapter (wraps /usr/bin/aa + aea), CLI contract, battery docs
tests/               smoke + per-codec batteries + sweep gate script
vectors/             self-generated test vectors (<1MB; generator+OS recorded)
spec/                derived behavior clauses (CR-nnn) + derivation log
docs/                firewall, recon notes, research
tmp/                 UNTRACKED scratch: worktrees, quiz dirs, claims (never committed,
                     except 4 legacy tracked files under tmp/{hints,queries,scratch}/)
```

Python is the reference prototype; C is the deliverable. Ports must
prove byte-parity (port == proto == oracle) before they count.

## Cleanroom firewall

Wall = vendor-published docs + black-box execution only. Questions
behavior-only (what does it output for X). Answers derived (beds +
numbers + verdicts), never transcribed. Disassembly, teardowns, and
patents are forbidden to implementers; decompile-side readers confirm
every static claim against the running binary before it becomes a
spec clause. Full rules: [docs/FIREWALL.md](docs/FIREWALL.md).

Posture note: Apple has NOT open-sourced AppleArchive.
`github.com/apple/apple-archive` returns 404 (verified 2026-09-29).
Only the LZFSE codec is open (BSD). Wall stays strict. If an Apple
source drop appears later, posture changes; re-survey first.

## Spec inventory (links fetch-verified 2026-09-29)

1. Apple Archive dev docs — <https://developer.apple.com/documentation/applearchive>
2. Compression dev docs — <https://developer.apple.com/documentation/compression>
3. `aa(1)` + `aea(1)` man pages — local, macOS 27.0
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

In-repo vectors are self-generated via local `aa`/`aea` (black-box),
<1MB each, with SHA256SUMS. Larger corpora stay out (link instead).
Never commit vendor binaries from elsewhere.

## License

Not yet chosen (private repo). No license file until the owner picks
one; nothing here is released under any terms yet.
