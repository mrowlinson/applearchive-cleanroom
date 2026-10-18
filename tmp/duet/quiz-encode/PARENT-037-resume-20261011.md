# PARENT-037: RESUME 2026-10-11 — session died of transport errors, relaunch all encode seats

1. CAUSE: 3 PV children died 10-09 18:23-18:26 (api.meta.ai transport
   errors after retries, not project state). Parent went idle; ~430
   watch fires queued unprocessed; session cancelled 10-11 01:45.
   All seats dark ~63h. No code fault anywhere.
2. STATE: decode JOINT DONE (no relaunch). w2 tip 1018e76 T10R74
   n≈43184 (~90% of ~48k est). cport tip b8b1278 (w2-R73 import,
   n<=42836). master merged+verified thru band46 n=33092 (~69%);
   GATEs on master thru R64/P65/band71 + hb143. Remote at band44
   (local ahead; push on owner order only, never unasked).
3. BACKLOG: merge bands 47..84 oldest-first as each greens (PV
   re-drive 47/48/49 first; stale tmp/wt-pv-* rebuilt fresh).
   w2 frontier R75+ toward ~48k. cport chase w2 (P75+R74 = band85+).
4. CLAIMS: all stale — successors OVERWRITE own claim at start,
   never yield to them.
5. STANDING: PARENT-027 /tmp ban + TMPDIR=NVME seats absolute.
   PARENT-032 lane-diff wall scope. PARENT-034 stale-Q MOOT rule.
   PARENT-035 hwaccel AFTER 100% only. PARENT-036 seats never
   commit on master / in main checkout — file records, parent lands.
6. FIRST-Q RULE: writer first Q ≤10min. Viewer oldest-first,
   VERIFY newest commits, silence banned.
