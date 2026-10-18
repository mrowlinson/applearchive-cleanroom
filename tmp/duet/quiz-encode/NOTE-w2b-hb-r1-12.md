# NOTE-w2b-hb-r1-12 + HANDOFF (r1 exit @~112 calls, refill please)
- LANDED: P136 8fb7560 (8156 REC DET 14/14), P137 e81d47b (8184 REC DET 14/14).
  All RGRAM-GREEN + SMOKE-GREEN first-hand, local-only, never pushed.
- WIP (uncommitted, DIRTY): P138 code+test+PINS, RECORD RGRAM-GREEN +26/-0
  first-hand (rec-p138.log). Refill: verify (sh tests/test_rgram.sh) + DET 13
  (64761 64762 64763 64778 64779 64786 64788 64789 64800 64805 64821 64837 64852)
  + smoke + commit msg: T10P138 (64761..64852): PB0+PB1+PBA16+PBB10+QUAD
  single-sig rows0==3 xor26 (8210 REC, DET 13/13).
- STAGED (NVME seat dir /Volumes/NVME/applearchive-cleanroom-ws/tmp/encode-writer2b/):
  beds+an+tables+ins for P139 (13 cells: 65109 65110 65111 65126 65127 65134 65136
  65137 65148 65153 65169 65185 65200), P140 (15 cells: 65457 65458 65459 65474 65475
  65476 65483 65484 65485 65496 65501 65517 65533 65536 65548), P141 (16 cells:
  65805 65806 65807 65813 65814 65822 65823 65824 65831 65832 65833 65844 65849
  65865 65881 65896), P142 (14 cells: 66153 66154 66155 66170 66171 66172 66179
  66180 66181 66192 66197 66213 66229 66244).
- Convention: run insNNN.py, syntax check, 92-sweep, append DET cells to
  test_rgram.sh tail, RECORD, verify, smoke, commit. Lower-bound guards
  (64xxx <= n <= ...) are INTENTIONAL (R-gap on this lane).
- Claim file CLAIM-encode-writer2b.md stays (remove ONLY at joint DONE).
