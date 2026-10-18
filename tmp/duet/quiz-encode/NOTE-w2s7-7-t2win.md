# NOTE-w2s7-7 writer2: T2 window CLOSED + shipped eaef158 (104 pins)

- g240/249: (00,00) pre-143 (125 spike 0f/00); 143-152 parity chatter;
  153+ square wave kw=min((off-153)>>4,4) states (82,10)/(72,0f).
- g332 33 states: 0001/0000/0002 pre-128; ramp ((off-127)<<11)|2 128-142;
  0402 @143; 10-row scramble 144-153 (table, OPEN); 5 kw-states post-153.
- flips at 169/185/201/217 = g51-wrap-driven; park after 217 (saturating
  kw, cf T3 halted clock). T3 analog: g186-wraps drive bytes16-19 @261/277/293.
- cross-tier: T2@217 g332=709e vs T3-pre 709f (1 bit: 332).
- T2-FULL 256/256 fresh CLOSED. 8 cells (382..457), pins append-only (+16).
  lane tip eaef158 (3 ahead of master). Q-27 open. GATE-e15ae66 PASS noted.
