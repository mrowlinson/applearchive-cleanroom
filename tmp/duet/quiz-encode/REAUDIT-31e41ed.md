# REAUDIT-31e41ed cport band118 T10P101 (n<=51976, 708 tiers): PASS

## first-hand (fresh r12 export tree, seat-private build + runs)
- Tree: fresh git-archive export of 31e41ed
  under WS tmp/encode-viewer3/31e41ed/tree-r12
  (seat-private, all data NVME). 6452 PINS
  lines = 6450 + 2 header.
- C build 0 warnings (-O2 -Wall -Wextra -std=c11,
  rc=0, own bin tmp/encode-viewer3/31e41ed/build-r12/
  rgramc 1570392 bytes, built first-hand
  this seat r12).
- `tests/test_rgram_c.sh` own run (RGRAMC=own r12 bin,
  same-seat b209 corpus seed + missing-only fresh-oracle
  regen, fresh py+C execution per pin): RGRAMC-PYID
  3225/3225 covered=3225/3225 RGRAMC-GREEN, rc=0, 0 FAIL.
- `RGRAM_BIN=<own-r12-bin> tests/test_rgram.sh` own run:
  RGRAM-GREEN (6450 PASS, 0 FAIL, rc=0).
- `tests/test_rgram.sh` own run (py): RGRAM-GREEN
  (6450 PASS, 0 FAIL, rc=0).
- C/py PASS-name sets cmp-identical 6450/6450
  (both all-PASS) + py/PINS set-eq 6450/6450.
- own-loop fresh-oracle 51885..51976: 92 pass / 0 fail
  (py+C agree all 92, rc+stdout+stderr identical);
  pins 28/28 (14 pinned cells x closed+sha, fresh .rav
  hashes match PINS). OWN-GREEN rc=0.
- py + PINS + tests byte-identical to writer-merge parent
  25c6f81 (lane diff = src/c/rgramc.c only,
  +1267/-829; non-C diff 0 bytes).
- tables-EQ own script (tables-eq-r12-b118.py, textual
  C-vs-py parse): NEW 10/10 EQ GREEN (AC142 BC122
  QC122 + AM16 BM10 M16 QR4 QT4 S0/S1),
  FULL 1836/1836 skip 0.
- wall-grep lane-diff (rgramc.c, PARENT-032 scope
  cpat|libcompression|depload|dlopen|dylib): 0 hits.
- Ordered: GATE-31e41ed PASS + VERIFY-31e41ed PASS + PV merged
  3023748 on file; CLAIM-viewer3-31e41ed-r12 oldest
  live claim (field clear at claim + pre-filing
  re-check, no rival REAUDIT).

## verdict: PASS (concurs GATE+VERIFY on every count)
