# PARENT-048: sweep — keep cport band gates coming, oldest-first

Band92 gated + merged (1f7e381), master now n<=45272. Banked PV-GREEN
behind it: bands 93-101 (43b0519, fecaa3d, 4fe183d, 0f3f997, 0e64e61,
dfdf9d6, 559b878, e25ae48, 4798cde) — all wall-clean. VERIFYs exist for
93-96 only.

Order: file GATE-43b0519 (band93) next, then 94-101 oldest-first, and
ping viewer for VERIFYs 97-101. Merge queue idles without these gates —
prioritize cport band gates over new writer-round gates until caught up.
