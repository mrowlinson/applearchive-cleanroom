# applearchive-cleanroom

Independent cleanroom reimplementation of AppleArchive (AAR archives,
AEA encrypted blobs): behavior-identical to Apple's `aa(1)`/`aea(1)`
from black-box observation only. No Apple code, headers, binaries, or
transcribed spec text in this repo. Private, early, moving fast.

Status date: 2026-10-08. Everything below is master HEAD.

## Status

Encode (master): container framing green end to end — PBZE + RAWENC +
OUTER2 + RB2 + RAVFRAME batteries all GREEN in Python prototype and C
port (`src/c/aae.c`, `lz4c`, lzma via pinned liblzma + own XZ framing).
LZFSE/LZBITMAP/LZMA/LZ4 cells green. rgram grammar map at 2822 pins
(N = 0..23000 continuous, T10P17 merged); mapping continues toward a
~48000 frontier; dedicated rgram C-port lane open.
Decode (master): JOINT DONE. C (`src/aad.c`) + proto mirror through
TIP1..TIP2e + thread-shape (-t-1-only) + -wt-1 TIPs, all merged:
CBATTERY 1069/1069 + cvp 150/150 + flip 200/200 + asan 13 + raw 130,
0 open questions, 0 open flags.
Scope: container only. Stock codecs link when byte-identical
(pinned hashes); lzmesh comes from the sibling lzmesh-cleanroom
project (link-only). Nothing here claims 100% until the gates say so.

## Quickstart

Prereqs: macOS with `/usr/bin/aa`, `/usr/bin/aea` (black-box oracles),
`cc`, `python3`. LZFSE cells use OSS liblzfse via `$LZFSE_DYLIB`.
Scratch MUST live on NVME (`export TMPDIR=<ws>/tmp`), never /tmp.

```sh
sh tests/smoke.sh <workdir>        # T0 oracle round-trip smoke
sh tests/test_rgram.sh             # rgram grammar battery (pins)
sh tests/test_pbze.sh <workdir>    # pbze byte-exact battery
sh tests/test_rawenc.sh <workdir>  # rawenc byte-exact battery
sh tests/c-battery.sh              # decode C battery (1069 cells)
make -C src/c                      # C port (see Makefile for out dir)
```

Batteries compare implementation bytes vs oracle bytes; GREEN means
every cell matched, pins held.

## Layout

```
README.md            this file
src/                 our code: rgram.py/pbze.py/rawenc.py/rb2.py/ravframe.py
                     (encode proto), aad.c (decode C), c/aae.c+lz4c (encode C)
proto/               decode prototype mirror (aad.py) + adapters
harness/             oracle adapter (wraps /usr/bin/aa + aea), CLI contract
tests/               smoke + per-codec batteries + c-battery + sweep gate script
vectors/             pins + self-generated vectors (<1MB; generator+OS recorded)
spec/                derived behavior clauses (CR-nnn) + derivation log
notes/               DPROBE-nn experiment records (decode)
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
