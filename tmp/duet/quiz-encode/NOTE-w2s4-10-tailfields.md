# NOTE-w2s4-15 (renumbered; filename still NOTE-w2s4-10-tailfields.md): raven tail = 32 independent prefix-fields (8/10/12-bit, LSB-first); A-22 ack

## R1: within-tier append = LOCAL-2B (length-bump); tier-edge = GLOBAL restructure
- n=64->65, 128->129: ndiff=2 (no re-parse). n=820->821: ndiff=31 + len44->48. n=2212->2213: ndiff=48 + len48->52.
- REVISED: parse = LOCAL/deterministic (greedy), NOT DP-global. Tier-edges = ENCODING-MODE switches (length-code upgrade -> bitstream resync).

## R2: bimodal jacobian -> sharp boundary @96
- pos<=95: GLOBAL resync (ndiff 9..25, shrinking 25->9 as pos->95). pos>=96: LOCAL 1-4B.
- Boundary EXACT at 96 (95:9-span-global vs 96:[41,42]).

## R3: tail-map 96..127 = piecewise-linear slot-walk (SEQUENTIAL bitstream, per-pos independent fields)
- Runs: 100-102->5,6,7; 104-106->13,14,15; 107-109->16/17,17/18,18/19; 112-113->20/21,22/23; 116-117,120-121,124-125 similar +1/pos; wraps at 98->30,100->5,118->0.
- Pair-interaction: NONE (3/3 adjacent pairs = exact union of singletons) -> NO re-tokenize, fields INDEPENDENT.

## R4: field formats decoded (value-readout 7pos x 6vals)
- RAW-8bit (pos100/101/104/105, slots5/6/13/14): slot=VAL IDENTITY -> literal-stored.
- 10-bit TAG-01 (pos96:[41,42], pos112:[20,21]): slotA=C|((V&3)<<6), slotB=V>>2. C=0x10@41, 0x01@20 (tag at BITS5-4 vs 1-0 -> BIT-packed, not byte-aligned).
- 12-bit TAG-0000 (pos120:[32,33]): slot32=(V&0xF)<<4, slot33=V>>4.
- Value bits = literal byte LSB-FIRST (low-bits-early). TAG widths {8,10,12} = prefix code; tag meaning OPEN (run-len? (len,off)-joint?).
- Coverage: 41/44 payload bytes touched by tail-pos singletons -> ~whole payload is the field array; head-pos fields WIDE/shared (OPEN).

## R5: ack A-22 (Q-20 CLOSED except pin-fork; my B-13 recount now consistent with N2)
- Taking N4(i): JOINT FIT (one rule + latent per-chunk counts over 516 SCR) next bitmap turn; N4(ii) many-tie bed queued.
- L2750 INSHA mismatch (mine ae35 vs A-21 138c, identical tables) still needs viewer re-hash.

## Next: bit-level tparse (LSB-first segmentation by tag) -> (len,off,lit) per field; head-field widths; 96B-block test (zeros-256 periodicity).
