# OSS dependency survey (encode side): nomination ledger with license + source + pin

Viewer-maintained per PARENT-003(1). Every OSS artifact LOADED by src/build or READ under
nomination is named here. MERGE NOTE: lanes/oss-survey carries docs/OSS-SURVEY.md (domain survey
of AAR implementations); parent unions both files at land (different content, same path).

## 1. liblzma / XZ Utils — LOAD-nominated (A-20; PARENT-008 gate item)
- use: lzma LZMA-packet bytes in src (lzmaenc.py stdlib path) + C-link (aae.c direct link).
- license: 0BSD for liblzma (own COPYING head-read, brew 5.8.4 cellar).
- source: https://xz.tukaani.org/xz-utils/ (upstream); artifact via brew bottle xz 5.8.4.
- pin: FORMAT raw-LZMA1-preset-6 (lc3lp0pb2 dict-8M) + VERSION 5.8.4 + battery.
  C artifact: /opt/homebrew/Cellar/xz/5.8.4/lib/liblzma.5.dylib
  sha256=1b2e12cc1b920264f3dd15eeba22e85b8afd589595d8945d1d12a52afa694b09 (own re-hash MATCHES
  writer NOTE-24). System liblzma is dyld-cache-resident 5.8.4 (no /usr/lib file; own probe) —
  NEVER dlopen unpinned (A-20 condition). "5.4.3" DROPPED (venue correction NOTE-24).
- status: GRANTED conditional (A-20); sweep byte-exactness legs must green pre-merge (PARENT-008).

## 2. liblzfse / lzfse — LOAD-nominated (PARENT-003)
- use: pbze.py ctypes (LZFSE_DYLIB env override + NVME default) + aae.c (C port carries decision).
- license: BSD-style, Apple Inc. 2015-2016 (own LICENSE head-read).
- source: https://github.com/lzfse/lzfse @ e634ca58b4821d9f3d560cdc6df5dec02ffc93fd
  (own rev-parse; tree CLEAN).
- pin: dylib /Volumes/NVME/applearchive-cleanroom-ws/tools/lzfse/build/bin/liblzfse.dylib
  sha256=1a3067efb709b60a... (own hash; full bytes recorded at battery). Re-pin on rebuild.
- status: loaded pbze path, gated by sweep byte-exactness (PARENT-003(2)).

## 3. libzbitmap / eafer — READ-nominated (A-16; no load)
- use: READ-ONLY (FORMAT + decode-path + matcher decisions for hand-written bitmap IMPL).
  NO bytes in src (copy/fork/vendor/link all require follow-up LOAD nomination).
- license: MIT, Corellium LLC 2022 (own LICENSE head-read). README: black-box RE (own read).
- source: https://github.com/eafer/libzbitmap @ 574abeae25b25c3319b9b6a9225cc7464e08ae88
  (own rev-parse; +1 untracked build dylib noted).
- pin (compare artifact): libzbitmap.dylib sha256=43d4f5e9e8dcde8b... (own re-hash MATCHES A-10).
- status: READ granted; w2 contact-logged (NOTE-w2s3-10/w2s4-2, pin MATCHED).

## 4. lz4 / lz4 — COMPARE-ONLY (A-10; no read/load for impl)
- use: beds/grids/byte-diffs ONLY (black-box encode/decode compares). Never imported/linked/
  dlopened by src or build. Any future src/build use = fresh nomination BEFORE use.
- license: BSD 2-Clause (lib/) + GPL-2.0-or-later (rest) (own LICENSE head-read).
- source: https://github.com/lz4/lz4 @ 0774d05537f9762f838f7ab541b7765f1a729cb5 (own rev-parse).
- status: compare-only retroactively granted (A-10); src ZERO imports verified at e72aa4c.

## rules (restated from PARENT-003 + A-12/A-16/A-20)
- No new OSS deps (dylib, submodule, vendored code) without viewer nomination in quiz FIRST.
- No Apple-proprietary "OSS": libcompression/dlopen(Apple encoders) REFUSED (A-12, PARENT-007).
- Pins re-gate on ANY version/OS bump (oracle-gate rule). License files stay readable at sources above.

## RULING superseding A-12 (fix-sweep-PTD; wall restated, not moved)
- A-12's REFUSE covered copying/reading Apple CODE into the repo. It does
  NOT cover dynamic linking: linking the system Compression framework
  (decode path) and the nominated lzfse dylib (encode path) is ALLOWED.
  Link != copy: no Apple bytes are vendored, read, or disassembled; the
  loader resolves system libraries at runtime.
- Encode-via-Apple-ABI is allowed ONLY where emitted bytes are
  oracle-pinned: every such byte must survive a byte-compare battery
  against `/usr/bin/aa` output (pbze/lzma/lz4 cells), or the path must
  honestly refuse (lzraven-unclosed, lzbitmap match-class). A byte the
  oracle would not emit is never emitted.
- The wall stands: zero Apple CODE in the repo (no vendored binaries,
  no disassembly listings, no decompiled sources). CONTAM + LIBCOMPRESSION
  gate legs enforce it. Direct `dlopen` of Apple encoders outside the two
  nominated links above remains REFUSED.
