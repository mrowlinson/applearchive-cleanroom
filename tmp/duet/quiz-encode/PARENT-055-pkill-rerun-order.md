# PARENT-055: pkill incident — rerun killed batteries + scoped-kill rule

Sweep seat's shutdown `pkill -f tests/test_rgram` (~00:35)
matched other lanes' command lines, killed ~15 procs
(NOTE-221). Affected batteries MUST RERUN from scratch;
partial logs after 00:35 suspect:
- VIEWER: band102-106 VERIFY batteries (eadf7cc/19ab457/
  2c55063/8f6c326 work, pyid, work-c). VERIFY102+ re-drive.
- WRITER2: bat-w2s13-p109rec x2.
- CPORT: rgram127-fh x2, pyid127.
Sweep's filed GATEs b102-b110 unaffected (legs completed
pre-pkill). GLOBAL RULE all seats: NEVER bare `pkill -f
<test-name>` — scope kills to own seat dir
(`pkill -f tmp/encode-<seat>/...`) or track own PIDs.
Violation = seat restart.
