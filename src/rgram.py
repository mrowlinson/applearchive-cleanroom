#!/usr/bin/env python3
"""rgram.py -- lzraven zeros-N payload grammar verifier (writer2 turf).

Asserts first-hand grammar rules (NOTE-w2s6-2/3, NOTE-w2s7-2/3) on
oracle bytes: tier length-code (off<<1)|1, T0/T1 echo placement +
formulas, marker consts, head 3-state, N=125 form-flip, T2 regimes,
T3 halted clock + cascade table. Usage: rgram.py FILE.rav N.
Exit 0 + CLOSED on pass; exit 1 + message on rule break; 2 bad input.
"""
import sys

# T3 bytes16-19 cascade rows, off 235..244 (literal table, formula OPEN).
_T3CASC = ("80004208", "68063ef7", "c607beff", "a70bbeff", "880fbeff",
           "ed153ef7", "4b17beff", "2c1bbeff", "0d1fbeff", "72453ef7")
# T3 bytes16-19 settled states: 245-260, 261-276, 277-292, 293-308.
_T3P245 = ("d046beff", "b14abeff", "924ebeff", "f7543ef7")
# T2 g332 scramble rows, off 144..153 (literal table, formula OPEN).
_T2SCRAM = (0x8dbe, 0x1386, 0x9d42, 0x230a, 0xacc6, 0x328e, 0xbc4a,
            0x4212, 0xcbce, 0x5196)
# T2 post-lock window states by kw=min((off-153)>>4,4).
_T2W32 = (0x5196, 0xdb52, 0x611a, 0xead6, 0x709e)
_T2W240 = ((0x82, 0x10), (0x72, 0x0f), (0x82, 0x10), (0x72, 0x0f),
           (0x82, 0x10))
# N=1077 dip-44 payload literal (formula OPEN).
_T4DIP1077 = ("780000066b0000000c0000000e00000060dd170dc40078000600e001"
              "048060840000000001000f000658b8fd")
# N=1078 post-dip resync row literal (1 row, formula OPEN).
_T4B1 = ("010000006d0000006c0024a1000000c00e00f03160dd170dc4007808"
         "86c7f37b8a0120180000000001000f000658b8fd")
# T4B3 bytes36-39 rows, off 274..283 (literal table, formula OPEN).
_T4B3TAB = ("4380168a", "35044f81", "07084f81", "d90b4f81", "ab0f4f81",
            "51148c78", "50174f81", "221b4f81", "f41e4f81", "9a438c78")
# T4C bytes37/38/46/47 16-periodic table, key (off-348)&15 (OPEN why).
_T4CTAB = ("8c07f5dd", "9c0765cf", "ac07d5c0", "bc0745b2", "bc0745f2",
           "cc07b5e3", "dc0725d5", "ec0795c6", "fc0705b8", "fc0705f8",
           "0c0875e9", "1c08e5da", "2c0855cc", "3c08c5bd", "3c08c5fd",
           "4c0835ef")
# T4D1 post-C transition rows, off 604..605 (literals, formula OPEN).
_T4D1 = ("06000000230300006c003c84000000c00e00f0e160dd170dc4007808"
         "86eff8bd69018060305de323640078000658b8fd",
         "80010000250300000c007cd100003c000e0000eb24dc838f06c043f0"
         "86eff8bd69014cd7247b6bac83c6434d065f823c")
# T4D3 bytes5-10 rows, off 622..631 (literal table, formula OPEN).
_T4D3TAB = ("231db8f00fc2", "633648f006c2", "7b5448f006c2", "937248f006c2",
            "5b8000f0fdc1", "7b9e00f0fdc1", "ebcc48f006c2", "03eb48f006c2",
            "1b094af006c2", "4b18ded0f4c1")
# T4E1 b11/b19 16-periodic tables, key (off-696)&15 (OPEN why).
_T4E1T11 = (0xc5, 0xcd, 0xd5, 0xd5, 0xdd, 0xe5, 0xe5, 0xed, 0xf5, 0xf5,
            0xfd, 0x05, 0x0d, 0x0d, 0x15, 0x1d)
_T4E1T19 = (0x51, 0x6a, 0x83, 0x83, 0x9c, 0xb5, 0xb5, 0xce, 0xe7, 0xe7,
            0x00, 0x19, 0x32, 0x32, 0x4b, 0x64)
# T4F D2a transition rows, off 952..953 (literals, formula OPEN).
_T4F12 = ("06040000db25c5866ff1e08b00003c000e0000eb24dc838f06c043f0"
          "86eff8bd69014cd724a7d63e83c6434d065fa6fc",
          "d2110100dd25c5866ff1202f00a0fcc3eeaa4ee08a37f7e0003c041f"
          "86eff8bd69014cd724a7d63e83c6434d065fa6fc")
# T4F D2a3 bytes25-26 rows, off 954..969 (literal table, formula OPEN).
_T4F2526 = ("7c76", "7c77", "3c80", "3c81", "3c82", "3c83", "3c84", "3c85",
            "3c86", "3c87", "3c88", "fc90", "fc91", "fc92", "fc93", "fc94")
# T4F D2a4 bytes24-29 rows, off 970..979 (literal table, formula OPEN).
_T4F2429 = ("3cfc276a6b0c", "833c48262b0c", "19bca3e3cb0b", "ecbc51262b0c",
            "943c33a28b0b", "387ca6e3cb0b", "ed3ca7e3cb0b", "c07c55262b0c",
            "56fcb0e3cb0b", "1dfc37a28b0b")
# T4G D2b1 band consts (b14/15/21/22/23/28), key (off-980)>>4 (OPEN why).
_T4GBAND = ((0x5a, 0x26, 0xee, 0x9b, 0x07, 0x61),
            (0xb2, 0xe3, 0xae, 0x8e, 0x77, 0x5e),
            (0x62, 0x26, 0x0e, 0x89, 0x3f, 0x61),
            (0x02, 0x62, 0x8e, 0x82, 0x8f, 0x5a))
# T4G D2b1 16-tables for b29/b30/b31, key (off-980)&15 (OPEN why).
_T4GB29 = (0x30, 0xe0, 0x90, 0x40, 0xf0, 0xa0, 0x50, 0x00, 0xb0, 0x60,
           0x10, 0xc0, 0x70, 0x20, 0xd0, 0x80)
_T4GB30 = (0xfc, 0xfc, 0xfd, 0xfe, 0xfe, 0xff, 0xe0, 0xe1, 0xe1, 0xe2,
           0xe3, 0xe3, 0xe4, 0xe5, 0xe5, 0xe6)
_T4GB31 = (0x1d, 0x5d, 0x9d, 0xdd, 0x1d, 0x5d, 0x9f, 0xdf, 0x1f, 0x5f,
           0x9f, 0xdf, 0x1f, 0x5f, 0x9f, 0xdf)
# T4H D2b2 16-tables for b26/b34/b35, key (off-1044)&15 (OPEN why).
_T4HT26 = (0xd3, 0xd3, 0xd5, 0xd7, 0xd7, 0xd9, 0xd9, 0xdb, 0xdd, 0xdd,
           0xdf, 0xdf, 0xe1, 0xe3, 0xe3, 0xe5)
_T4HT34 = (0x80, 0x80, 0xc0, 0x00, 0x00, 0x40, 0x40, 0x80, 0xc0, 0xc0,
           0x00, 0x00, 0x40, 0x80, 0x80, 0xc0)
_T4HT35 = (0x6c, 0x7c, 0x71, 0x67, 0x77, 0x6c, 0x7c, 0x71, 0x66, 0x76,
           0x6c, 0x7c, 0x71, 0x66, 0x76, 0x6b)
# T4J singletons N=2121/2122 (literals; 2121 zeros-only per PRE-021b).
_T4JSING = ("4847040093408a0df0e2418c00a0fcc3eeaa36d708aeeec124fc228b"
            "0976c7ef69014cd724a7d63e83c6434d0667a6fc",
            "947f180195408a0df0e201006e44228b57b5b916088e845fe94416f8"
            "b07d7f47e9b4fc774aa1a9b5683cd4940667a6fc")
# T4J c4 bytes40-45 rows, off 1318..1327 (literal table, formula OPEN).
_T4JC4 = ("e07cb2bfeb08", "b03cb2356b08", "d57c75f20b08", "a7bc027aab08",
          "e6fca4b0cb07", "c93c78f20b08", "f1bcb6356b08", "97bcb7356b08",
          "c47c82f20b08", "6b7c83f20b08")
# T4J c5 bytes40/41/46/47 16-table, key (off-1328)&15 (OPEN why).
_T4JT5 = ("6ba2e8fe", "eba2437b", "aba3b4be", "0ba4f8ff", "eba4807e",
          "4ba5c4bf", "cba51f3c", "8ba6907f", "eba6ebfb", "6ba72f3d",
          "2ba8b7bb", "8ba8fbfc", "6ba9837b", "cba9c7bc", "2baa0bfe",
          "0bab937c")
# T4J c5 band consts (b2/3/27/37/38/39/44), key (off-1328)>>4 (OPEN why).
_T4JBAND = ((0x78, 0x8d, 0x81, 0x60, 0x92, 0x3f, 0x43),
            (0xb8, 0xbc, 0x01, 0x00, 0x97, 0xa7, 0x40),
            (0x98, 0x9e, 0x21, 0x40, 0x91, 0x4f, 0x45),
            (0x18, 0x9c, 0x21, 0x40, 0x9c, 0x2f, 0x3c))


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
    if len(pay) not in (44, 48):
        return fail("paylen %d" % len(pay))
    if n <= 127:  # T0
        if len(pay) != 44:
            return fail("T0 paylen")
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
        if len(pay) != 44:
            return fail("T1 paylen")
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
    if n <= 511:  # T2 (NOTE-w2s6-9/10: pre-edge echo + regimes)
        if len(pay) != 44:
            return fail("T2 paylen")
        off = n - 256
        if grp(pay, (32, 33, 34, 35, 36, 37, 38, 39, 40)) != \
                ((off << 1) | 1):
            return fail("T2 lencode")
        op3 = off + 3
        g307 = grp(pay, (307, 308, 309, 310))
        g270 = grp(pay, (270, 271, 272, 273))
        g51 = grp(pay, (51, 52, 53, 54))
        if off <= 124:
            if (pay[0], pay[1], pay[2], pay[8]) != (0x00, 0x10, 0x00, 0x09):
                return fail("T2 pre-head")
            if g307 != op3 & 15 or g270 != ((op3 >> 4) | 8):
                return fail("T2 pre-echo")
        elif off == 125:
            if (pay[0], pay[1], pay[2], pay[8], g307) != \
                    (0x10, 0x00, 0x00, 0x09, 0):
                return fail("T2 r125")
        elif off == 126:
            if (pay[0], pay[1], g307) != (0x00, 0x08, 1):
                return fail("T2 r126")
        elif off <= 152:
            if (pay[1], pay[2], pay[8], g307) != (0x80, 0x00, 0x09, 1):
                return fail("T2 regA")
        elif off <= 216:
            if (pay[1], pay[2], pay[8]) != (0x00, 0x08, 0x0d) or \
                    g51 != (off - 153) & 15:
                return fail("T2 regB")
        elif off == 217:
            if (pay[0], pay[1], pay[2], pay[8], g51) != \
                    (0x00, 0x00, 0x80, 0x0d, 0):
                return fail("T2 piv217")
        else:
            if pay[0] != (((off - 217) & 15) << 4) or \
                    (pay[1], pay[2], pay[8]) != (0x00, 0x80, 0x0d):
                return fail("T2 regC")
        g240 = grp(pay, tuple(range(240, 248)))
        g249 = grp(pay, tuple(range(249, 254)))
        if off == 125:
            ew = (0x0f, 0x00)
        elif 143 <= off <= 152:
            ew = (0x82, 0x10) if off & 1 else (0x72, 0x0f)
        elif off >= 153:
            ew = _T2W240[min((off - 153) >> 4, 4)]
        else:
            ew = (0x00, 0x00)
        if (g240, g249) != ew:
            return fail("T2 window")
        g332 = grp(pay, (332, 334, 336, 337, 338, 339, 340, 341, 342, 343,
                         344, 346, 347, 348, 349, 350))
        if off <= 124:
            e32 = 0x0001
        elif off == 125:
            e32 = 0x0000
        elif off <= 127:
            e32 = 0x0002
        elif off <= 142:
            e32 = ((off - 127) << 11) | 2
        elif off == 143:
            e32 = 0x0402
        elif off <= 153:
            e32 = _T2SCRAM[off - 144]
        else:
            e32 = _T2W32[min((off - 153) >> 4, 4)]
        if g332 != e32:
            return fail("T2 w332")
        print("CLOSED T2 N=%d off=%d" % (n, off))
        return 0
    if n <= 820:  # T3 (NOTE-w2s7-2/3: halted clock C + cascade table)
        if len(pay) != 44:
            return fail("T3 paylen")
        off = n - 512
        if grp(pay, tuple(range(32, 42))) != ((off << 1) | 1):
            return fail("T3 lencode")
        if pay[5] != (off >> 7):
            return fail("T3 b5")
        c = min(off + 7, 225)
        if grp(pay, (5, 6, 7, 8)) != (c & 15):
            return fail("T3 clock")
        if pay[1] != (((c >> 3) & 1) | ((c == 224) << 7)):
            return fail("T3 b1")
        if grp(pay, (52, 53, 54, 55)) != (((c >> 4) + 2) & 15):
            return fail("T3 g5255")
        lit = 0 if off <= 217 else \
            (0x17 if off == 218 else (0x18 if off <= 234 else 0x1c))
        if pay[0] != (((c & 7) << 5) | lit):
            return fail("T3 b0")
        if pay[2] != (0x60 if off == 218 else 0):
            return fail("T3 b2")
        if pay[3] != (0x01 if off <= 216 else
                      (0x00 if off <= 218 else
                       (0x06 if off <= 244 else 0x60))):
            return fail("T3 b3")
        if pay[6] != ((((c >> 4) + 2) & 15) << 4):
            return fail("T3 b6")
        if pay[8] != (0x0e if off <= 216 else
                      (0x0a if off == 217 else 0x0b)):
            return fail("T3 b8")
        for b, v in ((7, 0), (9, 0), (10, 0), (11, 0), (13, 0), (14, 0),
                     (21, 0), (25, 0), (28, 4), (32, 0), (33, 0), (34, 0),
                     (35, 0), (36, 1), (37, 0), (38, 0x0f), (39, 0),
                     (40, 6), (41, 0x50)):
            if pay[b] != v:
                return fail("T3 const %d" % b)
        if pay[12] != (0x0c if off <= 216 else
                       (0x08 if off == 217 else 0x0e)):
            return fail("T3 b12")
        if pay[15] != (0x80 if off == 217 else 0):
            return fail("T3 b15")
        if pay[20] != (0x01 if off <= 218 else
                       (0x25 if off == 235 else 0x05)):
            return fail("T3 b20")
        if pay[22] != (0x0f if off <= 218 else 0xf0):
            return fail("T3 b22")
        if pay[23] != (0 if off <= 244 else (((off - 245) & 15) << 2)):
            return fail("T3 b23")
        p245 = off >= 245
        if pay[24] != (0x0a if p245 else 0x06):
            return fail("T3 b24")
        if pay[26] != (0x00 if p245 else 0xe0):
            return fail("T3 b26")
        if pay[27] != (0x1e if p245 else 0x01):
            return fail("T3 b27")
        p217 = off >= 217
        if pay[29] != (0x80 if p217 else 0x00):
            return fail("T3 b29")
        if pay[30] != (0x60 if p217 else 0x82):
            return fail("T3 b30")
        if pay[31] != (0x84 if p217 else 0x20):
            return fail("T3 b31")
        if pay[42] != (0xb8 if p217 else 0x27):
            return fail("T3 b42")
        if pay[43] != (0xfd if p217 else 0x38):
            return fail("T3 b43")
        b16 = pay[16:20]
        if off <= 219:
            if b16 != bytes(4):
                return fail("T3 cascade0")
        elif off <= 234:
            cc = off - 219
            if b16 != bytes((0, ((cc & 7) << 2) | ((cc & 8) << 3), 0, 0)):
                return fail("T3 byte17")
        elif off <= 244:
            if b16.hex() != _T3CASC[off - 235]:
                return fail("T3 cascade")
        elif off <= 260:
            if b16.hex() != _T3P245[0]:
                return fail("T3 p245")
        elif off <= 276:
            if b16.hex() != _T3P245[1]:
                return fail("T3 p261")
        elif off <= 292:
            if b16.hex() != _T3P245[2]:
                return fail("T3 p277")
        elif b16.hex() != _T3P245[3]:
            return fail("T3 p293")
        print("CLOSED T3 N=%d off=%d" % (n, off))
        return 0
    if n <= 1076:  # T4 plateau A (NOTE-w2s7-11: unified L10 + 1024 flip)
        if len(pay) != 48:
            return fail("T4A paylen")
        off = n - 821
        if grp(pay, tuple(range(32, 42))) != (((n << 1) | 1) & 0x3FF):
            return fail("T4A lencode")
        if pay[5] & 0xFC != 0:
            return fail("T4A b5hi")
        f = off >= 203
        if pay[0] != (0x0D if f else 0x06):
            return fail("T4A b0")
        if pay[8] != (0x6C if f else 0x2B):
            return fail("T4A b8")
        if pay[11] != (0x00 if f else 0x80):
            return fail("T4A b11")
        if pay[15] != (0xC0 if f else 0xE0):
            return fail("T4A b15")
        if pay[45] != (0x58 if f else 0x50):
            return fail("T4A b45")
        if pay[19] != (0x20 if (off >> 3) & 1 else 0x00):
            return fail("T4A b19")
        if pay[27] != ((off >> 4) << 2):
            return fail("T4A b27")
        if pay[31] != (0x1E | ((off & 7) << 5)):
            return fail("T4A b31")
        for b, v in ((1, 0), (2, 0), (3, 0), (6, 0), (7, 0), (9, 0),
                     (10, 0), (12, 0), (13, 0), (14, 0), (16, 0x0e),
                     (17, 0), (18, 0), (20, 0x55), (21, 0x56), (22, 0xbe),
                     (23, 0xff), (24, 0x05), (25, 0), (26, 0xf0),
                     (28, 0x0a), (29, 0), (30, 0), (32, 0x08), (33, 0),
                     (34, 0x08), (35, 0x46), (36, 0), (37, 0), (38, 0),
                     (39, 0), (40, 0x01), (41, 0), (42, 0x0f), (43, 0),
                     (44, 0x06), (46, 0xb8), (47, 0xfd)):
            if pay[b] != v:
                return fail("T4A const %d" % b)
        print("CLOSED T4A N=%d off=%d" % (n, off))
        return 0
    if n == 1077:  # dip-44 literal (formula OPEN)
        if len(pay) != 44:
            return fail("dip1077 paylen")
        if pay.hex() != _T4DIP1077:
            return fail("dip1077 bytes")
        print("CLOSED DIP44 N=1077")
        return 0
    if n <= 1168:  # T4 plateau B (NOTE-w2s7-13/15: B1..B5 dispatch)
        if n <= 1077:
            print("N out of scope", file=sys.stderr)
            return 2
        if len(pay) != 48:
            return fail("T4B paylen")
        off = n - 821
        if grp(pay, tuple(range(32, 42))) != (((n << 1) | 1) & 0x3FF):
            return fail("T4B lencode")
        if pay[5] & 0xFC != 0:
            return fail("T4B b5hi")
        if off == 257:
            if pay.hex() != _T4B1:
                return fail("T4B1 bytes")
            print("CLOSED T4B1 N=%d" % n)
            return 0
        if off <= 273:
            j = off - 258
            if pay[37] != (((j & 7) << 2) | ((j & 8) << 3)):
                return fail("T4B2 b37")
            consts = ((0, 0x10), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0),
                      (8, 0x6c), (9, 0), (10, 0x7c), (11, 0xd1), (12, 0),
                      (13, 0), (14, 0), (15, 0xc0), (16, 0x0e), (17, 0),
                      (18, 0), (19, 0xeb), (20, 0x24), (21, 0x10),
                      (22, 0x14), (23, 0xa1), (24, 0x06), (25, 0xc0),
                      (26, 0x43), (27, 0xf0), (28, 0x86), (29, 0x47),
                      (30, 0xf9), (31, 0x3b), (32, 0x0a), (33, 0x02),
                      (34, 0), (35, 0x82), (36, 0), (38, 0), (39, 0),
                      (40, 0x05), (41, 0), (42, 0xf0), (43, 0),
                      (44, 0x06), (45, 0x58), (46, 0xb8), (47, 0xfd))
            tag = "T4B2"
        elif off <= 283:
            if pay[36:40].hex() != _T4B3TAB[off - 274]:
                return fail("T4B3 tab")
            consts = ((0, 0x0d), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0),
                      (8, 0x6c), (9, 0), (10, 0x3c), (11, 0x08), (12, 0),
                      (13, 0), (14, 0), (15, 0xc0), (16, 0x0e), (17, 0),
                      (18, 0xf0), (19, 0xe1), (20, 0x60), (21, 0xdd),
                      (22, 0x17), (23, 0x0d), (24, 0xc4), (25, 0),
                      (26, 0x78), (27, 0x08), (28, 0x86), (29, 0xef),
                      (30, 0xf8), (31, 0xbd), (32, 0x69), (33, 0x01),
                      (34, 0), (35, 0xc1), (40, 0x25), (41, 0),
                      (42, 0xf0), (43, 0), (44, 0x06), (45, 0x58),
                      (46, 0xb8), (47, 0xfd))
            tag = "T4B3"
        elif off <= 331:
            k = (off - 284) >> 4
            j = (off - 284) & 15
            if pay[33] != (0x41 | ((k & 1) << 7)):
                return fail("T4B4 b33")
            if pay[34] != (0x82 | ((k >> 1) & 1) | ((9 - 3 * k) << 2)):
                return fail("T4B4 b34")
            if pay[35] != (0xD0 | (k + 1)):
                return fail("T4B4 b35")
            if pay[42] != (0x07 | ((j & 7) << 5)):
                return fail("T4B4 b42")
            if pay[43] != ((j >> 3) & 1):
                return fail("T4B4 b43")
            consts = ((0, 0xe0), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0),
                      (8, 0x0c), (9, 0), (10, 0x7c), (11, 0xd1), (12, 0),
                      (13, 0), (14, 0x3c), (15, 0), (16, 0x0e), (17, 0),
                      (18, 0), (19, 0xeb), (20, 0x24), (21, 0xdc),
                      (22, 0x33), (23, 0x05), (24, 0x06), (25, 0xc0),
                      (26, 0x43), (27, 0xf0), (28, 0x86), (29, 0xef),
                      (30, 0xf8), (31, 0xbd), (32, 0x69), (36, 0x05),
                      (37, 0x7c), (38, 0x30), (39, 0x42), (40, 0x01),
                      (41, 0x80), (44, 0x0a), (45, 0x80), (46, 0x85),
                      (47, 0xdb))
            tag = "T4B4"
        else:
            j = off - 332
            if pay[42] != (0x07 | ((j & 7) << 5)):
                return fail("T4B5 b42")
            if pay[43] != ((j >> 3) & 1):
                return fail("T4B5 b43")
            consts = ((0, 0xd0), (1, 0), (2, 0), (3, 0), (6, 0), (7, 0),
                      (8, 0x0c), (9, 0), (10, 0x7c), (11, 0xd1), (12, 0),
                      (13, 0), (14, 0x3c), (15, 0), (16, 0x0e), (17, 0),
                      (18, 0), (19, 0xeb), (20, 0x24), (21, 0xdc),
                      (22, 0x33), (23, 0xe2), (24, 0x06), (25, 0xc0),
                      (26, 0x43), (27, 0xf0), (28, 0x86), (29, 0xef),
                      (30, 0xf8), (31, 0xbd), (32, 0x69), (33, 0xc1),
                      (34, 0xb8), (35, 0x14), (36, 0x05), (37, 0x7c),
                      (38, 0x30), (39, 0x42), (40, 0x01), (41, 0x80),
                      (44, 0x0a), (45, 0x80), (46, 0x85), (47, 0xdb))
            tag = "T4B5"
        for b, v in consts:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n <= 1424:  # T4 plateau C (NOTE-w2s7-16: 16-table + block counter)
        if len(pay) != 48:
            return fail("T4C paylen")
        off = n - 821
        if grp(pay, tuple(range(32, 42))) != (((n << 1) | 1) & 0x3FF):
            return fail("T4C lencode")
        if pay[5] & 0xFC != 0:
            return fail("T4C b5hi")
        if bytes((pay[37], pay[38], pay[46], pay[47])).hex() != \
                _T4CTAB[(off - 348) & 15]:
            return fail("T4C tab16")
        if pay[42] != ((off - 348) >> 4) or pay[43] != 0:
            return fail("T4C b42")
        for b, v in ((0, 0x20), (1, 0x0d), (2, 0), (3, 0), (6, 0), (7, 0),
                     (8, 0x0c), (9, 0), (10, 0x7c), (11, 0xd1), (12, 0),
                     (13, 0), (14, 0x3c), (15, 0), (16, 0x0e), (17, 0),
                     (18, 0), (19, 0xeb), (20, 0xc4), (21, 0xdc),
                     (22, 0x33), (23, 0x05), (24, 0), (25, 0x3c),
                     (26, 0x04), (27, 0x1f), (28, 0x86), (29, 0xef),
                     (30, 0xf8), (31, 0xbd), (32, 0x69), (33, 0x81),
                     (34, 0x78), (35, 0xd5), (36, 0x25), (39, 0x23),
                     (40, 0), (41, 0x3c), (44, 0x0a), (45, 0x80)):
            if pay[b] != v:
                return fail("T4C const %d" % b)
        print("CLOSED T4C N=%d off=%d" % (n, off))
        return 0
    if n <= 1516:  # T4 plateau D (NOTE-w2s7-17: D1..D4 dispatch)
        if len(pay) != 48:
            return fail("T4D paylen")
        off = n - 821
        if grp(pay, tuple(range(32, 42))) != (((n << 1) | 1) & 0x3FF):
            return fail("T4D lencode")
        if off <= 605:
            if pay.hex() != _T4D1[off - 604]:
                return fail("T4D1 bytes")
            print("CLOSED T4D1 N=%d off=%d" % (n, off))
            return 0
        if off <= 621:
            cc = off - 606
            if pay[5] & 0xFC != 0:
                return fail("T4D2 b5hi")
            if pay[6] != ((cc & 7) << 5) or pay[7] != ((cc & 8) >> 2):
                return fail("T4D2 hole")
            consts = ((0, 0x0d), (1, 0x18), (2, 0), (3, 0), (8, 0x10),
                      (9, 0), (10, 0xc0), (11, 0x17), (12, 0), (13, 0),
                      (14, 0x3c), (15, 0), (16, 0x0e), (17, 0), (18, 0),
                      (19, 0xeb), (20, 0x24), (21, 0xdc), (22, 0x83),
                      (23, 0x8f), (24, 0x06), (25, 0xc0), (26, 0x43),
                      (27, 0xf0), (28, 0x86), (29, 0xef), (30, 0xf8),
                      (31, 0xbd), (32, 0x69), (33, 0x01), (34, 0x4c),
                      (35, 0xd7), (36, 0x24), (37, 0xe9), (38, 0x47),
                      (39, 0xb3), (40, 0x83), (41, 0xc6), (42, 0x43),
                      (43, 0x4d), (44, 0x06), (45, 0x5f), (46, 0xf7),
                      (47, 0xfe))
            tag = "T4D2"
        elif off <= 631:
            if pay[5:11].hex() != _T4D3TAB[off - 622]:
                return fail("T4D3 tab")
            consts = ((0, 0x0d), (1, 0x08), (2, 0), (3, 0), (11, 0x17),
                      (12, 0), (13, 0), (14, 0x3c), (15, 0), (16, 0x0e),
                      (17, 0), (18, 0), (19, 0xeb), (20, 0x24),
                      (21, 0xdc), (22, 0x83), (23, 0x8f), (24, 0x06),
                      (25, 0xc0), (26, 0x43), (27, 0xf0), (28, 0x86),
                      (29, 0xef), (30, 0xf8), (31, 0xbd), (32, 0x69),
                      (33, 0x01), (34, 0x4c), (35, 0xd7), (36, 0x24),
                      (37, 0xa7), (38, 0xd6), (39, 0x3e), (40, 0x83),
                      (41, 0xc6), (42, 0x43), (43, 0x4d), (44, 0x06),
                      (45, 0x5f), (46, 0xa6), (47, 0xfc))
            tag = "T4D3"
        else:
            k2 = (off - 632) >> 4
            l10 = (((n << 1) | 1) & 0x3FF) >> 8
            if (pay[5] & 3) != l10 or (pay[5] & 0xFC) != \
                    (0x58, 0x70, 0x88, 0xB8)[k2]:
                return fail("T4D4 b5")
            if pay[6] != (0x45, 0x63, 0x81, 0x90)[k2] or \
                    pay[7] != (0x4A, 0x4A, 0x4A, 0xDE)[k2]:
                return fail("T4D4 b67")
            if (pay[8], pay[9], pay[10]) != \
                    (((0xF0, 0x06, 0xC2),) * 3 +
                     ((0xD0, 0xF4, 0xC1),))[k2]:
                return fail("T4D4 b8910")
            if pay[15] != ((off - 632) & 15):
                return fail("T4D4 b15")
            consts = ((0, 0xd1), (1, 0x80), (2, 0), (3, 0), (11, 0x7d),
                      (12, 0), (13, 0), (14, 0x3c), (16, 0x12), (17, 0),
                      (18, 0), (19, 0xb0), (20, 0x24), (21, 0xdc),
                      (22, 0x83), (23, 0x8f), (24, 0x06), (25, 0xc0),
                      (26, 0x43), (27, 0xf0), (28, 0x86), (29, 0xef),
                      (30, 0xf8), (31, 0xbd), (32, 0x69), (33, 0x01),
                      (34, 0x4c), (35, 0xd7), (36, 0x24), (37, 0xa7),
                      (38, 0xd6), (39, 0x3e), (40, 0x83), (41, 0xc6),
                      (42, 0x43), (43, 0x4d), (44, 0x06), (45, 0x5f),
                      (46, 0xa6), (47, 0xfc))
            tag = "T4D4"
        for b, v in consts:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n <= 1772:  # T4 plateau E1 (NOTE-w2s7-18: 7-field + slip-16)
        if len(pay) != 48:
            return fail("T4E1 paylen")
        off = n - 821
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T4E1 lencode")
        i = off - 696
        if pay[0] != (0x18 if (i & 15) >= 11 else 0x17):
            return fail("T4E1 b0")
        if pay[5] != ((l10 >> 8) | (0xC8 if off <= 714 else 0xCC)):
            return fail("T4E1 b5")
        s = 0 if i < 10 else ((i - 10) >> 4) + 1
        if pay[10] != (0xE2, 0xC2, 0xA2)[(i - s) % 3]:
            return fail("T4E1 b10")
        if pay[11] != _T4E1T11[i & 15] or pay[19] != _T4E1T19[i & 15]:
            return fail("T4E1 b1119")
        if pay[15] != (i >> 4):
            return fail("T4E1 b15")
        for b, v in ((1, 0x8d), (2, 0x08), (3, 0), (6, 0xbd), (7, 0x4a),
                     (8, 0xf0), (9, 0x06), (12, 0), (13, 0), (14, 0x3c),
                     (16, 0x12), (17, 0), (18, 0), (20, 0x08),
                     (21, 0xcc), (22, 0x3d), (23, 0xf8), (24, 0),
                     (25, 0x3c), (26, 0x04), (27, 0x1f), (28, 0x86),
                     (29, 0xef), (30, 0xf8), (31, 0xbd), (32, 0x69),
                     (33, 0x01), (34, 0x4c), (35, 0xd7), (36, 0x24),
                     (37, 0xa7), (38, 0xd6), (39, 0x3e), (40, 0x83),
                     (41, 0xc6), (42, 0x43), (43, 0x4d), (44, 0x06),
                     (45, 0x5f), (46, 0xa6), (47, 0xfc)):
            if pay[b] != v:
                return fail("T4E1 const %d" % b)
        print("CLOSED T4E1 N=%d off=%d" % (n, off))
        return 0
    if n <= 1800:  # T4 plateau F = D2a (NOTE-w2s7-19: transition tables)
        if len(pay) != 48:
            return fail("T4F paylen")
        off = n - 821
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T4F lencode")
        if off <= 953:
            if pay.hex() != _T4F12[off - 952]:
                return fail("T4F12 bytes")
            print("CLOSED T4F12 N=%d off=%d" % (n, off))
            return 0
        if pay[5] != (0x24 | (l10 >> 8)):
            return fail("T4F b5")
        if off <= 969:
            if pay[25:27].hex() != _T4F2526[off - 954]:
                return fail("T4F2526 tab")
            consts = ((0, 0xca), (1, 0x3f), (2, 0x1c), (3, 0), (6, 0xc5),
                      (7, 0x86), (8, 0x6f), (9, 0xf1), (10, 0), (11, 0),
                      (12, 0xee), (13, 0x22), (14, 0xf5), (15, 0x11),
                      (16, 0x57), (17, 0xf5), (18, 0x3f), (19, 0x97),
                      (20, 0x8a), (21, 0xb7), (22, 0x75), (23, 0x0f),
                      (24, 0), (27, 0xf0), (28, 0x2a), (29, 0xf8),
                      (30, 0x8e), (31, 0xdf), (32, 0x69), (33, 0x01),
                      (34, 0x4c), (35, 0xd7), (36, 0x24), (37, 0xa7),
                      (38, 0xd6), (39, 0x3e), (40, 0x83), (41, 0xc6),
                      (42, 0x43), (43, 0x4d), (44, 0x06), (45, 0x5f),
                      (46, 0xa6), (47, 0xfc))
            tag = "T4F3"
        else:
            if pay[24:30].hex() != _T4F2429[off - 970]:
                return fail("T4F2429 tab")
            consts = ((0, 0xa4), (1, 0x8f), (2, 0x08), (3, 0), (6, 0xc5),
                      (7, 0x86), (8, 0x6f), (9, 0xf1), (10, 0x20),
                      (11, 0x46), (12, 0), (13, 0xa0), (14, 0xfc),
                      (15, 0xc3), (16, 0xee), (17, 0xaa), (18, 0x36),
                      (19, 0xd7), (20, 0x08), (21, 0xee), (22, 0xba),
                      (23, 0x07), (30, 0x1d), (31, 0xbf), (32, 0x69),
                      (33, 0x01), (34, 0x4c), (35, 0xd7), (36, 0x24),
                      (37, 0xa7), (38, 0xd6), (39, 0x3e), (40, 0x83),
                      (41, 0xc6), (42, 0x43), (43, 0x4d), (44, 0x06),
                      (45, 0x5f), (46, 0xa6), (47, 0xfc))
            tag = "T4F4"
        for b, v in consts:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n <= 1864:  # T4 plateau G = D2b1 (NOTE-w2s7-20: bands + 16-tabs)
        if len(pay) != 48:
            return fail("T4G paylen")
        off = n - 821
        if grp(pay, tuple(range(32, 42))) != (((n << 1) | 1) & 0x3FF):
            return fail("T4G lencode")
        if pay[5] != 0x26:
            return fail("T4G b5")
        k = (off - 980) >> 4
        m = (off - 980) & 15
        if (pay[14], pay[15], pay[21], pay[22], pay[23],
                pay[28]) != _T4GBAND[k]:
            return fail("T4G band")
        if pay[24] != (0x4B, 0x6B, 0x8B, 0xAB)[m >> 2]:
            return fail("T4G b24")
        if pay[29] != _T4GB29[m] or pay[30] != _T4GB30[m] or \
                pay[31] != _T4GB31[m]:
            return fail("T4G tab16")
        for b, v in ((0, 0xca), (1, 0x3f), (2, 0x8c), (3, 0), (6, 0xc5),
                     (7, 0x86), (8, 0x6f), (9, 0xf1), (10, 0), (11, 0),
                     (12, 0x6e), (13, 0x44), (16, 0x57), (17, 0xb5),
                     (18, 0xb9), (19, 0x16), (20, 0x08), (25, 0xdd),
                     (26, 0x8d), (27, 0x8f), (32, 0x6d), (33, 0x16),
                     (34, 0xc0), (35, 0x74), (36, 0x24), (37, 0xa7),
                     (38, 0xd6), (39, 0x3e), (40, 0x83), (41, 0xc6),
                     (42, 0x43), (43, 0x4d), (44, 0x06), (45, 0x5f),
                     (46, 0xa6), (47, 0xfc)):
            if pay[b] != v:
                return fail("T4G const %d" % b)
        print("CLOSED T4G N=%d off=%d" % (n, off))
        return 0
    if n <= 2047:  # T4 plateau H = D2b2 (NOTE-w2s7-21: tabs + counters)
        if len(pay) != 48:
            return fail("T4H paylen")
        off = n - 821
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T4H lencode")
        if pay[5] != (0x24 | (l10 >> 8)):
            return fail("T4H b5")
        k2 = (off - 1044) >> 4
        m = (off - 1044) & 15
        if pay[26] != _T4HT26[m] or pay[34] != _T4HT34[m] or \
                pay[35] != _T4HT35[m]:
            return fail("T4H tab16")
        if pay[28] != ((0x86 + k2 * 0x16) & 0xFF) or \
                pay[30] != ((0x43 + k2 * 8) & 0xFF):
            return fail("T4H ctr")
        if pay[29] != (0xFC if k2 >= 6 else 0xBF):
            return fail("T4H b29")
        for b, v in ((0, 0xca), (1, 0x3f), (2, 0xcc), (3, 0x08), (6, 0xc5),
                     (7, 0x86), (8, 0x6f), (9, 0xf1), (10, 0), (11, 0),
                     (12, 0xee), (13, 0xaa), (14, 0x66), (15, 0x26),
                     (16, 0xe6), (17, 0x5a), (18, 0x8c), (19, 0x48),
                     (20, 0x08), (21, 0x6e), (22, 0x96), (23, 0x77),
                     (24, 0x2b), (25, 0x0c), (27, 0xf8), (31, 0xdd),
                     (32, 0x6d), (33, 0x16), (36, 0x48), (37, 0x66),
                     (38, 0x6a), (39, 0xed), (40, 0x68), (41, 0x3c),
                     (42, 0xd4), (43, 0x94), (44, 0x06), (45, 0x5f),
                     (46, 0xa6), (47, 0xfc)):
            if pay[b] != v:
                return fail("T4H const %d" % b)
        print("CLOSED T4H N=%d off=%d" % (n, off))
        return 0
    if n <= 2120:  # T4 plateau I = D2c1 (NOTE-w2s7-22: H-regime cont)
        if len(pay) != 48:
            return fail("T4I paylen")
        off = n - 821
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T4I lencode")
        if pay[5] != (0x40 | (l10 >> 8)) or pay[29] != 0xFC:
            return fail("T4I b5b29")
        m = (off - 1044) & 15
        k2 = (off - 1044) >> 4
        if pay[26] != _T4HT26[m] or pay[34] != _T4HT34[m] or \
                pay[35] != _T4HT35[m]:
            return fail("T4I tab16")
        if pay[28] != ((0x86 + k2 * 0x16) & 0xFF) or \
                pay[30] != ((0x43 + k2 * 8) & 0xFF):
            return fail("T4I ctr")
        for b, v in ((0, 0x94), (1, 0x7f), (2, 0x98), (3, 0x11), (6, 0x8a),
                     (7, 0x0d), (8, 0xf0), (9, 0xe2), (10, 0x01),
                     (11, 0), (12, 0xee), (13, 0xaa), (14, 0x66),
                     (15, 0x26), (16, 0xe6), (17, 0x5a), (18, 0x8c),
                     (19, 0x48), (20, 0x08), (21, 0x6e), (22, 0x96),
                     (23, 0x77), (24, 0x2b), (25, 0x0c), (27, 0xf8),
                     (31, 0xdd), (32, 0x6d), (33, 0x16), (36, 0x48),
                     (37, 0x66), (38, 0x6a), (39, 0xed), (40, 0x68),
                     (41, 0x3c), (42, 0xd4), (43, 0x94), (44, 0x06),
                     (45, 0x67), (46, 0xa6), (47, 0xfc)):
            if pay[b] != v:
                return fail("T4I const %d" % b)
        print("CLOSED T4I N=%d off=%d" % (n, off))
        return 0
    if n <= 2212:  # T4 tail J (NOTE-w2s7-23: singletons + c3/c4/c5)
        if len(pay) != 48:
            return fail("T4J paylen")
        off = n - 821
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T4J lencode")
        if off <= 1301:
            if pay.hex() != _T4JSING[off - 1300]:
                return fail("T4J sing")
            print("CLOSED T4JS N=%d off=%d" % (n, off))
            return 0
        if pay[5] != (0x40 | (l10 >> 8)):
            return fail("T4J b5")
        if off <= 1317:
            if off <= 1304:
                ok = (pay[40], pay[41]) == (0xB8, 0x3C) and \
                    pay[42] == 0x76 + (off - 1302)
            elif off <= 1312:
                ok = (pay[40], pay[41]) == (0xC0, 0xBC) and \
                    pay[42] == 0x80 + (off - 1305)
            else:
                ok = (pay[40], pay[41]) == (0xC8, 0x3C) and \
                    pay[42] == 0x90 + (off - 1313)
            if not ok:
                return fail("T4J c3")
            consts = ((0, 0x94), (1, 0x7f), (2, 0xf8), (3, 0x11),
                      (6, 0x8a), (7, 0x0d), (8, 0xf0), (9, 0xe2),
                      (10, 0x01), (11, 0), (12, 0xee), (13, 0xaa),
                      (14, 0x26), (15, 0x8b), (16, 0xe6), (17, 0x5a),
                      (18, 0x8c), (19, 0x48), (20, 0x08), (21, 0x8e),
                      (22, 0x84), (23, 0x5f), (24, 0x09), (25, 0xf6),
                      (26, 0x68), (27, 0xbd), (28, 0xbe), (29, 0xbf),
                      (30, 0xa3), (31, 0x13), (32, 0xe9), (33, 0xf4),
                      (34, 0x2d), (35, 0xb7), (36, 0xea), (37, 0xa1),
                      (38, 0x9f), (39, 0x5a), (43, 0x4d), (44, 0x2a),
                      (45, 0x71), (46, 0x66), (47, 0xca))
            tag = "T4J3"
        elif off <= 1327:
            if pay[40:46].hex() != _T4JC4[off - 1318]:
                return fail("T4J c4")
            consts = ((0, 0x94), (1, 0x7f), (2, 0xf8), (3, 0x08),
                      (6, 0x8a), (7, 0x0d), (8, 0xf0), (9, 0xe2),
                      (10, 0x01), (11, 0), (12, 0xee), (13, 0xaa),
                      (14, 0x26), (15, 0x8b), (16, 0xe6), (17, 0x5a),
                      (18, 0x8c), (19, 0x48), (20, 0x08), (21, 0x8e),
                      (22, 0x84), (23, 0x5f), (24, 0x09), (25, 0x36),
                      (26, 0x9e), (27, 0xd1), (28, 0xbe), (29, 0xbf),
                      (30, 0xa3), (31, 0x13), (32, 0xe9), (33, 0x34),
                      (34, 0xad), (35, 0xb7), (36, 0x48), (37, 0xe0),
                      (38, 0x4f), (39, 0xad), (46, 0xcc), (47, 0x94))
            tag = "T4J4"
        else:
            m = (off - 1328) & 15
            k = (off - 1328) >> 4
            if bytes((pay[40], pay[41], pay[46], pay[47])).hex() != \
                    _T4JT5[m]:
                return fail("T4J c5tab")
            if (pay[2], pay[3], pay[27], pay[37], pay[38], pay[39],
                    pay[44]) != _T4JBAND[k]:
                return fail("T4J c5band")
            consts = ((0, 0x94), (1, 0x7f), (6, 0x8a), (7, 0x0d),
                      (8, 0xf0), (9, 0xe2), (10, 0x01), (11, 0),
                      (12, 0xee), (13, 0xaa), (14, 0x26), (15, 0x8b),
                      (16, 0xe6), (17, 0x5a), (18, 0x8c), (19, 0x48),
                      (20, 0x08), (21, 0x8e), (22, 0x84), (23, 0x5f),
                      (24, 0x09), (25, 0x36), (26, 0x9e), (28, 0xbe),
                      (29, 0xbf), (30, 0xa3), (31, 0x13), (32, 0xe9),
                      (33, 0x34), (34, 0xad), (35, 0xb7), (36, 0x48),
                      (42, 0xd6), (43, 0x3e), (45, 0x60))
            tag = "T4J5"
        for b, v in consts:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    print("N out of scope", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
