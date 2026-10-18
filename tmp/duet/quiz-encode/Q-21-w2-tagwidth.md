# Q-21 writer2: raven tail-field TAG-width selection rule (10-bit vs 12-bit vs raw-8)

## Bedded (mine, NOTE-15 R4, decode-verified singletons)
- tail pos 96..127 = independent prefix-fields, LSB-first value bits.
- RAW-8bit (pos100/101/104/105): slot=VAL identity, literal-stored.
- 10-bit TAG-01 (pos96,112): slotA=C|((V&3)<<6), slotB=V>>2.
- 12-bit TAG-0000 (pos120): slot32=(V&0xF)<<4, slot33=V>>4.
- ~whole payload = the field array; head-pos fields WIDE/shared (open).

## Ask (behavior-only, derived mechanism)
1. Which (len,off,lit) condition selects TAG-01 vs TAG-0000 vs RAW-8 at a
   tail field — run-len of the literal, (len,off)-joint match token, or
   position/length-code tier? Discriminating bed: which single input knob
   flips one field's width (e.g. extending a literal run past L*, or moving
   a match's (len,off) across a boundary)?
2. What do the tag PAYLOAD bits carry (literal value vs (len,off) parts)?

## Use
- Closes raven match-token byte-identity (last gap pre-matchfinder impl).
