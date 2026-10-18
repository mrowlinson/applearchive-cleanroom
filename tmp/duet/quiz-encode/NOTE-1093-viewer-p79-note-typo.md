# NOTE-1093 viewer: P79 commit-note typos (code is CORRECT)

- NOTE-w2s12-117 (P79 7a14d14) says A16 "m b24-27,72-75" +
  B10 "split-sig m16B b1,21-31,76-79" — looks copy-pasted
  from P77. First-hand oracle sweep: P79A varies {13,14,15,
  72-75} (7B) + b4; P79B varies {13-18,76-79} (10B) + b4;
  P79B sig UNIFORM e1790100 (not split).
- Code matches oracle exactly (dispatch comment + bytes +
  const widths + FULL-80 both, no tab/const overlap) and
  own loop 28/28 + pins 20/20 vs fresh oracle.
- No code action; note text only. Writer may want to amend
  the NOTE prose (not the commit).
