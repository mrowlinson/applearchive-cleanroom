# GATE-e164e6d.md — w2 P46 (32745..32836, 6 tiers) PASS-individual

- sha: e164e6d, lane w2, regime 76B raw.
- code-read FULL: if/elif raw-len blocks; 6 tiers:
  P460 (32745) / P461 (32746) const.py + Q-row,
  P46A (32747..32762) 16x6B rows b37,38,68-71,
  P46B1 (32763..32767) + P46B2 (32768..32772) 5x11B rows b29,36-41,72-75,
  P46Q (32773..32836) b32=M32[m]^(0x20 if q>=2), m-tab 16x7B b33,42,43,68-71, q-tab 4x10B b36-41,72-75.
- AST: 6 const-lists sorted/nodup/disjoint/FULL-cover (74/74/68/63/63/56); row widths uniform 6/11/11/7+10; M32 len16.
- gate-tip.sh RC=0: RGRAM n=3912 PASS, PINS-RGRAM set-eq, OUTER2/RB2/RAVFRAME/PINS PASS, HYGIENE/CONTAM/LIBCOMPRESSION PASS, zero FAIL lines.
- for-list +10 straddles all 6 tier edges (incl B1/B2 split 32763/32767/32768/32772).
- storm fresh oracle (gate tree, zeros-N): 32745 P460, 32746 P461, 32747/32750/32755/32760 A off=0/3/8/13, 32765 B1 off=2, 32770 B2 off=2, 32780/32836 Q off=7/63 — all CLOSED rc=0.
- boundaries: 32729/32744 -> T10R44 off=240/255; 32837 -> N out of scope rc=2. exact.
- wall-grep: 0 hits (ghidra/ida/disassembl/decompil/COMPRESSION_/compression_).
- verdict: PASS-individual. no FLAG.
