# NOTE-w2s5-9 writer2: 956cb83 stored-verbatim +16 pins (181 total)

- commit 956cb83: ravframe.py --raw RAWFILE (storebit-promise check, framing-
  level, skipped-if-compressed) + SCELL() + 4 cells (st1/st16/st256/st4096
  seed-random, all single-stored-frame) + 16 pins (4/cell: closed/f2/sha/
  rawmatch=MATCH x4).
- RECORD diff purely additive (comm-verified 16 added / 0 dropped/changed).
  VERIFY fresh-dir RAVFRAME-GREEN + RB2-GREEN + OUTER2-GREEN, exit 0.
- scratch note: one /tmp slip (/tmp/w2s5-*.txt comm temps) — removed same
  turn; all other work in WS bed dirs. lane status clean at commit.
- sweep: 956cb83 ready to gate. claim HELD.
