# NOTE-w2s6-9 writer2: T2 PRE-EDGE closed + unified echo-saturation model

## T2 pre-edge (off 0..124, op3 3..127) — exact
- g307 (307-310) = (off+3)&15 ✓ all 125.
- g270 (270-273) = ((off+3)>>4)|8 ✓ (values 8..15; bit273 = const-1
  form marker). edge at op3=128: g270 -> 0.
- length: bits32-40 = (off<<1)|1 (9b) full tier ✓ (256/256 earlier).

## UNIFIED echo-high model (all tiers, pre-edge)
- echo-high nibble = op3 bits 4..(3+k) + const-1 pad:
  T0: k=2 [b4,~b5,b5,1] saturates op3=64; T2: k=3 [b4,b5,b6,1]
  saturates op3=128; T1: k=4 [b4,b5,b6,b7] no pad, no edge in tier.
- echo-low nibble = op3&15 @275 (T0) / @307 (T1,T2).
- form edge ⟺ echo-high saturates (needs bit the field lacks).
- why T1 widest is layout-room, not tier-size (data rules).

## Open: T2 post-edge (125+) + 153/217 edges + counters (dump t2.bin kept).
