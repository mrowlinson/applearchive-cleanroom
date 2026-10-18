# NOTE-cport-06 attempt#2 heartbeat: band5 plan (master chase, gated only)

- seat relaunched per PARENT-031 @eb766e3 (band4, 303 tiers, n<=23000).
- survey: master 91a852c rgram = 321 tiers thru T10R19 (n<=24044);
  +18 = T10PI0/PI1/PIA/PIB/PIQ + R17 + PJ0/PJ1/PJA/PJB/PJQ + R18 +
  PK0/PK1/PKA/PKB/PKQ + R19. w2 tip 5d92e24 P21 (letter L, n<=24136,
  +5) UNGATED -> NOT in band5 (band6 after gate).
- plan: partial-merge master (rgram.py + PINS only, 5cdc204 pattern)
  with RGRAM+SMOKE first-hand, then regen rgramc.c --upto 24044,
  C-BUILD 0w + RGRAMC-PYID full + RGRAM-GREEN (py + C) + SMOKE/UNITS,
  commit band5 + NOTE-cport-07.
- transpiler IfExp OK (T10R19 b14 ternary covered). corpus extend +110.
- sweep: c1/c2/c3/c4 all still ungated; queue oldest-first per PARENT-031.
