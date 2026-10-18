# PRE-027b 4209-dip response: fragile-restore confirmed (numbers new)

- pos0 -> 52->56 RESTORE (content destroys short form, tier restored ✓).
- pos-mid -> 52->60 JUMP (+8, mask-or-jump class per A-35).
- tail d=2/d=1: samelen 16/43 diffs (no paylen move = transparent ✓ A-35).
- neighbors (4208/4210): pos0 samelen big-rewrite (213/199 diffs, no
  jump); mid 56->60 jump. dip-only signature = pos0 restore.
