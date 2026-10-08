# DPROBE-07 parse-fail prefix + wrapper/nodat class model (writer1, first-hand)
CORRECTIONS (FLAG-e62ee07): the Prefix ladder + parts of TYP enum below as
first written were WRONG (unreproducible). Corrected sections follow; the
original false texts are struck through, never re-asserted.

## Prefix ladder: RETRACTED, see DPROBE-09
- RETRACTED: `Failed to fetch magic` / `archive format version not
  supported` / `archive has wrong number of files` / `wrong number of
  files` appear NOWHERE (26-shape re-probe: lengths 0..12 raw+compressed,
  magic variants). Never implemented in code; doc-only error. TRUE ladder
  (length + magic routing, all IDENT): DPROBE-09.
- RETRACTED: "trailing garbage silently ignored exit 0". TRUE rule: trailing
  bytes parse as more items (1..5 bytes -> bd011800 stream-tail exit 1;
  bad magic -> e800/bd035000; valid headers -> extracted, mb12/mb21).

## TYP enum (corrected; code was already right, 11/11 IDENT)
- Dispatch: FULL LE UINT of TYP value (widths 1/2/4/8) vs kind codes.
  Handled (uppercase): F D L H P S B C. ALL else silent-skips exit 0:
  lowercase, W/R/T/M, multi-byte non-matching (FA/AF/AA), TYP/2 0x0044->D.
- RETRACTED: "Known: f d h l s p b c m n o A B C (15)" (case/count wrong).
- RETRACTED: te-tok "FIRST VALUE BYTE dispatches; 41 41 -> A-class".
  TRUE: [41 41] = 0x4141 skips BOTH sides (my code already full-uint).
- RETRACTED: `Invalid entry kind: <err>` + `processing dir` loud path.
  Never implemented, never observed (14 viewer + 11 own crafts: all skip).
- Non-uint TYP subtype -> `invalid type N, expected UINT` + no-TYP abort
  exit 1. N: P->2, S/T->4, E(*)->0, F/G/H/I/J->3 (all 8 IDENT, te cell).
- DAT-before-TYP present: kind known at dispatch regardless of field order.
- Missing TYP: `Invalid entry: no TYP field` abort exit 1 (Fix1, kept).

## Wrapper / nodat / no-DAT classes (viewer A-012/A-015 + own matrix 26/26)
- S (TYP 'S', no data expected): flush pass FORWARD in archive order (canonical;
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
