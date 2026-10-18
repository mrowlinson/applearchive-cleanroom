# NOTE-sweep2-r19-parked (3 GATES + 12 interim GREEN)

- GATED this run (all PASS-functional,
  first-hand, walls 0, OUTER2 clean
  284/284 first try, no FLAGs):
  b192 bd1ca6d T10P138 n<=64852
  (RGRAM 8280, PYID 4140, own-loop
  92 pins 26, added 4/4 EQ, audits
  167+844+11+263+1041 zero mism,
  inherit-vs-b190 IDENTICAL);
  b194 676626e T10P139 n<=65200
  (RGRAM 8330, PYID 4165, own-loop
  92 pins 26, added 3/3 EQ AC73/
  BC69/QC63, audits 167+848+11+
  265+1048 zero mism, inherit ALL
  IDENTICAL except counts);
  b196 4c9ff15 T10P140 n<=65548
  (RGRAM 8384, PYID 4192, own-loop
  92 pins 30, added 3/3 EQ AC76/
  BC71/QC62, audits 167+852+11+
  268+1056 zero mism, inherit ALL
  IDENTICAL except counts).
  C-py PASS-sets cmp-equal all 3;
  all builds rc=0 0-warn.
- INTERIM: 12 fresh-oracle re-audits
  ALL GREEN: b42 (92 pins 20), b46
  (348 pins 40), b48 (256 pins 20),
  b148-b156 (92 each), b158-b164
  (92 each, incl b160 now GATE-filed
  so claim-clear). 12 builds rc=0
  0-warn. Logs r19-interim.*.
- NEXT: b198 C-port NOT cut (tip =
  T10P141 writer merge 5215124).
  Refill: poll cport tip; claim +
  full gate b198 (range 65549..
  65896 per merge note; verify lo
  vs b197 ceiling at claim time).
  Further interim: b166-b188 all
  GATE-filed = claim-clear.
- Quiz diff 0, turf clean (odds
  b191/b193/b195/b197 untouched).
  No commits. 10 hb + this note.
