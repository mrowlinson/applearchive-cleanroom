# DPROBE-12 TIP2a: G9 traversal bar + modal 83058800 (C+proto)

## Oracle maps (own beds, WS probe/g9w1a3/, aa extract default threads)

- g9.aar (D a + F a/f.txt + L a/l.lnk + D b + D b/deep + F b/deep/g.txt),
  planted `a` (sym->victim / file / dangling): modal = replace with EMPTY
  real dir + children fail (L triple [`a parent...` + `invalid path` +
  `creating fs object`] + F pair + `N entries failed`), rc 1, victim
  pristine, b/deep/g.txt OK. Outcome SET over 17 runs: {2-fail L-first
  9, 2-fail F-first 2, f-only (+l.lnk dangling) 2, l-only (+f.txt full) 1,
  ...} — order races, subsets race; both-succeed 0/17. D-over-occupant
  itself silent, always replaced (mode = D MOD via phase 3).
- g6.aar (D dd MOD700 + F dd/kid, planted file dd): oracle ALWAYS replaces
  (dir 0700, 6/6); kid races (HAVE+rc0-silent 2/6 vs ABSENT+pair+count1+rc1
  4/6). Old G6-keep pin was oracle-false (never oracle-verified). A-022 ov2
  same class (replace + modal child fail).
- g9p.aar (settyppat a/f.txt F->P): P child = TRIPLE (A-027#1 non-F rule),
  4/4 both-fail. C clean-dest: fifo + rc 0 (no hang our side).
- hlink-basic.aar, planted hello: modal 4/4 = pair-on-TARGET
  (hello/repeat.txt) + `'H' LNK not a regular file` + `process hlinks` +
  count 1, rc 1, hello/ EMPTY (A-027#2). Target-F draws NOTHING (no pair,
  no count) — H-target silence rule (own finding, matches A-027#2 note).

## Design (C src/aad.c + proto mirror, identical rules)

- _mkparents/mkdirs gated: lstat walk; missing -> mkdir 0755; non-dir ->
  unlink + mkdir 0755 + record repl[] (dedup, cap 64). Root gated on
  scratch repl (never taints). Never writes through non-dir (SECURITY).
- Phase 1: after parents ensured, under_replaced(target) -> modal child
  fail: F pair / L+P triple (non-F rule) / D F-shape (hypothesis, unprobed);
  H-target F fully silent (no counters). fails++ + sfails++ (joint count
  via existing sfails line; shared hdr => first-failure head, A-027#3).
- Flush post-phase-1 in ARCHIVE order (A-026#5 prescription; oracle order
  races so any fixed order is a valid pin; batteries SET-pin oracle side).
- H pass: target missing/non-regular + under_replaced(src) -> 83058800
  pair-on-target + H diagnostic + trailer + N=1 (A-027#2). Else CR-043 path
  unchanged (c8104800, no count). H PATH-side pair = hypothesis (A-027#2
  covers target-side only); HLC-form untouched.
- D branch: non-dir occupant -> unlink + replace 0755 silent + repl record
  + dirs[] (MOD via phase 3). Real-dir occupant path unchanged (G6-keep
  only ever meant dir occupants; file/sym occupants now replace).

## Battery (tests/c-battery.sh: 403 -> 448)

- g-collision: G6 rewritten (7 asserts: oracle replace-0700 pin + shape-SET
  {success-leg, modal-leg} + ours pinned modal + mirror + trees). Old
  keep asserts deleted (oracle-false).
- g9-traversal 27 asserts x sym/file/dangling: exits 1 + victims intact +
  C pinned modal exact + proto mirror (minus blocks:) + oracle outcome-SET
  (head + count/member/tree correspondence) + C tree (a/ empty 0755, sib
  file) + C/proto tree lock + top-level purity.
- g9P 7 asserts (P-triple modal + SET incl fifo-present subset leg).
- g9H 7 asserts (H modal exact + oracle SET {modal, rc0-linked success}).

## Stack (TIP2a, first-hand 2x c-battery)

- c-battery 448/448 GREEN x2, smoke GREEN, asan 13/13, raw-trunc 130/130,
  flip-fuzz 200/200 0div, c-vs-proto 150/150 0div. C 0 warnings.
- Open: Q-027 fully answered (A-027 + A-027B); D-under-replaced + H-path-side
  hypotheses unprobed; G9+S mixed-head cell not yet crafted (TIP2b/G-round).
