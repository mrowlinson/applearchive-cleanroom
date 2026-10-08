#!/usr/bin/env python3
"""rgram.py -- lzraven zeros-N payload grammar verifier (writer2 turf).

Asserts first-hand grammar rules (NOTE-w2s6-2/3) on oracle bytes:
tier length-code (off<<1)|1, T0/T1 echo placement + formulas, marker
consts, head 3-state, N=125 form-flip. Usage: rgram.py FILE.rav N.
Exit 0 + CLOSED on pass; exit 1 + message on rule break; 2 bad input.
"""
import sys


def bit(p, i):
    return (p[i >> 3] >> (i & 7)) & 1


def grp(p, idx):
    v = 0
    for j, i in enumerate(idx):
        v |= bit(p, i) << j
    return v


def fail(msg):
    print("GRAMMAR-BREAK " + msg)
    return 1


def main():
    if len(sys.argv) != 3:
        print("usage: rgram.py FILE.rav N", file=sys.stderr)
        return 2
    raw = open(sys.argv[1], "rb").read()
    n = int(sys.argv[2])
    if len(raw) < 12:
        return fail("short file")
    pay = raw[12:-4] if len(raw) > 16 else raw[12:]
    if n <= 63:  # stored zeros
        if len(pay) != n:
            return fail("stored paylen %d != %d" % (len(pay), n))
        if pay != bytes(n):
            return fail("stored content not zeros")
        print("CLOSED stored N=%d" % n)
        return 0
    if len(pay) != 44:
        return fail("paylen %d != 44" % len(pay))
    if n <= 127:  # T0
        off = n - 64
        if pay[4] != ((off << 1) | 1):
            return fail("T0 byte4 %02x" % pay[4])
        if pay[8] != 0x07:
            return fail("T0 b8 %02x" % pay[8])
        if bit(pay, 131) != 1 or bit(pay, 290) != 1 or bit(pay, 67) != 0:
            return fail("T0 markers")
        edge = 1 if n >= 125 else 0
        if bit(pay, 226) != edge or bit(pay, 322) != edge:
            return fail("T0 form edge")
        if (pay[0], pay[1]) != ((0x40, 0x00) if n <= 124 else (0x00, 0x04)):
            return fail("T0 head %02x%02x" % (pay[0], pay[1]))
        if n <= 124:
            if grp(pay, (275, 276, 277, 278)) != (off + 3) & 15:
                return fail("T0 echo-low")
            g234 = grp(pay, (234, 235, 236, 237))
            op3 = off + 3
            exp = ((op3 >> 4) & 1) | ((1 - ((op3 >> 5) & 1)) << 1) | \
                (((op3 >> 5) & 1) << 2) | (1 << 3)
            if g234 != exp:
                return fail("T0 echo-mid")
            if grp(pay, (307, 308)) != 0:
                return fail("T0 g307")
            if grp(pay, (325, 326, 327, 329, 330, 331)) != 7:
                return fail("T0 g325")
        else:
            if grp(pay, (234, 235, 236, 237)) != 0:
                return fail("T0e g234")
            if grp(pay, (214, 215, 216)) != 7:
                return fail("T0e g214")
            if bit(pay, 258) != 0:
                return fail("T0e b258")
            if grp(pay, (325, 326, 327, 329, 330, 331)) != 56:
                return fail("T0e g325")
            if grp(pay, (307, 308)) != n - 125:
                return fail("T0e g307")
            want275 = (off + 3) & 15 if n == 125 else 0
            if grp(pay, (275, 276, 277, 278)) != want275:
                return fail("T0e echo-low")
        print("CLOSED T0 N=%d off=%d" % (n, off))
        return 0
    if n <= 255:  # T1
        off = n - 128
        if pay[4] != ((off << 1) | 1) & 0xFF:
            return fail("T1 lencode")
        if grp(pay, (307, 308, 309, 310)) != (off + 3) & 15:
            return fail("T1 echo-low")
        if grp(pay, (270, 271, 272, 273)) != (off + 3) >> 4:
            return fail("T1 echo-high")
        if (pay[0], pay[1], pay[8]) != (0x00, 0x08, 0x08):
            return fail("T1 head")
        for m in (11, 67, 131, 226, 290, 322, 160, 176, 177, 178, 179,
                  193, 194, 332):
            if bit(pay, m) != 1:
                return fail("T1 marker %d" % m)
        print("CLOSED T1 N=%d off=%d" % (n, off))
        return 0
    if n <= 511:  # T2 (length-code only; regime open)
        off = n - 256
        if grp(pay, (32, 33, 34, 35, 36, 37, 38, 39, 40)) != \
                ((off << 1) | 1):
            return fail("T2 lencode")
        print("CLOSED T2 N=%d off=%d" % (n, off))
        return 0
    print("N out of scope", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
