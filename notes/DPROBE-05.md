# DPROBE-05 committed fuzz legs + 3 corrupt-input fixes (writer-measured)

All black-box: oracle executed via harness adapter, I/O observed.
No binaries opened, no disassembly. 2026-10-07 (successor shift).

## Committed legs (were uncommitted claims; now first-hand re-runnable)

- tests/fuzz.py: seeded corruption differential driver. Modes orac
  (oracle-vs-C, 200 iters seed 49420) + proto (C-vs-proto, 150
  iters seed 40608). Hard bar: exit-class agree + no
  signal/timeout/hang. Tree sig = mode+content, NO mtime
  (creation-time race on corrupt inputs: both sides mtime-now).
  fifo-mixed excluded in orac mode (oracle hangs, DPROBE-04 Q1).
- Seed pins cases PER DRIVER VERSION: `a[f()] = g()` evaluates
  g() before f(); splitting the lines reorders the RNG stream
  (v1/v2 same-seed cases differ, proven by hash). No
  nondeterminism anywhere (oracle-3x + C-3x stable on retest).
- Tree-diff classification (mechanical): flip offsets vs own
  outer block map (comp!=unc regions). Diff with all flips
  outside compressed payloads = STRUCTURAL FAIL. Diff with a
  flip inside compressed payload = DIVERGENCE (corrupt-codec
  recovery is implementation-defined; listed, counted, non-fail).
- tests/flip-fuzz.sh, c-vs-proto.sh (wrappers), raw-trunc.sh
  (130 pts, exit-1-or-clean no crash), asan.sh (13 fixtures,
  ASan/UBSan exit parity + 0 reports).

## Fix 1: TYP required on EVERY item (C+proto; nt cell x7)

- Missing-TYP item: oracle aborts exit 1 ("Invalid entry: no TYP
  field", byte-stable stderr, stops, earlier entries stand,
  3/3 positions + root case). C used to silent-skip.
- Root item (PAT-empty) ALSO requires TYP (case175: destroyed
  TYP key + empty PAT -> oracle aborts). Rule: `if (!t) abort`
  before any PAT check. Valid archives unaffected (53/53).
- Battery: nt-exit0/1/2 + nt-tree0/1/2 + nt-stderr (runtime
  craft from hello-raw.aar, 3 TYP blanks asserted).

## Fix 2: XAT applies BEFORE chmod (C+proto; xo cell x3)

- MOD 566 (+x stripped) dir + XAT: setxattr on 566 dir = EPERM
  (proven direct: xattr needs +x). Oracle exits 0 WITH xattr +
  mode 566 present -> oracle orders xattr before chmod. C did
  chmod-first -> exit 1. Fix: XAT block first in apply_meta.
- Clean provenance XAT: full parity both sides exit 0 (xattr
  writable; FS stores normalized value). No policy gap there.
- Battery: xo-exit + xo-tree + xo-metax (mode + provenance
  presence both sides; MOD566 craft from hello-raw.aar).

## Fix 3: zlib adler-broken streams decode (C+proto; ad cell x2)

- Flip mid-deflate-stream (stream-valid, adler-wrong): python
  uncompress FAILs, raw-inflate OK (2445B valid inner), oracle
  exits 0 FULL tree. Fix: on Z_DATA_ERROR, raw-inflate fallback
  (skip 2B header, -15 windowBits, require unc bytes exactly).
  Over-acceptance guarded by the fuzz legs (exit-class bar).
- Battery: ad-exit + ad-tree (pinned flip off=201 0xac->0xf3
  in hello-zlib.aar, assert-guarded).

## A-018 consumed (dispute CLOSED, no code change)

- Viewer independently replicated W/R/T/M silent-skip exit 0
  (6/6 + 2/2 controls) and CORRECTED A-013. Tip behavior already
  matches. No revisit unless a loud vector fires.

## Accepted divergence classes (documented, not shipped silent)

- Corrupt-compressed-payload recovery (content): decoders may
  differ on corrupt bytes while both exit 0. DIVERGENCE class
  in fuzz.py. Current: 0 open (200/200 + 150/150 agree).
- Exit-class on compressed flips stays HARD (no case has shown
  a justified exit split there; adler fallback closed 188).
