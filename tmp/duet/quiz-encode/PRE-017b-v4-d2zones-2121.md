# PRE-017b D2 zones 1773..2212 @48B + 2121 singleton + L10-lo continuity (w2 accel)

## map (zeros beds, v5d2 440 rows first-hand)
- D2a 1773..1800: transition head, 27 var. 4 sub-phases (1773 / 1774 /
  1775-1790 / 1791-1800). tail b32..47 = D-body consts EXACT (frame
  still D-shaped); head b0..b31 re-frames.
- D2b 1801..2047: 33 var, split @1865. 1801..1864 = 4x16-row bands
  (b14/15/21/22/23/28 16-cycle; b24 4-cycle 4b/6b/8b/ab; b29/b30/b31
  16-ramps). 1865..2047 = b26/b34/b35 16-cycles w/ 1-2-row plateaus
  (same shape as D-body b11/b19); b28/b30 16-plateau counters (+0x16/+8).
- D2c 2048..2212: 43 var (only b6/7/8/9/20 const). 2048..2120 continues
  1865-regime (b28/b30 counters run on: 78..d0 / 9b..bb). 2123..2138
  16-band, 2139..2148 10-band, 2149..2212 64-tail (b46/b47 strict
  16-cycles e8..93 / fe..7c x4; b40/b41 16-cycles).
- D END 2212/2213 (paylen 48->52, v5slip). 48B total span 1517..2212.

## 2121 singleton: dip-class event
- N=2121 deviates in ALL 43 varying bytes (b0 48 vs 94, b10 41 vs 01,
  b11 8c vs 00, ...); 2120 + 2122 normal (2122 = own transition row:
  b12 6e, b13 44, b14 22, b15 8b then rejoin). paylen stays 48.
- treat as dip/edge grammar, not noise (single-N, full-frame, det).

## L10-lo (b4) continuous +2/row across ALL 1773..2212
- db@1773 -> ... -> 49@2212, no break (wraps ff->01 @1791/92, 1919/20,
  2175/76). extends PRE-016b: L10-lo unbroken 1517..2212.

## b5 plateaus: 25@1773-1791 (19) / 26@1792-1919 / 27@1920-2047 /
  40@2048-2175 / 41@2176-2212 (128s after 19-head).
