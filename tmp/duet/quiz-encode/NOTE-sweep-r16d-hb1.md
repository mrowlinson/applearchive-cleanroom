# NOTE-sweep-r16d-hb1: b203 claimed, battery setup

- Target b203 02c66ac T10R141 n<=66848 (878
  tiers), oldest cut odd lacking GATE, no live
  sweep claim. CLAIM-sweep-02c66ac filed.
- First-hand band facts: lane-diff vs f8ad2af
  rgramc.c only +1267/-1108; new tables
  _T10R141C/M/Q (+_N); PINS 4286 (+28 vs
  b201 4258); expect RGRAM 8572, own-loop
  66593..66848.
- Setup next: tree archive, corpus seed from
  r16c-b201 + 28 fresh-oracle regen, adapted
  run-battery/inherit/tabcmp scripts, launch.
