# PRE-059b M-zone 5949..6040: cluster + TIER EDGE 6041 (56->60B)

## sectioning (v5ah, 92 rows 56B, 47 var; 60B from 6041)
- 5949: transition literal (b0 be/b1 ee/b2 0c).
- 5950: transition (b0 7e/b1 f1/b2 e4 = K-body values).
- 5951..5966: 16-row (b0 80/b1 0d/b2 4f; b11 33; b19 cd).
- 5967..5976: 10-row (b0 7e/b1 f1/b2 e4 — K-body repeat).
- 5977..6040: 64-body (b0 e7/b1 17/b2 4f; b11 3e; b19 a1;
  b20-31 const; b52-55 const ad/b2/af/5e).
- edges>=8: 5950/5951/5967-5977 chatter + bands 5993/6009/6025.

## body knobs from 5977
- b5: 16-tab (8e 0e ae 4e 8e ee ce 8e ee ce ce 6e 6e ce
  2e 6e) + low-nibble +1 @6016 (xe->xf). b4 ramp.
- b42/b43/b50/b51: 16-bands @5993/6009/6025.
- TIER EDGE 6041: 56B->60B (60-tier head recon exists: v5i +
  PRE-046b/047b). M = last 56-tier cluster (5949..6040).
- one commit 5949..6040, then 60-tier campaign starts.
