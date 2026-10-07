# DPROBE-07 parse-fail prefix + wrapper/nodat class model (writer1, first-hand)

## Prefix ladder (own probes, oracle exit+stderr first-hand)
- 0..1 bytes: `Failed to fetch magic` + `stream cancelled`, exit 1.
- 2..3 bytes: magic ok, version short: `archive format version not supported` +
  `stream cancelled`, exit 1.
- 4..7 bytes: version ok, nfiles short: `archive has wrong number of files`
  + `stream cancelled`, exit 1.
- 8..N with nfiles=N: nfiles check passes with EXACTLY 8+N bytes present;
  fewer -> `wrong number of files` + `stream cancelled`, exit 1.
- all prefix fails: NO `Extraction failed` banner, NO `entries failed` count,
  `stream cancelled` immediately closes. Root still created (outdir in place).
- Trailing garbage after a good archive: silently ignored, exit 0 FULL tree.

## TYP enum (own crafts, exit+tree+stderr parity)
- Known: f d h l s p b c m n o A B C (15). Anything else incl multi-byte
  values and unknown singles = `Invalid entry kind: <err>` + `processing dir`
  + `2 entries failed`-style count, exit 1, root survives, NO per-item stderr.
- TYP stored-length != 1 with total-header-size kept (te-tok): oracle takes
  FIRST VALUE BYTE as kind: 41 41 -> A-class; 41=link-target in output path.
  Mine: same rule (first value byte dispatches).
- DAT-before-TYP present: kind known at dispatch regardless of field order.
- Missing TYP: `Invalid entry: no TYP field` abort exit 1 (Fix1, kept).

## Wrapper / nodat / no-DAT classes (viewer A-012/A-015 + own matrix 26/26)
- S (TYP s, no data expected): flush pass FORWARD in archive order (canonical;
  -wt 1 pins archive order; default threads RACE at n>=2 per NOTE-49/50:
  sort-or-pin in cells, SET parity).
- nodat class (TYP in wrapper set with no DAT / bare no-DAT file): REVERSE
  flush (archive-last-first, triple-nodat IDENT incl order); single shared
  `Error 0x` header then one `invalid entry final state 0` line each.
  S-flush runs BEFORE nodat-flush in both (tri IDENT single-run); cross-class
  relative order is racy per NOTE-44, cells pin tokens not order here.
- `invalid entry final state N`: N=0 in EVERY shape probed first-hand
  (single/triple nodat, no-TYP+nodat, S+nodat+dirXAT, nodat+H, EISDIR+nodat).
  No nonzero value ever observed; C+proto hardcode 0. If a future probe
  shows N!=0, this rule reopens.
- no-TYP + no-DAT (dd): single no-TYP abort, stderr byte-IDENT (dd-shape cell).
- EISDIR-rule file (dir where file expected): prints as nodat-class flush
  entry (ne-shape), continues; exit 1 + count.
- H hardlink pointing at failed/xattr-failed primary: H-pass prints per-link
  `Error` + trailer `invalid entry final state` iff primary failed; count
  line counts each failed H separately.
- Dir XAT-fail: dir still created; meta pass prints `Error` block; dirs-meta
  runs reverse AFTER files; count includes dir fails.
- Cross-class order RACES (NOTE-44 standing part): XAT-block vs S-stanza as
  units, arrival-ordered header. Cells sort cross-class stderr.

## Root/exit/count (kept from DPROBE-06, re-proved)
- Root = outdir in place (never recreated); exit 0 iff 0 fails; count line
  `N entr(y|ies) failed` iff N>0; aborts stop creation only (post-pass runs).
