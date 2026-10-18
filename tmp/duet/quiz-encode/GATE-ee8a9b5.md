# SUPERSEDED-VERDICT: PASS-functional per PARENT-032/033 (was RED-tree; evidence stands).
# GATE-ee8a9b5 sweep: RED-tree (same inherited base) / band2 changes PASS

- tip: lanes/encode-cport @ee8a9b5 (parent 0f57814 held). diff: rgramc.c
  +5617 single file (T3..top tiers, n<=6040).
- TREE verdict: RED — same 3 inherited legs as band1, identical
  signature. see FLAG-ee8a9b5-hold (= FLAG-0f57814-hold cause). no fault.
- code read (FULL-mechanical + spots): top-level dispatch bounds 68/68
  IDENTICAL (order+values) vs py; CLOSED tag sets 70/70 IDENTICAL;
  tables 205/205 exact (88 1D + 48 2D + 5 char[] + 64 char*[], audit
  scripts in NVME seat dir); full line-reads T3/dip-T4B-gap/T6M3 exact
  incl hex_of/buffers/kcells-concat/const-loops; scope exits 2/2 mirror
  (mid T4B-gap + final n<=6040 fallthrough).
- observation (message slip, no functional impact): commit msg claims
  "T3..T7D3" but C top tier = T6M3-6 (n<=6040); py confirms T7A starts
  6041 (bound probe: 6041 py=CLOSED-T7A vs C=scope-exit). numeric
  coverage n<=6040 + 68 new tiers + 341 pins all correct as claimed.
- battery: functional legs all green, outdir gate-cport-ee8a9b5-s12:
  C-BUILD w=0, RGRAM n=2822 rc=0, PINS-RGRAM set-eq 2822/2822. no flake.
- parity: RGRAMC-PYID 341/341 covered=341/1411 GREEN rc=0 (341 = exact
  in-band pin count; none escaped).
- C-side RGRAM: 682/682 in-band PASS, 0 out-band PASS, 1070 FAILs ALL
  out-of-scope (expected), 0 non-scope FAILs.
- storm: 6 EXTRA unpinned cells CLOSED py=C byte-identical on FRESH
  oracle bytes: 700 T3, 1000 T4A, 2500 T5F3, 4000 T6A, 5100 T6H,
  5900 T6L. unpinned-ness grepped vs PINS first.
- boundaries: 6040 CLOSED-T6M3 both identical; 6041 py=T7A vs C=exit2
  scope — exact band edge.
- wall: diff grep CLEAN (zero hits).
- verdict: band2 changes PASS-individual; tip HELD RED by base FLAGs.
  coverage: w2 192/193 + cport 0/2-held (shared cause).
