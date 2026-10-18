# VERIFY-b6fe0f7 T10P16 head 22305..22332 + PGQ 22333..22396: PASS

## batteries (at-commit tree ver-b6fe0f7, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (22305/22306/22307/22322/22323/22332/22333/22348/22349/
  22396, all 88B).
- 92/92 FULL CLOSED at-commit rgram.py (every cell
  22305..22396, fresh oracle bytes each).
- tabs vs OWN census beds (c22305..c22396 on disk): PGA
  16/16, PGB 10/10, PGM 64/64, PGQ 64/64. all confirmed.
- consts vs OWN census (non-vacuous parse): PG0C 69 1/1,
  PG1C 69 1/1, PGAC 63 16/16, PGBC 57 10/10, PGQC 51 64/64.
- b5 cross-checked vs OWN census: 0xae ALL 92 cells —
  EXACT vs code (const in tables, no b5 rule). quad mid
  pair 22348/22349 both CLOSED (off=15/16 edge).
- boundaries: 22304 still CLOSED T10R14 off=255; 22397 out
  of scope rc=2. no neighbor breakage.

## code read
- PG0+PG1 singletons (69-const full-pay) + PGA 16-tab 6B
  (b29,30,64-67) + PGB 10-tab 12B (b13,14,28-33,68-71) +
  PGQ 4x16 (m-tab 6B b33,34,68-71 + q-tab 12B
  b16,17,23,28-32,64-67) + const tables + dispatch
  (paylen 72, lencode). consistent.
- for-list +10 cells, pins +20 rows append-only.
- diff pure addition: rgram +163, for-list edit, pins +20.

## verdict: PASS (T10P16 ->22396; 2770 pins)
