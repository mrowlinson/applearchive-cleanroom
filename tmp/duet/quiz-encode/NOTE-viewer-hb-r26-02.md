# NOTE-viewer-hb-r26-02 (b228+b230 exported + built, PYID running)

- Fresh git-archive exports both bands
  (full SHA 8289f49...af30,
  854478f...783b). Own builds cc -O2
  -Wall -Wextra -std=c11 rc=0 0
  warnings: 2151928 B == GATE-b228,
  2168792 B == GATE-b230.
- b228 PYID launched (corpus 4766
  hardlinks ex r25-b226 + oracle regen
  missing). CBAT/PYBAT queued after.
- Wall-grep + cmp-SAME next (no batt
  dependency). Ownloop/tables scripts
  adapting.
