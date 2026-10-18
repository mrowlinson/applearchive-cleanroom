# PRE-245b 84: DIP BAND 10 SPLIT @52929 (mode change)

## census (v5d103 first-hand, 76x 80B + 16x 84B gap)
- band 10 = 52929..53020 SPLIT: 80B @52929-52930
  + 84B gap @52931-52946 (16 rows) + 80B @52947-
  53020 (76x 80B total, not 92).
- opener @52929 = fca20900 (SAME as band 9);
  b0-2 FROZEN 48/f8/6c from 52930; b3 eras 13
  (52930-52947, CONTINUES ACROSS the gap) ->09
  @52948 (19-flip) ->8d @52957 (50-flip).
- gap rows b0-3 frozen 01000000; 84B resumes
  @53021. MODE CHANGE at band 10: bands now
  admit 84B interior blocks. next band: 53277
  (watch: split persist?).
