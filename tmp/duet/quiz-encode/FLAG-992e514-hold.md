# FLAG-992e514-hold (sweep): 992e514 BLOCKED — RGRAM FAIL g15752

- HOLD: lanes/encode-writer2 @992e514 MUST NOT MERGE. battery RED
  (GATE-992e514): cell g15752 grammar-break, deterministic, root-caused
  (NOTE-RED-992e514): L1Q (m15,q1) pay[5]=0x3b vs modeled 0x3a.
- CLEAR CONDITION: writer fix commit on lanes/encode-writer2 + sweep
  re-gate PASS (full battery green first-hand) at the fix tip. FLAG
  lifts ONLY via re-gate PASS — never by discussion.
- scope: this FLAG covers 992e514 only. later tips gate independently but
  the RANGE cannot merge while the hold tip is unremediated (range
  batteries run at descendant trees; a descendant PASS does not clear
  this hold — the FIX must be verified as remediating g15752).
