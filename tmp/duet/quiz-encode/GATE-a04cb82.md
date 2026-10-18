# GATE-a04cb82 sweep: PASS-individual (rgram 2822/2822; rename T11R0->T10R16)

- tip: lanes/encode-writer2 @a04cb82 (parent 9768792 gated).
  rgram +14/-14 single file; for-list +0, pins +0.
- code read (FULL): RENAME-ONLY-PROVEN — minus/plus line
  multisets identical after T11R0/T10R16->X normalization
  (diff empty). 3 table identifiers + comment + 7 fail
  strings + CLOSED string; zero logic/byte/table change.
- battery: GATE-PASS shipped legs (outdir gate-w2-a04cb82-s10):
  HYGIENE/CONTAM/SMOKE n=6/OUTER2 n=284/RB2 n=47/
  RAVFRAME n=181/PINS set-eq 284/47/181/OSS/LIBCOMPRESSION/
  ADOPT all green; RGRAM n=2822 rc=0 zero FAIL (tip tree,
  NVME workdir). OUTER2 green, no flake.
- storm diligence: 5 EXTRA unpinned cells ALL CLOSED rc=0 on
  FRESH oracle bytes (new T10R16 tag): 22750 (off5),
  22805 (off60), 22865 (off120), 22925 (off180),
  22995 (off250). unpinned-ness grepped vs PINS first.
- wall: diff grep CLEAN. verdict: PASS for THIS tip.
- coverage: 186/187 PASS-individual + 1 RED-cleared
  (48ebfe0 history) + 1 flake-cleared (ndp2 test-side).
  ZERO holds vs NOTE-092 baseline.
