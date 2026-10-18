# PARENT-065: quota block state + relaunch plan (2026-10-15 14:57 EDT)

- ALL encode seats dark: spark quota dead until 2026-10-19,
  wonder quota dead until 2026-10-15T23:22:28Z (19:22 EDT).
  Relaunch attempts at 14:32 EDT all died API 429 at launch.
  Seats are DROPPED-quota, not dropped-silent: successor
  relaunch is physically blocked until a quota window opens.
- Plan: one-shot cron fires 19:24 EDT Oct 15 to relaunch all
  5 seats (viewer/writer2/cport/sweep/sweep2) + PV workflows
  on muse-wonder-1.0, one workflow per seat, STAY-ALIVE
  briefs. Any watch turn after 19:22 EDT does the same if
  the cron lands late. Spark seats resume Oct 19 if the
  owner prefers spark (PARENT-064 stays in force).
- Quiz: geometry Q backlog Q-321..Q-36x open since Oct 14
  06:26+ (viewer dark). Viewer-r6 first duty on relaunch:
  drain oldest-first, answer or MOOT-with-cause; silence
  banned. No parent answers (wall).
- Parent-side meanwhile: merges 155 (228c013) + 156
  (d219188) landed cmp-IDENTICAL; PV-157/159 running
  parent-side; merges 157-159 follow on PV PASS.
- Monitor v2 armed (lane tips + quiz filename set only).
