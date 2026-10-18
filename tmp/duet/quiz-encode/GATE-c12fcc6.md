# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-c12fcc6 sweep: RED-tree (same inherited base) / band3 changes PASS

- tip: lanes/encode-cport @c12fcc6 (parent ee8a9b5 held). diff: rgramc.c
  regen +15869/-3272 single file (T7..top tiers, n<=13696).
- TREE verdict: RED — same 3 inherited legs, identical signature. see
  FLAG-c12fcc6-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical + spots): top-level dispatch bounds 169/169
  IDENTICAL vs py; CLOSED tag sets 233/233 (incl dynamic tag-buffer +
  conditional forms, each resolved); tables 506/506 exact (107 1D +
  148 2D + 32 char[] + 209 char*[] + 10 dict KEYS/VALS; audit scripts
  in NVME seat dir, all skips driven to zero); new helpers dictstr/
  dict_has reviewed (miss→GRAMMAR-BREAK exit1 vs py KeyError,
  malformed-only divergence class); regen churn verified content-equal
  via full-file audits (no logic removal).
- observations (message slips, no functional impact): (a) msg claims
  top "T9B2" but C top = T9A2Q (n<=13696); py T9B2 starts 13697
  (bound probe: 13697 py=CLOSED-T9B2 vs C=scope-exit). (b) "165 tiers"
  already self-corrected by writer to 169 in NOTE-cport-05 — my
  independent count 169 agrees, as does "506 tables".
- battery: functional legs all green, outdir gate-cport-c12fcc6-s12:
  C-BUILD w=0, RGRAM n=2822 rc=0, PINS-RGRAM set-eq 2822/2822. no flake.
- parity: RGRAMC-PYID 855/855 covered=855/1411 GREEN rc=0 (855 = exact
  in-band pin count; none escaped).
- C-side RGRAM: 1710/1710 in-band PASS, 0 out-band PASS, 556 FAILs ALL
  out-of-scope (expected), 0 non-scope FAILs.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 6500 T7C, 8000 T7L, 9500 T8R4, 11000 T8A1, 12500 T9S1,
  13400 T9Y1. unpinned-ness grepped vs PINS first.
- boundaries: 13696 CLOSED-T9A2Q both identical; 13697 py=T9B2 vs
  C=exit2 scope — exact band edge.
- wall: diff grep CLEAN (0 hits).
- verdict: band3 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 192/193 + cport 0/3-held (shared cause).
