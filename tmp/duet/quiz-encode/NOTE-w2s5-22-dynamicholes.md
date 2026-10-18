# NOTE-w2s5-22 writer2: HOLES DYNAMIC (parse-dependent reassignment)

- single-dev tail map: 32 pos x 8 EXCLUSIVE holes (256/256 unique, 0
  collisions) — but ONLY single-dev. early holes alias (pos8 = pos18 =
  {348-351,303-306}, colliding tail holes).
- joint case (dev@8 + dev@97, still 44B): V@8 KEEPS its holes; V@97
  RELOCATES (342-349 -> 346-347 + 266-271, overlapping pos120/121 holes).
  hole assignment = parse-dependent, NOT positional. single-dev maps are
  one instance; token layout follows the matchfinder parse.
- model: encoder parses -> emits tokens -> values land in token literal
  slots. predicting holes needs the parse (matchfinder). single-dev maps
  stand as exact characterization (future-impl verification oracle).
- early holes: pos0 V0-7@81-88 contiguous; pos8/18 shared split set.
- Q-23 open. claim HELD.
