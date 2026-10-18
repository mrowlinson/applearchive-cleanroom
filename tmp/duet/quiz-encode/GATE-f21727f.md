# GATE-f21727f sweep: PASS-functional (cport band31; T10P370..P37Q ->29704)

- tip: lanes/encode-cport @f21727f (parent merge 0fe7615 P37-partial).
  rgramc.c +1017/-441: P37 5-tier port raw-lencode (P370/P371 76/76B
  + P37A 16x6B b21,22,68-71 + P37B 10x11B b0,20-25,72-75 +
  P37Q 4x16 P37M-16x7B b28-30,68-71 + P37Q-tab 4x11B b14,20-25,
  72-75), top bound 29704.
- code read (FULL): all 5 dispatch blocks line-for-line vs w2 f43ec6a
  (bounds 29613/29614/29630/29640/29704, offs, RAW l16 no-0x8000,
  b-sets incl b0-tabbed). tables P37A/P37B/P37M/P37Q EXACT;
  consts 74/74/68/63/56 EXACT numeric (9/9).
- battery: legs green incl OUTER2 + PINS-OUTER2 set-eq + RGRAM 3552
  + PINS-RGRAM set-eq 3552; C-BUILD w=0. HYGIENE/CONTAM/
  LIBCOMPRESSION FAIL = OBSERVED-inherited (diff rgramc.c only;
  same-cause 032/033, no FLAG).
- parity: RGRAMC-PYID 1776/1776 GREEN; RGRAM_BIN=C RGRAM-GREEN
  (message-exact 1776/1776, 3552/3552).
- storm diligence: 5 EXTRA unpinned cells py=C byte-identical rc=0
  on FRESH oracle bytes: 29622 P37A, 29636 P37B, 29650/29680/29695
  P37Q.
- boundaries: 29613 P370 + 29704 P37Q-off63 py=C CLOSED; 29705 rc=2
  scope both. exact.
- wall: diff grep CLEAN (0 hits). verdict: PASS for THIS tip.
- coverage: 227/227 PASS-individual (w2) + cport 32 PASS-functional.
