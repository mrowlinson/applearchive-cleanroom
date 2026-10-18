# NOTE-w2s6-3 writer2: T0/T1 ECHO CLOSED + skeleton correction + form-flip

## T1 echo = FULL off+3 (G2 corrected, lossless here)
- bits 307-310 = (off+3)&15 all 128 ✓; bits 270-273 = (off+3)>>4 all 128
  ✓ (vals 0..8). G2's 272-273 subsumed (top 2 of >>4 nibble). G2 "middle
  bits nowhere / lossy" was wrong input family or partial scan — CLOSED
  for zeros-N T1. byte4 = (off<<1)|1 + bit39 = O6 (7-bit off ✓ all 128).

## T0 echo (pre-edge off 0..60): low @275-278, mid-differential @234-236
- g275 = (off+3)&15 (off 0..61; frozen 0 @62,63).
- g234 = [op3b4, ~op3b5, op3b5, 1] EXACT off 0..60 (bit5 differential!).
- head: bit6 (N=64..124) / bit10 (N=125..127) / bit11 (T1) — 3 states.

## Form-flip at N=125 (op3=64), head flips at N=128
- T0-post (125..127) tail == T1 tail in 5/7 groups (g214=111, g234=0000,
  b258=0, g275=0000, g322=1); differ: g325 low-3 (111 vs 000000) + head
  b1 (04 vs 08). g325: 111000 -> 000111 -> 000000. g307 @125..127 =
  edge-relative counter (0,1,2).

## CORRECTION to NOTE-w2s5-24 skeleton map
- bits 209-211 = 0 @N=128 (verified), NOT 1. True 1-bits: 214,215,216
  (byte26=0xC0, byte27=0x01). 214-216 = 111 iff T1 or N>=125 (form flag).
- T1 markers const-1: 11,32,67,131,160,176-179,193-194,226,290,322,332.

## T2 (256..511): 85 varying bits (new regime; tail holes 334-349 N-driven)
- tools: bed-w2s6-seg/segbed1..4.py + logs (own, oracle-exec only).
