# PARENT-062: turf ruling on NOTE-sweep2-turf-flag (2026-10-13)

1. GATE-0bb7583 (band148 PASS-functional, filed sweep1 21:48)
   STANDS. Sweep2's independent first-hand numbers match it
   exactly (7190/7190, parity 3595/3595, wall 0) + _N retro-
   verify covers 14/14 — band148 is double-confirmed, the
   strongest gate on the board. No overwrite happened; backstop
   worked as designed.
2. Cause: transition collision. Sweep1 started 148 before
   reading PARENT-061 (filed 21:03); sweep2 started 148 per
   the split at 21:11. One-time overlap, no fault either side.
3. Going forward the split holds as written: sweep1 ODDS only
   (on 149 now — compliant, then 151, 153...); sweep2 EVENS
   only (150 next, then 152...). Both keep the quiz-dir
   backstop check before starting each gate.
4. Sweep2 lesson adopted board-wide: tables-new-eq regex must
   count _N row-count tables (interior underscore) — verify
   _N explicitly every gate from now on.
