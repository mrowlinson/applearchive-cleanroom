# FLAG-CLEARED w1-pbze-store-rule (cea6ba0 satisfies all 3 conditions)

- HOLD placed: FLAG-w1-pbze-store-rule (writer NOTE-5 "comp<unc" wrong).
- clear evidence @cea6ba0: (1) 15/16 rule IN code first-hand
  (pbze.py len(fr)*16<=len(ch)*15). (2) window spanned: committed
  battery cells don't isolate the window, but sweep razor 33/33
  byte-EQ spans it twice incl comp==unc stored sides (see
  GATE-cea6ba0) + rule 3-source closed (viewer bisect, writer
  100/100, w2 K-bisect). (3) re-gate green: PBZE 4/4 + RAWENC 8/8
  + pins 4/4 + roundtrips, first-hand pristine.
- HOLD LIFTED. cea6ba0 mergeable on sweep authority (viewer PASS
  concurs). non-blocking ask: fold 1 razor cell (name-ladder flip)
  into test_pbze.sh so the boundary is regression-pinned in-repo.
