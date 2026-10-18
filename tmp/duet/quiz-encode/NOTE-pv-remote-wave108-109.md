# NOTE-pv-remote-wave108-109 (parent, 03:22 EDT)

Speedup: PV batteries parallelized 3-wide. Local (M5 Max
18-core): band106 eadf7cc + band107 ee6b913 via pv-band.sh.
Remote MacBookPro18,4 (10-core, load 14-21 owner-active):
band108 f8fe14f submitted via easy-ssh (job pid 23990,
--cpus 4, ~/aa-pv/pvband108, build confirmed compiling
-O2 -Wall -Wextra -std=c11). Band109 b718d47 tree
extracted ~/aa-pv/pvband109, queued — submit when 108
DONE or MBP load drops. Pull: scp *.log to NVME
tmp/pv-remote108/, grep first-hand, then merge oldest-first.
ABORTED 03:28 per owner NVME-only order (MBP has no NVME
mount; mnt-nvme-tb is MBP local disk): remote job killed,
pvband108/109 + tgzs removed, 0 procs/files left. Bands
108+109 relaunched LOCALLY (3-wide with 107, all NVME).
TB UPDATE 10:45: smb://169.254.50.49/NVME mounted on MBP
at /Volumes/NVME-1 (AppleID/keychain auth, verified same
volume + writable). Future remote batteries use NVME-1
paths. Band113 remote attempt via .local ABORTED: 37min
for 11s CPU (SMB latency + MBP load 23 from lzmesh jobs);
relaunched locally. Use MBP remote only when its load is
low AND via NVME-1.
