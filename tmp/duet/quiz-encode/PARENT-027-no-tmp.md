# PARENT-027: ABSOLUTE BAN on /tmp (and $TMPDIR-default) writes

Owner call: ZERO project files in /tmp (/private/tmp). 2059 stale files
(~2.8G) just quarantined to NVME ws tmp/from-tmp-20261008/ by parent.

Rules, all seats, effective now:
1. NEVER write /tmp, /private/tmp, /var/folders/... directly.
2. NEVER rely on bare `mktemp` / `${TMPDIR:-/tmp}` defaults. Export
   TMPDIR=/Volumes/NVME/applearchive-cleanroom-ws/tmp/<seat>/ (mkdir first)
   at the top of EVERY shell session and before EVERY battery/probe run.
   tests/smoke.sh + test_rgram.sh + c-battery.sh all honor TMPDIR or take
   an explicit workdir arg — use one.
3. Relocate your own active /tmp files (<2h old, ~50 left, e.g. r14-*
   probes, det*.bin, gc-*): mv them under your NVME seat dir NOW, then
   re-point any open runs. Do not orphan them.
4. Probe binaries + .out/.err/.md5/.bin beds are regenerable — but they
   still live on NVME, never /tmp, while you need them.

Parent pv runs under the same ban (TMPDIR prefix from here on).
Violation = hold your next merge until your /tmp footprint is zero
(find /private/tmp -mmin -120 -user mrowlinson must show none of yours).
