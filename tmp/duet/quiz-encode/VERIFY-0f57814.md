# VERIFY-0f57814 cport band1 stored..T2 (n<=511): PASS

## first-hand (at-commit tree ver-0f57814, seat-local build)
- C build: `make BUILDDIR=seat/build-0f57814 rgramc` rc=0, 0 warnings
  (-O2 -Wall -Wextra -std=c11).
- parity `tests/test_rgram_c.sh` (own run, RGRAMC=seat binary):
  RGRAMC-PYID 31/31 covered=31/1411 => RGRAMC-GREEN. every
  covered N: py vs C rc + stdout + stderr byte-identical.
- python `tests/test_rgram.sh` (own run, fresh oracle bytes):
  RGRAM-GREEN (tail PASS g-z23000-closed, PASS g-z23000).
- code-read: rgramc.c 346 lines, header + Makefile target + parity
  test + RGRAM_BIN override. table values spot-verified vs
  src/rgram.py (_T2SCRAM 0x8dbe=36286 first-3 exact).
- wall-grep (ghidra/disasm/dylib/dlopen/ctypes/decompile): 0 hits
  in rgramc.c/rgramc.h. hygiene: 13 .aar = pre-existing selfgen
  fixtures (same count in parent), 0 new artifacts.
- scope: N>511 => "N out of scope" rc=2 (counted uncovered, never
  compared — correct per test contract).

## verdict: PASS (band1 31/31 py-identical, python RGRAM-GREEN)
