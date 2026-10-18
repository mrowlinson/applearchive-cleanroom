# NOTE-w2-hb-s20-73 (writer2 r2 @8aaeccb): A-297..299 consumed, Q-295 filed

- Consumed A-297/298/299: P227/P228/P229
  all CONFIRM geometry (streak 96) +
  prose/count fixes:
  - P227: 2 prose labels (B10 ==PB1 group,
    quad VPOS ex-b5 20). Tables stand.
  - P228: PBC M10/V11/C73, PBA C75, T
    V19. BUG FOUND (own): analyzer
    prints + Q-prose undercount consts
    by 1 on b5-const groups (ex-b5 set).
  - P229: b83 0x60 notation + PBA C77 +
    PBC C70 (same bug).
- First-hand audit: ALL staged tables
  position-exact + 84-VPOS counts exact
  (P228 75/73/63/65, P229 77/70/63/66,
  P230 75/71/63/68). Tables need NO
  restage. Fixed comment-only headers
  (p228/229/230 stage+patch).
- Rule adopted: consts = 84-VPOS always
  (b5 in consts iff b5-const); VPOS
  partitions list b5 iff varies.
- Amended Q-294 pre-answer (PBA 75 / PBB
  M12/V13/C71 / quad V20-ex-b5... filed
  V21-ex-b5-partition C63).
- P231 @97125..97472 staged GREEN
  first-hand (analyzer + patch + try-p231
  sweep 348/348; T88 needs base paylen
  += 88, noted in patch). Filed Q-295
  (correct 84-VPOS counts: 76/71/64/70;
  b19 ADD-vs-XOR ambiguity flagged).
- P232 census next. No joint DONE.
