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
# T5L tables (tier tail): 2 transition literals + 16-row L1
# tab + 10-row L2 tab + L3 16-tabs/k2. Row-tabs OPEN why.
_T5L0 = ("01cd09002bfe91b5f4cd736e0041bc433491d1deab9f74399254e007"
         "ed844c4aa2bf571eacae38b9c8759b37cccdddad2dcc06fc",
         "827887022dfe91b5f4cd7300b480e61a898cf6be4b923fe3823c45b6"
         "cd3da7f0129741979cdc4989c8759b37cccdddad2dcc06fc")
_T5L1T = ("475ff894", "a85bfd94", "b9de0195", "1adb0695",
          "1adf0695", "7bdb0b95", "8c5e1095", "ed5a1595",
          "fedd1995", "46db3695", "575e3b95", "b85a4095",
          "c9dd4495", "195b4595", "2ade4995", "8bda4e95")
_T5L1C = ((0, 0x82), (1, 0x78), (2, 0x87), (3, 0x22), (5, 0xfe),
          (6, 0x91), (7, 0xb5), (8, 0xf4), (9, 0xcd),
          (10, 0x73), (11, 0x00), (12, 0xb4), (13, 0x80),
          (14, 0xe6), (15, 0xce), (16, 0x89), (17, 0x8c),
          (18, 0xf6), (19, 0xbe), (20, 0x4b), (21, 0x92),
          (22, 0xcf), (23, 0x29), (24, 0x82), (25, 0x3c),
          (26, 0x45), (27, 0xb6), (28, 0xcd), (29, 0x3d),
          (30, 0x47), (31, 0xf1), (32, 0x52), (33, 0x72),
          (34, 0xc2), (35, 0x71), (40, 0x0c), (41, 0x5d),
          (42, 0xb7), (43, 0x79), (44, 0xcc), (45, 0xcd),
          (46, 0xdd), (47, 0xad), (48, 0x2d), (49, 0xcc),
          (50, 0x06), (51, 0xfc))
_T5L2T = ("0870625cebdfd6b00d006cf3", "0438322e7f5aae632cfab779",
          "0438322e8759acfeecf8b779", "0438322e475f8ace4cfbb779",
          "0438322e17dcb7632cfab779", "0438322efbdb4e9fccf7b779",
          "0438322e305a94ce4cfbb779", "0438322e3d5ad7feecf8b779",
          "0438322e63dac1632cfab779", "0438322e245fe0feecf8b779")
_T5L2C = ((0, 0x82), (1, 0x78), (2, 0x87), (5, 0xfe), (6, 0x91),
          (7, 0xb5), (8, 0xf4), (9, 0xcd), (10, 0x73),
          (11, 0x00), (12, 0xb4), (13, 0x80), (14, 0xe6),
          (16, 0x89), (17, 0x8c), (18, 0xf6), (19, 0xbe),
          (20, 0x4b), (21, 0x92), (22, 0x7f), (23, 0xaa),
          (24, 0x82), (25, 0x3c), (26, 0x45), (27, 0xb6),
          (28, 0xcd), (29, 0x3d), (30, 0x27), (31, 0xf4),
          (32, 0x2f), (33, 0xd8), (44, 0xcc), (45, 0xcd),
          (46, 0xdd), (47, 0xad), (48, 0x2d), (49, 0xcc),
          (50, 0x06), (51, 0xfc))
_T5L3T34 = (0x02, 0xb2, 0x22, 0xe2, 0x52, 0x02, 0x82, 0x32,
            0xb2, 0x72, 0xe2, 0xf2, 0x02, 0x22, 0x42, 0x52)
_T5L3T35 = (0x29, 0x2c, 0x44, 0x46, 0x5e, 0x62, 0x78, 0x7c,
            0x92, 0x96, 0xac, 0xc6, 0xc8, 0xe2, 0xe2, 0xfc)
_T5L3T42 = (0xb5, 0x55, 0x47, 0xd7, 0xc9, 0x69, 0x4b, 0xeb,
            0xcd, 0x6d, 0x4f, 0xd1, 0xe1, 0x63, 0x63, 0xe5)
_T5L3T43 = (0x78, 0xf8, 0x79, 0xf8, 0x79, 0xf9, 0xf8, 0xf9,
            0xf8, 0x78, 0xf9, 0xf9, 0xf9, 0x78, 0x78, 0x78)
_T5L3K = ("3c5ea2ce4cfb", "495ee5feecf8", "5edeab3e8cfc",
          "495e839fccf7")
# T6A tables (56-tier head off 0..142): 16-tabs b52-55
# (PRE-025b concur EXACT) + k2 segs b38/39/46/47 + b5 edge.
_T6AT52 = (0x8c, 0x0c, 0x0c, 0x6c, 0xec, 0xec, 0x4c, 0xac,
           0xcc, 0x2c, 0x2c, 0x8c, 0x0c, 0x0c, 0x8c, 0xcc)
_T6AT53 = (0x85, 0xae, 0x7f, 0xc2, 0xea, 0xbb, 0xff, 0x8a,
           0xf8, 0xa0, 0x71, 0x98, 0xdd, 0xae, 0xd6, 0x7c)
_T6AT54 = (0xc7, 0x2f, 0xff, 0x77, 0xdf, 0xaf, 0x27, 0x97,
           0x5f, 0xcf, 0x9f, 0x17, 0x7f, 0x4f, 0xb7, 0x37)
_T6AT55 = (0x84, 0x85, 0x85, 0x95, 0x95, 0x96, 0xa6, 0xa6,
           0xa7, 0xb2, 0xb3, 0xb8, 0xc3, 0xc4, 0xc4, 0xd4)
_T6AK = ("0229b578", "b22c55f8", "22444779", "e246d7f8",
         "525ec979", "026269f9", "82784bf8", "327cebf9",
         "b292cdf8")
# T6B tables: post-4096 reframe. b53/54/55 tabs SHARED with A;
# b52 post-tab (PRE-025b concur, rotated to off&15 key); body
# = PRE-024b reframe values; k2 segs continue k2=9..15.
_T6BT52 = (0x8d, 0x0d, 0x0d, 0x6d, 0xed, 0xed, 0x4d, 0xad,
           0xcd, 0x2d, 0x2d, 0x8d, 0x0d, 0x0d, 0x8d, 0xcd)
_T6BK = ("b292cdf8", "72966d78", "e2ac4ff9", "f2c6d1f9",
         "02c8e1f9", "22e26378", "42e26378", "52fce578")
_T6DIP256 = ("04f10e05e3e0236bf59be700b480e618898cf6be4b927faa823c45b6"
             "cd3d27f42fd8129718db42bcab03dbbccccdddad2ddc06fc")
# T6C tables (cluster C): 2 transition literals + 15-row C1
# + 10-row C2 + C3-6 shared 16-tab b13-17 + k2 b5-11.
_T6C0 = ("03000000e5e0236b15f10e0ddf3c07203491d180ef5b40734b927faa"
         "823c45b6cd3d27f42fd802cf18db42bcab036dbc2d8a75eccdf61fd1",
         "31000000e780530b19bf790e0041bc433491d180ef5b40734b927faa"
         "823c45b6cd3d27f42fd802cf18db42bcab036dbc2d8a61ae2dd44fda")
_T6C1T = ("e0908b19", "40ce0b39", "805c1b39", "e0999b39",
          "40d71b59", "80652b59", "80cfcb99", "201b5bb9",
          "8058dbb9", "e0955bd9", "20246bd9", "8061ebd9",
          "e19e6bf9", "212d7bf9", "816afbf9")
_T6C1C = ((0, 0x31), (1, 0x00), (2, 0x00), (3, 0x00), (9, 0xbf),
          (10, 0x79), (11, 0x0e), (12, 0x00), (13, 0x41),
          (14, 0xbc), (15, 0x43), (16, 0x34), (17, 0x91),
          (18, 0xd1), (19, 0x80), (20, 0xef), (21, 0x5b),
          (22, 0x40), (23, 0x73), (24, 0x4b), (25, 0x92),
          (26, 0x7f), (27, 0xaa), (28, 0x82), (29, 0x3c),
          (30, 0x45), (31, 0xb6), (32, 0xcd), (33, 0x3d),
          (34, 0x27), (35, 0xf4), (36, 0x2f), (37, 0xd8),
          (38, 0x02), (39, 0xcf), (40, 0x18), (41, 0xdb),
          (42, 0x42), (43, 0xbc), (44, 0xab), (45, 0x03),
          (46, 0x6d), (47, 0xbc), (48, 0x2d), (49, 0x8a),
          (50, 0x61), (51, 0xae), (52, 0x2d), (53, 0xd4),
          (54, 0x4f), (55, 0xda))
_T6C2T = ("c1abfb7d1af6", "61fe4be7a8f1", "4161fbe9a8f1",
          "c1c1eb5d8bf2", "c1f37beaa8f1", "c18a5b9be5ef",
          "61b71b618bf2", "815eabfec6f0", "c1359beba8f1",
          "a1aeabffc6f0")
_T6C2C = ((0, 0x04), (1, 0x00), (2, 0x00), (3, 0x00), (8, 0x59),
          (9, 0x10), (10, 0xef), (11, 0x50), (15, 0x00),
          (16, 0xb4), (17, 0x80), (18, 0xe6), (19, 0x00),
          (20, 0x89), (21, 0x8c), (22, 0xf6), (23, 0xbe),
          (24, 0x4b), (25, 0x92), (26, 0x7f), (27, 0xaa),
          (28, 0x82), (29, 0x3c), (30, 0x45), (31, 0xb6),
          (32, 0xcd), (33, 0x3d), (34, 0x27), (35, 0xf4),
          (36, 0x2f), (37, 0xd8), (38, 0x02), (39, 0xcf),
          (40, 0x18), (41, 0xdb), (42, 0x42), (43, 0xbc),
          (44, 0xab), (45, 0x03), (46, 0x6d), (47, 0xbc),
          (48, 0x2d), (49, 0x8a), (50, 0x5d), (51, 0x7b),
          (52, 0xad), (53, 0xa0), (54, 0xf7), (55, 0xa5))
_T6C3T = ("7abca4d811", "7abca5d811", "c77c55f811", "e37c72f811",
          "307c221812", "307c231812", "7d3cd31812", "7d3cd41812",
          "cafc833812", "e6fca03812", "33fc505812", "33fc515812",
          "80bc017812", "80bc027812", "cd7cb27812", "d13cc87812")
_T6C3K = ("01eb2b596c511e", "814f3b19e0181e", "41357b59cc6d1e",
          "41affbb9b3fc1d")
# T6E tables (cluster E, +348 mirror-shape of C): 3 transition
# literals + 15-row E1 + 10-row E2 + E3-6 shared tab + k2.
_T6E0 = ("010000009b233cdb17c43b14eb053380b480e600898cf6be4b927faa"
         "823c45b6cd3d27f42fd802cf18db42bcab036dbc2d8a5d7bada0f7a5",
         "880000009d233cdb77bd600600323cc815fb5aa82bdf6b1a5181f49f8"
         "23c45b6cd3d27f42fd802cf18db42bcab036dbc2d8a5d7bada0f7a5",
         "800800009f233cdb77bd60a600323cc815fb5aa4d7de5ca7d108f5ff"
         "a07c748071dd73422fd802cf18db42bcab036dbc2d8a5d7bada0f7a5")
_T6E1T = ("39bc5181", "d2fc2682", "697c4582", "02bc2283",
          "99fc4083", "327c1684", "cb7cf384", "03fcb388",
          "9cfc9089", "33bca789", "ccbc848a", "ccbc858a",
          "fc3c808b", "95bc558c", "95bc568c")
_T6E1C = ((0, 0x80), (1, 0x08), (2, 0x00), (3, 0x00), (5, 0x23),
          (6, 0x3c), (7, 0xdb), (8, 0x77), (9, 0xbd),
          (10, 0x60), (11, 0xa6), (12, 0x00), (13, 0x32),
          (14, 0x3c), (15, 0xc8), (16, 0x15), (17, 0xfb),
          (18, 0x5a), (19, 0xa4), (20, 0xd7), (21, 0xde),
          (22, 0x5c), (23, 0xa7), (24, 0xd1), (25, 0x08),
          (26, 0xf5), (27, 0xff), (32, 0x71), (33, 0xdd),
          (34, 0x73), (35, 0x42), (36, 0x2f), (37, 0xd8),
          (38, 0x02), (39, 0xcf), (40, 0x18), (41, 0xdb),
          (42, 0x42), (43, 0xbc), (44, 0xab), (45, 0x03),
          (46, 0x6d), (47, 0xbc), (48, 0x2d), (49, 0x8a),
          (50, 0x5d), (51, 0x7b), (52, 0xad), (53, 0xa0),
          (54, 0xf7), (55, 0xa5))
_T6E2T = ("8c0386ccd1e6b970", "4203a62c61e5f569",
          "440346d469e4f569", "c902667c51e64e6b",
          "4603463c61e2f569", "6b02c6f489e3f065",
          "d202a63ca9e34e6b", "5703063cf9e49d68",
          "4903e664c1e1f569", "5a03a62cc9e79d68")
_T6E2C = ((2, 0x00), (3, 0x00), (5, 0x23), (6, 0x3c), (7, 0xdb),
          (8, 0x77), (9, 0xbd), (10, 0x60), (12, 0x00),
          (13, 0x32), (14, 0x3c), (15, 0xc8), (16, 0x15),
          (17, 0xfb), (18, 0x5a), (20, 0x56), (21, 0xdb),
          (22, 0x84), (23, 0x22), (24, 0x8e), (25, 0x58),
          (28, 0xf2), (29, 0x4f), (30, 0x15), (31, 0x10),
          (34, 0x24), (35, 0xf4), (36, 0x2f), (37, 0xd8),
          (38, 0x02), (39, 0xcf), (40, 0x18), (41, 0xdb),
          (42, 0x42), (43, 0xbc), (44, 0xab), (45, 0x03),
          (46, 0x6d), (47, 0xbc), (48, 0x2d), (49, 0x8a),
          (50, 0x5d), (51, 0x7b), (52, 0xad), (53, 0xa0),
          (54, 0xf7), (55, 0xa5))
_T6E3T = ("f22b4b70f0", "f22f4bc8f0", "f2ed4d74f3", "f2f14dccf3",
          "f2494e88f0", "f29750a8f3", "f29b5000f4", "d25b53d8fe",
          "d25f5330ff", "f21d56dcf1", "f2215634f2", "d2715880fd",
          "f2c75810f2", "f2cb5868f2", "f2375bdcf0", "d28f5b98fd")
_T6E3K = ("d6224664f9e24e6b", "1d230684b9e74667",
          "142246d499e6a86c", "1e23c64401e14667")
# T6F tables (quiet-256): 16-tabs b40-43 + k2 segs b32-35
# + b5 edges @783/911.
_T6FT40 = (0xea, 0x4b, 0xeb, 0xfc, 0x44, 0x94, 0xf5, 0x06,
           0x67, 0x9e, 0xff, 0x10, 0xb0, 0x00, 0x09, 0xa9)
_T6FT41 = (0x5f, 0x5c, 0xd9, 0x5c, 0x5a, 0x5e, 0x5a, 0xde,
           0xda, 0xdf, 0xdb, 0x5f, 0xdc, 0x5a, 0x5d, 0xda)
_T6FT42 = (0xc1, 0xc6, 0x17, 0x1c, 0x39, 0x8a, 0x8f, 0x93,
           0x98, 0x01, 0x06, 0x0b, 0x5c, 0x5d, 0x7e, 0xcf)
_T6FT43 = (0xbf, 0xbf, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0, 0xc0,
           0xc0, 0xc1, 0xc1, 0xc1, 0xc1, 0xc1, 0xc1, 0xc1)
_T6FK = ("1cfc5796", "32fc5f96", "ddfcdb9b", "f3fce39b",
         "22fc939c", "eafc2fa1", "00fd37a1", "b6bfb7a6",
         "ccbfbfa6", "77fc3bac", "8dfc43ac", "60bfe3b0",
         "84fc8fb1", "9afc97b1", "37fc6fb6", "66bf1fb7")
# T6G tables (cluster G): 3 transition literals + 15-row G1
# + 10-row G2 + G3-6 shared b50-55 tab (b50 +1 in G5) + k2.
_T6G0 = ("4400000053263cdb77bd600600323cc815fb5a5456db84228e58f94f"
         "fbbc1534cf5a9fd02fd802cf18db42bcab036dbc2d8a5d7bada0f7a5",
         "6810000055263cdb77bd602600323cc815fb5ab456db84228e58d9e7"
         "efeb3883d67ae3dfefa1fcc247dc061f513f4c1b2d8a5d7bada0f7a5",
         "6812010057263cdb77bd602600323cc815fb5ab456db84228e58d9e7"
         "cf5a8ff8c6bfbf8eefa1fc4db9da4ebb31998c3911a2d8b5ada0f7a5")
_T6G1T = ("8ff8c48c2d", "bff894cc09", "cff80acc3d", "8ff9ca8c20",
          "9ff9418c14", "cff910cc30", "fff9530c01", "fff9570c01",
          "2ffa994c11", "2ffa9d4c11", "5ffadf8c21", "6ffa018c23",
          "9ffa43cc33", "3ffb194c38", "6ffb5c8c08")
_T6G1C = ((0, 0x68), (1, 0x12), (2, 0x01), (3, 0x00), (5, 0x26),
          (6, 0x3c), (7, 0xdb), (8, 0x77), (9, 0xbd),
          (10, 0x60), (11, 0x26), (12, 0x00), (13, 0x32),
          (14, 0x3c), (15, 0xc8), (16, 0x15), (17, 0xfb),
          (18, 0x5a), (19, 0xb4), (20, 0x56), (21, 0xdb),
          (22, 0x84), (23, 0x22), (24, 0x8e), (25, 0x58),
          (26, 0xd9), (27, 0xe7), (28, 0xcf), (29, 0x5a),
          (32, 0xc6), (33, 0xbf), (34, 0xbf), (35, 0x8e),
          (36, 0xef), (37, 0xa1), (38, 0xfc), (40, 0xb9),
          (41, 0xda), (42, 0x4e), (43, 0xbb), (44, 0x31),
          (45, 0x99), (48, 0x11), (49, 0xa2), (50, 0xd8),
          (51, 0xb5), (52, 0xad), (53, 0xa0), (54, 0xf7),
          (55, 0xa5))
_T6G2T = ("d89ccc1019f0116aee", "089c3cb471f031bfed",
          "589e3c3c8df2319ded", "989ccc610df331e1ed",
          "189c6cb465f231bfed", "989ccce951f3f137ed",
          "a89c0c620df131e1ed", "389f8c1969f2517bed",
          "189c4cf06df231bfed", "589e0cd401f1319ded")
_T6G2C = ((0, 0x68), (1, 0x10), (2, 0x00), (3, 0x00), (5, 0x26),
          (6, 0x3c), (7, 0xdb), (8, 0x77), (9, 0xbd),
          (10, 0x60), (11, 0x26), (12, 0x00), (13, 0x32),
          (14, 0x3c), (15, 0xc8), (16, 0x15), (17, 0xfb),
          (18, 0x5a), (19, 0xb4), (20, 0x56), (21, 0xdb),
          (22, 0x84), (23, 0x22), (24, 0x8e), (25, 0x58),
          (26, 0xd9), (27, 0xe7), (28, 0xef), (29, 0xeb),
          (32, 0xd6), (33, 0x7a), (34, 0xe3), (35, 0xdf),
          (36, 0xef), (37, 0xa1), (40, 0x5b), (41, 0x5f),
          (42, 0xe5), (43, 0xa8), (44, 0x0d), (45, 0x9d),
          (51, 0xb5), (52, 0xad), (53, 0xa0), (54, 0xf7),
          (55, 0xa5))
_T6G3T50 = (0xad, 0xad, 0xad, 0xad, 0xad, 0xad, 0xad, 0xed,
            0xed, 0xed, 0xed, 0xed, 0xed, 0xed, 0x2d, 0x2d)
_T6G3T51 = ("5dcd88a70e", "5d4db10f0f", "5d4d6a7f5e",
            "5dadadf76d", "5d6dadb7b9", "5d2d8fcfbd",
            "5d4dfd97be", "5d6db7f709", "5dcdfa6f19",
            "5dcdb3df68", "5dcd84af69", "5d4dad176a",
            "5d6d6777b5", "5d6df04fc5", "5ecd635f14",
            "5eedd12715")
_T6G3K = ("2fec9c244df131bf", "3fef6c5569f2517b",
          "afef5c31b5f13103", "afeebcf129f09159")
# T6H tables (run-256): 16-tabs b5-9 (b5 +edges @1167/1295)
# + b52-55 walk G3-tab by k2 (reuse) + b50/b51 k2-bands.
_T6HT5 = (0xc7, 0xc7, 0x27, 0xc7, 0x47, 0x87, 0xe7, 0x47,
          0xa7, 0x07, 0x67, 0x27, 0x27, 0x67, 0xc7, 0x87)
_T6HT6 = (0x34, 0x9e, 0xdc, 0x27, 0xb2, 0x40, 0x7d, 0xbb,
          0x80, 0xbe, 0xfb, 0x94, 0xfe, 0x8c, 0xc9, 0x62)
_T6HT7 = (0x8b, 0x2b, 0xab, 0x3b, 0x9b, 0xab, 0x2b, 0xab,
          0x3b, 0xbb, 0x3b, 0xab, 0x4b, 0x5b, 0xdb, 0x4b)
_T6HT8 = (0x1b, 0x7b, 0x7b, 0x9b, 0x7b, 0x7b, 0x9b, 0x9b,
          0xdb, 0xdb, 0xfb, 0xdb, 0x3b, 0x3b, 0x3b, 0x3b)
_T6HT9 = (0xd2, 0xd2, 0xd2, 0xd2, 0xd3, 0xd3, 0xd3, 0xd3,
          0xd4, 0xd4, 0xd4, 0xd5, 0xd6, 0xd6, 0xd6, 0xd7)
# T6I tables (cluster I): 3 transition literals + 15-row I1
# + 10-row I2 + I3-6 shared b20-23 tab + k2 b13-18.
_T6I0 = ("680400000b293cdb77bd602600323cc815fb5ab456db84228e58d9e7"
         "efeb8825d67ae3dfefa19c655b5fe5a80d9d19f1afd676edada0f7a5",
         "0a9a01000d4956bbbd8a4ca900323cc815fb5ab456db84228e58d9e7"
         "efeb8839d67ae3dfefa19c655b5fe5a80d9d19f1afd66639cdaedfb6",
         "aea019000f2971bbbd8a4ca9003bbc8819b5af4556db84228e58d9e7"
         "efeb8839d67ae3dfefa19c655b5fe5a80d9d19f1afd66639cdaedfb6")
_T6I1T = ("887c3839", "a47c5539", "f13c0559", "f13c0659",
          "3e3cb659", "3e3cb759", "8bfc6679", "a7fc8379",
          "3f3cb3b9", "8cfc62d9", "8cfc63d9", "d9bc13f9",
          "d9bc14f9", "26bcc4f9", "42bce1f9")
_T6I1C = ((0, 0xae), (1, 0xa0), (2, 0x19), (3, 0x00), (5, 0x29),
          (6, 0x71), (7, 0xbb), (8, 0xbd), (9, 0x8a),
          (10, 0x4c), (11, 0xa9), (12, 0x00), (17, 0xb5),
          (18, 0xaf), (19, 0x45), (20, 0x56), (21, 0xdb),
          (22, 0x84), (23, 0x22), (24, 0x8e), (25, 0x58),
          (26, 0xd9), (27, 0xe7), (28, 0xef), (29, 0xeb),
          (30, 0x88), (31, 0x39), (32, 0xd6), (33, 0x7a),
          (34, 0xe3), (35, 0xdf), (36, 0xef), (37, 0xa1),
          (38, 0x9c), (39, 0x65), (40, 0x5b), (41, 0x5f),
          (42, 0xe5), (43, 0xa8), (44, 0x0d), (45, 0x9d),
          (46, 0x19), (47, 0xf1), (48, 0xaf), (49, 0xd6),
          (50, 0x66), (51, 0x39), (52, 0xcd), (53, 0xae),
          (54, 0xdf), (55, 0xb6))
_T6I2T = ("fcfc8279ca3458", "153c71d98c8e57", "e0bcb4198d8e57",
          "2dbce71916aa57", "777c043916aa57", "0afcb259142157",
          "bdfce27916aa57", "dd7c6779157357", "b23c33598d8e57",
          "12fcc6598d8e57")
_T6I2C = ((0, 0x0a), (1, 0x9a), (2, 0x01), (3, 0x00), (5, 0x69),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0xf3), (12, 0x00), (20, 0x56),
          (21, 0xdb), (22, 0x84), (23, 0x22), (24, 0x8e),
          (25, 0x58), (26, 0xd9), (27, 0xe7), (28, 0xef),
          (29, 0xeb), (30, 0x88), (31, 0x39), (32, 0xd6),
          (33, 0x7a), (34, 0xe3), (35, 0xdf), (36, 0xef),
          (37, 0xa1), (38, 0x9c), (39, 0x65), (40, 0x5b),
          (41, 0x5f), (42, 0xe5), (43, 0xa8), (44, 0x0d),
          (45, 0x9d), (46, 0x19), (47, 0xf1), (48, 0xaf),
          (49, 0xd6), (50, 0x66), (51, 0x39), (52, 0xcd),
          (53, 0xae), (54, 0xdf), (55, 0xb6))
_T6I3T = ("edda821c", "a65b7b1f", "f7db801f", "735b1b20",
          "8e5ba022", "5e5a1423", "afda1923", "cada9e25",
          "655c3e26", "805cc328", "505b3729", "a1db3c29",
          "e7da562c", "385b5c2c", "a8dd662c", "425c5a2f")
_T6I3K = ("5dbce3598d8e", "507ce4991573", "a1fc7279b1c5",
          "107c4479593c")
# T6J tables (run-256): 16-tabs b0/1/2/26/27 + b20-23 walk
# the I3 tab by k2 (full 16, reuse) + b5 edges @1423/1551.
_T6JT0 = (0x0d, 0xb7, 0xa1, 0x01, 0xb7, 0xb9, 0xa3, 0x03,
          0xaf, 0xa3, 0x8b, 0x05, 0xb1, 0xb9, 0x05, 0xb1)
_T6JT1 = (0xb9, 0xbf, 0xc6, 0x1f, 0x1f, 0x3d, 0x44, 0x9d,
          0xa3, 0xa4, 0xab, 0x1b, 0x21, 0x21, 0x7b, 0x81)
_T6JT2 = (0x98, 0x98, 0x98, 0x99, 0x99, 0x99, 0x99, 0x99,
          0x99, 0x99, 0x99, 0x9a, 0x9a, 0x9a, 0x9a, 0x9a)
# T6K tables (cluster K): 3 transition literals + 15-row K1
# + 10-row K2 + K3-6 shared b40-43 tab + k2 b32-38 + b5 edge.
_T6K0 = ("82660000c36b325b79e1e0b300363c91f74126d156db84228e58d9e7"
         "efeb8839d67ae3dfefa19c655b5fe5a80d9d19f1afd66639cdaedfb6",
         "d4923300c56b325b79e1e07300363c91f74126d19a5f3cf9cec2b5e15"
         "62d77c1c6bfbf8eefa19c655b5fe5a80d9d19f1afd66639cdaedfb6",
         "ef923903c76b325b79e1e03300363c91f74126119a5f3cf9cec21de55"
         "62d773128fcafed131fca595b5fe5a80d9d19f1afd66639cdaedfb6")
_T6K1T = ("3efcb7ed13", "06fd53f213", "fffc3bf313", "d2bfdbf713",
          "e8bfe3f713", "c9bf27fd13", "dfbf2ffd13", "d8bf17fe13",
          "a0fcb30233", "b6fcbb0233", "26fc171333", "eefcb31733",
          "e7fc9b1833", "babf3b1d33", "d0bf431d33")
_T6K1C = ((0, 0xef), (1, 0x92), (2, 0x39), (3, 0x03), (5, 0x6b),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0x33), (12, 0x00), (13, 0x36),
          (14, 0x3c), (15, 0x91), (16, 0xf7), (17, 0x41),
          (18, 0x26), (19, 0x11), (20, 0x9a), (21, 0x5f),
          (22, 0x3c), (23, 0xf9), (24, 0xce), (25, 0xc2),
          (26, 0x1d), (27, 0xe5), (28, 0x56), (29, 0x2d),
          (30, 0x77), (31, 0x31), (37, 0x1f), (38, 0xca),
          (39, 0x59), (40, 0x5b), (41, 0x5f), (42, 0xe5),
          (43, 0xa8), (44, 0x0d), (45, 0x9d), (46, 0x19),
          (47, 0xf1), (48, 0xaf), (49, 0xd6), (50, 0x66),
          (51, 0x39), (52, 0xcd), (53, 0xae), (54, 0xdf),
          (55, 0xb6))
_T6K2T = ("e3bfd7d794574d", "1cfcbf50743448", "55bfc750743448",
          "19bfdf21f4ee48", "f3bf53bfd4a949", "f0bf2b05344f45",
          "4fbf6727f4ee48", "a1bf2f5f747a47", "c4fc1728f4ee48",
          "d5fc3760743448")
_T6K2C = ((0, 0xbe), (1, 0x2e), (2, 0x67), (3, 0x00), (5, 0x6b),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0x33), (12, 0x00), (13, 0x36),
          (14, 0x3c), (15, 0x91), (16, 0xf7), (17, 0x41),
          (18, 0x26), (19, 0x11), (20, 0x9a), (21, 0x5f),
          (22, 0x3c), (23, 0xf9), (24, 0xce), (25, 0xc2),
          (26, 0x3d), (27, 0xe3), (28, 0x92), (29, 0xb5),
          (30, 0x18), (31, 0x86), (39, 0xb2), (40, 0x5b),
          (41, 0x5f), (42, 0xe5), (43, 0xa8), (44, 0x0d),
          (45, 0x9d), (46, 0x19), (47, 0xf1), (48, 0xaf),
          (49, 0xd6), (50, 0x66), (51, 0x39), (52, 0xcd),
          (53, 0xae), (54, 0xdf), (55, 0xb6))
_T6K3T = ("ff5d7e7f", "7cdc3681", "8d5f3b81", "2ddd8c81",
          "bbda4983", "bbde4983", "53dcb783", "d05a7085",
          "e1dd7485", "42da7985", "fed97e87", "0f5d8387",
          "70598887", "ed5e9189", "3ddc9189", "cbd94e8b")
_T6K3K = ("0efc3f60743448", "04fdbb64747a47", "83bf07cfd4a949",
          "babf23fdd4c046")
# T6L tables (run-256): 16-tabs b40/41/42/46/47/48 + k2
# b22/23/30/31/39 + b15 flip k2>=1 + b5 edges @1807/1935.
_T6LT40 = (0xd1, 0x11, 0x31, 0x71, 0x91, 0xd1, 0xf1, 0x31,
           0x51, 0x91, 0xd1, 0xf1, 0x11, 0x51, 0x91, 0xb1)
_T6LT41 = (0x58, 0x61, 0x95, 0x95, 0xc9, 0xd1, 0xa4, 0xa5,
           0xd9, 0xe1, 0xe1, 0x15, 0x20, 0xf1, 0xf1, 0x25)
_T6LT42 = (0xff, 0xc1, 0xc1, 0xc1, 0xc1, 0xc3, 0xc4, 0xc4,
           0xc4, 0xc6, 0xc6, 0xc7, 0xc9, 0xc9, 0xc9, 0xca)
_T6LT46 = (0x06, 0x2c, 0xae, 0xae, 0x30, 0x56, 0x0c, 0x0c,
           0x8e, 0xb4, 0xb4, 0x36, 0x6c, 0x12, 0x12, 0x94)
_T6LT47 = (0xf9, 0xf8, 0xf8, 0xf8, 0xf9, 0xf8, 0xf9, 0xf9,
           0xf9, 0xf8, 0xf8, 0xf9, 0xf8, 0xf9, 0xf9, 0xf9)
_T6LT48 = (0xb3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3,
           0xd3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3, 0xd3)
_T6LK = ("f3fb985dfe", "b30918dcf8", "db09985f1a", "630c18dd5a",
         "4b1a98da76", "4b1a98de76", "bb1d18dca6", "832b985aa0",
         "a32b98ddc2", "cb2b18da84", "f33b98d9fc", "1b3c185d1e",
         "433c1859e0", "8b4c985eda", "8b4c18dc7a", "735a98d996")
# T6M tables (cluster M, tier end): 3 transition literals +
# 15-row M1 + 10-row M2 + M3-6 shared b5-10 tab (b5 +1 in
# M6, +(m>=7) in M5) + k2 b42/43/50-55.
_T6M0 = ("beee0c007b6e325b79e1e03300363c91f74126119a5f3cf9cec23de39"
         "2b5983021bf675391f76b965b5fe5a80d9d19f1afd66639cdaedfb6",
         "7ef1e4077d6e325b79e1e07300363c91f74126a18eaf336b16ee190f"
         "92b5983b21bf675391f7ebcb2e96739c2ac13cef555efe5acdaedfb6",
         "800d4f647f6e325b79e1e033f7c5939f0f3209cd8eaf336b16ee190f"
         "92b5983b21bf675391f7ebcb2e962bc72a0131ff555efea62dd79f18")
_T6M1T = ("a66d7d1f28", "a68debe728", "a60dfcef77", "a60dcdbf78",
          "aa6df9a773", "aa6de6777f", "aa6d9fe7ce", "aaedc74fcf",
          "aaed981fd0", "ae6da9271f", "ae6d96f72a", "ae8dec5f7a",
          "aeed77cf7a", "ae0de6977b", "b24d758776")
_T6M1C = ((0, 0x80), (1, 0x0d), (2, 0x4f), (3, 0x64), (5, 0x6e),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0x33), (12, 0xf7), (13, 0xc5),
          (14, 0x93), (15, 0x9f), (16, 0x0f), (17, 0x32),
          (18, 0x09), (19, 0xcd), (20, 0x8e), (21, 0xaf),
          (22, 0x33), (23, 0x6b), (24, 0x16), (25, 0xee),
          (26, 0x19), (27, 0x0f), (28, 0x92), (29, 0xb5),
          (30, 0x98), (31, 0x3b), (32, 0x21), (33, 0xbf),
          (34, 0x67), (35, 0x53), (36, 0x91), (37, 0xf7),
          (38, 0xeb), (39, 0xcb), (40, 0x2e), (41, 0x96),
          (42, 0x2b), (43, 0xc7), (44, 0x2a), (45, 0x01),
          (46, 0x31), (47, 0xff), (48, 0x55), (49, 0x5e),
          (50, 0xfe))
_T6M2T = ("b11aa9a9cddb2fd4", "f115291ccdc5f757",
          "9916a9bccdf927b1", "9916e9bc0ded2f00",
          "4917e96badd60f52", "41132924ed9577ab",
          "9916e9bccd9f6f50", "41152989ed8c27fe",
          "9916e9bc6dd14f60", "f115691cad79470f")
_T6M2C = ((0, 0x7e), (1, 0xf1), (2, 0xe4), (3, 0x0b), (5, 0x6e),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0x73), (12, 0x00), (13, 0x36),
          (14, 0x3c), (15, 0x91), (16, 0xf7), (17, 0x41),
          (18, 0x26), (19, 0xa1), (20, 0x8e), (21, 0xaf),
          (22, 0x33), (23, 0x6b), (24, 0x16), (25, 0xee),
          (26, 0x19), (27, 0x0f), (28, 0x92), (29, 0xb5),
          (30, 0x98), (31, 0x3b), (32, 0x21), (33, 0xbf),
          (34, 0x67), (35, 0x53), (36, 0x91), (37, 0xf7),
          (38, 0xeb), (39, 0xcb), (40, 0x4e), (41, 0xee),
          (44, 0x2a), (45, 0x41), (46, 0x24), (47, 0x0f),
          (48, 0x51), (49, 0x14))
_T6M3T5 = (0x8e, 0x0e, 0xae, 0x4e, 0x8e, 0xee, 0xce, 0x8e,
           0xee, 0xce, 0xce, 0x6e, 0x6e, 0xce, 0x2e, 0x6e)
_T6M3T6 = (0x4e, 0xd9, 0x24, 0xfb, 0x89, 0xc6, 0xab, 0x44,
           0x81, 0x66, 0xe6, 0x32, 0xdc, 0xa1, 0xdf, 0x97)
_T6M3T7 = (0xab, 0x0b, 0x9b, 0xcb, 0xdb, 0x5b, 0x9b, 0x0b,
           0x8b, 0xcb, 0xcb, 0x5b, 0x6b, 0xfb, 0x7b, 0x9b)
_T6M3T8 = (0x3d, 0x3d, 0x3d, 0x3d, 0x3d, 0x5d, 0x5d, 0x5d,
           0x5d, 0x5d, 0x5d, 0x7d, 0x3d, 0x5d, 0x7d, 0x3d)
_T6M3T9 = (0xf5, 0xf6, 0xf6, 0xfb, 0xfb, 0xfb, 0x00, 0x01,
           0x01, 0x06, 0x06, 0x06, 0x0b, 0x0c, 0x0c, 0x11)
_T6M3T10 = (0x0d, 0x0d, 0x0d, 0x0d, 0x0d, 0x0d, 0x0e, 0x0e,
            0x0e, 0x0e, 0x0e, 0x0e, 0x0e, 0x0e, 0x0e, 0x0e)
_T6M3K = ("f115691cadb2af5e", "411569892dd15799",
          "4917296ccd72dff8", "99146904cdc87726")
# T7A tables (60-tier head off 0..255, PRE-060b concur): 16-tabs
# b0/9/10/11/20/21 + b6/7 M3-walk + b5 walk+steps + k2 b12.
_T7AT0 = (0x09, 0x0b, 0x08, 0x0b, 0x0b, 0x09, 0x09, 0x08,
          0x09, 0x0b, 0x09, 0x09, 0x08, 0x0b, 0x0b, 0x08)
_T7AT9 = (0x7c, 0xb0, 0x20, 0x54, 0x54, 0xc8, 0xc8, 0xfc,
          0x6c, 0x80, 0xb4, 0xb4, 0xe8, 0xbc, 0xbc, 0x2c)
_T7AT10 = (0xf0, 0xf1, 0xf2, 0xf3, 0xf3, 0xf2, 0xf2, 0xf3,
           0xf0, 0xf1, 0xf2, 0xf2, 0xf3, 0xf3, 0xf3, 0xf0)
_T7AT11 = (0x0f, 0xce, 0x42, 0x01, 0x05, 0xd1, 0xd5, 0x94,
           0x09, 0x1c, 0xdb, 0xdf, 0x9e, 0x87, 0x8b, 0x00)
_T7AT20 = (0xf3, 0xf3, 0xf4, 0xf4, 0xf4, 0xfd, 0xfd, 0xfe,
           0xfe, 0x04, 0x05, 0x05, 0x06, 0x0e, 0x0e, 0x0f)
_T7AT21 = (0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20, 0x20,
           0x20, 0x21, 0x21, 0x21, 0x21, 0x21, 0x21, 0x21)
_T7AK12 = (0xa9, 0xb1, 0xb1, 0xd9, 0xd9, 0xda, 0x02, 0x0a,
           0x0a, 0x32, 0x32, 0x33, 0x59, 0x62, 0x63, 0x89)
# T7B tables (post-dip block): 16-row B1 + 10-row B2 +
# B3-6 shared b28-32 tab + k2 b20-26.
_T7B1T = ("9d7b03270a", "7d7fb327aa", "bd7a8329aa", "3d7b97330a",
          "dd7e7b35ea", "5d7f8f3f4a", "3d7df941ca", "7d7e0f42ea",
          "5d6a05674a", "1d742f674a", "5d7545676a", "bd6f1373aa",
          "fd702973ca", "3d723f73ea", "5d6fa77faa", "9d70bd7fca")
_T7B1C = ((0, 0x0b), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x51),
          (6, 0xc1), (7, 0x6b), (8, 0x1a), (9, 0x52),
          (10, 0x3e), (11, 0x18), (12, 0xb7), (13, 0x7f),
          (14, 0x2e), (15, 0x01), (20, 0x15), (21, 0xb5),
          (22, 0x9f), (24, 0x12), (25, 0xf8), (26, 0x3a),
          (27, 0xd5), (28, 0x6f), (29, 0xe1), (30, 0x9e),
          (31, 0xf1), (32, 0x92), (33, 0xb5), (34, 0x98),
          (35, 0x3d), (36, 0x21), (37, 0xbf), (38, 0x67),
          (39, 0x53), (40, 0x91), (41, 0xf7), (42, 0x6b),
          (43, 0x90), (44, 0x2f), (45, 0xdf), (46, 0x31),
          (47, 0x6b), (48, 0x4e), (49, 0x25), (50, 0x88),
          (51, 0xe4), (52, 0x51), (53, 0x14), (54, 0x69),
          (55, 0x1b), (56, 0x4d), (57, 0xaf), (58, 0xaf),
          (59, 0x69))
_T7B2T = ("d99720df90692039", "997637f1646a0b39",
          "995755ecee640e39", "79b756eca4640e39",
          "5917a9e3dc601139", "59572cf11296ff38",
          "f9b7bef2b06a0b39", "f9b6edfa8e720839",
          "595721ed88640e39", "b9b686f3846a0b39")
_T7B2C = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x51),
          (6, 0xc1), (7, 0x6b), (8, 0x9a), (9, 0x56),
          (10, 0x7e), (11, 0x11), (12, 0xb7), (13, 0x7f),
          (14, 0x2e), (15, 0x01), (20, 0x59), (21, 0x9e),
          (22, 0x56), (24, 0x33), (25, 0xf0), (26, 0x75),
          (27, 0xaa), (31, 0xe3), (32, 0x92), (33, 0xb5),
          (34, 0x98), (35, 0x3d), (36, 0x21), (37, 0xbf),
          (38, 0x67), (39, 0x53), (40, 0x91), (41, 0xf7),
          (42, 0x6b), (43, 0x90), (44, 0x2f), (45, 0xdf),
          (46, 0x31), (47, 0x6b), (48, 0x4e), (49, 0x25),
          (50, 0x88), (51, 0xe4), (52, 0x51), (53, 0x14),
          (54, 0x69), (55, 0x1b), (56, 0x4d), (57, 0xaf),
          (58, 0xaf), (59, 0x69))
_T7B3T = ("263c8117b6", "bdbc9717b6", "51fca322b6", "1bbcd74fb6",
          "50bc855eb6", "803c805fb6", "45fce296b6", "de3cb897b6",
          "defcc097b6", "3c3cf8cfb6", "743cc0d3b6", "0dbc95d4b6",
          "387cb7dfb6", "02fcf20cd6", "963cf717d6", "2f7cd418d6")
_T7B3K = ("ecdf1fce536d21", "fadde0ee530e21", "0cdfcc94132c22",
          "2c5d02e8135120")
_T7B3C = ((0, 0x17), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x51),
          (6, 0xc1), (7, 0x6b), (8, 0x9a), (9, 0x56),
          (10, 0x7e), (11, 0x11), (12, 0xb7), (13, 0x7f),
          (14, 0x2e), (15, 0x01), (16, 0x39), (17, 0xcb),
          (18, 0xd3), (19, 0x8a), (27, 0xa3), (33, 0x58),
          (34, 0x8b), (35, 0xd9), (36, 0x21), (37, 0xbf),
          (38, 0x67), (39, 0x53), (40, 0x91), (41, 0xf7),
          (42, 0x6b), (43, 0x90), (44, 0x2f), (45, 0xdf),
          (46, 0x31), (47, 0x6b), (48, 0x4e), (49, 0x25),
          (50, 0x88), (51, 0xe4), (52, 0x51), (53, 0x14),
          (54, 0x69), (55, 0x1b), (56, 0x4d), (57, 0xaf),
          (58, 0xaf), (59, 0x69))
_T7DIP256 = ("be4e75013371325b79e1e03300363c91f74126119a5f3cf9cec23de39"
             "2b5983d21bf675391f76b902fdf316b4e2588e45114691b4dafaf69",
             "8044bec03551c16bfaf6cf251dbe4e7514b59f2a9a5f3cf9cec23de39"
             "2b5983d21bf675391f76b902fdf316b4e2588e45114691b4dafaf69")
_T7AC = ((1, 0x00), (2, 0x00), (3, 0x00), (8, 0x1d), (14, 0xf0),
         (15, 0x19), (16, 0x9b), (17, 0x5f), (18, 0x3c),
         (19, 0xf9), (22, 0x93), (23, 0xd0), (24, 0x8e),
         (25, 0xaf), (26, 0x33), (27, 0x6b), (28, 0x16),
         (29, 0xee), (30, 0x19), (31, 0x0f), (32, 0x92),
         (33, 0xb5), (34, 0x98), (35, 0x3b), (36, 0x21),
         (37, 0xbf), (38, 0x67), (39, 0x53), (40, 0x91),
         (41, 0xf7), (42, 0xeb), (43, 0xcb), (44, 0x4e),
         (45, 0xee), (46, 0xf1), (47, 0x15), (48, 0x2a),
         (49, 0x41), (50, 0x24), (51, 0x0f), (52, 0x51),
         (53, 0x14), (54, 0xa9), (55, 0x1c), (56, 0x2d),
         (57, 0xe4), (58, 0xcf), (59, 0x5a))
_T6M3C = ((0, 0xe7), (1, 0x17), (2, 0x4f), (3, 0xbe), (11, 0x3e),
          (12, 0x00), (13, 0x36), (14, 0x3c), (15, 0x91),
          (16, 0xf7), (17, 0x41), (18, 0x26), (19, 0xa1),
          (20, 0x8e), (21, 0xaf), (22, 0x33), (23, 0x6b),
          (24, 0x16), (25, 0xee), (26, 0x19), (27, 0x0f),
          (28, 0x92), (29, 0xb5), (30, 0x98), (31, 0x3b),
          (32, 0x21), (33, 0xbf), (34, 0x67), (35, 0x53),
          (36, 0x91), (37, 0xf7), (38, 0xeb), (39, 0xcb),
          (40, 0x4e), (41, 0xee), (44, 0x2a), (45, 0x41),
          (46, 0x24), (47, 0x0f), (48, 0x51), (49, 0x14))
_T6LC = ((0, 0x80), (1, 0x0d), (2, 0x4f), (3, 0x64), (6, 0x32),
         (7, 0x5b), (8, 0x79), (9, 0xe1), (10, 0xe0),
         (11, 0x33), (12, 0xf7), (13, 0xc5), (14, 0x93),
         (16, 0x0f), (17, 0x32), (18, 0x09), (19, 0xcd),
         (20, 0x8e), (21, 0xaf), (24, 0x16), (25, 0xee),
         (26, 0x19), (27, 0x0f), (28, 0x92), (29, 0xb5),
         (32, 0xcc), (33, 0xfc), (34, 0x1f), (35, 0x76),
         (36, 0x74), (37, 0x34), (38, 0x48), (43, 0x38),
         (44, 0x8a), (45, 0xce), (49, 0x6a), (50, 0x6d),
         (51, 0x96), (52, 0xcd), (53, 0xae), (54, 0xdf),
         (55, 0xb6))
_T6K3C = ((0, 0x7e), (1, 0xf1), (2, 0xe4), (3, 0x07), (6, 0x32),
          (7, 0x5b), (8, 0x79), (9, 0xe1), (10, 0xe0),
          (11, 0x73), (12, 0x00), (13, 0x36), (14, 0x3c),
          (15, 0x91), (16, 0xf7), (17, 0x41), (18, 0x26),
          (19, 0xa1), (20, 0x8e), (21, 0xaf), (22, 0xc3),
          (23, 0x9c), (24, 0x16), (25, 0xee), (26, 0x19),
          (27, 0x0f), (28, 0x92), (29, 0xb5), (30, 0x98),
          (31, 0x65), (39, 0x3e), (44, 0x51), (45, 0xd1),
          (46, 0x99), (47, 0x11), (48, 0xaf), (49, 0xd6),
          (50, 0x66), (51, 0x39), (52, 0xcd), (53, 0xae),
          (54, 0xdf), (55, 0xb6))
_T6JT26 = (0x15, 0x95, 0x15, 0x15, 0x95, 0x95, 0x15, 0x15,
           0x95, 0x15, 0x95, 0x15, 0x95, 0x95, 0x15, 0x95)
_T6JT27 = (0x10, 0x5c, 0x29, 0x73, 0x3e, 0x5a, 0x27, 0x71,
           0x3d, 0x09, 0x55, 0x6f, 0x3b, 0x3b, 0x51, 0x1d)
_T6JC = ((3, 0x01), (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
         (10, 0xe0), (11, 0xf3), (12, 0x00), (13, 0x84),
         (14, 0xbc), (15, 0xb1), (16, 0x79), (17, 0x8d),
         (18, 0x8e), (19, 0x97), (24, 0x52), (25, 0x88),
         (28, 0x73), (29, 0xac), (30, 0xf5), (31, 0x98),
         (32, 0xc6), (33, 0xbf), (34, 0xbf), (35, 0x8e),
         (36, 0xef), (37, 0xa1), (38, 0x9c), (39, 0x65),
         (40, 0x5b), (41, 0x5f), (42, 0xe5), (43, 0xa8),
         (44, 0x0d), (45, 0x9d), (46, 0x19), (47, 0xf1),
         (48, 0xaf), (49, 0xd6), (50, 0x66), (51, 0x39),
         (52, 0xcd), (53, 0xae), (54, 0xdf), (55, 0xb6))
_T6I3C = ((0, 0xad), (1, 0xa0), (2, 0x19), (3, 0x00), (5, 0x69),
          (6, 0x32), (7, 0x5b), (8, 0x79), (9, 0xe1),
          (10, 0xe0), (11, 0xf3), (12, 0x00), (19, 0x97),
          (24, 0x52), (25, 0x88), (26, 0x95), (27, 0x7d),
          (28, 0xef), (29, 0xeb), (30, 0x88), (31, 0x39),
          (32, 0xd6), (33, 0x7a), (34, 0xe3), (35, 0xdf),
          (36, 0xef), (37, 0xa1), (38, 0x9c), (39, 0x65),
          (40, 0x5b), (41, 0x5f), (42, 0xe5), (43, 0xa8),
          (44, 0x0d), (45, 0x9d), (46, 0x19), (47, 0xf1),
          (48, 0xaf), (49, 0xd6), (50, 0x66), (51, 0x39),
          (52, 0xcd), (53, 0xae), (54, 0xdf), (55, 0xb6))
_T6HC = ((0, 0x82), (1, 0x26), (2, 0x11), (3, 0x00), (10, 0x0b),
         (11, 0x66), (12, 0x00), (13, 0x32), (14, 0x3c),
         (15, 0xc8), (16, 0x15), (17, 0xfb), (18, 0x5a),
         (19, 0xb4), (20, 0x56), (21, 0xdb), (22, 0x84),
         (23, 0x22), (24, 0x8e), (25, 0x58), (26, 0xd9),
         (27, 0xe7), (28, 0xcf), (29, 0x5a), (30, 0x6f),
         (31, 0xee), (32, 0xc6), (33, 0xbf), (34, 0xbf),
         (35, 0x8e), (36, 0xef), (37, 0xa1), (38, 0xec),
         (39, 0xd9), (40, 0x5b), (41, 0x5f), (42, 0xe5),
         (43, 0xa8), (44, 0x0d), (45, 0x9d), (46, 0xfd),
         (47, 0xf3), (48, 0x31), (49, 0x9d))
_T6G3C = ((0, 0x68), (1, 0x12), (2, 0x01), (3, 0x00), (6, 0x3c),
          (7, 0xdb), (8, 0x77), (9, 0xbd), (10, 0x60),
          (11, 0x26), (12, 0x00), (13, 0x32), (14, 0x3c),
          (15, 0xc8), (16, 0x15), (17, 0xfb), (18, 0x5a),
          (19, 0xb4), (20, 0x56), (21, 0xdb), (22, 0x84),
          (23, 0x22), (24, 0x8e), (25, 0x58), (26, 0xd9),
          (27, 0xe7), (28, 0xcf), (29, 0x5a), (32, 0xc6),
          (33, 0xbf), (34, 0xbf), (35, 0x8e), (36, 0xef),
          (37, 0xa1), (40, 0x5b), (41, 0x5f), (42, 0xe5),
          (43, 0xa8), (44, 0x0d), (45, 0x9d))
_T6FC = ((0, 0x5e), (1, 0x21), (2, 0x02), (3, 0x00), (6, 0x3c),
         (7, 0xdb), (8, 0x77), (9, 0xbd), (10, 0x60),
         (11, 0x86), (12, 0x00), (13, 0x32), (14, 0x3c),
         (15, 0xc8), (16, 0x15), (17, 0xfb), (18, 0x5a),
         (19, 0x1c), (20, 0x56), (21, 0xdb), (22, 0x84),
         (23, 0x22), (24, 0x8e), (25, 0x58), (26, 0x19),
         (27, 0xe6), (28, 0xb2), (29, 0x13), (30, 0x8d),
         (31, 0x67), (36, 0x53), (37, 0x82), (38, 0x2d),
         (39, 0x0b), (44, 0x6f), (45, 0x3b), (46, 0xd0),
         (47, 0xc6), (48, 0x2d), (49, 0x8a), (50, 0x5d),
         (51, 0x7b), (52, 0xad), (53, 0xa0), (54, 0xf7),
         (55, 0xa5))
_T6E3C = ((2, 0x00), (3, 0x00), (6, 0x3c), (7, 0xdb), (8, 0x77),
          (9, 0xbd), (10, 0x60), (12, 0x00), (13, 0x32),
          (14, 0x3c), (15, 0xc8), (16, 0x15), (17, 0xfb),
          (18, 0x5a), (20, 0x56), (21, 0xdb), (22, 0x84),
          (23, 0x22), (24, 0x8e), (25, 0x58), (31, 0x06),
          (36, 0x53), (37, 0x82), (38, 0x2d), (39, 0xf0),
          (40, 0x18), (41, 0xdb), (42, 0x42), (43, 0xbc),
          (44, 0xab), (45, 0x03), (46, 0x6d), (47, 0xbc),
          (48, 0x2d), (49, 0x8a), (50, 0x5d), (51, 0x7b),
          (52, 0xad), (53, 0xa0), (54, 0xf7), (55, 0xa5))
# T6D tables (quiet-256): 16-tabs b20-23 + b13-17 walk the
# C3 tab by k2 (full 16, reuse) + b5 edges @399/527.
_T6DT20 = (0xf1, 0x42, 0xbe, 0x0f, 0x60, 0xfb, 0x7e, 0xcf,
           0x6d, 0xbe, 0x41, 0xdc, 0x2d, 0x7e, 0xfa, 0x4b)
_T6DT21 = (0xdd, 0x5e, 0xdd, 0x5e, 0xde, 0x5f, 0x5a, 0xda,
           0x5f, 0xdf, 0xda, 0x5b, 0xdc, 0x5c, 0xdb, 0x5c)
_T6DT22 = (0xdd, 0xe3, 0x7d, 0x83, 0x88, 0x28, 0x2e, 0x33,
           0xa7, 0xac, 0xb2, 0x52, 0x57, 0x5d, 0xf7, 0xfd)
_T6DT23 = (0x2d, 0x2d, 0x2e, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f,
           0x2f, 0x2f, 0x2f, 0x30, 0x30, 0x30, 0x30, 0x30)
_T6DC = ((0, 0x40), (1, 0x04), (2, 0x00), (3, 0x00), (6, 0x45),
         (7, 0x6b), (8, 0x79), (9, 0xe0), (10, 0x18),
         (11, 0x5e), (12, 0x00), (18, 0x19), (19, 0x4d),
         (24, 0xef), (25, 0x24), (26, 0xf9), (27, 0xa7),
         (28, 0x82), (29, 0x3c), (30, 0x45), (31, 0xb6),
         (32, 0xcd), (33, 0x3d), (34, 0x27), (35, 0xf4),
         (36, 0x2f), (37, 0xd8), (38, 0x02), (39, 0xcf),
         (40, 0x18), (41, 0xdb), (42, 0x42), (43, 0xbc),
         (44, 0xab), (45, 0x03), (46, 0x6d), (47, 0xbc),
         (48, 0x2d), (49, 0x8a), (50, 0x5d), (51, 0x7b),
         (52, 0xad), (53, 0xa0), (54, 0xf7), (55, 0xa5))
_T6C3C = ((0, 0x44), (1, 0x00), (2, 0x00), (3, 0x00), (12, 0x00),
          (18, 0x19), (19, 0x0d), (20, 0xef), (21, 0x5b),
          (22, 0x40), (23, 0x73), (24, 0x4b), (25, 0x92),
          (26, 0x7f), (27, 0xaa), (28, 0x82), (29, 0x3c),
          (30, 0x45), (31, 0xb6), (32, 0xcd), (33, 0x3d),
          (34, 0x27), (35, 0xf4), (36, 0x2f), (37, 0xd8),
          (38, 0x02), (39, 0xcf), (40, 0x18), (41, 0xdb),
          (42, 0x42), (43, 0xbc), (44, 0xab), (45, 0x03),
          (46, 0x6d), (47, 0xbc), (48, 0x2d), (49, 0x8a),
          (50, 0x5d), (51, 0x7b), (52, 0xad), (53, 0xa0),
          (54, 0xf7), (55, 0xa5))
_T6BC = ((0, 0x0d), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0xe0),
         (6, 0x23), (7, 0x6b), (8, 0x15), (9, 0xf1),
         (10, 0x0e), (11, 0xb1), (12, 0xdf), (13, 0x3c),
         (14, 0x07), (15, 0x20), (16, 0x34), (17, 0x91),
         (18, 0xd1), (19, 0x8a), (20, 0xef), (21, 0x5b),
         (22, 0x40), (23, 0x73), (24, 0x4b), (25, 0x92),
         (26, 0x82), (27, 0x3c), (28, 0x6d), (29, 0xaa),
         (30, 0xc8), (31, 0x56), (32, 0xee), (33, 0x39),
         (34, 0xa1), (35, 0xff), (36, 0x2f), (37, 0xd8),
         (40, 0xe2), (41, 0xdf), (42, 0xee), (43, 0xfe),
         (44, 0xec), (45, 0xf8), (48, 0x70), (49, 0x5a),
         (50, 0xd8), (51, 0xdd))
_T6AC = ((0, 0x06), (1, 0x00), (2, 0x00), (3, 0x00), (6, 0x91),
         (7, 0xb5), (8, 0x94), (9, 0x78), (10, 0x87),
         (11, 0xd8), (12, 0x6f), (13, 0x9e), (14, 0x03),
         (15, 0x10), (16, 0x34), (17, 0x91), (18, 0xd1),
         (19, 0x8a), (20, 0xef), (21, 0x5b), (22, 0x40),
         (23, 0x73), (24, 0x4b), (25, 0x92), (26, 0x82),
         (27, 0x3c), (28, 0x6d), (29, 0xaa), (30, 0xc8),
         (31, 0x56), (32, 0xee), (33, 0x39), (34, 0xa1),
         (35, 0xff), (36, 0x2f), (37, 0xd8), (40, 0xe2),
         (41, 0xdf), (42, 0xee), (43, 0xfe), (44, 0xec),
         (45, 0xf8), (48, 0x70), (49, 0x5a), (50, 0xd8),
         (51, 0xdd))
_T5L3C = ((0, 0x82), (1, 0x78), (2, 0x87), (3, 0x54), (5, 0xfe),
          (6, 0x91), (7, 0xb5), (8, 0xf4), (9, 0xcd),
          (10, 0x73), (11, 0x00), (12, 0x34), (13, 0x91),
          (14, 0xd1), (15, 0x90), (16, 0xef), (17, 0x5b),
          (18, 0x40), (19, 0x73), (20, 0x4b), (21, 0x92),
          (22, 0x7f), (23, 0xaa), (24, 0x82), (25, 0x3c),
          (26, 0x45), (27, 0xb6), (28, 0xcd), (29, 0x3d),
          (30, 0x27), (31, 0xf4), (32, 0x2f), (33, 0xd8),
          (44, 0x70), (45, 0x5a), (46, 0xd8), (47, 0xdd),
          (48, 0x6c), (49, 0xc0), (50, 0xef), (51, 0xe6))
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
    if len(pay) not in (44, 48, 52, 56, 60):
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
    if n <= 3862:  # T5L0: 2 transition literals (off=1648/1649)
        off = n - 2213
        if len(pay) != 52 or pay.hex() != _T5L0[off - 1648]:
            return fail("T5L0")
        print("CLOSED T5L0 N=%d" % n)
        return 0
    if n <= 3878:  # T5L1: 16-row b36-39 tab
        off = n - 2213
        if len(pay) != 52:
            return fail("T5L1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5L1 lencode")
        if pay[36:40].hex() != _T5L1T[off - 1650]:
            return fail("T5L1 row")
        for b, v in _T5L1C:
            if pay[b] != v:
                return fail("T5L1 const %d" % b)
        print("CLOSED T5L1 N=%d off=%d" % (n, off))
        return 0
    if n <= 3888:  # T5L2: 10-row tab b3/15/34-43
        off = n - 2213
        if len(pay) != 52:
            return fail("T5L2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5L2 lencode")
        row = pay[3:4].hex() + pay[15:16].hex() + pay[34:44].hex()
        if row != _T5L2T[off - 1666]:
            return fail("T5L2 row")
        for b, v in _T5L2C:
            if pay[b] != v:
                return fail("T5L2 const %d" % b)
        print("CLOSED T5L2 N=%d off=%d" % (n, off))
        return 0
    if n <= 3952:  # T5L3: 16-tabs b34/35/42/43 + k2 b36-41
        off = n - 2213
        if len(pay) != 52:
            return fail("T5L3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T5L3 lencode")
        m = (off - 1676) & 15
        k2 = (off - 1676) >> 4
        if pay[34] != _T5L3T34[m] or pay[35] != _T5L3T35[m]:
            return fail("T5L3 tabA")
        if pay[36:42].hex() != _T5L3K[k2]:
            return fail("T5L3 k2")
        if pay[42] != _T5L3T42[m] or pay[43] != _T5L3T43[m]:
            return fail("T5L3 tabB")
        for b, v in _T5L3C:
            if pay[b] != v:
                return fail("T5L3 const %d" % b)
        print("CLOSED T5L3 N=%d off=%d" % (n, off))
        return 0
    if n <= 4095:  # T6A: 56-tier head, tabs b52-55 + k2 segs
        off = n - 3953
        if len(pay) != 56:
            return fail("T6A paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6A lencode")
        m = off & 15
        k2 = off >> 4
        if pay[5] != (0xfe + (off >= 15)):
            return fail("T6A b5")
        krow = bytes((pay[38], pay[39], pay[46], pay[47])).hex()
        if krow != _T6AK[k2]:
            return fail("T6A k2")
        if pay[52] != _T6AT52[m] or pay[53] != _T6AT53[m] or \
                pay[54] != _T6AT54[m] or pay[55] != _T6AT55[m]:
            return fail("T6A tab")
        for b, v in _T6AC:
            if pay[b] != v:
                return fail("T6A const %d" % b)
        print("CLOSED T6A N=%d off=%d" % (n, off))
        return 0
    if n <= 4208:  # T6B: post-reframe, shared tabs + new segs
        off = n - 3953
        if len(pay) != 56:
            return fail("T6B paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6B lencode")
        m = off & 15
        k2 = off >> 4
        krow = bytes((pay[38], pay[39], pay[46], pay[47])).hex()
        if krow != _T6BK[k2 - 8]:
            return fail("T6B k2")
        if pay[52] != _T6BT52[m] or pay[53] != _T6AT53[m] or \
                pay[54] != _T6AT54[m] or pay[55] != _T6AT55[m]:
            return fail("T6B tab")
        for b, v in _T6BC:
            if pay[b] != v:
                return fail("T6B const %d" % b)
        print("CLOSED T6B N=%d off=%d" % (n, off))
        return 0
    if n == 4209:  # 52B short-form dip (off=256, +256 rule)
        if len(pay) != 52 or pay.hex() != _T6DIP256:
            return fail("T6DIP256")
        print("CLOSED T6DIP256 N=4209")
        return 0
    if n <= 4211:  # T6C0: 2 transition literals (off=257/258)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6C0[off - 257]:
            return fail("T6C0")
        print("CLOSED T6C0 N=%d" % n)
        return 0
    if n <= 4226:  # T6C1: 15-row b5-8 tab
        off = n - 3953
        if len(pay) != 56:
            return fail("T6C1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6C1 lencode")
        if pay[5:9].hex() != _T6C1T[off - 259]:
            return fail("T6C1 row")
        for b, v in _T6C1C:
            if pay[b] != v:
                return fail("T6C1 const %d" % b)
        print("CLOSED T6C1 N=%d off=%d" % (n, off))
        return 0
    if n <= 4236:  # T6C2: 10-row tab b5-7/b12-14
        off = n - 3953
        if len(pay) != 56:
            return fail("T6C2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6C2 lencode")
        cells = bytes((pay[5], pay[6], pay[7], pay[12], pay[13],
                       pay[14])).hex()
        if cells != _T6C2T[off - 274]:
            return fail("T6C2 row")
        for b, v in _T6C2C:
            if pay[b] != v:
                return fail("T6C2 const %d" % b)
        print("CLOSED T6C2 N=%d off=%d" % (n, off))
        return 0
    if n <= 4300:  # T6C3-6: shared b13-17 tab + k2 b5-11
        off = n - 3953
        if len(pay) != 56:
            return fail("T6C3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6C3 lencode")
        m = (off - 284) & 15
        k2 = (off - 284) >> 4
        if pay[5:12].hex() != _T6C3K[k2]:
            return fail("T6C3 k2")
        cells = bytes((pay[13], pay[14], pay[15], pay[16],
                       pay[17])).hex()
        if cells != _T6C3T[m]:
            return fail("T6C3 tab")
        for b, v in _T6C3C:
            if pay[b] != v:
                return fail("T6C3 const %d" % b)
        print("CLOSED T6C3 N=%d off=%d" % (n, off))
        return 0
    if n <= 4556:  # T6D: quiet-256, tabs + C3-walk + b5 edges
        off = n - 3953
        if len(pay) != 56:
            return fail("T6D paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6D lencode")
        m = (off - 348) & 15
        k2 = (off - 348) >> 4
        if pay[5] != (0x21 + (off >= 399) + (off >= 527)):
            return fail("T6D b5")
        cells = bytes((pay[13], pay[14], pay[15], pay[16],
                       pay[17])).hex()
        if cells != _T6C3T[k2]:
            return fail("T6D walk")
        if pay[20] != _T6DT20[m] or pay[21] != _T6DT21[m] or \
                pay[22] != _T6DT22[m] or pay[23] != _T6DT23[m]:
            return fail("T6D tab")
        for b, v in _T6DC:
            if pay[b] != v:
                return fail("T6D const %d" % b)
        print("CLOSED T6D N=%d off=%d" % (n, off))
        return 0
    if n <= 4559:  # T6E0: 3 transition literals (off=604..606)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6E0[off - 604]:
            return fail("T6E0")
        print("CLOSED T6E0 N=%d" % n)
        return 0
    if n <= 4574:  # T6E1: 15-row b28-31 tab
        off = n - 3953
        if len(pay) != 56:
            return fail("T6E1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6E1 lencode")
        if pay[28:32].hex() != _T6E1T[off - 607]:
            return fail("T6E1 row")
        for b, v in _T6E1C:
            if pay[b] != v:
                return fail("T6E1 const %d" % b)
        print("CLOSED T6E1 N=%d off=%d" % (n, off))
        return 0
    if n <= 4584:  # T6E2: 10-row scattered tab
        off = n - 3953
        if len(pay) != 56:
            return fail("T6E2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6E2 lencode")
        cells = bytes((pay[0], pay[1], pay[11], pay[19], pay[26],
                       pay[27], pay[32], pay[33])).hex()
        if cells != _T6E2T[off - 622]:
            return fail("T6E2 row")
        for b, v in _T6E2C:
            if pay[b] != v:
                return fail("T6E2 const %d" % b)
        print("CLOSED T6E2 N=%d off=%d" % (n, off))
        return 0
    if n <= 4648:  # T6E3-6: shared tab + k2 + b5 edge
        off = n - 3953
        if len(pay) != 56:
            return fail("T6E3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6E3 lencode")
        m = (off - 632) & 15
        k2 = (off - 632) >> 4
        if pay[5] != (0x23 + (off >= 655)):
            return fail("T6E3 b5")
        kcells = bytes((pay[0], pay[1], pay[11], pay[19], pay[26],
                        pay[27], pay[32], pay[33])).hex()
        if kcells != _T6E3K[k2]:
            return fail("T6E3 k2")
        cells = bytes((pay[28], pay[29], pay[30], pay[34],
                       pay[35])).hex()
        if cells != _T6E3T[m]:
            return fail("T6E3 tab")
        for b, v in _T6E3C:
            if pay[b] != v:
                return fail("T6E3 const %d" % b)
        print("CLOSED T6E3 N=%d off=%d" % (n, off))
        return 0
    if n <= 4904:  # T6F: quiet-256, tabs b40-43 + k2 b32-35
        off = n - 3953
        if len(pay) != 56:
            return fail("T6F paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6F lencode")
        m = (off - 696) & 15
        k2 = (off - 696) >> 4
        if pay[5] != (0x24 + (off >= 783) + (off >= 911)):
            return fail("T6F b5")
        if pay[32:36].hex() != _T6FK[k2]:
            return fail("T6F k2")
        if pay[40] != _T6FT40[m] or pay[41] != _T6FT41[m] or \
                pay[42] != _T6FT42[m] or pay[43] != _T6FT43[m]:
            return fail("T6F tab")
        for b, v in _T6FC:
            if pay[b] != v:
                return fail("T6F const %d" % b)
        print("CLOSED T6F N=%d off=%d" % (n, off))
        return 0
    if n <= 4907:  # T6G0: 3 transition literals (off=952..954)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6G0[off - 952]:
            return fail("T6G0")
        print("CLOSED T6G0 N=%d" % n)
        return 0
    if n <= 4922:  # T6G1: 15-row tab b30/31/39/46/47
        off = n - 3953
        if len(pay) != 56:
            return fail("T6G1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6G1 lencode")
        cells = bytes((pay[30], pay[31], pay[39], pay[46],
                       pay[47])).hex()
        if cells != _T6G1T[off - 955]:
            return fail("T6G1 row")
        for b, v in _T6G1C:
            if pay[b] != v:
                return fail("T6G1 const %d" % b)
        print("CLOSED T6G1 N=%d off=%d" % (n, off))
        return 0
    if n <= 4932:  # T6G2: 10-row tab b30/31/38/39/46-50
        off = n - 3953
        if len(pay) != 56:
            return fail("T6G2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6G2 lencode")
        cells = bytes((pay[30], pay[31], pay[38], pay[39], pay[46],
                       pay[47], pay[48], pay[49], pay[50])).hex()
        if cells != _T6G2T[off - 970]:
            return fail("T6G2 row")
        for b, v in _T6G2C:
            if pay[b] != v:
                return fail("T6G2 const %d" % b)
        print("CLOSED T6G2 N=%d off=%d" % (n, off))
        return 0
    if n <= 4996:  # T6G3-6: shared b50-55 tab + k2 + b5 edge
        off = n - 3953
        if len(pay) != 56:
            return fail("T6G3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6G3 lencode")
        m = (off - 980) & 15
        k2 = (off - 980) >> 4
        if pay[5] != (0x26 + (off >= 1039)):
            return fail("T6G3 b5")
        kcells = pay[30:32].hex() + pay[38:40].hex() + \
            pay[46:50].hex()
        if kcells != _T6G3K[k2]:
            return fail("T6G3 k2")
        if pay[50] != ((_T6G3T50[m] + (k2 == 2)) & 0xff):
            return fail("T6G3 b50")
        if pay[51:56].hex() != _T6G3T51[m]:
            return fail("T6G3 tab")
        for b, v in _T6G3C:
            if pay[b] != v:
                return fail("T6G3 const %d" % b)
        print("CLOSED T6G3 N=%d off=%d" % (n, off))
        return 0
    if n <= 5252:  # T6H: run-256, tabs + G3-walk + bands
        off = n - 3953
        if len(pay) != 56:
            return fail("T6H paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6H lencode")
        m = (off - 1044) & 15
        k2 = (off - 1044) >> 4
        if pay[5] != ((_T6HT5[m] + (off >= 1167) + (off >= 1295)) & 0xff):
            return fail("T6H b5")
        if pay[6] != _T6HT6[m] or pay[7] != _T6HT7[m] or \
                pay[8] != _T6HT8[m] or pay[9] != _T6HT9[m]:
            return fail("T6H tab")
        if pay[50] != (0xad, 0xed, 0x2d)[(k2 >= 7) + (k2 >= 14)]:
            return fail("T6H b50")
        if pay[51] != (0x5d + (k2 >= 14)):
            return fail("T6H b51")
        if pay[52:56].hex() != _T6G3T51[k2][2:]:
            return fail("T6H walk")
        for b, v in _T6HC:
            if pay[b] != v:
                return fail("T6H const %d" % b)
        print("CLOSED T6H N=%d off=%d" % (n, off))
        return 0
    if n <= 5255:  # T6I0: 3 transition literals (off=1300..1302)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6I0[off - 1300]:
            return fail("T6I0")
        print("CLOSED T6I0 N=%d" % n)
        return 0
    if n <= 5270:  # T6I1: 15-row b13-16 tab
        off = n - 3953
        if len(pay) != 56:
            return fail("T6I1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6I1 lencode")
        if pay[13:17].hex() != _T6I1T[off - 1303]:
            return fail("T6I1 row")
        for b, v in _T6I1C:
            if pay[b] != v:
                return fail("T6I1 const %d" % b)
        print("CLOSED T6I1 N=%d off=%d" % (n, off))
        return 0
    if n <= 5280:  # T6I2: 10-row tab b13-19
        off = n - 3953
        if len(pay) != 56:
            return fail("T6I2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6I2 lencode")
        if pay[13:20].hex() != _T6I2T[off - 1318]:
            return fail("T6I2 row")
        for b, v in _T6I2C:
            if pay[b] != v:
                return fail("T6I2 const %d" % b)
        print("CLOSED T6I2 N=%d off=%d" % (n, off))
        return 0
    if n <= 5344:  # T6I3-6: shared b20-23 tab + k2 b13-18
        off = n - 3953
        if len(pay) != 56:
            return fail("T6I3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6I3 lencode")
        m = (off - 1328) & 15
        k2 = (off - 1328) >> 4
        if pay[13:19].hex() != _T6I3K[k2]:
            return fail("T6I3 k2")
        if pay[20:24].hex() != _T6I3T[m]:
            return fail("T6I3 tab")
        for b, v in _T6I3C:
            if pay[b] != v:
                return fail("T6I3 const %d" % b)
        print("CLOSED T6I3 N=%d off=%d" % (n, off))
        return 0
    if n <= 5600:  # T6J: run-256, tabs + I3-walk + b5 edges
        off = n - 3953
        if len(pay) != 56:
            return fail("T6J paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6J lencode")
        m = (off - 1392) & 15
        k2 = (off - 1392) >> 4
        if pay[5] != (0x69 + (off >= 1423) + (off >= 1551)):
            return fail("T6J b5")
        if pay[0] != _T6JT0[m] or pay[1] != _T6JT1[m] or \
                pay[2] != _T6JT2[m]:
            return fail("T6J tabA")
        if pay[20:24].hex() != _T6I3T[k2]:
            return fail("T6J walk")
        if pay[26] != _T6JT26[m] or pay[27] != _T6JT27[m]:
            return fail("T6J tabB")
        for b, v in _T6JC:
            if pay[b] != v:
                return fail("T6J const %d" % b)
        print("CLOSED T6J N=%d off=%d" % (n, off))
        return 0
    if n <= 5603:  # T6K0: 3 transition literals (off=1648..1650)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6K0[off - 1648]:
            return fail("T6K0")
        print("CLOSED T6K0 N=%d" % n)
        return 0
    if n <= 5618:  # T6K1: 15-row tab b32-36
        off = n - 3953
        if len(pay) != 56:
            return fail("T6K1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6K1 lencode")
        cells = bytes((pay[32], pay[33], pay[34], pay[35],
                       pay[36])).hex()
        if cells != _T6K1T[off - 1651]:
            return fail("T6K1 row")
        for b, v in _T6K1C:
            if pay[b] != v:
                return fail("T6K1 const %d" % b)
        print("CLOSED T6K1 N=%d off=%d" % (n, off))
        return 0
    if n <= 5628:  # T6K2: 10-row tab b32-38
        off = n - 3953
        if len(pay) != 56:
            return fail("T6K2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6K2 lencode")
        if pay[32:39].hex() != _T6K2T[off - 1666]:
            return fail("T6K2 row")
        for b, v in _T6K2C:
            if pay[b] != v:
                return fail("T6K2 const %d" % b)
        print("CLOSED T6K2 N=%d off=%d" % (n, off))
        return 0
    if n <= 5692:  # T6K3-6: shared b40-43 tab + k2 + b5 edge
        off = n - 3953
        if len(pay) != 56:
            return fail("T6K3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6K3 lencode")
        m = (off - 1676) & 15
        k2 = (off - 1676) >> 4
        if pay[5] != (0x6b + (off >= 1679)):
            return fail("T6K3 b5")
        if pay[32:39].hex() != _T6K3K[k2]:
            return fail("T6K3 k2")
        if pay[40:44].hex() != _T6K3T[m]:
            return fail("T6K3 tab")
        for b, v in _T6K3C:
            if pay[b] != v:
                return fail("T6K3 const %d" % b)
        print("CLOSED T6K3 N=%d off=%d" % (n, off))
        return 0
    if n <= 5948:  # T6L: run-256, tabs + k2 + b15/b5 edges
        off = n - 3953
        if len(pay) != 56:
            return fail("T6L paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6L lencode")
        m = (off - 1740) & 15
        k2 = (off - 1740) >> 4
        if pay[5] != (0x6c + (off >= 1807) + (off >= 1935)):
            return fail("T6L b5")
        if pay[15] != (0xbf + ((k2 >= 1) << 4)):
            return fail("T6L b15")
        kcells = bytes((pay[22], pay[23], pay[30], pay[31],
                        pay[39])).hex()
        if kcells != _T6LK[k2]:
            return fail("T6L k2")
        if pay[40] != _T6LT40[m] or pay[41] != _T6LT41[m] or \
                pay[42] != _T6LT42[m]:
            return fail("T6L tabA")
        if pay[46] != _T6LT46[m] or pay[47] != _T6LT47[m] or \
                pay[48] != _T6LT48[m]:
            return fail("T6L tabB")
        for b, v in _T6LC:
            if pay[b] != v:
                return fail("T6L const %d" % b)
        print("CLOSED T6L N=%d off=%d" % (n, off))
        return 0
    if n <= 5951:  # T6M0: 3 transition literals (off=1996..1998)
        off = n - 3953
        if len(pay) != 56 or pay.hex() != _T6M0[off - 1996]:
            return fail("T6M0")
        print("CLOSED T6M0 N=%d" % n)
        return 0
    if n <= 5966:  # T6M1: 15-row b51-55 tab
        off = n - 3953
        if len(pay) != 56:
            return fail("T6M1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6M1 lencode")
        if pay[51:56].hex() != _T6M1T[off - 1999]:
            return fail("T6M1 row")
        for b, v in _T6M1C:
            if pay[b] != v:
                return fail("T6M1 const %d" % b)
        print("CLOSED T6M1 N=%d off=%d" % (n, off))
        return 0
    if n <= 5976:  # T6M2: 10-row tab b42/43/50-55
        off = n - 3953
        if len(pay) != 56:
            return fail("T6M2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6M2 lencode")
        cells = pay[42:44].hex() + pay[50:56].hex()
        if cells != _T6M2T[off - 2014]:
            return fail("T6M2 row")
        for b, v in _T6M2C:
            if pay[b] != v:
                return fail("T6M2 const %d" % b)
        print("CLOSED T6M2 N=%d off=%d" % (n, off))
        return 0
    if n <= 6040:  # T6M3-6: shared b5-10 tab + k2 (tier end)
        off = n - 3953
        if len(pay) != 56:
            return fail("T6M3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T6M3 lencode")
        m = (off - 2024) & 15
        k2 = (off - 2024) >> 4
        b5bump = (k2 == 3) + (k2 == 2 and m >= 7)
        if pay[5] != ((_T6M3T5[m] + b5bump) & 0xff):
            return fail("T6M3 b5")
        if pay[6] != _T6M3T6[m] or pay[7] != _T6M3T7[m] or \
                pay[8] != _T6M3T8[m]:
            return fail("T6M3 tabA")
        if pay[9] != _T6M3T9[m] or pay[10] != _T6M3T10[m]:
            return fail("T6M3 tabB")
        kcells = pay[42:44].hex() + pay[50:56].hex()
        if kcells != _T6M3K[k2]:
            return fail("T6M3 k2")
        for b, v in _T6M3C:
            if pay[b] != v:
                return fail("T6M3 const %d" % b)
        print("CLOSED T6M3 N=%d off=%d" % (n, off))
        return 0
    if n <= 6296:  # T7A: 60-tier head, tabs + M3-walk + steps
        off = n - 6041
        if len(pay) != 60:
            return fail("T7A paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T7A lencode")
        m = off & 15
        k2 = off >> 4
        b5bump = 1 + (k2 >= 7) + (k2 == 15) + \
            (k2 in (6, 14) and m >= 7)
        if pay[5] != ((_T6M3T5[k2] + b5bump) & 0xff):
            return fail("T7A b5")
        if pay[6] != _T6M3T6[k2] or pay[7] != _T6M3T7[k2]:
            return fail("T7A walk")
        if pay[0] != _T7AT0[m] or pay[9] != _T7AT9[m] or \
                pay[10] != _T7AT10[m] or pay[11] != _T7AT11[m]:
            return fail("T7A tabA")
        if pay[12] != _T7AK12[k2]:
            return fail("T7A b12")
        if pay[13] != (0x6f + (off >= 96)):
            return fail("T7A b13")
        if pay[20] != _T7AT20[m] or pay[21] != _T7AT21[m]:
            return fail("T7A tabB")
        for b, v in _T7AC:
            if pay[b] != v:
                return fail("T7A const %d" % b)
        print("CLOSED T7A N=%d off=%d" % (n, off))
        return 0
    if n <= 6298:  # 56B dip pair (off=256/257, +256 rule)
        off = n - 6041
        if len(pay) != 56 or pay.hex() != _T7DIP256[off - 256]:
            return fail("T7DIP256")
        print("CLOSED T7DIP256 N=%d" % n)
        return 0
    if n <= 6314:  # T7B1: 16-row tab b16-19/23
        off = n - 6041
        if len(pay) != 60:
            return fail("T7B1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T7B1 lencode")
        cells = bytes((pay[16], pay[17], pay[18], pay[19],
                       pay[23])).hex()
        if cells != _T7B1T[off - 258]:
            return fail("T7B1 row")
        for b, v in _T7B1C:
            if pay[b] != v:
                return fail("T7B1 const %d" % b)
        print("CLOSED T7B1 N=%d off=%d" % (n, off))
        return 0
    if n <= 6324:  # T7B2: 10-row tab b16-19/23/28-30
        off = n - 6041
        if len(pay) != 60:
            return fail("T7B2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T7B2 lencode")
        cells = bytes((pay[16], pay[17], pay[18], pay[19], pay[23],
                       pay[28], pay[29], pay[30])).hex()
        if cells != _T7B2T[off - 274]:
            return fail("T7B2 row")
        for b, v in _T7B2C:
            if pay[b] != v:
                return fail("T7B2 const %d" % b)
        print("CLOSED T7B2 N=%d off=%d" % (n, off))
        return 0
    if n <= 6388:  # T7B3-6: shared b28-32 tab + k2 b20-26
        off = n - 6041
        if len(pay) != 60:
            return fail("T7B3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if grp(pay, tuple(range(32, 42))) != l10:
            return fail("T7B3 lencode")
        m = (off - 284) & 15
        k2 = (off - 284) >> 4
        if pay[20:27].hex() != _T7B3K[k2]:
            return fail("T7B3 k2")
        if pay[28:33].hex() != _T7B3T[m]:
            return fail("T7B3 tab")
        for b, v in _T7B3C:
            if pay[b] != v:
                return fail("T7B3 const %d" % b)
        print("CLOSED T7B3 N=%d off=%d" % (n, off))
        return 0
    print("N out of scope", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
