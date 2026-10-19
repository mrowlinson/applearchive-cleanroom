# Q-363 (w2d-r1): T10P502 geometry 191433..191780 (348, first-hand, NO-WAIT)

Range seat P501-850. Tier cut proceeds on own census; memo CONFIRM async?

## geometry (first-hand, 350-cell census 191433..191782)
All raw104/pay88. PB0 n191433 sig b8020000 REPEAT-sig P501 (33 body bytes differ);
PB1 n191434 sig 92720500 NEW (links C10).
PBA16-PLAIN n191435..191450 sig 92225800, M9 b40-42,46,47,80-83 16/16, b5-const d7, consts 77.
C10 n191451..191460 sig 92720500 links PB1 (24 body bytes diverge PB1-vs-C10[0]),
M4 b84-87 10/10, b5-const d7 (no step), consts 82.
QUAD88 n191461..191524 sig 92725700: M8 b52-55,80-83 row-shared 16/16,
R4 b84-87 rows f5ad17b1/346daad7/546daad7/0b6e99d8 all-4-distinct (r1/r2 share last 3B 6daad7),
b5 step @off27, consts 74.
T88-RING n191525..191780 sig 24297705: TM8 b52-55,80-83 by COL 16/16 / TR8 b48-51,76-79
by ROW 16/16 UNPAIRED; b5 d8+(o>=91)+(o>=219); b84-87 ring-const 2b6e99d8; consts 70.
Next P503 PB0 @191781 sig bc020000 NEW, PB1 @191782 sig 83780500 NEW.
Battery: staged sweep 348/348 CLOSED err 0. Confirm?
