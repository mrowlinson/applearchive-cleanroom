# NOTE-w2s2-4 writer2: 14c859f flip cells 103/103, doubles closed

- commit 14c859f: FLIP() helper + 16 cells (rule+sha), pins 74->106
  lines, diff purely additive, every rule+size matches bed rows.
  verify run: 103/103 PASS exit 0 OUTER2-GREEN (log
  $WS/bat-w2s2-verify.log). zero writer1 files touched.
- doubles CLOSED: lz4 tiny last-S=62/first-C=63 (S<=62, C63..274,
  S>=275); bitmap window last-S=50/first-C=51 + last-C=70/first-S=71
  (C51..70), RT-OK 3/3 via adapter aar-decode. puzzle for impl-time:
  bitmap/lz4 tiny-store + bitmap window are non-monotonic in n —
  decision is NOT a single size threshold (mechanism open, behavior
  pinned both edges).
- shift totals: 2 commits (53add85 hygiene, 14c859f flips), Q-13 open
  (no A-13 yet), battery 71->103, ~500 oracle cells, zero wall contacts.
- next: raven/bitmap multi-block structure walk (magic-scan offsets,
  -b splits, payload leads). claim HELD, polling.
