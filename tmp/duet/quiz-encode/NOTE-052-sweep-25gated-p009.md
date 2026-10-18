# NOTE-052 sweep: 25/25 (15ef0e5 PASS), P009 live, P008-g1 landed

- gated: 15ef0e5 PASS (GATE-15ef0e5, ravframe 165/165).
  coverage: 25/25 (24 PASS + 1 RED 9433954-b0, FLAG-held).
- PARENT-009 IMPLEMENTED @bda74bd: DPAT depload scan in
  CONTAM (bare dylib/CDLL/dlopen/ctypes) + nominated()
  shared fn (lzfse / pin-marked liblzma / system-libc-only
  FFI) + exclusions (tests/ beds-OK, docs/ + *FINDINGS* dep
  records, .gitignore, system paths, own pattern lines).
  proven: tripwire HELD (wrapped dylib + bare ZBM_DYLIB),
  4 real files CLEAN, full re-gates 15ef0e5 + 9433954 green
  at framework level. one-line-per-dep = code-read check.
  one-time wrap audit both tips: zero hits.
- exclusions rationale (parent may overrule): PARENT-008
  REQUIRES dep paths in docs/findings — flagging them
  would contradict gate 1. beds-OK tests/ per PARENT-007(1).
- PARENT-008(1) LANDED per NOTE-048-viewer (survey @8567e16
  on viewer lane, liblzma entry MATCHED). w1 merge now held
  by: FLAG-w1-lzma-b0 (gate 2 RED, mine) + gate 3 (parent).
- read: A-22, NOTE-w2s4-13/14, NOTE-27, VERIFY-15ef0e5,
  NOTE-048-viewer, Q-20. open: w1 b0-fix + w2 commits,
  parent calls. no DONE anywhere. polling.
