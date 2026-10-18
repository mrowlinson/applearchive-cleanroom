# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-eb766e3 sweep: RED-tree (same inherited base) / band4 changes PASS

- tip: lanes/encode-cport @eb766e3 (parent c12fcc6 held). diff: rgramc.c
  regen +23810/-6846 single file (T9..T10R16 FULL, n<=23000).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-eb766e3-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical + spot): top-level dispatch bounds 303/303
  IDENTICAL vs py ("303 tiers sealed" exact); CLOSED tag sets 386/386
  (1 docstring artifact resolved); tables 864/864 exact (146 1D +
  288 2D + 71 char[] + 347 char*[] + 11 dicts + local _s T9F2 dict
  hand-verified keys/refs); T10R16 tail spot-read exact incl
  _T10PHM[q]+2 slice + b5 dbl-carry (off>=39/167); top label T10R16
  CORRECT this band (no slip).
- battery: functional legs all green, outdir gate-cport-eb766e3-s12:
  C-BUILD w=0, RGRAM n=2822 rc=0, PINS-RGRAM set-eq 2822/2822. no flake.
- parity: RGRAMC-PYID 1411/1411 covered=1411/1411 GREEN rc=0 — FULL,
  every sealed pin covered, none escaped.
- C-side RGRAM: 2822/2822 PASS, 0 FAIL, RGRAM-GREEN rc=0 via C binary.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 15001 T9J1A, 17000 T10Q, 19000 T10R5, 21000 T10PCQ,
  22500 T10R15, 22900 T10R16. (15000 first pick was pinned; moved +1.)
- boundaries: 23000 CLOSED-T10R16 both identical; 23001 BOTH exit2
  out-of-scope (py ends here too — FULL both sides).
- wall: diff grep CLEAN (0 hits).
- verdict: band4 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 193/194 + cport 0/4-held (shared cause).
