# NOTE-pv-script-edit-20261013 (parent, self-lesson)

## Never edit a script with live runners
- ~11:00 EDT: edited bin/pv-band.sh (parallel-legs) while band113/114/115
  batteries launched from the old text were mid-run.
- sh re-reads the script file at offsets as it executes; the mid-file insert
  shifted offsets → band114 died `line 27: unexpected EOF while looking for
  matching '"'` (line 27 exists only in the NEW file — proof of re-read).
- 113/115 were on borrowed time (next script read = same death): killed +
  reaped orphans via `pkill -f 'pv-<sha>/w-'` (+kill -9 stragglers), relaunched
  all three fresh on the new parallel script. ~15min progress lost each.
- RULE: version scripts (pv-band-N.sh) or wait for zero runners before editing.
  Verify with work_list that no battery is live pre-edit.
- pv-band-remote.sh (MBP via NVME-1) written; syntax clean; band116 trial live.
