# NOTE-w2s4-5 writer2: raven FRAME rule (F3=PAYLOAD*4096+STORE 7/7)

- own ct-oracle tiny matrix (12 beds, WS bed-w2s4-order/raven/):
  magic 2b00caec + F2(4B) + F3(4B) + payload + trailer 00000000(4B).
- F3 = PAYLOADLEN*4096 + STOREBIT, EXACT 7/7 single-frame:
  stored (1B/8B-det/1K-rand/100K-rand): 4097/32769/4096001/
  409600001 = raw*4096+1 (payload==raw size; content TBD).
  compressed (64B-zero/pat,1K-zero): 180224/212992/196608 =
  44/52/48*4096 (payload<raw). bit0 = STORE flag.
- F2 = 0 thru 1K; 0x0c000000 @100K stored, 0x40000000 @1M-zero.
  needs 4K..128K stored sweep. 1M-zero (196B) breaks F3 rule
  (100 vs payload 180) -> multi-frame? interior TBD.
- STORE rule OPEN: 8B-zero STORED, 64B-zero COMPRESSED (44B);
  64B-pat COMPRESSED (52B); 1K-rand STORED. boundary 8..64 +
  random-64..1000 queued.
- ORDER hunt parked for viewer (Q-18); even/odd-DESC globally
  dead (both 18, neither 61). Q-17/Q-18 open. claim HELD.
