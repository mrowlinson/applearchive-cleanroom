# NOTE-sweep-221 — INCIDENT: overbroad pkill killed other lanes (~00:35)

- Sweep seat ending: ran `pkill -f tests/test_rgram` to reap
  own 5 orphaned sweep-band children. Pattern matched OTHER
  seats' command lines too. Killed ~15 procs, incl:
  encode-viewer (eadf7cc/19ab457/2c55063/8f6c326 work,
  pyid, work-c), encode-writer2 (bat-w2s13-p109rec x2),
  encode-cport work (rgram127-fh x2, pyid127).
- All affected batteries need RERUN; partial logs under
  their own WS dirs are suspect from 00:35. Sweep's own
  filed GATEs (b102-b110) unaffected — all legs completed
  and verified before the pkill.
- Cause: pkill -f without seat-path scoping. Fix for next
  seats: scope kills to own dir
  (`pkill -f tmp/encode-sweep/<sha>/`) or track PIDs.
- Apologies to viewer/writer2/cport seats.
