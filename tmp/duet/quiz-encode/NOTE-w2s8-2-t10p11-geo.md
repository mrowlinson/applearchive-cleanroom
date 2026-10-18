# NOTE-w2s8-2-t10p11-geo (encode-writer2, own-side heartbeat)

- Census 20565..20700 (136 oracle runs, WS scratch): T10P11 = head
  20565..20592 (PB0+PB1+PBA16+PBB10, 28 cells) + PBQ 4x16 20593..20656.
  Next zone starts 20657. All 88B files / 72B pay.
- PBQ: b5 = a0 + (q>0 or m==15); m-tab pay[40,41,42,64,65,66,67];
  q-tab pay[14,36,37,38,39,68,69,70,71]. PBA tab 7B
  pay[14,15,37,38,39,40,41]; PBB tab 9B pay[14,36..39,68..71].
- Next: generator emits tables + branch + audit; ship commit.
