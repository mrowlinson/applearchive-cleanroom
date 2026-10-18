# NOTE-cport-hb87: r7 battery running, blobs verified fh

- mrg-b178-py-r7 fresh run in progress (~1650 PASS at check, staged P131 state). stale r6 log left untouched for reference.
- blobs re-verified FIRST-HAND (not on handoff word): staged rgram.py MATCH 3556c57, staged PINS MATCH 3556c57, staged test.sh = w2 + RGRAM_BIN hook (2-line diff confirmed).
- procedure reconfirmed for band178 cut: rgram_gen.py no-upto -> regen-b178-fh.c (must become new rgramc.c; b177 regen IDENTICAL to committed), seat-private build 0 warnings, pyid.py full (seed corpus from pyidb177-fh), RGRAM C+py GREEN, SMOKE/UNITS re-run, NOTE + commit in lane style.
- no joint DONE. never push.
