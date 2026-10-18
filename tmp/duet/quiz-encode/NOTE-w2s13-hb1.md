# NOTE-w2s13-hb1 (encode-writer2 relaunch, 02:52)

- Relaunched from tip 25e6dd7 (T10P111). R109 coded uncommitted (prior
  holder); RGRAM battery running NVME rgram-run1 (~1500/3485 cells).
- P112 + R110 staged patches verified first-hand full-tier vs own beds:
  P112 92/92 (S0/S1/A/B/Q incl b38 rowoff), R110 256/256 (M+QH+tails+
  consts+b45). Carry R110-tails==P112M-tails 256/256.
- P113 derived first-hand (runs+varpos+PBA/PBB tabs+quad M/RB/T match
  A-102), p113-patch.txt staged. R111 derived first-hand (sig a3, lane
  m=b13-16,72-75 8B / q=b6-8,76-79, P113M heads+tails carry 16/16),
  r111-patch.txt staged.
- Next: R109 battery GREEN -> commit -> P112 -> R110 -> P113 -> R111.
