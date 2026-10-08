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
# T5E E-plateau tables (PRE-018b/019b concurred): 16-tabs keyed off&15,
# k2-tables keyed off>>4 (OPEN why).
_T5DIP = ("947f38024b438a0df0e201006e44228b57b5b916088e845fe9049ef1b"
          "07d7f47e934adb748e0536b08fc164b492833e5",
          "00e51ffe4d8388cd164d09016e44228b57b5b916088e845fe9049e51b"
          "07d7f47e934adb748e0a75608fc164b49285bfb")
_T5DIP604 = ("747c52fc0356ef9d5337800091251d59e65a8c48088e845fe9049e51b"
             "07d7f47e934adb748e0a75608fc164b49285bfb")
# T5G tables: action moves to b28-39. G1b/G2 = fixed row-tabs
# (OPEN why); G3 = 16-tabs + k2 segs.
_T5G0 = ("7d0000000556ef9d5337804000747c5291251dae55df39d1694e309f"
        "2fe28f67bebfa313e934adb748e0a75608fc164b49285bfb")
_T5G1T = ("a7fc8f3c", "92bfd33c", "a8bfdb3c", "bebfe33c",
          "d4bfeb3c", "eabff33c", "00fcfb3c", "16fc033d",
          "2cfc0b3d", "42fc133d", "2dbf573d", "43bf5f3d",
          "59bf673d", "6fbf6f3d", "85bf773d", "9bbf7f3d")
_T5G1C = ((0, 0xa8), (1, 0x0f), (2, 0x00), (3, 0x00), (5, 0x56),
          (6, 0xef), (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80),
          (11, 0xcb), (12, 0x00), (13, 0x74), (14, 0x7c),
          (15, 0x52), (16, 0x91), (17, 0x25), (18, 0x1d),
          (19, 0x97), (20, 0x55), (21, 0xdf), (22, 0x39),
          (23, 0xd1), (24, 0x69), (25, 0x8e), (26, 0x08),
          (27, 0x6f), (28, 0xb0), (29, 0x04), (30, 0x60),
          (31, 0xf1), (36, 0x2d), (37, 0x4e), (38, 0xd3),
          (39, 0x7a), (40, 0x48), (41, 0xe0), (42, 0xa7),
          (43, 0x56), (44, 0x08), (45, 0xfc), (46, 0x16),
          (47, 0x4b), (48, 0x49), (49, 0x28), (50, 0x5b),
          (51, 0xfb))
_T5G2T = ("d6fc1f02ce48", "c0fcb7d4ae41", "37fcaf2f6e3f",
          "c0bffb830e44", "20fcbf950e3d", "19bfc72f6e3f",
          "adbf17d5ae41", "24bf0f306e3f", "bafc13306e3f",
          "5bfc1b306e3f")
_T5G2C = ((0, 0xea), (1, 0x03), (2, 0x00), (3, 0x00), (5, 0x56),
          (6, 0xef), (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80),
          (11, 0x39), (12, 0x00), (13, 0x74), (14, 0x7c),
          (15, 0x52), (16, 0x91), (17, 0x25), (18, 0x1d),
          (19, 0xfa), (20, 0x55), (21, 0xdf), (22, 0x39),
          (23, 0xd1), (24, 0x69), (25, 0x8e), (26, 0x02),
          (27, 0x3f), (28, 0xed), (29, 0x84), (30, 0x58),
          (31, 0x3c), (38, 0xa0), (39, 0xf5), (40, 0x48),
          (41, 0xe0), (42, 0xa7), (43, 0x56), (44, 0x08),
          (45, 0xfc), (46, 0x16), (47, 0x4b), (48, 0x49),
          (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5G3T30 = (0x58, 0x58, 0xf8, 0x88, 0x28, 0xb8, 0x58, 0xe8,
            0xf8, 0x88, 0x28, 0xb8, 0x58, 0xe8, 0xf8, 0x88)
_T5G3T31 = (0xc2, 0xc2, 0xc2, 0xc3, 0xc4, 0xc4, 0xc5, 0xc5,
            0xc5, 0xc6, 0xc7, 0xc7, 0xc8, 0xc8, 0xc8, 0xc9)
_T5G3T38 = (0xa0, 0xa0, 0xa8, 0x30, 0x38, 0xc0, 0xc8, 0x50,
            0xd0, 0x58, 0x60, 0xe8, 0xf0, 0x78, 0xf8, 0x80)
_T5G3T39 = (0xd6, 0xf6, 0xd9, 0xf2, 0xd5, 0xed, 0xd0, 0xe9,
            0xd3, 0xec, 0xcf, 0xe7, 0xca, 0xe3, 0xcd, 0xe6)
_T5G3K = ("e4bf67840e44", "9bbf2b306e3f", "24bf77840e44",
          "aafc2306ce3a")
# T5H tables (256 rows): 16-tabs b44-47 + k2-tabs b32/37/38/39
# + b33/b5 step edges. K39 near-cycle6 (k2=1 breaks it); K37
# near-cycle4 (pauses at k2=1,8,14). OPEN why.
_T5HT44 = (0xb0, 0xb0, 0x80, 0x80, 0x48, 0x48, 0x50, 0x18,
           0x18, 0xe8, 0xe8, 0xb8, 0xb8, 0xb8, 0x88, 0x88)
_T5HT45 = (0x7c, 0x7c, 0x3c, 0x3c, 0x7c, 0x7c, 0xfc, 0x3c,
           0x3c, 0xbc, 0xbc, 0x7c, 0x7c, 0x7c, 0x3c, 0x3c)
_T5HT46 = (0x61, 0x62, 0x80, 0x81, 0x97, 0x98, 0xa0, 0xb7,
           0xb8, 0xd5, 0xd6, 0xf4, 0xf5, 0xf6, 0x14, 0x15)
_T5HT47 = (0xb0, 0xb0, 0xb0, 0xb0, 0xb0, 0xb0, 0xb0, 0xb0,
           0xb0, 0xb0, 0xb0, 0xb0, 0xb0, 0xb0, 0xb1, 0xb1)
_T5HK32 = (0x8e, 0x8e, 0xae, 0xee, 0x0e, 0x2e, 0x4e, 0x6e,
           0x6e, 0xae, 0xce, 0xee, 0x0e, 0x2e, 0x2e, 0x6e)
_T5HK37 = (0x02, 0x02, 0x42, 0x82, 0xc2, 0x02, 0x42, 0x82,
           0x82, 0xc2, 0x02, 0x42, 0x82, 0xc2, 0xc2, 0x02)
_T5HK38 = (0xb5, 0xb5, 0xcd, 0x91, 0xa9, 0x6e, 0x86, 0x4a,
           0x9e, 0x62, 0x7b, 0x3f, 0x57, 0x1b, 0x6f, 0x34)
_T5HK39 = (0xb6, 0xb7, 0xf6, 0x17, 0x56, 0x77, 0xb6, 0xd7,
           0xf6, 0x17, 0x56, 0x77, 0xb6, 0xd7, 0xf6, 0x17)
# T5I1 tables: transition pair + 16-row tail-tab (I1a) +
# 10-row tab (I1b). Row-tabs OPEN why.
_T5I0 = ("fa000000bb58ef9d5337808900747c5291251dfa55df39d1698e023f"
         "ed8414cfa2bf571eacae68bd48e0a75608fc164b49285bfb",
         "bf370000bd58ef9d5337804900747c5291251dfa55df39d1698e023f"
         "ed844c4aa2bf571eacae38b9c8d592dfef4fadea2965b6f6")
_T5I1AT = ("4cafb781", "ccd71f82", "cca8ef82", "2cd06787",
           "acf8cf87", "0c843f88", "2cf20789", "8c7d7789",
           "0ca6df89", "0c77af8a", "8c9f178b", "8c70e78b",
           "6ceff78f", "6cc0c790", "ece82f91", "4c749f91")
_T5I1AC = ((0, 0x4e), (1, 0xf4), (2, 0x03), (3, 0x00), (5, 0x58),
           (6, 0xef), (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80),
           (11, 0x77), (12, 0x00), (13, 0x74), (14, 0x7c),
           (15, 0x52), (16, 0x91), (17, 0x25), (18, 0x5d),
           (19, 0xd5), (20, 0xe9), (21, 0xa7), (22, 0x57),
           (23, 0x1e), (24, 0x73), (25, 0x14), (26, 0xf8),
           (27, 0x41), (28, 0xed), (29, 0x84), (30, 0x88),
           (31, 0xfe), (32, 0x8c), (33, 0x12), (34, 0xfd),
           (35, 0x9e), (36, 0x75), (37, 0xc5), (38, 0xc9),
           (39, 0x9d), (40, 0xc8), (41, 0xf5), (42, 0x8f),
           (43, 0xe7), (44, 0x2f), (45, 0xa5), (46, 0xdc),
           (47, 0xaa))
_T5I1BT = ("4eac76e1058ef7", "0e0ca21cfee47c", "0e8c2ff6f8ccf9",
           "4e8c19b200ceff", "0e2c31f6f8cefc", "0e0c32f6f8527e",
           "0e4cae1cfe8a7a", "0eecb888fbb677", "0eac3cf6f8f478",
           "0e4cbb88fb167f")
# T5I2 tables: 16-tabs b5/6/7 (b5 steps +1 for k2>=1,m<=6),
# b8 = cycle3 on m-bands (OPEN), k2 rows b35/b44-47/b50-51.
_T5I2T5 = (0x38, 0xe8, 0x08, 0xb8, 0x68, 0x88, 0x38, 0xe9,
           0x09, 0xb9, 0x69, 0x39, 0x39, 0xe9, 0xb9, 0xb9)
_T5I2T6 = (0xbc, 0xda, 0xa2, 0xc0, 0xdf, 0xa6, 0xc5, 0xe3,
           0xab, 0xc9, 0xe8, 0x8e, 0xce, 0xec, 0x92, 0xd2)
_T5I2T7 = (0x25, 0x65, 0x6d, 0xad, 0xed, 0xf5, 0x35, 0x75,
           0x7d, 0xbd, 0xfd, 0x45, 0x45, 0x85, 0xcd, 0xcd)
_T5I2K = ("4eec20b2006c7f", "0eec3ff6f80078", "4eac2ab2008af8",
          "0e6c5d65f6d87b")
# T5I3 tables: b6/b7 walk I2-tab by k2; b5 = own k2-tab +
# mid-seg +1 (m>=7) in k2=4,12 (OPEN); b8 = cycle3 on k2
# bands; b13-16 16-tabs.
_T5I3K5 = (0x39, 0xe9, 0x09, 0xb9, 0x69, 0x8a, 0x3a, 0xea,
           0x0a, 0xba, 0x6a, 0x3a, 0x3a, 0xeb, 0xbb, 0xbb)
# T5J tables: 3 transition literals + 15-row J1 tab +
# 10-row J2 tab. Glitchy ramps, shipped literal (OPEN).
_T5J0 = ("97230000735bef9d5337804900747c5291251dfa55df39d1698e023f"
         "ed844c4aa2bf571eacae38b9c8759b37cccdddad2dcc06fc",
         "a4cb110075fb91b5f4cd73fc00e43cb31747eb8955df39d1698e023f"
         "ed844c4aa2bf571eacae38b9c8759b37cccdddad2dcc06fc",
         "fb8f020177fb91b5f4cd73aa008fbc96b740087a8d7ed2e53d47811f"
         "ed844c4aa2bf571eacae38b9c8759b37cccdddad2dcc06fc")
_T5J1T = ("ab90b48a", "5b91be9a", "0b92c8aa", "bb92d2ba",
          "6b93dcca", "1b94e6da", "cb94f0ea", "7b95fafa",
          "3b964c2a", "bb9b6afa", "6b9c760a", "1b9d801a",
          "6b9ece1a", "1b9fd82a", "cb9fe23a")
_T5J1C = ((2, 0x02), (3, 0x01), (5, 0xfb), (6, 0x91), (7, 0xb5),
          (8, 0xf4), (9, 0xcd), (10, 0x73), (12, 0x00),
          (13, 0x8f), (14, 0xbc), (15, 0x96), (16, 0xb7),
          (17, 0x40), (18, 0x08), (20, 0x8d), (21, 0x7e),
          (22, 0xd2), (23, 0xe5), (24, 0x3d), (25, 0x47),
          (26, 0x81), (27, 0x1f), (28, 0xed), (29, 0x84),
          (30, 0x4c), (31, 0x4a), (32, 0xa2), (33, 0xbf),
          (34, 0x57), (35, 0x1e), (36, 0xac), (37, 0xae),
          (38, 0x38), (39, 0xb9), (40, 0xc8), (41, 0x75),
          (42, 0x9b), (43, 0x37), (44, 0xcc), (45, 0xcd),
          (46, 0xdd), (47, 0xad), (48, 0x2d), (49, 0xcc),
          (50, 0x06), (51, 0xfc))
_T5J2T = ("1b7422704ceb", "c178207ac4b6", "cb46237e28a8",
          "b3c82168c2c3", "e3462372eaa8", "b534227abc9b",
          "f3c8217ce2c3", "254723706ea8", "3b47236ef0a8",
          "5147236e72a8")
# T5J3-6 tables: ONE shared 16-tab b24-27 + k2 body overrides
# + b5 edge @1371. (Tab reuse 4/4, OPEN why.)
_T5J3T = ("8cbcd0f1", "bc7cc3f2", "bc7cc4f2", "ec3cb7f3",
          "ec3cb8f3", "857c95f4", "b53c88f5", "b5fc90f5",
          "4e7c66f6", "7efc60f7", "7efc61f7", "aebc54f8",
          "aebc55f8", "47fc32f9", "77bc25fa", "77bc26fa")
_T5J3K = ("a5e41c36e76db8", "0ba41d56be0db5",
          "fee41c06c86db8", "f51a1de6b66db3")
# T5K tables: 16-tabs b15/22/23/30/31 + b24-27 walk the J3
# tab by k2 (full 16) + b5 edge @1499.
_T5KT15 = (0xcb, 0xcb, 0xcb, 0xcd, 0xcd, 0xcf, 0xcf, 0xcf,
           0xd1, 0xd1, 0xd1, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3)
_T5KT22 = (0xbd, 0xfd, 0xfd, 0xbd, 0xbd, 0xbd, 0xbd, 0xbd,
           0xbd, 0xbd, 0xbd, 0xbd, 0xbd, 0xbd, 0xbd, 0xbd)
_T5KT23 = (0x2f, 0x6f, 0x77, 0x27, 0x2f, 0x17, 0x1f, 0x27,
           0x0f, 0x17, 0x1f, 0x07, 0x0f, 0x17, 0xc7, 0xcf)
_T5KT30 = (0x88, 0x88, 0x08, 0xc8, 0x48, 0x88, 0x08, 0x88,
           0xc8, 0x48, 0xc8, 0x08, 0x88, 0x08, 0xc8, 0x48)
_T5KT31 = (0xcf, 0x07, 0x0d, 0xd8, 0xde, 0xdc, 0xe2, 0xe7,
           0xe5, 0xeb, 0xf0, 0xef, 0xf4, 0xfa, 0xc5, 0xcb)
_T5KC = ((0, 0x82), (1, 0x78), (2, 0x87), (3, 0x22), (6, 0x91),
         (7, 0xb5), (8, 0xf4), (9, 0xcd), (10, 0x73),
         (11, 0x00), (12, 0xb4), (13, 0x21), (14, 0xa4),
         (16, 0x89), (17, 0x8c), (18, 0x66), (19, 0xed),
         (20, 0x0d), (21, 0xb5), (28, 0x31), (29, 0x4f),
         (32, 0x30), (33, 0x29), (34, 0xd1), (35, 0xe5),
         (36, 0x51), (37, 0x57), (38, 0x9c), (39, 0xdc),
         (40, 0xc8), (41, 0x75), (42, 0x9b), (43, 0x37),
         (44, 0xcc), (45, 0xcd), (46, 0xdd), (47, 0xad),
         (48, 0x2d), (49, 0xcc), (50, 0x06), (51, 0xfc))
_T5J3C = ((0, 0x82), (1, 0x78), (2, 0x87), (3, 0x02), (6, 0x91),
          (7, 0xb5), (8, 0xf4), (9, 0xcd), (10, 0x73),
          (11, 0x00), (12, 0xb4), (16, 0x89), (17, 0x8c),
          (22, 0x11), (23, 0x5d), (28, 0x31), (29, 0x4f),
          (30, 0xc8), (31, 0xa4), (32, 0xa2), (33, 0xbf),
          (34, 0x57), (35, 0x1e), (36, 0xac), (37, 0xae),
          (38, 0x38), (39, 0xb9), (40, 0xc8), (41, 0x75),
          (42, 0x9b), (43, 0x37), (44, 0xcc), (45, 0xcd),
          (46, 0xdd), (47, 0xad), (48, 0x2d), (49, 0xcc),
          (50, 0x06), (51, 0xfc))
_T5J2C = ((3, 0x00), (5, 0xfb), (6, 0x91), (7, 0xb5), (8, 0xf4),
          (9, 0xcd), (10, 0x73), (12, 0x00), (13, 0x41),
          (14, 0xbc), (15, 0x43), (16, 0x34), (17, 0x91),
          (18, 0xd1), (20, 0x8d), (21, 0x7e), (22, 0xd2),
          (23, 0xe5), (25, 0x4d), (26, 0x81), (27, 0x1f),
          (28, 0xed), (29, 0x84), (30, 0x4c), (31, 0x4a),
          (32, 0xa2), (33, 0xbf), (34, 0x57), (35, 0x1e),
          (36, 0xac), (37, 0xae), (38, 0x38), (39, 0xb9),
          (40, 0xc8), (41, 0x75), (42, 0x9b), (43, 0x37),
          (44, 0xcc), (45, 0xcd), (46, 0xdd), (47, 0xad),
          (48, 0x2d), (49, 0xcc), (50, 0x06), (51, 0xfc))
_T5I3T13 = (0xa4, 0xa4, 0xa4, 0xc0, 0xc0, 0xc4, 0xc4, 0xdc,
            0xe0, 0xe0, 0xfc, 0xfc, 0xfc, 0x18, 0x18, 0x34)
_T5I3T14 = (0x7c, 0x7c, 0x7c, 0x7c, 0x7c, 0x3c, 0x3c, 0x7c,
            0x3c, 0x3c, 0x3c, 0x3c, 0x3c, 0x7c, 0x7c, 0x7c)
_T5I3T15 = (0xd1, 0xd2, 0xd3, 0xf0, 0xf1, 0x07, 0x08, 0x10,
            0x26, 0x27, 0x44, 0x45, 0x46, 0x63, 0x64, 0x81)
_T5I3T16 = (0x75, 0x75, 0x75, 0x75, 0x75, 0x95, 0x95, 0x95,
            0x95, 0x95, 0x95, 0x95, 0x95, 0x95, 0x95, 0x95)
_T5I3C = ((0, 0x77), (1, 0x4e), (2, 0xb4), (3, 0x00), (9, 0x75),
          (10, 0x03), (11, 0xd8), (12, 0x00), (17, 0x58),
          (18, 0xd2), (19, 0x55), (20, 0xe9), (21, 0xa7),
          (22, 0x57), (23, 0x1e), (24, 0x73), (25, 0x14),
          (26, 0xf8), (27, 0x41), (28, 0xed), (29, 0x84),
          (30, 0x88), (31, 0xfe), (32, 0x8c), (33, 0x12),
          (34, 0x5d), (35, 0x0e), (36, 0x75), (37, 0xc5),
          (38, 0xc9), (39, 0x9d), (40, 0xc8), (41, 0x75),
          (42, 0x9b), (43, 0x37), (44, 0x8c), (45, 0xc7),
          (46, 0x88), (47, 0xfb), (48, 0x2d), (49, 0xcc),
          (50, 0xba), (51, 0x7c))
_T5I2C = ((0, 0xe7), (1, 0x44), (2, 0x0b), (3, 0x00), (9, 0x75),
          (10, 0x03), (11, 0x78), (12, 0x00), (13, 0x74),
          (14, 0x7c), (15, 0x52), (16, 0x91), (17, 0x25),
          (18, 0x5d), (19, 0xd5), (20, 0xe9), (21, 0xa7),
          (22, 0x57), (23, 0x1e), (24, 0x73), (25, 0x14),
          (26, 0xf8), (27, 0x41), (28, 0xed), (29, 0x84),
          (30, 0x88), (31, 0xfe), (32, 0x8c), (33, 0x12),
          (34, 0x5d), (36, 0x75), (37, 0xc5), (38, 0xc9),
          (39, 0x9d), (40, 0xc8), (41, 0x75), (42, 0x9b),
          (43, 0x37), (48, 0x2d), (49, 0xcc))
_T5I1BC = ((0, 0x4e), (1, 0xb4), (2, 0x00), (3, 0x00), (5, 0x58),
           (6, 0xef), (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80),
           (11, 0x77), (12, 0x00), (13, 0x74), (14, 0x7c),
           (15, 0x52), (16, 0x91), (17, 0x25), (18, 0x5d),
           (19, 0xd5), (20, 0xe9), (21, 0xa7), (22, 0x57),
           (23, 0x1e), (24, 0x73), (25, 0x14), (26, 0xf8),
           (27, 0x41), (28, 0xed), (29, 0x84), (30, 0x88),
           (31, 0xfe), (32, 0x8c), (33, 0x12), (34, 0x5d),
           (36, 0x75), (37, 0xc5), (38, 0xc9), (39, 0x9d),
           (40, 0xc8), (41, 0x75), (42, 0x9b), (43, 0x37),
           (48, 0x2d), (49, 0xcc))
_T5HC = ((0, 0x4e), (1, 0xf4), (2, 0x03), (3, 0x00), (6, 0xef),
         (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80), (11, 0x77),
         (12, 0x00), (13, 0x74), (14, 0x7c), (15, 0x52),
         (16, 0x91), (17, 0x25), (18, 0x5d), (19, 0xd5),
         (20, 0xe9), (21, 0xe7), (22, 0x4f), (23, 0xd5),
         (24, 0x73), (25, 0x14), (26, 0xf8), (27, 0x41),
         (28, 0xed), (29, 0x84), (30, 0x70), (31, 0xf2),
         (34, 0xb4), (35, 0xaa), (36, 0x0d), (40, 0x2c),
         (41, 0x04), (42, 0xfe), (43, 0xa7), (48, 0x8d),
         (49, 0x84), (50, 0xb2), (51, 0xb5))
_T5G3C = ((0, 0xab), (1, 0x3e), (2, 0x00), (3, 0x00), (5, 0x56),
          (6, 0xef), (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80),
          (11, 0x39), (12, 0x00), (13, 0x74), (14, 0x7c),
          (15, 0x52), (16, 0x91), (17, 0x25), (18, 0x1d),
          (19, 0xfa), (20, 0x55), (21, 0xdf), (22, 0x39),
          (23, 0xd1), (24, 0x69), (25, 0x8e), (26, 0x02),
          (27, 0x3f), (28, 0xed), (29, 0x84), (40, 0x2c),
          (41, 0x04), (42, 0x7e), (43, 0x6a), (44, 0x08),
          (45, 0xfc), (46, 0x16), (47, 0x4b), (48, 0x49),
          (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5ET5H = (0x20, 0x20, 0x40, 0x60, 0x60, 0x80, 0x80, 0xa0, 0xa0, 0xc0,
           0xc0, 0xe0, 0xe0, 0x00, 0x00, 0x20)
_T5ET6 = (0xb9, 0xf9, 0xc0, 0x87, 0xc7, 0x8e, 0xce, 0x95, 0xd5, 0x9c,
          0xdc, 0xa3, 0xe3, 0xab, 0xeb, 0xb2)
_T5ET7 = (0x85, 0x85, 0x8d, 0x95, 0x95, 0x9d, 0x9d, 0xa5, 0xa5, 0xad,
          0xad, 0xb5, 0xb5, 0xbd, 0xbd, 0xc5)
_T5EK44 = (0x6b, 0xeb, 0xab, 0x0b, 0xeb, 0x4b, 0xcb, 0x8b, 0xeb, 0x6b,
           0x2b, 0x8b, 0x6b, 0xcb, 0x2b, 0x0b)
_T5EK45 = (0xa2, 0xa2, 0xa3, 0xa4, 0xa4, 0xa5, 0xa5, 0xa6, 0xa6, 0xa7,
           0xa8, 0xa8, 0xa9, 0xa9, 0xaa, 0xab)
_T5EK50 = (0xe8, 0x43, 0xb4, 0xf8, 0x80, 0xc4, 0x1f, 0x90, 0xeb, 0x2f,
           0xb7, 0xfb, 0x83, 0xc7, 0x0b, 0x93)
_T5EK51 = (0xfe, 0x7b, 0xbe, 0xff, 0x7e, 0xbf, 0x3c, 0x7f, 0xfb, 0x3d,
           0xbb, 0xfc, 0x7b, 0xbc, 0xfe, 0x7c)
# T5F-head tables (52-tier): F1 = L10(b4)+ramp(b10) over frozen body,
# two halves (F1a/F1b); F2 = L10(b4)+10 T2-rows over frozen body.
_T5F1A = ((0, 0x0f), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x03),
          (6, 0xab), (7, 0x75), (8, 0x56), (9, 0xe5), (11, 0xc3),
          (12, 0xd7), (13, 0x97), (14, 0x08), (15, 0x00), (16, 0x92),
          (17, 0xaf), (18, 0x6a), (19, 0xb2), (20, 0xe6), (21, 0x5a),
          (22, 0x8c), (23, 0x48), (24, 0x08), (25, 0x8e), (26, 0x84),
          (27, 0x5f), (28, 0xe9), (29, 0x04), (30, 0x9e), (31, 0x51),
          (32, 0xb0), (33, 0x7d), (34, 0x7f), (35, 0x47), (36, 0xe9),
          (37, 0x34), (38, 0xad), (39, 0xb7), (40, 0x48), (41, 0xe0),
          (42, 0xa7), (43, 0x56), (44, 0x08), (45, 0xfc), (46, 0x16),
          (47, 0x4b), (48, 0x49), (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5F1B = ((0, 0x0f), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x03),
          (6, 0xab), (7, 0x75), (8, 0x16), (9, 0xe6), (11, 0xc4),
          (12, 0xd7), (13, 0x97), (14, 0x08), (15, 0x00), (16, 0x92),
          (17, 0xaf), (18, 0x6a), (19, 0xb2), (20, 0xe6), (21, 0x5a),
          (22, 0x8c), (23, 0x48), (24, 0x08), (25, 0x8e), (26, 0x84),
          (27, 0x5f), (28, 0xe9), (29, 0x04), (30, 0x9e), (31, 0x51),
          (32, 0xb0), (33, 0x7d), (34, 0x7f), (35, 0x47), (36, 0xe9),
          (37, 0x34), (38, 0xad), (39, 0xb7), (40, 0x48), (41, 0xe0),
          (42, 0xa7), (43, 0x56), (44, 0x08), (45, 0xfc), (46, 0x16),
          (47, 0x4b), (48, 0x49), (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5F2C = ((0, 0x03), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x53),
          (6, 0xef), (7, 0x9d), (11, 0xf1), (12, 0xba), (13, 0x01),
          (14, 0x04), (19, 0x64), (20, 0xe6), (21, 0x5a), (22, 0x8c),
          (23, 0x48), (24, 0x08), (25, 0x8e), (26, 0x84), (27, 0x5f),
          (28, 0xe9), (29, 0x04), (30, 0x9e), (31, 0x51), (32, 0xb0),
          (33, 0x7d), (34, 0x7f), (35, 0x47), (36, 0xe9), (37, 0x34),
          (38, 0xad), (39, 0xb7), (40, 0x48), (41, 0xe0), (42, 0xa7),
          (43, 0x56), (44, 0x08), (45, 0xfc), (46, 0x16), (47, 0x4b),
          (48, 0x49), (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5F2T = ("73bc56c8f31106", "f3bc3068333705", "b37c520093ee04",
          "137c5300f37f05", "d37cb63813a604", "733c555093ee04",
          "f33c3540333705", "933c3600333705", "33fc579893ee04",
          "d3bc586093ee04")
# T5F3/F4 tables: 16-tabs keyed (off-zone)&15; k2 segs keyed >>4.
# F4 b20-22 walk the F3 tab (k2=0..8). F4 b11 = cycle3 over a
# 4-step advance that pauses when (off-348)&15==8 (OPEN why).
_T5F3T20 = (0xd7, 0x5a, 0xab, 0xfc, 0x4d, 0x9e, 0xef, 0x40,
            0x91, 0xe2, 0x33, 0x84, 0xd5, 0x26, 0x77, 0xc8)
_T5F3T21 = (0x5f, 0x5a, 0xda, 0x5a, 0xdb, 0x5b, 0xdb, 0x5c,
            0xdc, 0x5c, 0xdd, 0x5d, 0xdd, 0x5e, 0xde, 0x5e)
_T5F3T22 = (0x86, 0x8c, 0x91, 0x97, 0x9c, 0xa2, 0xa7, 0xad,
            0xb2, 0xb8, 0xbd, 0xc3, 0xc8, 0xce, 0xd3, 0xd9)
_T5F3K = ("44fc60f37f05", "14fc6193ee04", "74bc62f37f05",
          "823c87d35d04")
_T5F3C = ((0, 0x3f), (1, 0x00), (2, 0x00), (3, 0x00), (6, 0xef),
          (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80), (11, 0x16),
          (12, 0x00), (19, 0x45), (23, 0x88), (24, 0x8c),
          (25, 0xe0), (26, 0x48), (27, 0xf8), (28, 0xe9),
          (29, 0x04), (30, 0x9e), (31, 0x51), (32, 0xb0),
          (33, 0x7d), (34, 0x7f), (35, 0x47), (36, 0xe9),
          (37, 0x34), (38, 0xad), (39, 0xb7), (40, 0x48),
          (41, 0xe0), (42, 0xa7), (43, 0x56), (44, 0x08),
          (45, 0xfc), (46, 0x16), (47, 0x4b), (48, 0x49),
          (49, 0x28), (50, 0x5b), (51, 0xfb))
_T5F4T19 = (0x90, 0xcc, 0xce, 0xe0, 0x0d, 0x0f, 0x4c, 0x4e,
            0x8b, 0x8d, 0xca, 0xcc, 0x08, 0x0a, 0x47, 0x49)
_T5F4T26 = (0x9a, 0xc8, 0xc8, 0xc8, 0xf6, 0xf6, 0x24, 0x24,
            0x52, 0x52, 0x80, 0x80, 0xae, 0xae, 0xdc, 0xdc)
_T5F4T27 = (0x78, 0xf9, 0xf9, 0x79, 0xf8, 0xf8, 0xf8, 0xf8,
            0x79, 0x79, 0x78, 0x78, 0xf9, 0xf9, 0xf8, 0xf8)
_T5F4C = ((0, 0xeb), (1, 0x03), (2, 0x00), (3, 0x00), (6, 0xef),
          (7, 0x9d), (8, 0x53), (9, 0x37), (10, 0x80), (12, 0x00),
          (13, 0xc4), (14, 0xbc), (15, 0x43), (16, 0x33),
          (17, 0x37), (18, 0x05), (23, 0x88), (24, 0x8c),
          (25, 0xe0), (28, 0x0d), (29, 0x61), (30, 0xe3),
          (31, 0x19), (32, 0xbe), (33, 0xbf), (34, 0xa3),
          (35, 0x13), (36, 0xe9), (37, 0x34), (38, 0xad),
          (39, 0xb7), (40, 0x48), (41, 0xe0), (42, 0xa7),
          (43, 0x56), (44, 0x08), (45, 0xfc), (46, 0x16),
          (47, 0x4b), (48, 0x49), (49, 0x28), (50, 0x5b),
          (51, 0xfb))


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
    if len(pay) not in (44, 48, 52):
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
    if n <= 2468:  # T5 E-plateau (NOTE-w2s7-24: tabs + k2-tabs)
        if len(pay) != 52:
            return fail("T5E paylen")
        off = n - 2213
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5E lencode")
        m = off & 15
        k2 = off >> 4
        if pay[5] != (_T5ET5H[m] | (l10 >> 8)):
            return fail("T5E b5")
        if pay[6] != _T5ET6[m] or pay[7] != _T5ET7[m]:
            return fail("T5E b67")
        if pay[44] != _T5EK44[k2] or pay[45] != _T5EK45[k2] or \
                pay[50] != _T5EK50[k2] or pay[51] != _T5EK51[k2]:
            return fail("T5E K")
        for b, v in ((0, 0x08), (1, 0), (2, 0), (3, 0), (8, 0x54),
                     (9, 0xf9), (10, 0x87), (11, 0xd7), (12, 0x70),
                     (13, 0xf1), (14, 0), (15, 0), (16, 0xee),
                     (17, 0xaa), (18, 0x26), (19, 0x8b), (20, 0xe6),
                     (21, 0x5a), (22, 0x8c), (23, 0x48), (24, 0x08),
                     (25, 0x8e), (26, 0x84), (27, 0x5f), (28, 0x09),
                     (29, 0x36), (30, 0x9e), (31, 0x81), (32, 0xbe),
                     (33, 0xbf), (34, 0xa3), (35, 0x13), (36, 0xe9),
                     (37, 0x34), (38, 0xad), (39, 0xb7), (40, 0x48),
                     (41, 0xc0), (42, 0x85), (43, 0xb7), (46, 0xd6),
                     (47, 0x3e), (48, 0x43), (49, 0x60)):
            if pay[b] != v:
                return fail("T5E const %d" % b)
        print("CLOSED T5E N=%d off=%d" % (n, off))
        return 0
    if n <= 2496:  # T5 F-head: dip-pair + F1 ramp + F2
        off = n - 2213
        if off <= 257:  # 48B dip literals N=2469/2470
            if len(pay) != 48 or pay.hex() != _T5DIP[off - 256]:
                return fail("T5DIP N=%d" % n)
            print("CLOSED T5DIP N=%d" % n)
            return 0
        if len(pay) != 52:
            return fail("T5F paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5F lencode")
        if off <= 273:  # F1 ramp halves
            if off <= 265:
                consts, ramp = _T5F1A, (0x8b + (off - 258) * 8) & 0xff
            else:
                consts, ramp = _T5F1B, (0x05 + (off - 266) * 8) & 0xff
            tag = "T5F1"
        else:  # F2 fixed rows
            consts, ramp = _T5F2C, None
            tag = "T5F2"
        if ramp is not None and pay[10] != ramp:
            return fail("T5F1 b10")
        if ramp is None:
            row = _T5F2T[off - 274]
            if pay[8:11].hex() + pay[15:19].hex() != row:
                return fail("T5F2 row")
        for b, v in consts:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n <= 2560:  # T5F3: 16-tabs + k2 b13-18 + b5 edge flip
        off = n - 2213
        if len(pay) != 52:
            return fail("T5F3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5F3 lencode")
        m = (off - 284) & 15
        k2 = (off - 284) >> 4
        if pay[5] != (83 + (off == 347)):
            return fail("T5F3 b5")
        if pay[13:19].hex() != _T5F3K[k2]:
            return fail("T5F3 k2")
        if pay[20] != _T5F3T20[m] or pay[21] != _T5F3T21[m] or \
                pay[22] != _T5F3T22[m]:
            return fail("T5F3 tab")
        for b, v in _T5F3C:
            if pay[b] != v:
                return fail("T5F3 const %d" % b)
        print("CLOSED T5F3 N=%d off=%d" % (n, off))
        return 0
    if n <= 2816:  # T5F4/F5: unified tabs+walk+b11; F5 cont F4
        off = n - 2213
        tag = "T5F4" if off <= 487 else "T5F5"
        if len(pay) != 52:
            return fail("T5F4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5F4 lencode")
        m = (off - 348) & 15
        k2 = (off - 348) >> 4
        if pay[5] != (84 + (off >= 475) + (off == 603)):
            return fail("T5F4 b5")
        q = (off - 348) >> 2
        pauses = ((q - 2) >> 2) + 1 if q >= 2 else 0
        if pay[11] != (0x63, 0x64, 0x65)[(q - pauses) % 3]:
            return fail("T5F4 b11")
        if pay[19] != _T5F4T19[m]:
            return fail("T5F4 b19")
        if pay[20] != _T5F3T20[k2] or pay[21] != _T5F3T21[k2] or \
                pay[22] != _T5F3T22[k2]:
            return fail("T5F4 walk")
        if pay[26] != _T5F4T26[m] or pay[27] != _T5F4T27[m]:
            return fail("T5F4 tab")
        for b, v in _T5F4C:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n == 2817:  # 48B short-form dip (off=604)
        if len(pay) != 48 or pay.hex() != _T5DIP604:
            return fail("T5DIP604")
        print("CLOSED T5DIP604 N=2817")
        return 0
    if n == 2818:  # 52B transition singleton (off=605)
        if len(pay) != 52 or pay.hex() != _T5G0:
            return fail("T5G0")
        print("CLOSED T5G0 N=2818")
        return 0
    if n <= 2834:  # T5G1: 16-row b32-35 tab + frozen body
        off = n - 2213
        if len(pay) != 52:
            return fail("T5G1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5G1 lencode")
        if pay[32:36].hex() != _T5G1T[off - 606]:
            return fail("T5G1 row")
        for b, v in _T5G1C:
            if pay[b] != v:
                return fail("T5G1 const %d" % b)
        print("CLOSED T5G1 N=%d off=%d" % (n, off))
        return 0
    if n <= 2844:  # T5G2: 10-row b32-37 tab + frozen body
        off = n - 2213
        if len(pay) != 52:
            return fail("T5G2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5G2 lencode")
        if pay[32:38].hex() != _T5G2T[off - 622]:
            return fail("T5G2 row")
        for b, v in _T5G2C:
            if pay[b] != v:
                return fail("T5G2 const %d" % b)
        print("CLOSED T5G2 N=%d off=%d" % (n, off))
        return 0
    if n <= 2908:  # T5G3: 16-tabs b30/31/38/39 + k2 b32-37
        off = n - 2213
        if len(pay) != 52:
            return fail("T5G3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5G3 lencode")
        m = (off - 632) & 15
        k2 = (off - 632) >> 4
        if pay[30] != _T5G3T30[m] or pay[31] != _T5G3T31[m]:
            return fail("T5G3 tab30")
        if pay[32:38].hex() != _T5G3K[k2]:
            return fail("T5G3 k2")
        if pay[38] != _T5G3T38[m] or pay[39] != _T5G3T39[m]:
            return fail("T5G3 tab38")
        for b, v in _T5G3C:
            if pay[b] != v:
                return fail("T5G3 const %d" % b)
        print("CLOSED T5G3 N=%d off=%d" % (n, off))
        return 0
    if n <= 3164:  # T5H: 16-tabs b44-47 + k2 b32/37/38/39 + edges
        off = n - 2213
        if len(pay) != 52:
            return fail("T5H paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5H lencode")
        m = (off - 696) & 15
        k2 = (off - 696) >> 4
        if pay[5] != (86 + (off >= 731) + (off >= 859)):
            return fail("T5H b5")
        if pay[32] != _T5HK32[k2] or pay[37] != _T5HK37[k2]:
            return fail("T5H k2a")
        if pay[33] != (240 + (k2 >= 4) + (k2 >= 12)):
            return fail("T5H b33")
        if pay[38] != _T5HK38[k2] or pay[39] != _T5HK39[k2]:
            return fail("T5H k2b")
        if pay[44] != _T5HT44[m] or pay[45] != _T5HT45[m] or \
                pay[46] != _T5HT46[m] or pay[47] != _T5HT47[m]:
            return fail("T5H tab")
        for b, v in _T5HC:
            if pay[b] != v:
                return fail("T5H const %d" % b)
        print("CLOSED T5H N=%d off=%d" % (n, off))
        return 0
    if n <= 3166:  # T5I0: transition pair literals (off=952/953)
        off = n - 2213
        if len(pay) != 52 or pay.hex() != _T5I0[off - 952]:
            return fail("T5I0")
        print("CLOSED T5I0 N=%d" % n)
        return 0
    if n <= 3182:  # T5I1a: 16-row b48-51 tab + frozen body
        off = n - 2213
        if len(pay) != 52:
            return fail("T5I1a paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5I1a lencode")
        if pay[48:52].hex() != _T5I1AT[off - 954]:
            return fail("T5I1a row")
        for b, v in _T5I1AC:
            if pay[b] != v:
                return fail("T5I1a const %d" % b)
        print("CLOSED T5I1a N=%d off=%d" % (n, off))
        return 0
    if n <= 3192:  # T5I1b: 10-row b35/b44-47/b50-51 tab
        off = n - 2213
        if len(pay) != 52:
            return fail("T5I1b paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5I1b lencode")
        row = _T5I1BT[off - 970]
        if pay[35:36].hex() + pay[44:48].hex() + pay[50:52].hex() != row:
            return fail("T5I1b row")
        for b, v in _T5I1BC:
            if pay[b] != v:
                return fail("T5I1b const %d" % b)
        print("CLOSED T5I1b N=%d off=%d" % (n, off))
        return 0
    if n <= 3256:  # T5I2: 16-tabs b5/6/7 + b8 bands + k2 segs
        off = n - 2213
        if len(pay) != 52:
            return fail("T5I2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5I2 lencode")
        m = (off - 980) & 15
        k2 = (off - 980) >> 4
        if pay[5] != ((_T5I2T5[m] + (k2 >= 1 and m <= 6)) & 0xff):
            return fail("T5I2 b5")
        if pay[6] != _T5I2T6[m] or pay[7] != _T5I2T7[m]:
            return fail("T5I2 tab67")
        if pay[8] != (0x37, 0x57, 0x77)[(m >= 6) + (m >= 11)]:
            return fail("T5I2 b8")
        row = _T5I2K[k2]
        if pay[35:36].hex() + pay[44:48].hex() + pay[50:52].hex() != row:
            return fail("T5I2 k2")
        for b, v in _T5I2C:
            if pay[b] != v:
                return fail("T5I2 const %d" % b)
        print("CLOSED T5I2 N=%d off=%d" % (n, off))
        return 0
    if n <= 3512:  # T5I3: I2-walk b6/7 + b5 k2-tab + b8 + tabs
        off = n - 2213
        if len(pay) != 52:
            return fail("T5I3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5I3 lencode")
        m = (off - 1044) & 15
        k2 = (off - 1044) >> 4
        if pay[5] != ((_T5I3K5[k2] + (m >= 7 and k2 in (4, 12))) & 0xff):
            return fail("T5I3 b5")
        if pay[6] != _T5I2T6[k2] or pay[7] != _T5I2T7[k2]:
            return fail("T5I3 walk")
        if pay[8] != (0x37, 0x57, 0x77)[(k2 >= 6) + (k2 >= 11)]:
            return fail("T5I3 b8")
        if pay[13] != _T5I3T13[m] or pay[14] != _T5I3T14[m] or \
                pay[15] != _T5I3T15[m] or pay[16] != _T5I3T16[m]:
            return fail("T5I3 tab")
        for b, v in _T5I3C:
            if pay[b] != v:
                return fail("T5I3 const %d" % b)
        print("CLOSED T5I3 N=%d off=%d" % (n, off))
        return 0
    if n <= 3515:  # T5J0: 3 transition literals (off=1300..1302)
        off = n - 2213
        if len(pay) != 52 or pay.hex() != _T5J0[off - 1300]:
            return fail("T5J0")
        print("CLOSED T5J0 N=%d" % n)
        return 0
    if n <= 3530:  # T5J1: 15-row b0/b1/b11/b19 tab
        off = n - 2213
        if len(pay) != 52:
            return fail("T5J1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5J1 lencode")
        cells = bytes((pay[0], pay[1], pay[11], pay[19])).hex()
        if cells != _T5J1T[off - 1303]:
            return fail("T5J1 row")
        for b, v in _T5J1C:
            if pay[b] != v:
                return fail("T5J1 const %d" % b)
        print("CLOSED T5J1 N=%d off=%d" % (n, off))
        return 0
    if n <= 3540:  # T5J2: 10-row tab b0/b1/b2/b11/b19/b24
        off = n - 2213
        if len(pay) != 52:
            return fail("T5J2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5J2 lencode")
        cells = bytes((pay[0], pay[1], pay[2], pay[11], pay[19],
                       pay[24])).hex()
        if cells != _T5J2T[off - 1318]:
            return fail("T5J2 row")
        for b, v in _T5J2C:
            if pay[b] != v:
                return fail("T5J2 const %d" % b)
        print("CLOSED T5J2 N=%d off=%d" % (n, off))
        return 0
    if n <= 3604:  # T5J3-6: shared b24-27 tab + k2 overrides
        off = n - 2213
        if len(pay) != 52:
            return fail("T5J3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5J3 lencode")
        m = (off - 1328) & 15
        k2 = (off - 1328) >> 4
        tag = "T5J%d" % (k2 + 3)
        if pay[5] != (0xfb + (off >= 1371)):
            return fail("T5J3 b5")
        if pay[13:16].hex() + pay[18:22].hex() != _T5J3K[k2]:
            return fail("T5J3 k2")
        if pay[24:28].hex() != _T5J3T[m]:
            return fail("T5J3 tab")
        for b, v in _T5J3C:
            if pay[b] != v:
                return fail("%s const %d" % (tag, b))
        print("CLOSED %s N=%d off=%d" % (tag, n, off))
        return 0
    if n <= 3860:  # T5K: 16-tabs + J3-walk b24-27 + b5 edge
        off = n - 2213
        if len(pay) != 52:
            return fail("T5K paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5K lencode")
        m = (off - 1392) & 15
        k2 = (off - 1392) >> 4
        if pay[5] != (252 + (off >= 1499) + (off >= 1627)):
            return fail("T5K b5")
        if pay[15] != _T5KT15[m] or pay[22] != _T5KT22[m] or \
                pay[23] != _T5KT23[m]:
            return fail("T5K tabA")
        if pay[24:28].hex() != _T5J3T[k2]:
            return fail("T5K walk")
        if pay[30] != _T5KT30[m] or pay[31] != _T5KT31[m]:
            return fail("T5K tabB")
        for b, v in _T5KC:
            if pay[b] != v:
                return fail("T5K const %d" % b)
        print("CLOSED T5K N=%d off=%d" % (n, off))
        return 0
    print("N out of scope", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
