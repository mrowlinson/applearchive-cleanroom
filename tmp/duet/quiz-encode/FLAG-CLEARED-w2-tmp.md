# FLAG-CLEARED w2-tmp-cleanup @53add85 (sweep, first-hand)

- condition: git rm -r --cached tmp/scratch-* + no
  tmp/scratch-* in tip: MET (19 paths removed, ls-tree
  grep 0; .gitignore += tmp/scratch-*/). hygiene re-gate
  GREEN (see GATE-53add85; behavior 71/71 re-verified
  fresh, not carried).
- FLAG-w2-tmp-cleanup CLEARED. w2 line holds NOTHING from
  sweep. PARENT-005 complied; future tmp/scratch-*
  tips FAIL on land per the standing rule.
