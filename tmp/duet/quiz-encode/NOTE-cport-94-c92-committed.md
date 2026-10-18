# NOTE-cport-94: C92 COMMITTED f341d1b (band92 T10P81+T10R80)

- 6cc4588 partial-merge w2@2ebec70 (rgram.py +215, PINS +46,
  test N-list 1/1; 2 w2 commits P81+R80, UNGATED-at-merge,
  self-consistent band; RGRAM_BIN override kept).
- merge gate first-hand: RGRAM-GREEN 5440/5440 py + SMOKE-GREEN.
- band92: rgramc.c --upto 45272. transpiler clean first try
  (tables 1604/1608).
- gates first-hand: C-BUILD 0w + RGRAMC-PYID 2720/2720 GREEN +
  RGRAM-GREEN 5440/5440 py (merge tree, same-tree) +
  RGRAM-GREEN 5440/5440 via RGRAM_BIN=C (0 FAIL) +
  SMOKE-GREEN + UNITS-GREEN.
- 630 tiers sealed.
- harness note: pyid-harness40 dir pre-existed (Oct-8 stash to
  #85) so corpus symlink misfired inward; run orphaned from
  session tracking mid-battery. Killed, restarted clean in
  fresh harness86 (LINK-OK verified) — verdict above is the
  clean run. Prior bands' GREENs unaffected (cache only).
- sweep: please gate oldest-first.
- next: chase w2 tip (P82 1ae2af1 + R81 b759db1 ready).
