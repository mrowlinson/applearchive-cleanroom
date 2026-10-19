# Q-370 (w2e-r1): T10P851 geometry 312885..313232 (348, first-hand, NO-WAIT)

Range seat P851-1200. Tier cut proceeds on own census; memo CONFIRM async?

## geometry (first-hand, 350-cell census 312885..313234)
All raw108/pay92. PB0 n312885 sig a5040000 NEW; PB1 n312886 sig 65cc0900 NEW
(vs P850 head 6c020000/fca70400 first-hand).
PBA16 n312887..312902 sig 65cc9d00 (shares PB1 b0-1), M9 b36-40,84-87 16/16, consts 81.
PBB10 n312903..312912 sig 257a0800 OWN-SIG, M4 b88-91 10/10, consts 86.
QUAD64 n312913..312976 sig 257a9e00 (shares PBB b0-1): M9 b44-48,84-87 by COL
16/16 row-shared, NO R zone (vpos fully partitioned M9+T4+lencode),
T4 b88-91 by ROW all-4-distinct 7ee4c079/db2a1782/fb2a1782/1b2b1782,
b5 step @312960 lencode-covered, consts 77.
T256 n312977..313232 SINGLE-sig e5e54108: TM9 b51-55,80-83 by COL 16/16 /
TR9 b44-48,84-87 by ROW 16/16 UNPAIRED; b5 steps @313088/313216 lencode-covered;
consts 72.
Next P852 PB0 @313233 sig 65050000 NEW, PB1 @313234 sig 257a0800 (=P851 PBB sig).
Lencode ((n<<1)|1)&0xFFFF 350/350. Battery: staged sweep92 at splice (expect 92/92 CLOSED err 0). Confirm?
