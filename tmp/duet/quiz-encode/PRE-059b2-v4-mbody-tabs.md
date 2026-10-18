# PRE-059b2 M-body tabs (CORRECTION: PRE-059b omitted b6-b10)

- GAP (mine): PRE-059b reported M-body const bytes but MISSED
  b6/b7 16-tabs + b8/b9/b10 patterns. c-seat PRE-059c caught
  them; verified FIRST-HAND below. nothing in 059b was wrong,
  it was incomplete.
- b6: strict 16-tab (period16 ✓ 4 cycles): 4e d9 24 fb 89 c6
  ab 44 81 66 e6 32 dc a1 df 97 (== PRE-059c EXACT).
- b7: strict 16-tab: ab 0b 9b cb db 5b 9b 0b 8b cb cb 5b 6b
  fb 7b 9b (== PRE-059c EXACT).
- b8: plateau-duty 3d/5d/7d (nruns 25, nval 3 ✓). b9: ramp-ish
  f5/f6/fb/00/01/06/0b/0c/11 (nruns 36, nval 9 ✓). b10: 0d/0e
  alternation (nruns 8 ✓).
- regularity (both seats, worth a line): M-body b6 tab values
  == 60-head b6 BAND sequence in order (4e d9 24...); same b7.
  tab prefigures next tier's bands. mechanism OPEN.
