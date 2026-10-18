# PRE-062c 60-regime 6389..6644: minimal 12-field + tabs (60 campaign)

## only 12 var (b4/5/28-32/36-40; 48 const; v5aj 256 rows @60B)
## 16-tabs from 6389 (verify all 16 cycles)
- b36: 4e 14 dc f2 a8 6e 84 9a ff c5 98 91 59 88 4e 2e (15).
- b37: fcx4 bfx4 fcx2 bfx2 fc bf bfx2 fc (2 values, duty 4/4/2/2/1/1/2).
- b38: ef db 77 7f ff eb f3 fb 53 3f df c7 63 13 ff 3f (14).
- b39: 7e a9 ae ae b3 de de de ef 1a 1e 1f 24 25 4f 50 (13).
- b40: b5x9 d5x7 (2 values).
- b28/30: 16-plateaus (15/16 runs). b29/31: 14 runs (16/32-mix).
  b32: ONE flip @6597 (b6->d6). b5: 128s 51/52/53 (@6389/6400/6528).
- b0 75 / b4 ramps. b21 duty ENDS exactly @6388/6389 (5d->dc frozen;
  coincides with b0 17->75 edge — true regime boundary, not survey seam).
