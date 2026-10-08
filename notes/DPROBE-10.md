# DPROBE-10 midchain presence + content chunks + drop-last (M-fix)

## Presence (rule B)
- present ⟺ whole>=524288 AND avail>=(kcut-1)*65536.
- whole-side: u2 (262144) + u3 (393216) ABSENT 3/3; u4
  (524288 exact) present-empty 2/2. Threshold inclusive.
- avail-side: mc4 (114000 < 3*64K) ABSENT; m2c (507577 >=
  6*64K) present. Window (114000,507577] open, both sides far.
- avail = n-end (short item blob-region bytes); whole = decoded
  bytes before failing block (raw-sum, P1 zeros proven).

## Drop-last (E4)
- clean parse + truncated tail (complete .aar + 10 zero bytes):
  last item dropped, prefix FULL, fc normalized. 2 vectors x5.
- C+proto: midchain && shortidx==NONE -> skip items[n-1].

## Content chunks (30+ vectors, stable zones 2-9x each)
- nch = #{j : whole >= 786432+j*262144}; chunk j held ⟺
  end <= (nch-j)*262144; bytes = held*262144 DAT-prefix,
  capped at avail/DATlen. Exact-prefix proven (s64 cmp IDENT).
- W0 = 786432 inclusive (window (720896,786432]; round-pattern:
  u6-whole EXACTLY 786432 -> 1 chunk; u8q1 EXACTLY 1M -> 2).
- E0 = 262144 @whole<=917504 (window (260419,264515], 4/4
  both sides, no race); E0 = 524288 @whole 1M (n-formula;
  500-c8 end 512323 holds 3/3, margin 12K -> NOT shipped).
- E1 = 262144 modal. Multi-file chunk1 RACY (MT flush):
  100K 4/6 twos, 150K 3/4, 200K 2/6, 130K+170K 4/4 (luck);
  pooled 15/19. Single-file chunk1 stable 9/9. Mine = modal 2.
- battery: cxG (100K-c8) exists-only; all other cells in
  stable zones, margins 28K-217K. E1 zone (201,100K) unexplored.

## Killed theories
- pure-whole (m2c: 917504 -> 0); pure-avail (N=8 720573 -> 1
  vs k11 720695 -> 0, 122B inversion); round-half-up (k11/k15
  split); sum-gate (cA 1382077 -> 1 vs cB 1527485 -> 0).

## Unpinned / follow-up
- n>=3 chunks (whole>1.25M): formula extrapolated, no vector.
- E4-tiny (Q-020, viewer-side). -t1 determinism of E1 race.
- presence-avail window above; W0 window above (64K-block steps
  cannot split; battery avoids interiors).
