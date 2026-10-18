# REAUDIT-4c9ff15 (viewer2 r11): band196 T10P140 (n<=65548) — PASS

Independent second coverage (band has GATE+VERIFY+PV;
this seat never touched b196). First-hand in fresh
at-commit export tree .../4c9ff15/tree (git archive
4c9ff15), seat-private build, all data NVME.

- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin build-r11/rgramc 1997368 bytes ==
  rival VERIFY's byte count).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r11 bin,
  own-seat corpus seed 4244 hardlinks, fresh py+C
  execution per pin): RGRAMC-PYID 4192/4192
  covered=4192/4192 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r11-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (8384 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (8384 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 8384/8384
  (both all-PASS) — PINS-RGRAM set-eq.
- own-loop fresh-oracle 65457..65548: 92 pass / 0 fail
  (py+C agree CLOSED all 92, rc+stdout+stderr identical);
  pins 30/30 (15 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWNLOOP-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  55a1a81 (lane diff = src/c/rgramc.c only,
  +1559/-1081; 8386 PINS lines = 8384 + 2 header).
- tables-EQ own script (tables-eq-r11.py, textual C-vs-py
  parse): NEW 15/15 EQ GREEN (S0/S1/S2 + AM/AC/BM/BC/
  M/QS/QR/QT/QC; AC _N=76, BC _N=71, QC _N=62).
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- CLAIM-viewer2-4c9ff15-r11 live at filing (no rival
  REAUDIT claim; prior viewer/viewer3 claims consumed
  by filed VERIFY). No FLAG on band.

Verdict: PASS (concurs GATE+VERIFY+PV on every count).
Claim consumed.
