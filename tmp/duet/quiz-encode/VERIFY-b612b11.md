# VERIFY-b612b11 T10P17 head 22653..22680 + PHQ 22681..22744: PASS

## batteries (at-commit tree ver-b612b11, WS tmp/encode-viewer)
- 10/10 new-pin shas MATCH independent oracle re-runs
  (22653/22654/22655/22670/22671/22680/22681/22696/22697/
  22744, all 88B).
- 92/92 FULL CLOSED at-commit rgram.py (every cell
  22653..22744, fresh oracle bytes each).
- tabs vs OWN census beds (c22653..c22744 on disk): PHA
  16/16, PHB 10/10, PHM 64/64, PHQ 64/64. all confirmed.
- consts vs OWN census (non-vacuous parse): PH0C 69 1/1,
  PH1C 69 1/1, PHAC 61 16/16, PHBC 60 10/10, PHQC 52 64/64.
- b5/sig cross-checked vs OWN census: head b5 {0xb0:3,
  0xb1:25} (b5 in PHA tab, singletons const); quad b5
  {0x31:36, 0xb1:28} (b5 in PHM tab — no rule needed);
  quad per-row sigs (4 distinct a957*) inside PHQ tab.
  quad mid pair 22696/22697 both CLOSED (off=15/16).
- boundaries: 22652 still CLOSED T10R15 off=255; 22745 out
  of scope rc=2. no neighbor breakage.

## code read
- PH0+PH1 singletons (69-const full-pay) + PHA 16-tab 8B
  (b5,25,46,47,64-67) + PHB 10-tab 9B (b2,15,45-47,68-71,
  sig byte in tab) + PHQ 4x16 (m-tab 7B b5,6,7,64-67 +
  q-tab 10B b2,3,15,45-47,68-71) + consts + dispatch
  (paylen 72, lencode). consistent.
- for-list +10 cells, pins +20 rows append-only.
- diff pure addition: rgram +164, for-list edit, pins +20.

## verdict: PASS (T10P17 ->22744; 2806 pins)
