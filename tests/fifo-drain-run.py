#!/usr/bin/env python3
# fifo-drain-run.py — run a decode cmd with fifo-drain + timeout.
# Problem: oracle blocks in open() on an extracted fifo until a
# writer end exists (proven: g9p.aar + fifo-mixed.aar hang, fifo
# created, empty stderr, never exit). This wrapper holds every fifo
# under OUTDIR open O_RDWR so the child completes genuinely, voids
# any payload written, and kills on TIMEOUT.
# Usage: fifo-drain-run.py TIMEOUT OUTDIR OUTFILE ERRFILE CMD...
# Exit: child's rc; 124 on timeout (nothing swallowed: partial tree kept).
import os
import stat
import subprocess
import sys
import threading


def drain(path):
    # Reader arm: pairs with our held O_RDWR end immediately, voids
    # anything the child writes so a big payload can't fill the pipe.
    try:
        fd = os.open(path, os.O_RDONLY)
    except OSError:
        return
    try:
        while True:
            try:
                b = os.read(fd, 65536)
            except OSError:
                break
            if not b:
                break
    finally:
        try:
            os.close(fd)
        except OSError:
            pass


def hold_rw(path):
    # Writer arm: O_RDWR succeeds with no peer and pairs with the
    # child's blocking fifo open in EITHER direction (proven
    # black-box: reader arm alone still hangs, O_RDWR hold
    # completes RC=0 — the oracle waits for a writer end).
    # Held till child exit.
    try:
        return os.open(path, os.O_RDWR)
    except OSError:
        return None


def main():
    to = float(sys.argv[1])
    outdir = sys.argv[2]
    outf = sys.argv[3]
    errf = sys.argv[4]
    cmd = sys.argv[5:]
    import time
    with open(outf, "wb") as fo, open(errf, "wb") as fe:
        p = subprocess.Popen(cmd, stdout=fo, stderr=fe, start_new_session=True)
        seen = set()
        held = []
        t0 = time.time()
        while True:
            for dp, dn, fn in os.walk(outdir, followlinks=True):
                for n in dn + fn:
                    fp = os.path.join(dp, n)
                    if fp in seen:
                        continue
                    try:
                        st = os.lstat(fp)
                    except OSError:
                        continue
                    if stat.S_ISFIFO(st.st_mode):
                        seen.add(fp)
                        h = hold_rw(fp)
                        if h is not None:
                            held.append(h)
                        th = threading.Thread(target=drain, args=(fp,), daemon=True)
                        th.start()
            rc = p.poll()
            if rc is not None:
                for h in held:
                    try:
                        os.close(h)
                    except OSError:
                        pass
                print(f"RC={rc} PID={p.pid}")
                return rc
            if time.time() - t0 >= to:
                try:
                    os.killpg(p.pid, 9)
                except ProcessLookupError:
                    pass
                p.wait()
                for h in held:
                    try:
                        os.close(h)
                    except OSError:
                        pass
                print(f"TIMEOUT PID={p.pid}")
                return 124
            time.sleep(0.05)


if __name__ == "__main__":
    sys.exit(main())
