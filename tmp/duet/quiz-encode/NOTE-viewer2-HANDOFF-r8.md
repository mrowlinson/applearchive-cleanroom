# HANDOFF viewer2 r8 -> r9 (band189 VERIFY done, run cap reached)

- Filed VERIFY-fac36c9: PASS (band189 T10R134,
  n<=64412, 850 tiers). All legs first-hand with
  r8 seat-private build (build-r8/rgramc, rc=0,
  0 warnings): PYID 4101/4101, CBAT 8202/8202,
  PYBAT 8202/8202, set-eq 8202/8202, own-loop
  256/256 + pins 22/22, tables-EQ 2/2,
  diff rgramc.c-only +1220/-1061, wall 0.
- GATE-first ordered: GATE-fac36c9 PASS-functional
  (sweep-r13) was on file before VERIFY.
- Quiz: Q max 361, A-361 on file, diff 0,
  nothing owed.
- CORRECTION for future rounds: band189 sealed
  count is 4101 (PINS `g-z*-closed`), NOT 4102;
  r8 round-plan figure was off by one. 8202 =
  2 x 4101 consistent everywhere (incl. GATE).
- Run cap reached (1 VERIFY b187 r7 + 1 VERIFY
  b189 r8 + 2 REAUDITs). r9: fresh claim turf;
  standby REAUDIT candidates e5ed337 (b180),
  267690f (b170), f01b41d (b168) were identified
  but NOT started (no GATE-hold filler needed).
- Seat state: WS tmp/encode-viewer2/fac36c9/
  (tree/ HEAD fac36c9 clean, build-r8/,
  work-pyid/ corpus 4101 .rav, *-r8.logs).
  r8 bin NOT cmp-identical to r7 bin (byte 1209,
  same size; separate-link metadata) — functional
  identity proven by batteries, not bytes.
