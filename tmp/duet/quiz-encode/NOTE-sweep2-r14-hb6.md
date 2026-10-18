# NOTE-sweep2-r14-hb6 (ext5 green, PYID re-run underway)

- Cport tip still 7c2e8d4 b185 (checked pre-PYID).
- Interim first-hand:
  - own-loop ext5 61373..61720 (b173+b174 span):
    348/0, pins 50/50
  - continuous regression now 61373..63460: 2088 N
    green, 294/294 pins (b173-b184)
  - PYID re-run with seat-private b184 binary over
    4038 sealed pins underway (corpus seeded from
    r13 cache, py+C freshly executed).
- Next: PYID verdict, then sleep/poll for b186.
