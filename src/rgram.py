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
# T7C tables (quiet-256): 16-tabs b36-40 + b28-32 walk the
# B3 tab by k2 (full 16, reuse) + b5 edges @359/487.
_T7CT36 = (0x4e, 0x14, 0xdc, 0xf2, 0xa8, 0x6e, 0x84, 0x9a,
           0xff, 0xc5, 0x98, 0x91, 0x59, 0x88, 0x4e, 0x2e)
_T7CT37 = (0xfc, 0xfc, 0xfc, 0xfc, 0xbf, 0xbf, 0xbf, 0xbf,
           0xfc, 0xfc, 0xbf, 0xbf, 0xfc, 0xbf, 0xbf, 0xfc)
_T7CT38 = (0xef, 0xdb, 0x77, 0x7f, 0xff, 0xeb, 0xf3, 0xfb,
           0x53, 0x3f, 0xdf, 0xc7, 0x63, 0x13, 0xff, 0x3f)
_T7CT39 = (0x7e, 0xa9, 0xae, 0xae, 0xb3, 0xde, 0xde, 0xde,
           0xef, 0x1a, 0x1e, 0x1f, 0x24, 0x25, 0x4f, 0x50)
_T7CT40 = (0xb5, 0xb5, 0xb5, 0xb5, 0xb5, 0xb5, 0xb5, 0xb5,
           0xb5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5)
_T7DIP604 = "70cb9323eb53c16bfaf6cf2500adfc2239cbd30a10be4e75" \
    "717f673c92b5983d21bf675391f76b902fdf316b4e2588e45" \
    "114691b4dafaf69"
_T7D0 = ("17000000ed53c16b9a567e11b77f2e0139cbd38a805b9e1"
        "c30eecfa3423c80df329d57e4f8bf178ab83adf212fdf31"
        "6b4e2588e45114691b4dafaf69",
        "6e010000ef53c16bfaf6cfa500adfc2239cbd3ca805b9e1"
        "c30eeafbc423c80df329d579a17bf639cd8f1092212e41"
        "ed5a61244f25114691b4dafaf69")
_T7D1T = ("6f53258ed7ed02", "6f53a50857c6c2", "6f53a509579bc2",
          "6f53a51257cce2", "7053252557b982", "7053252e57eaa2",
          "7053252f57bfa2", "7053a54257ac42", "7054a54b57dd62",
          "7054a55557a382", "7254252fd7a822", "72542538d7d942",
          "72542542d79f62", "7254a54c579be2", "7254a555d7cc02")
_T7D1C = ((1, 0x01), (2, 0x00), (3, 0x00), (6, 0xc1),
          (7, 0x6b), (8, 0xfa), (9, 0xf6), (10, 0xcf),
          (12, 0x00), (13, 0xad), (14, 0xfc), (15, 0x22),
          (16, 0x39), (17, 0xcb), (18, 0xd3), (19, 0x0a),
          (20, 0x80), (21, 0x5b), (22, 0x9e), (23, 0x1c),
          (24, 0x30), (25, 0xee), (26, 0xaf), (28, 0x42),
          (29, 0x3c), (30, 0x80), (31, 0xdf), (32, 0x32),
          (33, 0x9d), (36, 0x17), (37, 0xbf), (38, 0x63),
          (39, 0x9c), (40, 0xd8), (41, 0xf1), (42, 0x09),
          (44, 0x12), (45, 0xe4), (46, 0x1e), (47, 0xd5),
          (48, 0xa6), (49, 0x12), (50, 0x44), (51, 0xf2),
          (52, 0x51), (53, 0x14), (54, 0x69), (55, 0x1b),
          (56, 0x4d), (57, 0xaf), (58, 0xaf), (59, 0x69))
_T7D2S = "0b0000000f54c16b9a567e91b77f2e01f9962747599e56" \
    "0030ee8f12423c80df329dd72d54bf4bf0d348c0bf12e41" \
    "ed5d57c45f25114691b4dafaf69"
_T7D2T = ("0b11474fc6572dfa0370", "0b11478fc6d76e0a0370",
          "0b9107cfecd7af7bd471", "0a91074f9a576e02a773",
          "0b11878f5157eec2ff66", "0b1147efe8d7ae1d0370",
          "0b1187af4ed72d3e336e", "0b11878f09d76ee90370",
          "0b1187cf09d7aff90370")
_T7D2C = ((1, 0x00), (2, 0x00), (3, 0x00), (5, 0x54),
          (6, 0xc1), (7, 0x6b), (8, 0x9a), (9, 0x56),
          (10, 0x7e), (12, 0xb7), (13, 0x7f), (14, 0x2e),
          (15, 0x01), (16, 0xf9), (17, 0x96), (18, 0x27),
          (20, 0x59), (21, 0x9e), (22, 0x56), (23, 0x00),
          (24, 0x30), (25, 0xee), (28, 0x42), (29, 0x3c),
          (30, 0x80), (31, 0xdf), (32, 0x32), (33, 0x9d),
          (36, 0x54), (37, 0xbf), (38, 0x4b), (39, 0xf0),
          (40, 0xd3), (41, 0x48), (42, 0xc0), (44, 0x12),
          (45, 0xe4), (46, 0x1e), (47, 0xd5), (50, 0x45),
          (51, 0xf2), (52, 0x51), (53, 0x14), (54, 0x69),
          (55, 0x1b), (56, 0x4d), (57, 0xaf), (58, 0xaf),
          (59, 0x69))
_T7D3T = ("c77c9204", "387c4605", "083c6405", "9bfc840d",
          "9efc8130", "df7c5231", "727c7339", "3dbc855c",
          "3dbc865c", "5b7cd667", "2b3cf467", "2e3cf18a",
          "893c2793", "02bce293", "8c3c25b6", "60bc15bf")
_T7D3B = ("bb258aaf4bd72e397200ae", "bba58a0f14d72cdf928cad",
          "baa50a0fdc57ed5cf274ae", "baa50a8f00d7aceaf252ad")
_T7D3C = ((1, 0x00), (2, 0x00), (3, 0x00), (5, 0x54),
          (6, 0xc1), (7, 0x6b), (8, 0xfa), (9, 0xf6),
          (10, 0xcf), (12, 0x00), (13, 0xad), (14, 0xfc),
          (15, 0x22), (16, 0x39), (17, 0xcb), (18, 0xd3),
          (20, 0x80), (21, 0x5b), (22, 0x9e), (23, 0x1c),
          (24, 0x30), (25, 0xee), (28, 0x42), (29, 0x3c),
          (30, 0x80), (31, 0xdf), (32, 0x32), (33, 0x9d),
          (36, 0x54), (37, 0xbf), (38, 0x4b), (39, 0xf0),
          (40, 0xd3), (41, 0x48), (42, 0xc0), (47, 0x50),
          (52, 0x75), (53, 0x44), (54, 0x91), (55, 0xb6),
          (56, 0x4d), (57, 0xaf), (58, 0xaf), (59, 0x69))
_T7ET = ("066d7c0771", "06cdbf7f80", "06cd904f81", "064da157d0",
          "124dc55fde", "12cdedc7de", "16eda7272a", "164dcf9f2e",
          "1e0d811f8d", "1e8d9127dc", "1eadffefdc", "22adb85f2c",
          "222de1c72c", "2e8dbf6f3a", "2e8d78df89", "2e0da1478a")
_T7EC = ((0, 0xe0), (1, 0x0b), (2, 0x00), (3, 0x00), (6, 0xc1),
         (7, 0x6b), (8, 0xfa), (9, 0xf6), (10, 0xcf),
         (11, 0xa5), (12, 0x00), (13, 0xad), (14, 0xfc),
         (15, 0x22), (16, 0x39), (17, 0xcb), (18, 0xd3),
         (19, 0x0a), (20, 0x80), (21, 0x5b), (22, 0x9e),
         (23, 0x1c), (24, 0x30), (25, 0xee), (26, 0xef),
         (27, 0xbb), (28, 0x42), (29, 0x3c), (30, 0x80),
         (31, 0xdf), (32, 0x32), (33, 0x9d), (34, 0x57),
         (35, 0xaa), (36, 0x53), (37, 0xba), (38, 0xa8),
         (39, 0xd5), (40, 0x46), (41, 0x02), (42, 0x46),
         (43, 0xe0), (44, 0x72), (45, 0xc6), (46, 0xad),
         (47, 0x0d), (52, 0x75), (53, 0x44), (54, 0x91))
_T7G0 = ("01000000a356c16b9a567e11b77f2e01f99627c7599e56"
        "0010f03baa717f423c329d57ee54bf4bf0d348c083c8de31"
        "a98f5a1bc95114691b4dafaf69",
        "ed000000a556c16bfaf6cf2500adfc2239cbd38a805b9e1"
        "c30ee0f93423c80df329d57ef54bf4bf0d348c0c88f5a9b"
        "d9fbfc3584b27b127a8d93a7c0",
        "d20e0000a7b62c1b1e87ff5c00adfc2239cbd38a805b9e1"
        "c30ee0f93423c80df329d57ef54bf4bf0d348c0c88f5a9b"
        "d9fbfc3584b27b127aadaca7c0")
_T7G1T = ("166a9b1e87", "f6643bde8b", "56a2bbde8b", "961a6b3e8c",
          "96c47bfe90", "565debde91", "56c78b3e92", "36c22bfe96",
          "96ffabfe96", "5682bb3e98", "56de0b1ea3", "f6299b1ea3",
          "d60edb1ea8", "364c5b3ea8", "36cc5b3ea8")
_T7G1C = ((0, 0xd2), (1, 0x0e), (2, 0x00), (3, 0x00),
          (10, 0xff), (11, 0x5c), (12, 0x00), (13, 0xad),
          (14, 0xfc), (15, 0x22), (16, 0x39), (17, 0xcb),
          (18, 0xd3), (19, 0x8a), (20, 0x80), (21, 0x5b),
          (22, 0x9e), (23, 0x1c), (24, 0x30), (25, 0xee),
          (26, 0x0f), (27, 0x93), (28, 0x42), (29, 0x3c),
          (30, 0x80), (31, 0xdf), (32, 0x32), (33, 0x9d),
          (34, 0x57), (35, 0xef), (36, 0x54), (37, 0xbf),
          (38, 0x4b), (39, 0xf0), (40, 0xd3), (41, 0x48),
          (42, 0xc0), (43, 0xc8), (44, 0x8f), (45, 0x5a),
          (46, 0x9b), (47, 0xd9), (48, 0xfb), (49, 0xfc),
          (50, 0x35), (51, 0x84), (52, 0xb2), (53, 0x7b),
          (54, 0x12), (55, 0x7a), (56, 0xad), (57, 0xac),
          (58, 0xa7), (59, 0xc0))
_T7G2S = "b6000000c7d65b3b3e4fe92f00adfc22f9962787599e56" \
    "0030ee0f93423c80df329d57ef54bf4bf0d348c0c84f43a8c" \
    "7d4da7dfeb27b92fc2dcbb7f1"
_T7G2T = ("b6d6762bde837a09", "b6964e0bbe043d0e",
          "b6566a8bbe043d0e", "b656a72bde8ccb17",
          "b5d64b5b3e4ddef1", "b6d6eacbbe093d0e",
          "b6f6dd7b3e4abb04", "b616e0eb7e0e3d0e",
          "b656859bfe8e7a09")
_T7G2C = ((1, 0x00), (2, 0x00), (3, 0x00), (12, 0x00),
          (13, 0xad), (14, 0xfc), (15, 0x22), (16, 0xf9),
          (17, 0x96), (18, 0x27), (19, 0x87), (20, 0x59),
          (21, 0x9e), (22, 0x56), (23, 0x00), (24, 0x30),
          (25, 0xee), (26, 0x0f), (27, 0x93), (28, 0x42),
          (29, 0x3c), (30, 0x80), (31, 0xdf), (32, 0x32),
          (33, 0x9d), (34, 0x57), (35, 0xef), (36, 0x54),
          (37, 0xbf), (38, 0x4b), (39, 0xf0), (40, 0xd3),
          (41, 0x48), (42, 0xc0), (43, 0xc8), (44, 0x4f),
          (45, 0x43), (46, 0xa8), (47, 0xc7), (48, 0xd4),
          (49, 0xda), (50, 0x7d), (51, 0xfe), (52, 0xb2),
          (53, 0x7b), (54, 0x92), (55, 0xfc), (56, 0x2d),
          (57, 0xcb), (58, 0xb7), (59, 0xf1))
_T7G3T = ("99fc155d92", "d27ca57d96", "1bbc409d96", "1f7c569d96",
          "6c3c06bd96", "a1fc80dd9a", "a1fc81dd9a", "a5bc97dd9a",
          "f27c47fd9a", "277cc21d9f", "277cc31d9f", "743c733d9f",
          "91bce65da3", "adbc037da3", "76bcc5bda3", "92bce2bda3")
_T7G3B = ("46b69ffbbe0f3d0e", "45d6963bfe4cffff",
          "4697255b1e9ecb17", "45b7ad5b9e8646fb")
_T7G3C = ((1, 0x0b), (2, 0x00), (3, 0x00), (12, 0x00),
          (18, 0x3c), (19, 0xad), (20, 0x80), (21, 0x5b),
          (22, 0x9e), (23, 0x1c), (24, 0x30), (25, 0xee),
          (26, 0x0f), (27, 0x93), (28, 0x42), (29, 0x3c),
          (30, 0x80), (31, 0xdf), (32, 0x32), (33, 0x9d),
          (34, 0x57), (35, 0xef), (36, 0x54), (37, 0xbf),
          (38, 0x4b), (39, 0xf0), (40, 0xd3), (41, 0x48),
          (42, 0xc0), (43, 0xc8), (44, 0x4f), (45, 0x43),
          (46, 0xa8), (47, 0xc7), (48, 0xd4), (49, 0xda),
          (50, 0x7d), (51, 0xfe), (52, 0xb2), (53, 0x7b),
          (54, 0x92), (55, 0xfc), (56, 0x2d), (57, 0xcb),
          (58, 0xb7), (59, 0xf1))
_T7HT = ("3eda9696", "3bdbc296", "a3dfb599", "3f5c52a0",
          "3ddb5bb3", "58dbe0b5", "d45a7bb6", "ef5a00b9",
          "0cdc0ecc", "a65a02cf", "f7da07cf", "735aa2cf",
          "8e5a27d2", "a55bc7eb", "f6dbcceb", "3cdbe6ee")
_T7HC = ((0, 0x26), (1, 0xb5), (2, 0x00), (3, 0x00),
         (6, 0xac), (7, 0x9b), (8, 0x3e), (9, 0x9a),
         (10, 0x7a), (11, 0x09), (12, 0x00), (18, 0x3c),
         (19, 0xad), (24, 0x34), (25, 0xe2), (26, 0xfe),
         (27, 0x30), (28, 0x42), (29, 0x3c), (30, 0x80),
         (31, 0xdf), (32, 0x32), (33, 0x9d), (34, 0x57),
         (35, 0xef), (36, 0x54), (37, 0xbf), (38, 0x4b),
         (39, 0xf0), (40, 0xd3), (41, 0x48), (42, 0xc0),
         (43, 0xc8), (44, 0x4f), (45, 0x43), (46, 0xa8),
         (47, 0xc7), (48, 0xd4), (49, 0xda), (50, 0x7d),
         (51, 0xfe), (52, 0xb2), (53, 0x7b), (54, 0x92),
         (55, 0xfc), (56, 0x2d), (57, 0xcb), (58, 0xb7),
         (59, 0xf1))
_T7I0 = ("2c0000005bd9537bfcd1bd1900adfc22f9962787599e56"
        "0030ee0f93423c80df329d57ef54bf4bf0d348c0c84f43a8"
        "c7d4da7dfeb27b92fc2dcbb7f1",
        "520b00005dd9537bfcd1bd19007cfc7639760c276f5c711"
        "af61a7ec7423c80df329d57ef54bf4bf0d348c0c84f43a8"
        "c7d4da7dfeb27b92fc2dcbb7f1")
_T7I1T = ("433c02e376", "a1fc401b96", "3a7c161c96", "a67c219f96",
          "a67c229f96", "3ffcf79f96", "9dbc36d896", "343c55d896",
          "693c03e796", "00bc21e796", "c7fc421fb6", "f7bc3520b6",
          "f7bc3620b6", "55bc7558b6", "8dfc355cb6", "5a3c56dcb6")
_T7I1C = ((0, 0x26), (1, 0xb5), (2, 0x00), (3, 0x00),
          (5, 0xd9), (6, 0x53), (7, 0x7b), (8, 0xfc),
          (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
          (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
          (17, 0x76), (18, 0x0c), (19, 0x27), (20, 0x35),
          (21, 0x5d), (22, 0x71), (23, 0x1a), (24, 0xf6),
          (25, 0x1a), (26, 0x7e), (27, 0x77), (33, 0xd3),
          (34, 0x79), (35, 0xf5), (36, 0x54), (37, 0xbf),
          (38, 0x4b), (39, 0xf0), (40, 0xd3), (41, 0x48),
          (42, 0xc0), (43, 0xc8), (44, 0x4f), (45, 0x43),
          (46, 0xa8), (47, 0xc7), (48, 0xd4), (49, 0xda),
          (50, 0x7d), (51, 0xfe), (52, 0xb2), (53, 0x7b),
          (54, 0x92), (55, 0xfc), (56, 0x2d), (57, 0xcb),
          (58, 0xb7), (59, 0xf1))
_T7I2T = ("94bcb71f17c2bf", "307c550437c685", "f8fc070ed7258c",
          "0c3ce3aad78992", "4dbcd0d517f298", "e17cf767b72966",
          "be7cf7e3d78992", "d5fc42b3f76a7f", "663c46cad7258c",
          "083c71c137c685")
_T7I2C = ((0, 0xa4), (1, 0x16), (2, 0x00), (3, 0x00),
          (5, 0xd9), (6, 0x53), (7, 0x7b), (8, 0xfc),
          (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
          (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
          (17, 0x76), (18, 0x0c), (19, 0x67), (20, 0x49),
          (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
          (25, 0xdd), (26, 0xb5), (27, 0x8e), (35, 0xe2),
          (36, 0x54), (37, 0xbf), (38, 0x4b), (39, 0xf0),
          (40, 0xd3), (41, 0x48), (42, 0xc0), (43, 0xc8),
          (44, 0x4f), (45, 0x43), (46, 0xa8), (47, 0xc7),
          (48, 0xd4), (49, 0xda), (50, 0x7d), (51, 0xfe),
          (52, 0xb2), (53, 0x7b), (54, 0x92), (55, 0xfc),
          (56, 0x2d), (57, 0xcb), (58, 0xb7), (59, 0xf1))
_T7I3T36 = (0x51, 0x67, 0x6e, 0x8c, 0x6d, 0x4d, 0x2e, 0x5a,
            0x53, 0x69, 0x31, 0x90, 0x56, 0x37, 0x4d, 0xa1)
_T7I3T37 = (0xfc, 0xfc, 0xfc, 0xbf, 0xbf, 0xfc, 0xfc, 0xbf,
            0xbf, 0xbf, 0xfc, 0xbf, 0xbf, 0xbf, 0xbf, 0xfc)
_T7I3T38 = (0x87, 0x8f, 0x27, 0xb7, 0xfb, 0x3b, 0x7f, 0xbf,
            0xa7, 0xaf, 0x4b, 0x87, 0x73, 0xb7, 0xbf, 0xf7)
_T7I3T39 = (0xcb, 0xcb, 0x06, 0xa7, 0xac, 0xad, 0xb2, 0x8d,
            0x8e, 0x8e, 0x93, 0x44, 0x6f, 0x74, 0x74, 0x25)
_T7I3T40 = (0x77, 0x77, 0x97, 0x97, 0x97, 0x97, 0x97, 0xb7,
            0xb7, 0xb7, 0xb7, 0xd7, 0xd7, 0xd7, 0xd7, 0xf7)
_T7I3B = ("fc3cf667f78992", "457c61e7371479", "59fc42bf37f298",
          "aa3c66f2371479")
_T7I3C = ((0, 0x4c), (1, 0x6a), (2, 0x01), (3, 0x00),
          (6, 0x53), (7, 0x7b), (8, 0xfc),
          (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
          (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
          (17, 0x76), (18, 0x0c), (19, 0x27), (20, 0x49),
          (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
          (25, 0xdd), (26, 0x35), (27, 0xef),
          (35, 0xc2), (41, 0x8d),
          (42, 0x04), (43, 0x8c), (44, 0x4f), (45, 0x43),
          (46, 0xa8), (47, 0xc7), (48, 0xd4), (49, 0xda),
          (50, 0x7d), (51, 0xfe), (52, 0xb2), (53, 0x7b),
          (54, 0x92), (55, 0xfc), (56, 0x2d), (57, 0xcb),
          (58, 0xb7), (59, 0xf1))
_T7JT = ("b71582c8e094", "f7dd9dc8e0b3", "d7e59dc8e05b",
          "f72d9ec860e4", "d79560c9e08d", "b72d81c960f4",
          "f77581c9e07c", "d70dc5c96099", "b715c5c96041",
          "f77587cae042", "d745a3cae009", "f78da3ca6092",
          "d725aacae0d5", "b72dc4cae0a0", "f75588cb609e",
          "d75d88cb6046")
_T7JB = ("1e2e17e7b5e2126b", "3e2e17e735e3726b",
          "9e1814e735e3e26c", "de9e166735fcc26c",
          "eeb3166735fbd26c", "eeb416e735e2d26c",
          "fec916e735e1e26c", "fe361667b5faa26d",
          "9e3a1667b5fa326d", "be3a166735fb926d",
          "2e4d16e7b5e1126d", "1e121567b5fc026e",
          "cebd1567b5fa626e", "ded21567b5f9726e",
          "fed2156735fad26e", "de9714e735e5126f")
_T7JC = ((3, 0x00), (6, 0x53), (7, 0x7b), (8, 0xfc),
         (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
         (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
         (17, 0x76), (18, 0x0c), (20, 0x49), (21, 0x5f),
         (22, 0x4d), (23, 0x82), (24, 0x32), (25, 0xdd),
         (28, 0xc3), (29, 0x3c), (30, 0x46), (31, 0xfe),
         (32, 0x37), (33, 0xc6), (34, 0x85), (41, 0x24),
         (44, 0x53), (45, 0xa9), (46, 0xb5), (47, 0x7a),
         (48, 0xfb), (49, 0xfc), (50, 0x35), (51, 0x84),
         (52, 0xb2), (53, 0x7b), (54, 0x92), (55, 0xfc),
         (56, 0x2d), (57, 0xcb), (58, 0xb7), (59, 0xf1))
_T7K0 = ("d402000013dc537bfcd1bd19007cfc7639760c67495f4d"
        "8232ddb531a8bc2167147da4bc54bf4bf0d348c0c84f43a8"
        "c7d4da7dfeb27b92fc2dcbb7f1",
        "f4e2020015dc537bfcd1bd19007cfc7639760ce7495f4d82"
        "32dd35bfa8bc2167147da4b6b4e036c76811d3c5b68eeed"
        "0fbfc3584b27b92fc2dcbb7f1",
        "f4622e0017dc537bfcd1bd19007cfc7639760ce7495f4d82"
        "32dd35bfa8bc2167147da4b6142d627a8bdaa45f9648fa7"
        "8bffc77a056bb27c92dcbb7f1")
_T7K1T = ("083c50a156", "083c51a156", "b07ce2ce56",
          "f1fcb2cf56", "f1fcb3cf56", "0ebc16fa56",
          "4f3ce7fa56", "c87ca2fb56", "b53c865476",
          "f6bc565576", "89bc775d76", "5c7c918076",
          "5c7c928076", "603c668976", "30fc838976")
_T7K1C = ((0, 0xf4), (1, 0x62), (2, 0x2e), (3, 0x00),
          (5, 0xdc), (6, 0x53), (7, 0x7b), (8, 0xfc),
          (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
          (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
          (17, 0x76), (18, 0x0c), (19, 0xe7), (20, 0x49),
          (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
          (25, 0xdd), (26, 0x35), (27, 0xbf), (28, 0xa8),
          (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
          (33, 0x7d), (34, 0xa4), (35, 0xb6), (36, 0x14),
          (37, 0x2d), (38, 0x62), (39, 0x7a), (40, 0x8b),
          (41, 0xda), (42, 0xa4), (43, 0x5f), (44, 0x96),
          (45, 0x48), (46, 0xfa), (47, 0x78), (53, 0xbb),
          (54, 0x27), (55, 0xc9), (56, 0x2d), (57, 0xcb),
          (58, 0xb7), (59, 0xf1))
_T7K2S = "f462010037dc537bfcd1bd19007cfc7639760ce7495f4d" \
    "8232dd35bfa8bc2167147da4b6b40647e2681113b8b197e3" \
    "eb76fc516e9651eecc2dcbb7f1"
_T7K2AT = ("027c671d9630ca", "72fc87259630ca", "8e7cd310b6a9ce",
           "df3c2330f625d3", "6c7c27ca369baf", "86bc063cb6a9ce",
           "b4bc1115d647c1", "ed3c8073b6a9ce", "88fc65c8b6bac5")
_T7K2AC = ((0, 0xf4), (1, 0x62), (2, 0x01), (3, 0x00),
           (5, 0xdc), (6, 0x53), (7, 0x7b), (8, 0xfc),
           (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
           (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
           (17, 0x76), (18, 0x0c), (19, 0xe7), (20, 0x49),
           (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
           (25, 0xdd), (26, 0x35), (27, 0xbf), (28, 0xa8),
           (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
           (33, 0x7d), (34, 0xa4), (35, 0xb6), (36, 0xb4),
           (37, 0x06), (38, 0x47), (39, 0xe2), (40, 0x68),
           (41, 0x11), (42, 0x13), (43, 0xb8), (44, 0xb1),
           (45, 0x97), (46, 0xe3), (47, 0xeb), (55, 0xcc),
           (56, 0x2d), (57, 0xcb), (58, 0xb7), (59, 0xf1))
_T7K2S2 = "f46217004bdc537bfcd1bd19007cfc7639760ce7495f4d" \
    "8232dd35bfa8bc2167147da4b6142d623c815b8323b197e3" \
    "bea23c7696b6a9cea44dadc7f4"
_T7K2BT = ("e3bebc8d9adf47", "e3bef4ed898ffe", "23bf0cadce3f51")
_T7K2BC = ((0, 0xf4), (1, 0x62), (2, 0x17), (3, 0x00),
           (5, 0xdc), (6, 0x53), (7, 0x7b), (8, 0xfc),
           (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
           (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
           (17, 0x76), (18, 0x0c), (19, 0xe7), (20, 0x49),
           (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
           (25, 0xdd), (26, 0x35), (27, 0xbf), (28, 0xa8),
           (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
           (33, 0x7d), (34, 0xa4), (35, 0xb6), (36, 0x14),
           (37, 0x2d), (38, 0x62), (39, 0x3c), (40, 0x81),
           (41, 0x5b), (42, 0x83), (43, 0x23), (44, 0xb1),
           (45, 0x97), (48, 0xa2), (49, 0x3c), (50, 0x76),
           (51, 0x96), (52, 0xb6), (53, 0xa9), (54, 0xce))
_T7K3AT = ("230cad87afa0", "230c0dcb27b0", "235c4d63a70d",
           "235cada7efb9", "2374cdaf171c", "2374ed697767",
           "23bc8d70ff79", "23bc4d70bfc5", "23bcad9737ca",
           "23c4ad6d77c1", "63148dfa871e", "63248d65b780")
_T7K3AC = ((0, 0xf4), (1, 0x62), (2, 0x17), (3, 0x00),
           (5, 0xdc), (6, 0x53), (7, 0x7b), (8, 0xfc),
           (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
           (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
           (17, 0x76), (18, 0x0c), (19, 0xe7), (20, 0x49),
           (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
           (25, 0xdd), (26, 0x35), (27, 0xbf), (28, 0xa8),
           (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
           (33, 0x7d), (34, 0xa4), (35, 0xb6), (36, 0x14),
           (37, 0x2d), (38, 0x62), (39, 0x3c), (40, 0x81),
           (41, 0x5b), (42, 0x83), (43, 0x23), (44, 0xb1),
           (45, 0x97), (47, 0xbf), (48, 0xa2), (49, 0x3c),
           (50, 0x76), (51, 0x96), (52, 0xb6), (53, 0xa9),
           (54, 0xce))
_T7K3B = ("cb7cc7f416d8bc", "d3bcc6b5f625d3", "c77c98f516d8bc")
_T7K3T = ("e3bea44dadc7f4", "e3bebc8d9adf47", "e3bef4ed898ffe",
          "23bf0cadce3f51", "23bf0cad87afa0", "23bf0c0dcb27b0",
          "23bf5c4d63a70d", "23bf5cada7efb9", "23bf74cdaf171c",
          "23bf74ed697767", "23bfbc8d70ff79", "23bfbc4d70bfc5",
          "23bfbcad9737ca", "23bfc4ad6d77c1", "63bf148dfa871e",
          "63bf248d65b780")
_T7K3C = ((0, 0xf4), (1, 0x62), (2, 0x17), (3, 0x00),
          (5, 0xdc), (6, 0x53), (7, 0x7b), (8, 0xfc),
          (9, 0xd1), (10, 0xbd), (11, 0x19), (12, 0x00),
          (13, 0x7c), (14, 0xfc), (15, 0x76), (16, 0x39),
          (17, 0x76), (18, 0x0c), (19, 0xe7), (20, 0x49),
          (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
          (25, 0xdd), (26, 0x35), (27, 0xbf), (28, 0xa8),
          (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
          (33, 0x7d), (34, 0xa4), (35, 0xb6), (36, 0x14),
          (37, 0x2d), (38, 0x62), (39, 0x3c), (40, 0x81),
          (41, 0x5b), (42, 0x83), (43, 0x23), (44, 0xb1),
          (45, 0x97))
_T7LT = ("79d83b52", "32de8752", "8f588c52", "5ad94255",
          "81d88456", "14da995d", "ffdb9d5d", "c1d9ce5e",
          "7adf1a5f", "d7591f5f", "cfde6067", "2c596567",
          "175b6967", "3e5aab68", "925ee668", "05dfad72")
_T7LC = ((0, 0x4e), (1, 0x2f), (2, 0x76), (3, 0x01),
         (6, 0xde), (7, 0x0c), (8, 0x00), (9, 0x80),
         (10, 0x8f), (11, 0xdf), (12, 0x39), (13, 0x76),
         (14, 0x0c), (15, 0xe7), (16, 0x49), (17, 0x5f),
         (18, 0x4d), (19, 0x82), (20, 0x32), (21, 0xdd),
         (22, 0x35), (23, 0xbf), (24, 0xa8), (25, 0xbc),
         (26, 0x21), (27, 0x67), (28, 0x14), (29, 0x7d),
         (30, 0xa4), (31, 0xb6), (32, 0x14), (33, 0x2d),
         (34, 0x62), (35, 0x3c), (36, 0x81), (37, 0x5b),
         (38, 0x83), (39, 0x23), (40, 0xb1), (41, 0x97),
         (44, 0xa1), (45, 0xbc), (46, 0x37), (47, 0x4d),
         (48, 0xd6), (49, 0xba), (50, 0xc5))
_T7M0 = ("222e0000cbde537bfcd1bd19007cfc7639760ce7495f4d"
        "8232ddb506a8bc2167147da46e5bbfebc5142d6202b19763"
        "3db6fcc2193359bdf92dcbb7f1",
        "bb880f00cd3e8c9222003e7e39760ce7495f4d8232ddb506"
        "a8bc2167147da46e5bbfebc5142d6202b197a33db6fcc219"
        "3359bdf6cda94f33c25f8e1c")
_T7M1T = ("29003a9edd72", "2a003a1edd72", "4c00081e1d73",
          "1280361efd73", "6100495e5d77", "610049de5d77",
          "39806fbe7d77", "7c00123e3d78", "73007efe9d7b",
          "4b8024febd7b", "5a80327ebd7b", "02006c1e5d84",
          "10007a9e5d84", "6880209e5d84", "22002f5e9d88",
          "22002fde9d88")
_T7M1C = ((1, 0x8f), (2, 0xf8), (3, 0x00), (5, 0x3e),
          (6, 0x8c), (7, 0x92), (8, 0x22), (14, 0xc7),
          (15, 0x70), (16, 0x49), (17, 0x5f), (18, 0x4d),
          (19, 0x82), (20, 0x32), (21, 0xdd), (22, 0xb5),
          (23, 0x06), (24, 0xa8), (25, 0xbc), (26, 0x21),
          (27, 0x67), (28, 0x14), (29, 0x7d), (30, 0xa4),
          (31, 0x6e), (32, 0x5b), (33, 0xbf), (34, 0xeb),
          (35, 0xc5), (36, 0x14), (37, 0x2d), (38, 0x62),
          (39, 0x02), (40, 0xb1), (41, 0x97), (42, 0xa3),
          (43, 0x3d), (44, 0xb6), (45, 0xfc), (46, 0xc2),
          (47, 0x19), (48, 0x33), (49, 0x59), (50, 0xbd),
          (51, 0xf6), (52, 0xcd), (53, 0xa9), (54, 0x4f),
          (55, 0x33), (56, 0xf5), (57, 0xd8), (58, 0x8e),
          (59, 0x1c))
_T7M2S = "e7880f00efde2a3bbd6ff55a00e3fcd1fea7a23c495f4d" \
    "8232ddb506a8bc2167147da46e5bbfebc5142d6202b197a33" \
    "db6fcc2193359bdf6cda94f33"
_T7MBT = ("de2efca3de3b6f22", "de1cbcc0de3b6f22",
          "de4d7c131e7aad25", "de2afc907e1cee28",
          "de96bc02fe62290f", "deebfcb27e7dad25",
          "dee67c809e8df91b", "de223ce75e7ead25",
          "dfb87c08de40331f")
_T7MBC = ((0, 0xe7), (1, 0x88), (2, 0x0f), (3, 0x00),
          (6, 0x2a), (7, 0x3b), (8, 0xbd), (9, 0x6f),
          (10, 0xf5), (11, 0x5a), (12, 0x00), (20, 0x49),
          (21, 0x5f), (22, 0x4d), (23, 0x82), (24, 0x32),
          (25, 0xdd), (26, 0xb5), (27, 0x06), (28, 0xa8),
          (29, 0xbc), (30, 0x21), (31, 0x67), (32, 0x14),
          (33, 0x7d), (34, 0xa4), (35, 0x6e), (36, 0x5b),
          (37, 0xbf), (38, 0xeb), (39, 0xc5), (40, 0x14),
          (41, 0x2d), (42, 0x62), (43, 0x02), (44, 0xb1),
          (45, 0x97), (46, 0xa3), (47, 0x3d), (48, 0xb6),
          (49, 0xfc), (50, 0xc2), (51, 0x19), (52, 0x33),
          (53, 0x59), (54, 0xbd), (55, 0xf6), (56, 0xcd),
          (57, 0xa9), (58, 0x4f), (59, 0x33))
_T7RAT = ("bcdfc6fbf6d2", "3fdaccfbf6d2", "905ad2fbf6d2",
          "a4dfebfef6d2", "34db875316d3", "d25ffb5316d3",
          "9a5e846916d3", "ebde896916d3", "f95d97b816d3",
          "145e1cbb16d3", "afdfbbbb16d3", "addbe4c116d3",
          "3fdf571036d3", "f85f501336d3", "27db7c1336d3",
          "3cde732936d3")
_T7RAB = ("c67ce85e7ead25", "1cbc68de17c218", "aafc459e28ee28",
          "b63c23fe18c218")
_T7RAC = ((0, 0x07), (1, 0x8e), (2, 0xf8), (3, 0x00),
          (5, 0xdf), (6, 0x2a), (7, 0x3b), (8, 0xbd),
          (9, 0x6f), (10, 0xf5), (11, 0x5a), (12, 0x00),
          (26, 0x5d), (27, 0x6b), (28, 0xa8), (29, 0xbc),
          (30, 0x21), (31, 0x67), (32, 0x14), (33, 0x7d),
          (34, 0xa4), (35, 0x6e), (36, 0x5b), (37, 0xbf),
          (38, 0xeb), (39, 0xc5), (40, 0x14), (41, 0x2d),
          (42, 0x62), (43, 0x02), (44, 0xb1), (45, 0x97),
          (46, 0xa3), (47, 0x3d), (48, 0xb6), (49, 0xfc),
          (50, 0xc2), (51, 0x19), (52, 0x33), (53, 0x59),
          (54, 0xbd), (55, 0xf6), (56, 0xcd), (57, 0xa9),
          (58, 0x4f), (59, 0x33))
_T7RBT = ("827c160458", "1bbcf30458", "00bc454278",
          "00bc464278", "5e7c857a78", "96bc457e78",
          "2ffc227f78", "14fc74bc98", "d97cd7f398",
          "72bcb4f498", "a27ca7f598", "08fcb330b8",
          "c03c16a8d8", "5c3ce8b5d8", "bffcf7e3d8",
          "517c45eed8")
_T7RBB = ("c7e0880fdf2a3bbd6ff55acd", "8ec1111f8055765edfeab5ce")
_T7RBC = ((12, 0x00), (13, 0x4a), (14, 0x7c), (15, 0x53),
          (16, 0xbe), (17, 0x49), (18, 0x33), (19, 0x1f),
          (26, 0x5d), (27, 0xb3), (33, 0xd0), (34, 0x47),
          (35, 0xea), (36, 0x5b), (37, 0xbf), (38, 0xeb),
          (39, 0xc5), (40, 0x14), (41, 0x2d), (42, 0x62),
          (43, 0x02), (44, 0xb1), (45, 0x97), (46, 0xa3),
          (47, 0x3d), (48, 0xb6), (49, 0xfc), (50, 0xc2),
          (51, 0x19), (52, 0x33), (53, 0x59), (54, 0xbd),
          (55, 0xf6), (57, 0xa9), (58, 0x4f), (59, 0x33))
_T7N0 = ("3ee20300838155765edfeab5002cbc947bf8fc2f495f4d"
        "8232ddb506a8bc2167147da46e5bbfebc5142d6202b197a3"
        "3db6fcc2193359bdf6cea94f33",
        "0e8ef800858155765edfeab5002cbc947bf8fc2f955a28bd"
        "9230f2adf83c90195a3dade25bbfebc5142d6202b197a33"
        "db6fcc2193359bdf6cea94f33",
        "f6d2710e878155765edfeab5002cbc947bf8fc2f955a28bd"
        "9230725d3afe2d9d44f51e2f786b70c495163181b197a33"
        "db6fcc2193359bdf6cea94f33")
_T7N1T = ("3afe319d8795", "1afe43f0c795", "3afe47f01f95",
          "badfe78d9f96", "9adff9e0df96", "1afe19e15f96",
          "7afe67e37f96", "dadf4be97796", "1afe61afdb98",
          "fadfd7c4f398", "1afedbc44b98", "dadf09cd0b98",
          "1afe37a07399", "1afe3ba0cb99", "fadfb1b5e399")
_T7N1C = ((0, 0xf6), (1, 0xd2), (2, 0x71), (3, 0x0e),
          (5, 0x81), (6, 0x55), (7, 0x76), (8, 0x5e),
          (9, 0xdf), (10, 0xea), (11, 0xb5), (12, 0x00),
          (13, 0x2c), (14, 0xbc), (15, 0x94), (16, 0x7b),
          (17, 0xf8), (18, 0xfc), (19, 0x2f), (20, 0x95),
          (21, 0x5a), (22, 0x28), (23, 0xbd), (24, 0x92),
          (25, 0x30), (26, 0x72), (27, 0x5d), (32, 0x44),
          (33, 0xf5), (34, 0x1e), (36, 0x78), (37, 0x6b),
          (38, 0x70), (39, 0xc4), (41, 0x16), (42, 0x31),
          (43, 0x81), (44, 0xb1), (45, 0x97), (46, 0xa3),
          (47, 0x3d), (48, 0xb6), (49, 0xfc), (50, 0xc2),
          (51, 0x19), (52, 0x33), (53, 0x59), (54, 0xbd),
          (55, 0xf6), (56, 0xce), (57, 0xa9), (58, 0x4f),
          (59, 0x33))
_T7N2S = "fe21f700a78155765edfeab5002cbc947bf8fc2f955a28" \
    "bd923072f077fc610776eceae8786b70c45a65bc81b197a33" \
    "db6fcc2193359bdf6cea94f33"
_T7N2T = ("7ed8e5f2f3f84965b7", "f635eb72fe604965b7",
          "7e36eb72f1f04965b7", "76e7ebf2fea897a2b8",
          "7e26e672f360fdb7b3", "76a5ff72ff30b603b8",
          "f6d0e472fcc8c629b6", "fe0ee2f2f1884a65b7",
          "7625e6f2fc584fc7b6")
_T7N2C = ((3, 0x00), (5, 0x81), (6, 0x55), (7, 0x76),
          (8, 0x5e), (9, 0xdf), (10, 0xea), (11, 0xb5),
          (12, 0x00), (13, 0x2c), (14, 0xbc), (15, 0x94),
          (16, 0x7b), (17, 0xf8), (18, 0xfc), (19, 0x2f),
          (20, 0x95), (21, 0x5a), (22, 0x28), (23, 0xbd),
          (24, 0x92), (25, 0x30), (28, 0x77), (29, 0xfc),
          (30, 0x61), (31, 0x07), (32, 0x76), (33, 0xec),
          (34, 0xea), (36, 0x78), (37, 0x6b), (38, 0x70),
          (39, 0xc4), (43, 0x81), (44, 0xb1), (45, 0x97),
          (46, 0xa3), (47, 0x3d), (48, 0xb6), (49, 0xfc),
          (50, 0xc2), (51, 0x19), (52, 0x33), (53, 0x59),
          (54, 0xbd), (55, 0xf6), (56, 0xce), (57, 0xa9),
          (58, 0x4f), (59, 0x33))
_T7N3S = "f6871d0cbb8155765edfeab5002cbc947bf8fc2f955a28" \
    "bd9230f23bf6fdaae46357c7c6187700770f5f66cdf57939da" \
    "b6fcc2193359bdf6cea94f33"
_T7N3T = ("4ddde7eff579", "a05a0efcf579", "e8de7bfcf579",
          "7e5c1cfef579", "b7da5502157a", "3c5df82e157a",
          "f85cfd30157a", "59590231157a", "435e403d157a",
          "925bc65f157a", "4e5bcb61157a", "12dea46d157a",
          "645bc671157a", "a2d94794157a", "9d5d8aa0157a")
_T7N3C = ((0, 0xf6), (1, 0x87), (2, 0x1d), (3, 0x0c),
          (5, 0x81), (6, 0x55), (7, 0x76), (8, 0x5e),
          (9, 0xdf), (10, 0xea), (11, 0xb5), (12, 0x00),
          (13, 0x2c), (14, 0xbc), (15, 0x94), (16, 0x7b),
          (17, 0xf8), (18, 0xfc), (19, 0x2f), (20, 0x95),
          (21, 0x5a), (22, 0x28), (23, 0xbd), (24, 0x92),
          (25, 0x30), (26, 0xf2), (27, 0x3b), (28, 0xf6),
          (29, 0xfd), (30, 0xaa), (31, 0xe4), (32, 0x63),
          (33, 0x57), (34, 0xc7), (35, 0xc6), (36, 0x18),
          (37, 0x77), (38, 0x00), (39, 0x77), (46, 0x39),
          (47, 0xda), (48, 0xb6), (49, 0xfc), (50, 0xc2),
          (51, 0x19), (52, 0x33), (53, 0x59), (54, 0xbd),
          (55, 0xf6), (56, 0xce), (57, 0xa9), (58, 0x4f),
          (59, 0x33))
_T7N4T = ("0f5f66cdf579", "4ddde7eff579", "a05a0efcf579",
          "e8de7bfcf579", "7e5c1cfef579", "b7da5502157a",
          "3c5df82e157a", "f85cfd30157a", "59590231157a",
          "435e403d157a", "925bc65f157a", "4e5bcb61157a",
          "12dea46d157a", "645bc671157a", "a2d94794157a",
          "9d5d8aa0157a")
_T7N4B = ("8121e587227895b176", "8196e7c71418531477",
          "82fde7873b58009e76")
_T7N4C = ((0, 0xf6), (1, 0x87), (2, 0x1d), (3, 0x0c),
          (6, 0x55), (7, 0x76), (8, 0x5e), (9, 0xdf),
          (10, 0xea), (11, 0xb5), (12, 0x00), (13, 0x2c),
          (14, 0xbc), (15, 0x94), (16, 0x7b), (17, 0xf8),
          (18, 0xfc), (19, 0x2f), (20, 0x95), (21, 0x5a),
          (22, 0x28), (23, 0xbd), (24, 0x92), (25, 0x30),
          (26, 0xf2), (27, 0x3b), (28, 0xf6), (29, 0x5f),
          (32, 0x63), (33, 0x57), (46, 0x39), (47, 0xda),
          (48, 0xb6), (49, 0xfc), (50, 0xc2), (51, 0x19),
          (52, 0x33), (53, 0x59), (54, 0xbd), (55, 0xf6),
          (56, 0xce), (57, 0xa9), (58, 0x4f), (59, 0x33))
_T7OT = ("27bc60e517", "6ebca2c437", "01bcc3cc37",
          "ccbcd5ef37", "ccbcd6ef37", "a03cc7f837",
          "efbc10d857", "60bcc4d857", "c33c02e157",
          "4dfc440377", "c63c000477", "a03c62eb77",
          "97fc371897", "22fc671b97", "47fcd14597",
          "887ca24697")
_T7OC = ((0, 0xf6), (1, 0x87), (2, 0x1d), (3, 0xf8),
         (6, 0x55), (7, 0x76), (8, 0x5e), (9, 0xdf),
         (10, 0xea), (11, 0xb5), (12, 0x00), (13, 0x2c),
         (14, 0xbc), (15, 0x94), (16, 0x7b), (17, 0xf8),
         (18, 0xfc), (19, 0x2f), (20, 0x95), (21, 0x5a),
         (22, 0x28), (23, 0xbd), (24, 0x92), (25, 0x30),
         (26, 0xf2), (27, 0x3b), (28, 0x76), (29, 0xec),
         (30, 0xea), (31, 0x38), (32, 0x55), (33, 0xbf),
         (34, 0x63), (35, 0xc9), (36, 0x18), (37, 0xea),
         (38, 0xd8), (39, 0xb6), (46, 0x39), (47, 0xbe),
         (53, 0x92), (54, 0xd5), (55, 0x6b), (56, 0xce),
         (57, 0xa9), (58, 0x4f), (59, 0x33))
_T7TAIL = ("c6111f003b8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23577fc610776ecea7094fcbfd615f9d406b197"
           "a33db6fcc2193359bdf6cea94f33",
           "f6871d1c3d8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5c66357072515f9d4f6e15ec886d24"
           "583bd353c178a9a9e9b17cea94f33")
_T8HT = ("83cf17eea7ef55", "83cf170efe57a5", "03d0174eeb6ff8",
          "03d0978e91ef07", "83d297cee24711", "83d297ee9ca75c",
          "83d2974ec41f61", "83d297ceec8761", "03d8978ecf4f76",
          "83d817ae91af31", "83d817cee71781", "03d9170ed52fd4",
          "83db174e6daf31", "83db17ce951732", "83db17eeeb7f81",
          "83db970eaedf3c")
_T8HC = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00),
         (5, 0x84), (6, 0x55), (7, 0x76), (8, 0xfe),
         (9, 0x87), (10, 0x1d), (11, 0xf0), (12, 0xfa),
         (13, 0x56), (14, 0xaf), (15, 0xb5), (16, 0x00),
         (17, 0x2c), (18, 0xbc), (19, 0x94), (20, 0x7b),
         (21, 0xf8), (22, 0xfc), (23, 0x2f), (24, 0x95),
         (25, 0x5a), (26, 0x28), (27, 0xbd), (28, 0x92),
         (29, 0x30), (30, 0xf2), (31, 0x3b), (32, 0x76),
         (33, 0xec), (34, 0xea), (35, 0x78), (36, 0x94),
         (37, 0xfc), (38, 0xbf), (39, 0xd6), (40, 0x15),
         (41, 0xf9), (42, 0xd4), (43, 0x6e), (44, 0xe1),
         (45, 0x5e), (46, 0xc8), (47, 0x86), (48, 0xd2),
         (49, 0x45), (52, 0xf1), (53, 0x3c), (54, 0x17),
         (55, 0x8a), (56, 0x9a), (57, 0x9e), (58, 0x9b))
_T8DIPW = ("f6871d145f8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5c66357072515f9d436e15ec886d24"
           "5831f253c57db15e7aa6d6e817f75",
           "f6871d14618455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5b66357072515f9d41ae15ec886d24"
           "58363253c57db15e7aabdcea74fad",
           "f6871d14638455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5ae6357072515f9d4d6e15ec886d24"
           "583c3253c57db15e7aa69ce6ef713",
           "f6871d14658455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5b66357072515f9d41ae15ec886d24"
           "58363253c57db15e7aabdcec22fbd",
           "f6871d14678455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5b66357072515f9d45ee15ec886d24"
           "50310253c57db15e7aaa56eae07f7",
           "f6871d14698455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5a66357072515f9d48ee15ec886d24"
           "58358253c57db15e7aa016ec0977a",
           "f6871d146b8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5b66357072515f9d45ee15ec886d24"
           "50310253c57db15e7aab5ee641705",
           "f6871d146d8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5ae6357072515f9d452e15ec886d24"
           "503a8253c57db15e7aa892ec02fdf",
           "f6871d146f8455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5b66357072515f9d41ae15ec886d24"
           "50364253c57db15e7aa19ce8117ce",
           "f6871d14718455765edfeab5002cbc947bf8fc2f955a28"
           "bd9230f23bf6ffb5ae6357072515f9d4d6e15ec886d24"
           "583c3253c57db15e7aac1ce9a47d8")
_T8RT = ("d5586b46", "d55c6b46", "b8dfb04e", "155ab54e",
         "ce5f014f", "d6db246c", "015a716c", "51dfa16d",
         "ae59a66d", "fd5e158b", "6fdb158b", "9f5ddd8d",
         "c65c1f8f", "b15e238f", "22dd7dac", "5dde96ac")
_T8RB = ("b61a0364414ee68f2b", "ae5203a8e54eedd703",
         "b65e83100d0ea57f6a", "ae12032c3d0ef8b76b")
_T8RC = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00),
         (5, 0x04), (6, 0xf5), (7, 0x5a), (8, 0x42),
         (9, 0x7f), (10, 0xd8), (11, 0x41), (12, 0x03),
         (13, 0xb0), (14, 0xf0), (15, 0x52), (16, 0x7b),
         (17, 0xf8), (18, 0xfc), (19, 0x2f), (20, 0x95),
         (21, 0x5a), (22, 0x28), (23, 0xbd), (24, 0x92),
         (25, 0x30), (26, 0xf2), (27, 0x3b), (28, 0xf6),
         (29, 0xff), (30, 0xb5), (32, 0x63), (33, 0x57),
         (34, 0x07), (35, 0x25), (36, 0x15), (37, 0xf9),
         (38, 0xd4), (40, 0xe1), (41, 0x5e), (42, 0xc8),
         (43, 0x86), (44, 0xd2), (45, 0x45), (48, 0x25),
         (49, 0x3c), (50, 0x57), (51, 0xdb), (52, 0x15),
         (53, 0xe7), (54, 0xaa))
_T8S1T = ("429cf392bf2d", "4264f0147f35", "02d8f1445f36",
           "620cf3035f36", "620cf3075f36", "0278f2975f4b",
           "42ecf3c71f4c", "42ecf3cb1f4c", "2280f0469f4f",
           "2280f04a9f4f", "628cf01f1f61", "2200f24fff61",
           "2260f10e5f65", "2260f1125f65", "6294f2d15f65",
           "0200f0c61f7a")
_T8S1C = ((0, 0x14), (1, 0x00), (2, 0x00), (3, 0x00),
          (6, 0xf5), (7, 0x5a), (9, 0xf1), (10, 0x87),
          (11, 0x1d), (12, 0x03), (18, 0xcf), (19, 0xff),
          (20, 0x95), (21, 0x5a), (22, 0x28), (23, 0xbd),
          (24, 0x92), (25, 0x30), (26, 0xf2), (27, 0x3b),
          (28, 0xf6), (29, 0xff), (30, 0xb5), (31, 0xae),
          (32, 0x63), (33, 0x57), (34, 0x07), (35, 0x25),
          (36, 0x15), (37, 0xf9), (38, 0xd4), (39, 0xd6),
          (40, 0xe1), (41, 0x5e), (42, 0xc8), (43, 0x86),
          (44, 0xd2), (45, 0x45), (46, 0x83), (47, 0xc3),
          (48, 0x25), (49, 0x3c), (50, 0x57), (51, 0xdb),
          (52, 0x15), (53, 0xe7), (54, 0xaa), (55, 0xcd),
          (56, 0x4e), (57, 0x63), (58, 0xaf), (59, 0x8a))
_T8DIP346 = "fed7ba02f38655765edfeab5002cbc947bf8fc2f955a28" \
    "bd923072f277fc610776eceaa075211bb2c8a736dcd245035f2" \
    "53c57db15e7aa91eea81706"
_T8P0 = ("01000000f546e936fffe6b5d3bc0999900ba4e4961a5164a"
        "923072f277fc610776eceaa075211bb2c8a736dcd245035f2"
        "53c57db15e7aa91eea81706943c5890",
        "14000000f746e9361fe08c4c3bc09919e1ff6b5da5bb9a7b"
        "f608232777fc610776eceaa075211bb2c8a736dcd245035f2"
        "53c57db15e7aa91eea81706867c072e",
        "14000000f946e9361fe08c4c3bc09919c1ff6b5d37be6157"
        "1609232777fc610776eceaa075211bb2c8a736dcd245035f2"
        "53c57db15e7aa91eea81706867c072e")
_T8P1T = ("46c1bfb948f416", "46c161ba53f416", "46c13fbc45f516",
          "47c175bc4ffa16", "47e187bdb0a416", "47e129bebba416",
          "47e15fbec5a916", "47e1b1ba02d116", "47c11dbdeb4736",
          "47c1a1ba208036", "47c143bb2b8036", "47e1dfbaac4f36",
          "47e16fbcd2cd36", "47e13bbbcbf936")
_T8P1C = ((0, 0x14), (1, 0x00), (2, 0x00), (3, 0x00),
          (6, 0xe9), (7, 0x36), (8, 0x1f), (9, 0xe0),
          (10, 0x8c), (11, 0x4c), (12, 0x3b), (13, 0xc0),
          (14, 0x99), (15, 0x19), (17, 0xff), (18, 0x6b),
          (19, 0x5d), (25, 0x09), (26, 0x23), (27, 0x27),
          (28, 0x77), (29, 0xfc), (30, 0x61), (31, 0x07),
          (32, 0x76), (33, 0xec), (34, 0xea), (35, 0xa0),
          (36, 0x75), (37, 0x21), (38, 0x1b), (39, 0xb2),
          (40, 0xc8), (41, 0xa7), (42, 0x36), (43, 0xdc),
          (44, 0xd2), (45, 0x45), (46, 0x03), (47, 0x5f),
          (48, 0x25), (49, 0x3c), (50, 0x57), (51, 0xdb),
          (52, 0x15), (53, 0xe7), (54, 0xaa), (55, 0x91),
          (56, 0xee), (57, 0xa8), (58, 0x17), (59, 0x06),
          (60, 0x86), (61, 0x7c), (62, 0x07), (63, 0x2e))
_T8P2S = "010000001747e936dfff6b5d3bc0999900887c745cfecbb" \
    "d32ddbec317c7c24677fc610776eceaa075211bb2c8a736dcd" \
    "245035f253c57db15e7aa91eea81706"
_T8P2T = ("10de9c68d7c676", "dddc216bd7c676", "035d5baad7c676",
          "d05f1a3e977e87", "005ceb4c973345", "07dcd7ab977e87",
          "625ab517d7e15d", "7f5d77c3d7c676", "cadb1e6af7c676")
_T8P2C = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00),
          (5, 0x47), (6, 0xe9), (7, 0x36), (8, 0xdf),
          (9, 0xff), (10, 0x6b), (11, 0x5d), (12, 0x3b),
          (13, 0xc0), (14, 0x99), (15, 0x99), (16, 0x00),
          (17, 0x88), (18, 0x7c), (19, 0x74), (20, 0x5c),
          (21, 0xfe), (22, 0xcb), (23, 0xbd), (31, 0x46),
          (32, 0x77), (33, 0xfc), (34, 0x61), (35, 0x07),
          (36, 0x76), (37, 0xec), (38, 0xea), (39, 0xa0),
          (40, 0x75), (41, 0x21), (42, 0x1b), (43, 0xb2),
          (44, 0xc8), (45, 0xa7), (46, 0x36), (47, 0xdc),
          (48, 0xd2), (49, 0x45), (50, 0x03), (51, 0x5f),
          (52, 0x25), (53, 0x3c), (54, 0x57), (55, 0xdb),
          (56, 0x15), (57, 0xe7), (58, 0xaa), (59, 0x91),
          (60, 0xee), (61, 0xa8), (62, 0x17), (63, 0x06))
_T8P3S = "170000002b47e9361f80c8473bc099199c1f2e49f25fee" \
    "2dcd5a246af7c676565afe5febfd75755075211bb2c8a736dc" \
    "d245035f253c57db15e7aa91eea81706"
_T8P3T = ("c74849bde6fd75", "07f350ad36fe75", "1ff450ad36fe75",
          "377058ad26fe75", "af8e469d660276", "27ae4e1dc60376",
          "87dc5cbd460376", "ffb45e8d060376", "4fec524d860776",
          "17f052ddf60776", "579a5acd460876", "879e418db60976",
          "57a2412d260976", "073550bd760c76", "3fe0579dc60d76")
_T8P3C = ((0, 0x17), (1, 0x00), (2, 0x00), (3, 0x00),
          (5, 0x47), (6, 0xe9), (7, 0x36), (8, 0x1f),
          (9, 0x80), (10, 0xc8), (11, 0x47), (12, 0x3b),
          (13, 0xc0), (14, 0x99), (15, 0x19), (16, 0x9c),
          (20, 0xf2), (21, 0x5f), (22, 0xee), (24, 0xcd),
          (25, 0x5a), (26, 0x24), (27, 0x6a), (28, 0xf7),
          (29, 0xc6), (30, 0x76), (32, 0x5a), (33, 0xfe),
          (34, 0x5f), (35, 0xeb), (38, 0x75), (39, 0x50),
          (40, 0x75), (41, 0x21), (42, 0x1b), (43, 0xb2),
          (44, 0xc8), (45, 0xa7), (46, 0x36), (47, 0xdc),
          (48, 0xd2), (49, 0x45), (50, 0x03), (51, 0x5f),
          (52, 0x25), (53, 0x3c), (54, 0x57), (55, 0xdb),
          (56, 0x15), (57, 0xe7), (58, 0xaa), (59, 0x91),
          (60, 0xee), (61, 0xa8), (62, 0x17), (63, 0x06))
_T8P4T = ("1f2e492d56fd75", "c74849bde6fd75", "07f350ad36fe75",
          "1ff450ad36fe75", "377058ad26fe75", "af8e469d660276",
          "27ae4e1dc60376", "87dc5cbd460376", "ffb45e8d060376",
          "4fec524d860776", "17f052ddf60776", "579a5acd460876",
          "879e418db60976", "57a2412d260976", "073550bd760c76",
          "3fe0579dc60d76")
_T8P4B = ("84de2612172866", "b5dcda8c971f7f", "58de04d7d7e15d")
_T8P4C = ((0, 0x17), (1, 0x00), (2, 0x00), (3, 0x00),
          (5, 0x47), (6, 0xe9), (7, 0x36), (8, 0x1f),
          (9, 0x80), (10, 0xc8), (11, 0x47), (12, 0x3b),
          (13, 0xc0), (14, 0x99), (15, 0x19), (16, 0x9c),
          (20, 0xf2), (21, 0x5f), (22, 0xee), (32, 0x5a),
          (33, 0xfe), (34, 0x5f), (35, 0xeb), (38, 0x75),
          (39, 0x50), (40, 0x75), (41, 0x21), (42, 0x1b),
          (43, 0xb2), (44, 0xc8), (45, 0xa7), (46, 0x36),
          (47, 0xdc), (48, 0xd2), (49, 0x45), (50, 0x03),
          (51, 0x5f), (52, 0x25), (53, 0x3c), (54, 0x57),
          (55, 0xdb), (56, 0x15), (57, 0xe7), (58, 0xaa),
          (59, 0x91), (60, 0xee), (61, 0xa8), (62, 0x17),
          (63, 0x06))
_T8QT = ("23bf972c3992", "39bf9f2c3992", "d0fc878c9992",
          "babf9b72b992", "19bfd723d992", "d4fcbf4ed992",
          "03fc6f4fd992", "cbfc0b54d992", "75bf7f555993",
          "ccbf33655993", "e2bf3b655993", "a8bf27905993",
          "78bf4b367993", "45fcfb95d993", "f0fc779bd993",
          "7dfcf3aad993")
_T8QB = ("0f97d4b312babf", "63a4d4335fbabf", "8379d8b351dabf",
         "0f7ad8b351dabf", "1b38dc3351dabf", "5747d3334b5ac0",
         "1357d7330e7ac0", "436ede335a7ac0", "7f5adf33407ac0",
         "2776d93324fac0", "0b78d9b36ffac0", "2b4ddd33621ac1",
         "43cfd0b3453ac1", "2bd1d033113ac1", "831ad8b35b9ac1",
         "1ff0db334ebac1")
_T8QC = ((0, 0x43), (1, 0x01), (2, 0x00), (3, 0x00),
         (6, 0xe9), (7, 0x36), (8, 0x7f), (9, 0x07),
         (10, 0x38), (11, 0x33), (12, 0x00), (13, 0x88),
         (14, 0x7c), (15, 0x74), (16, 0x5c), (17, 0xbf),
         (18, 0x02), (19, 0xfa), (20, 0xf2), (21, 0x5f),
         (22, 0xee), (23, 0x5d), (24, 0xd7), (28, 0xa3),
         (29, 0x73), (34, 0xae), (35, 0x8e), (42, 0x4f),
         (43, 0x2d), (44, 0xe1), (45, 0x5e), (46, 0xc8),
         (47, 0x86), (48, 0xd2), (49, 0x45), (50, 0x03),
         (51, 0x5f), (52, 0x25), (53, 0x3c), (54, 0x57),
         (55, 0xdb), (56, 0x15), (57, 0xe7), (58, 0xaa),
         (59, 0x91), (60, 0xee), (61, 0xa8), (62, 0x17),
         (63, 0x06))
_T8DIP694 = "f37fad2bab49e9367f07383300887c745cfecbbd09dee" \
    "ce9d4b891c877fc610776eceaa075211bb2c8a736dcd245035" \
    "f253c57db15e7aa91eea81706"
_T8R0 = ("17000000ad49e9361f80c8473bc09919fc058e5bf25fee8"
        "d09deece9d4b8914a16a887c316bfffdefca9a963e15ec88"
        "6d245035f253c57db15e7aa91eea81706",
        "53010000af49e9367f07383300887c741cbcd9d3f25fee9"
        "df402c7d9c68d54c216a887537ffc93e3fca9a963acdc12"
        "54165d34f0253c57db15e7aa91eea81706")
_T8R1T = ("295bcb5516", "b05c409516", "c1df449516", "025eecc316",
          "7fdca4c516", "905fa9c516", "30ddfac516", "0a5c8af816",
          "5ad98af816", "a0dd2afa16", "ebda6d0636", "68da3b2936",
          "795d402936", "ccda663536", "575b096a36")
_T8R1C = ((0, 0x53), (1, 0x01), (2, 0x00), (3, 0x00),
          (5, 0x49), (6, 0xe9), (7, 0x36), (8, 0x7f),
          (9, 0x07), (10, 0x38), (11, 0x33), (12, 0x00),
          (13, 0x88), (14, 0x7c), (15, 0x74), (16, 0x1c),
          (17, 0xbc), (18, 0xd9), (19, 0xd3), (20, 0xf2),
          (21, 0x5f), (22, 0xee), (23, 0x9d), (24, 0xf4),
          (25, 0x02), (26, 0xc7), (27, 0xd9), (28, 0xc6),
          (29, 0x8d), (30, 0x54), (31, 0xc2), (32, 0x16),
          (33, 0xa8), (34, 0x87), (35, 0x53), (36, 0x7f),
          (37, 0xfc), (38, 0x93), (39, 0xe3), (40, 0xfc),
          (41, 0xa9), (42, 0xa9), (43, 0x63), (49, 0x5d),
          (50, 0x34), (51, 0xf0), (52, 0x25), (53, 0x3c),
          (54, 0x57), (55, 0xdb), (56, 0x15), (57, 0xe7),
          (58, 0xaa), (59, 0x91), (60, 0xee), (61, 0xa8),
          (62, 0x17), (63, 0x06))
_T8R2S = "0a000000cf49e9361f5fe0f83bc0999900887c745cfecbb" \
    "d09deece9d4b8914a16a8876373fce780d727d9548d5da9c57" \
    "61b8af4253c57db15e7aa91eea81706"
_T8R2T = ("c5de7b9076e65a", "29dd809276e65a", "e25e859276e65a",
          "515dcd3a96ea68", "29dcfa37963c3f", "235b8f22163b64",
          "ec5bba1216a051", "f7d966c576e65a", "a2dc8cd176e65a")
_T8R2C = ((0, 0x0a), (1, 0x00), (2, 0x00), (3, 0x00),
          (5, 0x49), (6, 0xe9), (7, 0x36), (8, 0x1f),
          (9, 0x5f), (10, 0xe0), (11, 0xf8), (12, 0x3b),
          (13, 0xc0), (14, 0x99), (15, 0x99), (16, 0x00),
          (17, 0x88), (18, 0x7c), (19, 0x74), (20, 0x5c),
          (21, 0xfe), (22, 0xcb), (23, 0xbd), (24, 0x09),
          (25, 0xde), (26, 0xec), (27, 0xe9), (28, 0xd4),
          (29, 0xb8), (30, 0x91), (31, 0x4a), (32, 0x16),
          (33, 0xa8), (34, 0x87), (35, 0x63), (36, 0x73),
          (37, 0xfc), (38, 0xe7), (39, 0x80), (40, 0xd7),
          (41, 0x27), (42, 0xd9), (43, 0x54), (51, 0xf4),
          (52, 0x25), (53, 0x3c), (54, 0x57), (55, 0xdb),
          (56, 0x15), (57, 0xe7), (58, 0xaa), (59, 0x91),
          (60, 0xee), (61, 0xa8), (62, 0x17), (63, 0x06))
_T8R3S = "b3000000e349e9367f07383300887c741cbcd9d3f25fee9" \
    "df402c76dc68d54c216a8872b73fce780d727d9f46f5f79a9f" \
    "68e5f4c233c581a796dae1aeea81706"
_T8R3T = ("496c3c301b796d", "49fffc5023796d", "49e47ca458d96d",
          "49557c5859d96d", "49a9fc81b0d96d", "49713c98b0d96d",
          "49963c02dbd96d", "49ec7c0811596e", "4965fcc311596e",
          "4935bce111596e", "49c87c021a596e", "49c3fcf73c596e",
          "4921fc0573b96e", "49847c437bb96e", "4a847c447bb96e")
_T8R3C = ((0, 0xb3), (1, 0x00), (2, 0x00), (3, 0x00),
          (6, 0xe9), (7, 0x36), (8, 0x7f), (9, 0x07),
          (10, 0x38), (11, 0x33), (12, 0x00), (13, 0x88),
          (14, 0x7c), (15, 0x74), (16, 0x1c), (17, 0xbc),
          (18, 0xd9), (19, 0xd3), (20, 0xf2), (21, 0x5f),
          (22, 0xee), (23, 0x9d), (24, 0xf4), (25, 0x02),
          (26, 0xc7), (27, 0x6d), (28, 0xc6), (29, 0x8d),
          (30, 0x54), (31, 0xc2), (32, 0x16), (33, 0xa8),
          (34, 0x87), (35, 0x2b), (36, 0x73), (37, 0xfc),
          (38, 0xe7), (39, 0x80), (40, 0xd7), (41, 0x27),
          (42, 0xd9), (43, 0xf4), (44, 0x6f), (45, 0x5f),
          (46, 0x79), (47, 0xa9), (48, 0xf6), (49, 0x8e),
          (50, 0x5f), (51, 0x4c), (58, 0xae), (59, 0x1a),
          (60, 0xee), (61, 0xa8), (62, 0x17), (63, 0x06))
_T8R4T = ("233c581a796d", "6c3c301b796d", "fffc5023796d",
          "e47ca458d96d", "557c5859d96d", "a9fc81b0d96d",
          "713c98b0d96d", "963c02dbd96d", "ec7c0811596e",
          "65fcc311596e", "35bce111596e", "c87c021a596e",
          "c3fcf73c596e", "21fc0573b96e", "847c437bb96e",
          "847c447bb96e")
_T8R4B = ("075b9b4516a051", "215d7ea9f68e5f", "eddbff8bf6014d")
_T8R4C = ((0, 0xb3), (1, 0x00), (2, 0x00), (3, 0x00),
          (5, 0x4a), (6, 0xe9), (7, 0x36), (8, 0x7f),
          (9, 0x07), (10, 0x38), (11, 0x33), (12, 0x00),
          (13, 0x88), (14, 0x7c), (15, 0x74), (16, 0x1c),
          (17, 0xbc), (18, 0xd9), (19, 0xd3), (20, 0xf2),
          (21, 0x5f), (22, 0xee), (23, 0x9d), (24, 0xf4),
          (25, 0x02), (26, 0xc7), (27, 0x6d), (28, 0xc6),
          (29, 0x8d), (30, 0x54), (31, 0xc2), (32, 0x16),
          (33, 0xa8), (34, 0x87), (35, 0x2b), (36, 0x73),
          (37, 0xfc), (38, 0xe7), (39, 0x80), (40, 0xd7),
          (41, 0x27), (42, 0xd9), (43, 0xf4), (51, 0x4c),
          (58, 0xae), (59, 0x1a), (60, 0xee), (61, 0xa8),
          (62, 0x17), (63, 0x06))
_T8ST = ("34d49aae8be753", "34d49acef9af54", "34d4da0e899f4f",
          "44349aced1ffea", "4434dace8a6f3a", "4434da4eb3d73a",
          "444c1aaee84f98", "44645a8ebe0750", "44645a6eaae75f",
          "44c45a8e7a57db", "44c45a8e6727e7", "44d4daee9c9f44",
          "44d4da6ec50745", "44d4da6e7e7794", "54341a0e907fce",
          "5434da6e6e27dc")
_T8SC = ((0, 0xd3), (1, 0x0a), (2, 0x00), (3, 0x00),
         (6, 0xe9), (7, 0x36), (8, 0x7f), (9, 0x07),
         (10, 0x38), (11, 0x33), (12, 0x00), (13, 0x88),
         (14, 0x7c), (15, 0x74), (16, 0x5c), (17, 0xfe),
         (18, 0xcb), (19, 0xbd), (20, 0x09), (21, 0xde),
         (22, 0xec), (23, 0xe9), (24, 0xd4), (25, 0xb8),
         (26, 0x91), (27, 0xc4), (28, 0x25), (29, 0x7c),
         (30, 0x81), (31, 0xe3), (32, 0x16), (33, 0xa8),
         (34, 0x87), (35, 0xfb), (36, 0x73), (37, 0xfc),
         (38, 0xe7), (39, 0x80), (40, 0xd7), (41, 0x27),
         (42, 0xd9), (44, 0xbc), (45, 0x5d), (46, 0xf1),
         (47, 0x01), (48, 0x96), (49, 0xe6), (50, 0x5a),
         (58, 0xae))
_T8T0 = ("01000000634ce9361f5fe0783bc0999900887c745cfecbb"
        "d09deece9d4b8914af63f076c403ddc1cd727d9844c5b58f1"
        "53925bbe253c57db15e7aa91eea81706",
        "73000000654ce9367f07383300887c741cbcd9d3f25fee9"
        "df402c7dbc68d54c216a887a373fce780d727d9944c5b58f1"
        "53925b694bbc5400b5e5423f6e767fb7",
        "74070000670c9c992300887c1cbcd9d3f25fee9df402c7d5"
        "c68d54c216a887eb73fce780d727d9544c5b58f153925b084"
        "bbc5400b5e5421bce9ab7c4cad8e400")
_T8T1T = ("6edc3401", "abdeb129", "6ddce22a", "58dee62a",
          "2e5e5248", "8bd85648", "405f9849", "06dcd349",
          "ecde0b67", "b25b4767", "895b7468", "d95e8968",
          "075f8d6f", "2fdf64a7", "8c5969a7")
_T8T1C = ((0, 0x74), (1, 0x07), (2, 0x00), (3, 0x00),
          (5, 0x0c), (6, 0x9c), (7, 0x99), (8, 0x23),
          (9, 0x00), (10, 0x88), (11, 0x7c), (12, 0x1c),
          (13, 0xbc), (14, 0xd9), (15, 0xd3), (16, 0xf2),
          (17, 0x5f), (18, 0xee), (19, 0x9d), (20, 0xf4),
          (21, 0x02), (22, 0xc7), (23, 0xd5), (24, 0xc6),
          (25, 0x8d), (26, 0x54), (27, 0xc2), (28, 0x16),
          (29, 0xa8), (30, 0x87), (31, 0xeb), (32, 0x73),
          (33, 0xfc), (34, 0xe7), (35, 0x80), (36, 0xd7),
          (37, 0x27), (38, 0xd9), (39, 0x54), (40, 0x4c),
          (41, 0x5b), (42, 0x58), (43, 0xf1), (44, 0x53),
          (45, 0x92), (46, 0x5b), (47, 0x08), (48, 0x4b),
          (49, 0xbc), (50, 0x54), (51, 0x00), (52, 0xb5),
          (53, 0xe5), (54, 0x42), (55, 0x1b), (56, 0xce),
          (57, 0x9a), (58, 0xb7), (59, 0xc4))
_T8T2S = "43000000878c04e5c3f1058e00887c745cfecbbd09deece" \
    "9d4b8914af63f070c403ddc1cd727d9c44c5b58f153925bda4" \
    "bbc5400b5e542072ef63fabc35a6189"
_T8T2T = ("ccb8b10a5eaf58", "4c1bace05f6791", "4c1bac4d5a32b7",
          "4c00bd3a597078", "ccc48aa0da6047", "4c5ab71adab580",
          "8ceda08c5d2ee0", "ccb8b1d3d92c7a", "4c1bacdadd0dd6")
_T8T2C = ((0, 0x43), (1, 0x00), (2, 0x00), (3, 0x00),
          (8, 0xc3), (9, 0xf1), (10, 0x05), (11, 0x8e),
          (12, 0x00), (13, 0x88), (14, 0x7c), (15, 0x74),
          (16, 0x5c), (17, 0xfe), (18, 0xcb), (19, 0xbd),
          (20, 0x09), (21, 0xde), (22, 0xec), (23, 0xe9),
          (24, 0xd4), (25, 0xb8), (26, 0x91), (27, 0x4a),
          (28, 0xf6), (29, 0x3f), (30, 0x07), (31, 0x0c),
          (32, 0x40), (33, 0x3d), (34, 0xdc), (35, 0x1c),
          (36, 0xd7), (37, 0x27), (38, 0xd9), (39, 0xc4),
          (40, 0x4c), (41, 0x5b), (42, 0x58), (43, 0xf1),
          (44, 0x53), (45, 0x92), (46, 0x5b), (47, 0xda),
          (48, 0x4b), (49, 0xbc), (50, 0x54), (51, 0x00),
          (52, 0xb5), (53, 0xe5), (54, 0x42), (55, 0x07),
          (56, 0x2e), (57, 0xf6), (58, 0x3f), (59, 0xab))
_T8T3S = "de0400009bccb8b1c300ebe5005fe03809deece9d4b8914" \
    "af63f070c403ddc1cd727d9c44c5b58f153925bda4bbc5400b5" \
    "e542072ef63fab7f598797d5bcb3e0"
_T8T3T = ("ee183c0021", "ee79fca027", "ee79fca127", "ee9e7c4043",
          "ee9e7c4143", "efbf3ce0ff", "f075bca68b", "f0d2bc3292",
          "f0f73cd1ad", "f051fcc2d0", "f2407c824f", "f27f7ca3f4",
          "f29b7cc0f4", "f3853cb51f", "f38ebc373b")
_T8T3C = ((0, 0xde), (1, 0x04), (2, 0x00), (3, 0x00),
          (5, 0xcc), (6, 0xb8), (7, 0xb1), (8, 0xc3),
          (9, 0x00), (11, 0xe5), (12, 0x00), (13, 0x5f),
          (14, 0xe0), (15, 0x38), (16, 0x09), (17, 0xde),
          (18, 0xec), (19, 0xe9), (20, 0xd4), (21, 0xb8),
          (22, 0x91), (23, 0x4a), (24, 0xf6), (25, 0x3f),
          (26, 0x07), (27, 0x0c), (28, 0x40), (29, 0x3d),
          (30, 0xdc), (31, 0x1c), (32, 0xd7), (33, 0x27),
          (34, 0xd9), (35, 0xc4), (36, 0x4c), (37, 0x5b),
          (38, 0x58), (39, 0xf1), (40, 0x53), (41, 0x92),
          (42, 0x5b), (43, 0xda), (44, 0x4b), (45, 0xbc),
          (46, 0x54), (47, 0x00), (48, 0xb5), (49, 0xe5),
          (50, 0x42), (51, 0x07), (52, 0x2e), (53, 0xf6),
          (54, 0x3f), (55, 0xab), (56, 0x7f), (57, 0x59),
          (58, 0x87), (59, 0x97))
_T8T4T = ("ebd5bcb3e0", "ee183c0021", "ee79fca027", "ee79fca127",
          "ee9e7c4043", "ee9e7c4143", "efbf3ce0ff", "f075bca68b",
          "f0d2bc3292", "f0f73cd1ad", "f051fcc2d0", "f2407c824f",
          "f27f7ca3f4", "f29b7cc0f4", "f3853cb51f", "f38ebc373b")
_T8T4B = ("cceda0565c5000", "ccb8b171de40b6", "0c5d9b99da2dbe")
_T8T4C = ((0, 0xde), (1, 0x04), (2, 0x00), (3, 0x00),
          (8, 0xc3), (9, 0x00), (11, 0xe5), (12, 0x00),
          (13, 0x5f), (14, 0xe0), (15, 0x38), (16, 0x09),
          (17, 0xde), (18, 0xec), (19, 0xe9), (20, 0xd4),
          (21, 0xb8), (22, 0x91), (23, 0x4a), (24, 0xf6),
          (25, 0x3f), (26, 0x07), (27, 0x0c), (28, 0x40),
          (29, 0x3d), (30, 0xdc), (31, 0x1c), (32, 0xd7),
          (33, 0x27), (34, 0xd9), (35, 0xc4), (36, 0x4c),
          (37, 0x5b), (38, 0x58), (39, 0xf1), (40, 0x53),
          (41, 0x92), (42, 0x5b), (43, 0xda), (44, 0x4b),
          (45, 0xbc), (46, 0x54), (47, 0x00), (48, 0xb5),
          (49, 0xe5), (50, 0x42), (51, 0x07), (52, 0x2e),
          (53, 0xf6), (54, 0x3f), (55, 0xab))
_T8UT = ("48c0e84b6766", "58e055fbc267", "580060abc367",
          "5900ed0b2267", "4260e91bf168", "42404fabf668",
          "45e0b18bb568", "53a0e07b4d69", "53c0ea2b4e69",
          "55e04dfbff69", "56a0e16b0e69", "5f80f34be269",
          "4120f61b056a", "46405c6bbb6b", "50a0587b8a6b",
          "50c0622b8b6b")
_T8UC = ((0, 0xde), (2, 0x00), (3, 0x00), (6, 0x1b),
         (7, 0xac), (8, 0xc3), (9, 0x00), (11, 0xe5),
         (16, 0x98), (17, 0x2f), (18, 0x70), (19, 0x1c),
         (21, 0xdc), (22, 0x48), (23, 0x25), (24, 0xf6),
         (25, 0x3f), (26, 0x07), (27, 0x0c), (28, 0x40),
         (29, 0x3d), (30, 0xdc), (31, 0x1c), (32, 0xd7),
         (33, 0x27), (34, 0xd9), (35, 0xc4), (36, 0x4c),
         (37, 0x5b), (38, 0x58), (39, 0xf1), (40, 0x53),
         (41, 0x92), (42, 0x5b), (43, 0xda), (44, 0x4b),
         (45, 0xbc), (46, 0x54), (47, 0x00), (48, 0xb5),
         (49, 0xe5), (50, 0x42), (51, 0x07), (52, 0x2e),
         (53, 0xf6), (54, 0x3f), (55, 0xab), (56, 0xa7),
         (57, 0xda), (58, 0x1b), (59, 0xda))
_T8V0 = ("080000001b4ff08c20bec07100887c745cfecbbd09dee"
        "ce9d4b8914af63f070c403ddc1cd727d9c44c5b58f153925"
        "bda4bbc5400b5e542072ef63fab26de0b7e",
        "030400001d4ff08c00209c171de179c0fede2bf91abec07"
        "1c6df6397f63f070c403ddc1cd727d9c44c5b58f153925bd"
        "a4bbc5400b5e542072ef63fab26de0b7e",
        "034000001f4ff08c00209c171de179c0b0df2bf9daf87b6"
        "c37bc80233a807ab873fce780d727d9c44c5b58f153925bd"
        "a4bbc5400b5e542072ef63fab26de0b7e")
_T8V1T = ("93bc36d09a80", "997c3618ba80", "63fc7145ba80",
          "48fcc382da80", "dd3c61f73a81", "3b3ca02f5a81",
          "2c7ca41afa81", "2c7ca51afa81", "b2fca05b1a82",
          "77bc03931a82", "0c3ca1079a82", "6ffcb0359a82",
          "54fc0273ba82", "5abc02bbba82", "b87c41f3ba82")
_T8V1C = ((0, 0x03), (1, 0x40), (2, 0x00), (3, 0x00),
          (5, 0x4f), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0xb0),
          (17, 0xdf), (18, 0x2b), (19, 0xf9), (20, 0xda),
          (21, 0xf8), (22, 0x7b), (23, 0x6c), (30, 0x7a),
          (31, 0xb8), (32, 0x73), (33, 0xfc), (34, 0xe7),
          (35, 0x80), (36, 0xd7), (37, 0x27), (38, 0xd9),
          (39, 0xc4), (40, 0x4c), (41, 0x5b), (42, 0x58),
          (43, 0xf1), (44, 0x53), (45, 0x92), (46, 0x5b),
          (47, 0xda), (48, 0x4b), (49, 0xbc), (50, 0x54),
          (51, 0x00), (52, 0xb5), (53, 0xe5), (54, 0x42),
          (55, 0x07), (56, 0x2e), (57, 0xf6), (58, 0x3f),
          (59, 0xab), (60, 0x26), (61, 0xde), (62, 0x0b),
          (63, 0x7e))
_T8V2S = "030400003f4ff08c00209c171de179c0795eeeedf55fde0" \
    "4561c1b827be49f2273fce780d727d9c44c5b58f153925bda4" \
    "bbc5400b5e542072ef63fab26de0b7e"
_T8V2T = ("602e055b92dbd1a71e", "5c7f04db92dba1381e",
          "cf82047b98dba1381e", "8aec06db9bbb33871f",
          "11fb073b8f9b82a41b", "9f56075b869b56171f",
          "0d6b071b8abb445b1d", "0adc075b9c9bd2a71e",
          "133a04db967ba2381e")
_T8V2C = ((0, 0x03), (1, 0x04), (2, 0x00), (3, 0x00),
          (5, 0x4f), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xf5),
          (24, 0x56), (25, 0x1c), (32, 0x73), (33, 0xfc),
          (34, 0xe7), (35, 0x80), (36, 0xd7), (37, 0x27),
          (38, 0xd9), (39, 0xc4), (40, 0x4c), (41, 0x5b),
          (42, 0x58), (43, 0xf1), (44, 0x53), (45, 0x92),
          (46, 0x5b), (47, 0xda), (48, 0x4b), (49, 0xbc),
          (50, 0x54), (51, 0x00), (52, 0xb5), (53, 0xe5),
          (54, 0x42), (55, 0x07), (56, 0x2e), (57, 0xf6),
          (58, 0x3f), (59, 0xab), (60, 0x26), (61, 0xde),
          (62, 0x0b), (63, 0x7e))
_T8V3S = "03400000534ff08c00209c171de179c0795eeeedd58a637" \
    "3b6bc06d63bd3a71e0dfc9b55db74924d4c5b58f153925bda4" \
    "bbc5400b5e542072ef63fab26de0b7e"
_T8V3T = ("d3bf8780db74", "32bfc331fb74", "23bfeb403b76",
          "39bff3403b76", "06fca3a09b76", "cefc3fa59b76",
          "c7fc27a69b76", "4abf33eadb77", "60bf3beadb77",
          "b4fc739bfb77", "c7fc47f05b78", "54fcc3ff5b78",
          "93bf570abb79", "59bf4335bb79", "21fcdf39bb79")
_T8V3C = ((0, 0x03), (1, 0x40), (2, 0x00), (3, 0x00),
          (5, 0x4f), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xd5),
          (21, 0x8a), (22, 0x63), (23, 0x73), (24, 0xb6),
          (25, 0xbc), (26, 0x06), (27, 0xd6), (28, 0x3b),
          (29, 0xd3), (30, 0xa7), (31, 0x1e), (38, 0x92),
          (39, 0x4d), (40, 0x4c), (41, 0x5b), (42, 0x58),
          (43, 0xf1), (44, 0x53), (45, 0x92), (46, 0x5b),
          (47, 0xda), (48, 0x4b), (49, 0xbc), (50, 0x54),
          (51, 0x00), (52, 0xb5), (53, 0xe5), (54, 0x42),
          (55, 0x07), (56, 0x2e), (57, 0xf6), (58, 0x3f),
          (59, 0xab), (60, 0x26), (61, 0xde), (62, 0x0b),
          (63, 0x7e))
_T8V4T = ("0dfc9b55db74", "d3bf8780db74", "32bfc331fb74",
          "23bfeb403b76", "39bff3403b76", "06fca3a09b76",
          "cefc3fa59b76", "c7fc27a69b76", "4abf33eadb77",
          "60bf3beadb77", "b4fc739bfb77", "c7fc47f05b78",
          "54fcc3ff5b78", "93bf570abb79", "59bf4335bb79",
          "21fcdf39bb79")
_T8V4B = ("eb3c2253fb445b1d", "dffc07d63bd3a71e",
          "5b7cf3e09b15ed1c")
_T8V4C = ((0, 0x03), (1, 0x40), (2, 0x00), (3, 0x00),
          (5, 0x4f), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xd5),
          (21, 0x8a), (22, 0x63), (23, 0x73), (38, 0x92),
          (39, 0x4d), (40, 0x4c), (41, 0x5b), (42, 0x58),
          (43, 0xf1), (44, 0x53), (45, 0x92), (46, 0x5b),
          (47, 0xda), (48, 0x4b), (49, 0xbc), (50, 0x54),
          (51, 0x00), (52, 0xb5), (53, 0xe5), (54, 0x42),
          (55, 0x07), (56, 0x2e), (57, 0xf6), (58, 0x3f),
          (59, 0xab), (60, 0x26), (61, 0xde), (62, 0x0b),
          (63, 0x7e))
_T8WT = ("0cdd8cc5b724", "5f5ab3d1b724", "eada5506d724",
          "44dbdba4d724", "fd5dc6d9d724", "8b5b83dbd724",
          "9cde87dbd724", "ef5baee7d724", "6c5b7c0af724",
          "7f59d7bcf724", "90dcdbbcf724", "d15a83ebf724",
          "e2dd87ebf724", "9edd8cedf724", "ffd991edf724",
          "835eb5c01725")
_T8WC = ((0, 0x83), (1, 0x03), (2, 0x04), (3, 0x00),
         (6, 0xf0), (7, 0x8c), (8, 0x00), (9, 0x20),
         (10, 0x9c), (11, 0x17), (12, 0x1d), (13, 0xe1),
         (14, 0x79), (15, 0xc0), (16, 0x79), (17, 0x5e),
         (18, 0xee), (19, 0xed), (20, 0xd5), (21, 0x8a),
         (22, 0x63), (23, 0x37), (24, 0x80), (25, 0xbc),
         (26, 0x56), (27, 0xf8), (28, 0x9b), (29, 0xa2),
         (30, 0x38), (31, 0x1e), (38, 0x92), (39, 0x4d),
         (46, 0xb9), (47, 0xa5), (48, 0x4b), (49, 0xbc),
         (50, 0x54), (51, 0x00), (52, 0xb5), (53, 0xe5),
         (54, 0x42), (55, 0x07), (56, 0x2e), (57, 0xf6),
         (58, 0x3f), (59, 0xab), (60, 0x26), (61, 0xde),
         (62, 0x0b), (63, 0x7e))
_T8X0 = ("43000000d351f08c00209c17dd6f5e0608cf0346795eee"
        "edd58a633b77751b1d73fce780d727d9c44c5b58f153925b"
        "da4bbc5400b5e542072ef63fab26de0b7e",
        "03100000d551f08c00209c171de179c0795eeeedd58a631f"
        "8efce66577751b3d08fc4f4f9750426a495a703379be63be"
        "4bbc5400b5e542072ef63fab26de0b7e",
        "83000100d751f08c00209c171de179c0795eeeedd58a63cf"
        "8efce66577751b6d08fc4f4f9750428af95a703379be633e"
        "b53ce80899592e742ef63fab26de0b7e")
_T8X1T = ("eabcb5e59959", "01bc823cf959", "1e3ce566f959",
          "5fbcb567f959", "ea7ce56af959", "413c204f195a",
          "507ce5a5595a", "1bbcf7c8595a", "f7fc5300795a",
          "81bc9622795a", "3e3c97df795a", "727cc560d95a",
          "287c93bf395b", "69fc63c0395b", "16fc00cb395b")
_T8X1C = ((0, 0x83), (1, 0x00), (2, 0x01), (3, 0x00),
          (5, 0x51), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xd5),
          (21, 0x8a), (22, 0x63), (23, 0xcf), (24, 0x8e),
          (25, 0xfc), (26, 0xe6), (27, 0x65), (28, 0x77),
          (29, 0x75), (30, 0x1b), (31, 0x6d), (32, 0x08),
          (33, 0xfc), (34, 0x4f), (35, 0x4f), (36, 0x97),
          (37, 0x50), (38, 0x42), (39, 0x8a), (40, 0xf9),
          (41, 0x5a), (42, 0x70), (43, 0x33), (44, 0x79),
          (45, 0xbe), (46, 0x63), (47, 0x3e), (54, 0x2e),
          (55, 0x74), (56, 0x2e), (57, 0xf6), (58, 0x3f),
          (59, 0xab), (60, 0x26), (61, 0xde), (62, 0x0b),
          (63, 0x7e))
_T8X2S = "03100000f751f08c00209c171de179c0795eeeedd58a631" \
    "f8efce66577751b3d08fc4f4f9750426aacdadb2e5446cc81ca" \
    "bc14b19ac1e3b92ef63fab26de0b7e"
_T8X2T = ("51ea7ce325bad54fb7", "518cbc15805aa207b7",
          "518fbcd0805aa207b7", "51a77c63733a4098b7",
          "5208bca03ada145bb5", "52287c87ec7a4098b7",
          "525f7c184f7ae977b6", "526ffc25871ad64fb7",
          "52057c27cebaaabfb6")
_T8X2C = ((0, 0x03), (1, 0x10), (2, 0x00), (3, 0x00),
          (6, 0xf0), (7, 0x8c), (8, 0x00), (9, 0x20),
          (10, 0x9c), (11, 0x17), (12, 0x1d), (13, 0xe1),
          (14, 0x79), (15, 0xc0), (16, 0x79), (17, 0x5e),
          (18, 0xee), (19, 0xed), (20, 0xd5), (21, 0x8a),
          (22, 0x63), (23, 0x1f), (24, 0x8e), (25, 0xfc),
          (26, 0xe6), (27, 0x65), (28, 0x77), (29, 0x75),
          (30, 0x1b), (31, 0x3d), (32, 0x08), (33, 0xfc),
          (34, 0x4f), (35, 0x4f), (36, 0x97), (37, 0x50),
          (38, 0x42), (39, 0x6a), (40, 0xac), (41, 0xda),
          (42, 0xdb), (43, 0x2e), (44, 0x54), (45, 0x46),
          (46, 0xcc), (47, 0x81), (56, 0x2e), (57, 0xf6),
          (58, 0x3f), (59, 0xab), (60, 0x26), (61, 0xde),
          (62, 0x0b), (63, 0x7e))
_T8X3S = "830001000b52f08c00209c171de179c0795eeeedd58a63c" \
    "f8efce66577751b6d08fc4f4f9750424aacdadb2e5446ccbd5f" \
    "bc82be1ad64fb74ec107ec26de0b7e"
_T8X3T = ("4ac7b7aef67f49", "4af7376e87d7d5", "4af7b76ef91fd1",
          "5a79378ee35f16", "5a7937ee6ecf16", "5a79374eb24726",
          "5a83376e66a72f", "5a83378ebc0f7f", "6a03b7ee7ccf6f",
          "6a3337ceaa1ffc", "6a3337ce7beffc", "6a33b74e8cf74b",
          "6a33b76efabf4c", "6ab537ceba7f3d", "6abdb72ef0f79a")
_T8X3C = ((0, 0x83), (1, 0x00), (2, 0x01), (3, 0x00),
          (5, 0x52), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xd5),
          (21, 0x8a), (22, 0x63), (23, 0xcf), (24, 0x8e),
          (25, 0xfc), (26, 0xe6), (27, 0x65), (28, 0x77),
          (29, 0x75), (30, 0x1b), (31, 0x6d), (32, 0x08),
          (33, 0xfc), (34, 0x4f), (35, 0x4f), (36, 0x97),
          (37, 0x50), (38, 0x42), (40, 0xac), (41, 0xda),
          (42, 0xdb), (43, 0x2e), (44, 0x54), (45, 0x46),
          (46, 0xcc), (48, 0x5f), (49, 0xbc), (50, 0x82),
          (51, 0xbe), (52, 0x1a), (53, 0xd6), (54, 0x4f),
          (60, 0x26), (61, 0xde), (62, 0x0b), (63, 0x7e))
_T8X4T = ("4abdb64ec107ec", "4ac7b6aef67f49", "4af7366e87d7d5",
          "4af7b66ef91fd1", "5a79368ee35f16", "5a7936ee6ecf16",
          "5a79364eb24726", "5a83366e66a72f", "5a83368ebc0f7f",
          "6a03b6ee7ccf6f", "6a3336ceaa1ffc", "6a3336ce7beffc",
          "6a33b64e8cf74b", "6a33b66efabf4c", "6ab536ceba7f3d",
          "6abdb62ef0f79a")
_T8X4B = ("78fc70a7dae9", "893c55c57ad6", "58fcb49aba60")
_T8X4C = ((0, 0x83), (1, 0x00), (2, 0x01), (3, 0x00),
          (5, 0x52), (6, 0xf0), (7, 0x8c), (8, 0x00),
          (9, 0x20), (10, 0x9c), (11, 0x17), (12, 0x1d),
          (13, 0xe1), (14, 0x79), (15, 0xc0), (16, 0x79),
          (17, 0x5e), (18, 0xee), (19, 0xed), (20, 0xd5),
          (21, 0x8a), (22, 0x63), (23, 0xcf), (24, 0x8e),
          (25, 0xfc), (26, 0xe6), (27, 0x65), (28, 0x77),
          (29, 0x75), (30, 0x1b), (31, 0x6d), (32, 0x08),
          (33, 0xfc), (34, 0x4f), (35, 0x4f), (36, 0x97),
          (37, 0x50), (38, 0x42), (40, 0xac), (41, 0xda),
          (42, 0xdb), (43, 0x2e), (44, 0x54), (45, 0x46),
          (46, 0xcc), (60, 0x26), (61, 0xde), (62, 0x0b),
          (63, 0x7e))
_T8YT = ("64dd80b8", "945f48bb", "5adc83bb", "40dfbbd8",
          "065cf7d8", "2d5b39da", "98df4f40", "0a5c5040",
          "cbd9bf5d", "1b5ff05e", "2659677f", "1edea887",
          "b8dcbfe6", "795a2f04", "795e2f04", "a05d7105")
_T8YB = ("4abdb74ec107ec", "4ac7b7aef67f49", "4af7376e87d7d5",
         "4af7b76ef91fd1", "5a79378ee35f16", "5a7937ee6ecf16",
         "5a79374eb24726", "5a83376e66a72f", "5a83378ebc0f7f",
         "6a03b7ee7ccf6f", "6a3337ceaa1ffc", "6a3337ce7beffc",
         "6a33b74e8cf74b", "6a33b76efabf4c", "6ab537ceba7f3d",
         "6abdb72ef0f79a")
_T8YC = ((0, 0x31), (1, 0x08), (2, 0x10), (3, 0x00),
         (6, 0x05), (7, 0xcf), (8, 0x04), (9, 0x01),
         (10, 0xc2), (11, 0x79), (12, 0x1d), (13, 0xe1),
         (14, 0x79), (15, 0xc0), (16, 0x79), (17, 0x5e),
         (18, 0xee), (19, 0xed), (20, 0xd5), (21, 0x8a),
         (22, 0x63), (23, 0xcf), (24, 0x8e), (25, 0xfc),
         (26, 0xe6), (27, 0x65), (28, 0x77), (29, 0x75),
         (30, 0x1b), (31, 0x6d), (32, 0x08), (33, 0xfc),
         (34, 0x4f), (35, 0x4f), (36, 0x97), (37, 0x50),
         (38, 0x42), (40, 0xac), (41, 0xda), (42, 0xdb),
         (43, 0x2e), (44, 0x54), (45, 0x46), (46, 0xcc),
         (48, 0x49), (49, 0xbc), (50, 0xd1), (51, 0xc7),
         (52, 0xda), (53, 0xa2), (54, 0x07))
_T8Z0 = {10821: "630200008b54f08c00209c17fd79b9b708cf0326f59b9701561cdb9177751bed08fc4f4f9750426aacdadb2e5446ccd1363cf84c1728ec112ef63fab26de0b7e",
          10822: "8b7101008dd41f00470210cefd79b9b708cf0326f59b9701561cdb9177751bfd08fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f443f5bb20b",
          10823: "03b617008fd41f004702d0cd419e977bf59b9701561cdb9177751bfd08fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f44ed5bb20b79bc7121",
          10839: "eebd0000af54343902805650619e977bf59b9701561cdb9177751bfd08fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae95fc85c5",
          10849: "e7160a00c35434390200085a21c41707b9ac38368efce66577751bfd08fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae1bfc2447"}
_T8Z1T = ("e0cd75fc72c2", "e0cdc2bc22c3", "f0cd91fc4670", "f0cdadfc6370",
           "f0cdfabc1371", "10ce1bbcb22d", "10ce1bbcb32d", "10ce5abcd4d2",
           "10ce76bcf1d2", "40ce773c7722", "40cea97c5760", "40ce06bce366",
           "50cebd7cb5fa", "60ce277c8323", "60ce743c3324")
_T8Z1C = ((0, 0x03), (1, 0xb6), (2, 0x17), (3, 0x00), (5, 0xd4),
          (6, 0x1f), (7, 0x00), (8, 0x47), (9, 0x02), (12, 0x41),
          (13, 0x9e), (14, 0x97), (15, 0x7b), (16, 0xf5), (17, 0x9b),
          (18, 0x97), (19, 0x01), (20, 0x56), (21, 0x1c), (22, 0xdb),
          (23, 0x91), (24, 0x77), (25, 0x75), (26, 0x1b), (27, 0xfd),
          (28, 0x08), (29, 0xfc), (30, 0x4f), (31, 0x4f), (32, 0x97),
          (33, 0x50), (34, 0x42), (35, 0xca), (36, 0xac), (37, 0xda),
          (38, 0xdb), (39, 0x2e), (40, 0x54), (41, 0x46), (42, 0xcc),
          (43, 0x27), (44, 0x36), (45, 0x3c), (46, 0xf8), (47, 0x4c),
          (48, 0x17), (49, 0x28), (50, 0xec), (51, 0x21), (52, 0x4e),
          (53, 0x64), (54, 0x6f), (55, 0x44), (56, 0xed), (57, 0x5b),
          (58, 0xb2), (59, 0x0b))
_T8Z2T = ("e780055a18fcc095", "e500bed40dbc6819", "e6001697033c081c",
           "e880931de27cb65d", "e1006153207cb5fe", "e880931d9e7c3387",
           "e5800813337cc065", "e6801697f6bc57d9", "e500bfd4bf7ca5a4")
_T8Z2C = ((1, 0xbd), (2, 0x00), (3, 0x00), (5, 0x54), (6, 0x34),
          (7, 0x39), (8, 0x02), (12, 0x61), (13, 0x9e), (14, 0x97),
          (15, 0x7b), (16, 0xf5), (17, 0x9b), (18, 0x97), (19, 0x01),
          (20, 0x56), (21, 0x1c), (22, 0xdb), (23, 0x91), (24, 0x77),
          (25, 0x75), (26, 0x1b), (27, 0xfd), (28, 0x08), (29, 0xfc),
          (30, 0x4f), (31, 0x4f), (32, 0x97), (33, 0x50), (34, 0x42),
          (35, 0xca), (36, 0xac), (37, 0xda), (38, 0xdb), (39, 0x2e),
          (40, 0x54), (41, 0x46), (42, 0xcc), (43, 0x27), (44, 0x36),
          (45, 0x3c), (46, 0xf8), (47, 0x4c), (48, 0x17), (49, 0x28),
          (50, 0xec), (51, 0x21), (52, 0x4e), (53, 0x64), (54, 0x6f),
          (55, 0x44), (56, 0x92), (57, 0xdc), (58, 0xe3), (59, 0xae))
_T8Z3T = ("e716a16af7c3b9ac", "e716e17e57c5b9ac", "671a219d7710b9ac",
           "e70161b5d712d9ac", "671aa1aa77fd39ad", "671d2184977c39ad",
           "670ae182b72379ad", "670a2197172579ad", "e70c2149578779ad",
           "e70c21fd56a479ad", "e70fe1d6b62bf9ad", "e70f61fe9748f9ad",
           "e70f219f164af9ad", "671aa121977af9ad", "e71f616117e719ae")
_T8Z3C = ((2, 0x0a), (3, 0x00), (5, 0x54), (6, 0x34), (7, 0x39),
          (8, 0x02), (9, 0x00), (10, 0x08), (11, 0x5a), (18, 0x38),
          (19, 0x36), (20, 0x8e), (21, 0xfc), (22, 0xe6), (23, 0x65),
          (24, 0x77), (25, 0x75), (26, 0x1b), (27, 0xfd), (28, 0x08),
          (29, 0xfc), (30, 0x4f), (31, 0x4f), (32, 0x97), (33, 0x50),
          (34, 0x42), (35, 0xca), (36, 0xac), (37, 0xda), (38, 0xdb),
          (39, 0x2e), (40, 0x54), (41, 0x46), (42, 0xcc), (43, 0x27),
          (44, 0x36), (45, 0x3c), (46, 0xf8), (47, 0x4c), (48, 0x17),
          (49, 0x28), (50, 0xec), (51, 0x21), (52, 0x4e), (53, 0x64),
          (54, 0x6f), (55, 0x44), (56, 0x92), (57, 0xdc), (58, 0xe3),
          (59, 0xae), (60, 0x1b), (61, 0xfc), (62, 0x24), (63, 0x47))
_T8Z4T = ("e41621c41707b9ac", "e416a16af7c3b9ac", "e416e17e57c5b9ac",
           "641a219d7710b9ac", "e40161b5d712d9ac", "641aa1aa77fd39ad",
           "641d2184977c39ad", "640ae182b72379ad", "640a2197172579ad",
           "e40c2149578779ad", "e40c21fd56a479ad", "e40fe1d6b62bf9ad",
           "e40f61fe9748f9ad", "e40f219f164af9ad", "641aa121977af9ad",
           "e41f616117e719ae", "e71621c41707b9ac", "e716a16af7c3b9ac",
           "e716e17e57c5b9ac", "671a219d7710b9ac", "e70161b5d712d9ac",
           "671aa1aa77fd39ad", "671d2184977c39ad", "670ae182b72379ad",
           "670a2197172579ad", "e70c2149578779ad", "e70c21fd56a479ad",
           "e70fe1d6b62bf9ad", "e70f61fe9748f9ad", "e70f219f164af9ad",
           "671aa121977af9ad", "e71f616117e719ae", "e41621c41707b9ac",
           "e416a16af7c3b9ac", "e416e17e57c5b9ac", "641a219d7710b9ac",
           "e40161b5d712d9ac", "641aa1aa77fd39ad", "641d2184977c39ad",
           "640ae182b72379ad", "640a2197172579ad", "e40c2149578779ad",
           "e40c21fd56a479ad", "e40fe1d6b62bf9ad", "e40f61fe9748f9ad",
           "e40f219f164af9ad", "641aa121977af9ad", "e41f616117e719ae")
_T8Z4B = ("80e6511a7cd347", "00085a42bcc362", "80e651617c584e")
_T8Z4C = ((2, 0x0a), (3, 0x00), (6, 0x34), (7, 0x39), (8, 0x02),
          (18, 0x38), (19, 0x36), (20, 0x8e), (21, 0xfc), (22, 0xe6),
          (23, 0x65), (24, 0x77), (25, 0x75), (26, 0x1b), (27, 0xfd),
          (28, 0x08), (29, 0xfc), (30, 0x4f), (31, 0x4f), (32, 0x97),
          (33, 0x50), (34, 0x42), (35, 0xca), (36, 0xac), (37, 0xda),
          (38, 0xdb), (39, 0x2e), (40, 0x54), (41, 0x46), (42, 0xcc),
          (43, 0x27), (44, 0x36), (45, 0x3c), (46, 0xf8), (47, 0x4c),
          (48, 0x17), (49, 0x28), (50, 0xec), (51, 0x21), (52, 0x4e),
          (53, 0x64), (54, 0x6f), (55, 0x44), (56, 0x92), (57, 0xdc),
          (58, 0xe3), (59, 0xae))
_T8A1T = ("373c513d9b45", "d07c263e9b45", "2e7c65769b45", "7ffcb3a8bb45",
           "78bc85965b46", "363cd41cbb47", "80bcd0cd3b48", "a23c33e5db48",
           "cdfc54f0db48", "06fc7165fb48", "36bc6466fb48", "84fca0a31b49",
           "31bc81437b4b", "fcfce2c27b4b", "e6fc05f69b4b", "e6fc06f69b4b")
_T8A1B = ("e57621c41707b9ac", "e576a16af7c3b9ac",
           "e576e17e57c5b9ac", "657a219d7710b9ac",
           "e56161b5d712d9ac", "657aa1aa77fd39ad",
           "657d2184977c39ad", "656ae182b72379ad",
           "656a2197172579ad", "e56c2149578779ad",
           "e56c21fd56a479ad", "e56fe1d6b62bf9ad",
           "e56f61fe9748f9ad", "e56f219f164af9ad",
           "657aa121977af9ad", "e57f616117e719ae")
_T8A1C = ((2, 0xa0), (3, 0x00), (6, 0x34), (7, 0x39), (8, 0x02),
          (9, 0x00), (10, 0xc0), (11, 0xd4),
          (18, 0x38), (19, 0xf6), (26, 0xb7), (27, 0xd1), (28, 0x08),
          (29, 0xfc), (30, 0x4f), (31, 0x4f), (32, 0x97), (33, 0x50),
          (34, 0x42), (35, 0xca), (36, 0xac), (37, 0xda), (38, 0xdb),
          (39, 0x2e), (40, 0x54), (41, 0x46), (42, 0xcc), (43, 0x27),
          (44, 0x36), (45, 0x3c), (46, 0xf8), (47, 0x4c), (48, 0x17),
          (49, 0x28), (50, 0xec), (51, 0x21), (52, 0x4e), (53, 0x64),
          (54, 0x6f), (55, 0x44), (56, 0x92), (57, 0xdc), (58, 0xe3),
          (59, 0xae), (60, 0x33), (61, 0x3c), (62, 0x13), (63, 0xed))
_T8B10 = {11169: "8a150000435734390280035e5e0d567a795eeeedf59b9701561cdb9177751bfd08fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae",
          11170: "8a0d1400455734390280035e5e0d567abe5d3c90962329d190bcb7fbde2ad9e408fc4f4f975042caacdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae",
          11171: "8afd4001475734390280035e5e0d567abe5d3c9096232911aa3ca15f3e58a2d413fc570d3b1925a4acdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae",
          11187: "8a0d1400675734390280035e5e0d567abe5d3c90962329f1077c7045199f470d90bf53dd3cadeab5acdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae",
          11197: "8afd40017b5734390280035e5e0d567abe5d3c9096232909077c7045199f470d6bfcdf0f5ce4fcabbf597025d863c47c363cf84c1728ec214e646f4492dce3ae"}
_T8B1AT = ("f4bf9b123b19", "f6fc0f6d9b19", "07fddf22bb19", "5dfc3faabb1a",
           "44fcd731fb1a", "91bf4bf57b1c", "70fc5bdb9b1c", "86fc63db9b1c",
           "95bf83b7bb1c", "62fc33173b1d", "41fc1f8f3b1e", "69fc63267b1e",
           "7ffc6b267b1e", "52bf0b2b7b1e", "a4bf93029b1e")
_T8B1AC = ((0, 0x8a), (1, 0xfd), (2, 0x40), (3, 0x01), (5, 0x57),
          (6, 0x34), (7, 0x39), (8, 0x02), (9, 0x80), (10, 0x03),
          (11, 0x5e), (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a),
          (16, 0xbe), (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96),
          (21, 0x23), (22, 0x29), (23, 0x11), (24, 0xaa), (25, 0x3c),
          (26, 0xa1), (27, 0x5f), (28, 0x3e), (29, 0x58), (30, 0xa2),
          (31, 0xd4), (38, 0x25), (39, 0xa4), (40, 0xac), (41, 0xda),
          (42, 0xdb), (43, 0x2e), (44, 0x54), (45, 0x46), (46, 0xcc),
          (47, 0x27), (48, 0x36), (49, 0x3c), (50, 0xf8), (51, 0x4c),
          (52, 0x17), (53, 0x28), (54, 0xec), (55, 0x21), (56, 0x4e),
          (57, 0x64), (58, 0x6f), (59, 0x44), (60, 0x92), (61, 0xdc),
          (62, 0xe3), (63, 0xae))
_T8B1BT = ("7bbf07c81cf5e6aa", "85bf5339dce7d1a9", "20bfff39dce7d1a9",
           "44bf677b3cb513ad", "79bf0b3b5cd156a2", "fcbf53a63cb513ad",
           "d3bf879b9c6baaa7", "4dfcb708bcf5e6aa", "babfaba3fcb9bda8")
_T8B1BC = ((0, 0x8a), (1, 0x0d), (2, 0x14), (3, 0x00), (5, 0x57),
          (6, 0x34), (7, 0x39), (8, 0x02), (9, 0x80), (10, 0x03),
          (11, 0x5e), (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a),
          (16, 0xbe), (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96),
          (21, 0x23), (22, 0x29), (23, 0xf1), (24, 0x07), (25, 0x7c),
          (26, 0x70), (27, 0x45), (28, 0x19), (29, 0x9f), (30, 0x47),
          (31, 0x0d), (40, 0xac), (41, 0xda), (42, 0xdb), (43, 0x2e),
          (44, 0x54), (45, 0x46), (46, 0xcc), (47, 0x27), (48, 0x36),
          (49, 0x3c), (50, 0xf8), (51, 0x4c), (52, 0x17), (53, 0x28),
          (54, 0xec), (55, 0x21), (56, 0x4e), (57, 0x64), (58, 0x6f),
          (59, 0x44), (60, 0x92), (61, 0xdc), (62, 0xe3), (63, 0xae))
_T8B1QT = ("d559264cd863", "a2dc61431864", "edd9a44f1864", "97da2a741864",
           "465db5243864", "96dab5243864", "7f5f79533864", "05de93407864",
           "3f5cd24c7864", "c3daf3707864", "d45df8707864", "0edc367d7864",
           "74dcf398b864", "855ff898b864", "595d1c6cd864", "bf597025d863")
_T8B1QB = ("6bfcdf0f5ce4fcab", "c4fcdf3fbcfb97a6", "5abf5b50dce4fcab",
           "f7fcef4dfcfc97a6")
_T8B1QN = "dafcdb49fcead1a9"
_T8B1QC = ((0, 0x8a), (1, 0xfd), (2, 0x40), (3, 0x01), (5, 0x57),
          (6, 0x34), (7, 0x39), (8, 0x02), (9, 0x80), (10, 0x03),
          (11, 0x5e), (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a),
          (16, 0xbe), (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96),
          (21, 0x23), (22, 0x29), (23, 0x09), (24, 0x07), (25, 0x7c),
          (26, 0x70), (27, 0x45), (28, 0x19), (29, 0x9f), (30, 0x47),
          (31, 0x0d), (46, 0xc4), (47, 0x7c), (48, 0x36), (49, 0x3c),
          (50, 0xf8), (51, 0x4c), (52, 0x17), (53, 0x28), (54, 0xec),
          (55, 0x21), (56, 0x4e), (57, 0x64), (58, 0x6f), (59, 0x44),
          (60, 0x92), (61, 0xdc), (62, 0xe3), (63, 0xae))
_T8C1T = ("387ca4ce3b76", "95bc22289b77", "b23c85529b77", "853c6485fb77",
           "c6fc60e75b78", "59fc81ef5b78", "213c98ef5b78", "7e7c1649bb79",
           "a37c8073bb79", "2e7cb076bb79", "5b7c7653db79", "723c43aa1b7a",
           "d5bc80b21b7a", "d03c76d51b7a", "8d3c82017b7b", "fefc35027b7b")
_T8C1B = ("bf597025d863", "d559264cd863", "a2dc61431864", "edd9a44f1864",
           "97da2a741864", "465db5243864", "96dab5243864", "7f5f79533864",
           "05de93407864", "3f5cd24c7864", "c3daf3707864", "d45df8707864",
           "0edc367d7864", "74dcf398b864", "855ff898b864", "595d1c6cd864")
_T8C1C = ((0, 0x8a), (1, 0xc1), (2, 0x0f), (3, 0x14), (6, 0x34),
          (7, 0x39), (8, 0x02), (9, 0x80), (10, 0x03), (11, 0x5e),
          (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a), (16, 0xbe),
          (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96), (21, 0x23),
          (22, 0x29), (23, 0x99), (24, 0x07), (25, 0x7c), (26, 0x70),
          (27, 0x45), (28, 0x19), (29, 0x9f), (30, 0x47), (31, 0x0d),
          (32, 0xda), (33, 0xfc), (34, 0xdb), (35, 0x49), (36, 0xfc),
          (37, 0xea), (38, 0xd1), (39, 0xa9), (46, 0xc4), (47, 0x5c),
          (54, 0xc2), (55, 0x1e), (56, 0x4e), (57, 0x64), (58, 0x6f),
          (59, 0x44), (60, 0x92), (61, 0xdc), (62, 0xe3), (63, 0xae))
_T8D10 = {11517: "8a410100fb5934390280035e5e0d567abe5d3c9096232939077c7045199f47cd43bf6f39d82e1e9eacdadb2e5446cc27363cf84c1728ec214e646f4492dce3ae",
          11518: "8a7da000fd5934390280035e5e0d567abe5d3c9096232981077c7045199f478d43bf6f39d82e1e7e8bdad4f13577ac2826fc50e47d9686c94e646f4492dce3ae",
          11519: "8a9d9209ff5934390280035e5e0d567abe5d3c9096232939077c7045199f478d43bf6f39d82e1e5e8bdad4f13577ace8bd3ef881b6344c76aef2dfa192dce3ae",
          11535: "8ab586001f5a34390280035e5e0d567abe5d3c9096232951077c7045199f47cd43bf6f39d82e1e1e8bdad4f13577ac048ebc078318d66eceab7e11b192dce3ae",
          11545: "a5984808331a4693660038e05e0d567abe5d3c9096232949077c7045199f470d43bf6f39d82e1e3e8bdad4f13577acd48ebc078318d66ece4b7de1dc3adc153b"}
_T8D1AT = ("bd3e760e7e4fa2", "bd3ed62e867704", "bd40968eacd793",
           "bd40f6ce818f35", "7d41966e93976f", "7d4196ced60f7f",
           "9d41d66ee20788", "9d41d66e9b77d7", "9d43f66ea197c8",
           "9d43f6eec9ffc8", "bd43562eb7171c", "5d44f6ceb0bfa4",
           "9d46564e7ca703", "9d46568ed3ff4e", "5d4736aebaffde")
_T8D1AC = ((0, 0x8a), (1, 0x9d), (2, 0x92), (3, 0x09), (5, 0x5a),
          (6, 0x34), (7, 0x39), (8, 0x02), (9, 0x80), (10, 0x03),
          (11, 0x5e), (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a),
          (16, 0xbe), (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96),
          (21, 0x23), (22, 0x29), (23, 0x39), (24, 0x07), (25, 0x7c),
          (26, 0x70), (27, 0x45), (28, 0x19), (29, 0x9f), (30, 0x47),
          (31, 0x8d), (32, 0x43), (33, 0xbf), (34, 0x6f), (35, 0x39),
          (36, 0xd8), (37, 0x2e), (38, 0x1e), (39, 0x5e), (40, 0x8b),
          (41, 0xda), (42, 0xd4), (43, 0xf1), (44, 0x35), (45, 0x77),
          (46, 0xac), (47, 0xe8), (50, 0xf8), (51, 0x81), (52, 0xb6),
          (53, 0x34), (54, 0x4c), (60, 0x92), (61, 0xdc), (62, 0xe3),
          (63, 0xae))
_T8D1BT = ("518499cddeb4e93c13f9", "1d84014d3e74e63d8e0d",
           "518499cdfe146dbd2fbd", "bd84f98d3e54973cafcb",
           "d982394d3e649d7dd133", "bd84f98d3eb4147efe3e",
           "ad83e90d7e44737fa45f", "8984490d3ed40f3d28ca",
           "e58369cdfed4827f021b")
_T8D1BC = ((0, 0x8a), (3, 0x00), (5, 0x5a), (6, 0x34), (7, 0x39),
          (8, 0x02), (9, 0x80), (10, 0x03), (11, 0x5e), (12, 0x5e),
          (13, 0x0d), (14, 0x56), (15, 0x7a), (16, 0xbe), (17, 0x5d),
          (18, 0x3c), (19, 0x90), (20, 0x96), (21, 0x23), (22, 0x29),
          (24, 0x07), (25, 0x7c), (26, 0x70), (27, 0x45), (28, 0x19),
          (29, 0x9f), (30, 0x47), (32, 0x43), (33, 0xbf), (34, 0x6f),
          (35, 0x39), (36, 0xd8), (37, 0x2e), (38, 0x1e), (40, 0x8b),
          (41, 0xda), (42, 0xd4), (43, 0xf1), (44, 0x35), (45, 0x77),
          (46, 0xac), (48, 0x8e), (49, 0xbc), (50, 0x07), (51, 0x83),
          (52, 0x18), (53, 0xd6), (54, 0x6e), (55, 0xce), (60, 0x92),
          (61, 0xdc), (62, 0xe3), (63, 0xae))
_T8D1QT = ("0059513b", "4f5ec058", "acd8c458", "245eff86", "7959458f",
           "795d458f", "57de790e", "195a8f0e", "045c930e", "b65c4842",
           "dd5b8a43", "145f6a5b", "925e8362", "545cb463", "c6d8b463",
           "3adc153b")
_T8D1QB = ("9848493ed44b7de1dc", "d83ae97ea453ffe01e",
           "9848495e34d0fdfda0")
_T8D1QN = "9837697e142ffdbf59"
_T8D1QC = ((0, 0xa5), (3, 0x08), (6, 0x46), (7, 0x93),
          (8, 0x66), (9, 0x00), (10, 0x38), (11, 0xe0), (12, 0x5e),
          (13, 0x0d), (14, 0x56), (15, 0x7a), (16, 0xbe), (17, 0x5d),
          (18, 0x3c), (19, 0x90), (20, 0x96), (21, 0x23), (22, 0x29),
          (24, 0x07), (25, 0x7c), (26, 0x70), (27, 0x45), (28, 0x19),
          (29, 0x9f), (30, 0x47), (32, 0x43), (33, 0xbf),
          (34, 0x6f), (35, 0x39), (36, 0xd8), (37, 0x2e), (38, 0x1e),
          (40, 0x8b), (41, 0xda), (42, 0xd4), (43, 0xf1), (44, 0x35),
          (45, 0x77), (46, 0xac), (48, 0x8e), (49, 0xbc), (50, 0x07),
          (51, 0x83), (52, 0x18), (53, 0xd6), (54, 0x6e), (55, 0xce))
_T8E10 = "e9455284b31a46936600785822df2e1e96232999077c7045199f47cd43bf6f39d82e1efe8bdad4f13577ac748ebc078318d66ecefd7ce48e3adc153b3abc5036"
_T8E1T = ("1a0059513b", "1a4f5ec058", "1aacd8c458", "5a245eff86",
           "5a7959458f", "5a795d458f", "9a57de790e", "9a195a8f0e",
           "9a045c930e", "dab65c4842", "dadd5b8a43", "da145f6a5b",
           "da925e8362", "da545cb463", "dac6d8b463")
_T8E1C = ((0, 0xa5), (1, 0x98), (2, 0x37), (3, 0x08), (6, 0x46),
          (7, 0x93), (8, 0x66), (9, 0x00), (10, 0x38), (11, 0xe0),
          (12, 0x5e), (13, 0x0d), (14, 0x56), (15, 0x7a), (16, 0xbe),
          (17, 0x5d), (18, 0x3c), (19, 0x90), (20, 0x96), (21, 0x23),
          (22, 0x29), (23, 0x69), (24, 0x07), (25, 0x7c), (26, 0x70),
          (27, 0x45), (28, 0x19), (29, 0x9f), (30, 0x47), (31, 0x8d),
          (32, 0x43), (33, 0xbf), (34, 0x6f), (35, 0x39), (36, 0xd8),
          (37, 0x2e), (38, 0x1e), (39, 0x7e), (40, 0x8b), (41, 0xda),
          (42, 0xd4), (43, 0xf1), (44, 0x35), (45, 0x77), (46, 0xac),
          (47, 0x14), (48, 0x8e), (49, 0xbc), (50, 0x07), (51, 0x83),
          (52, 0x18), (53, 0xd6), (54, 0x6e), (55, 0xce), (56, 0x2f),
          (57, 0xfd), (58, 0xbf), (59, 0x59))
_T8E1QT = ("dbfcb155", "733ce157", "da7c13e2", "f67c30e2", "fb3cb39e",
           "65fc82b2", "cc3cb53c", "edfc53f9", "4a3ce0ff", "4a3ce1ff",
           "577c781b", "e23c9037", "2f3c4038", "2f3c4138", "6a7c627e",
           "3abc5036")
_T8E1QB = ("3adc153b", "0059513b", "4f5ec058", "acd8c458", "245eff86",
           "7959458f", "795d458f", "57de790e", "195a8f0e", "045c930e",
           "b65c4842", "dd5b8a43", "145f6a5b", "925e8362", "545cb463")
_T8E1QN = "c6d8b463"
_T8E1B10 = "7878787888b0b8c0c0c0c80000001078"
_T8E1QC = ((0, 0xe9), (1, 0x45), (2, 0x52), (3, 0x84), (6, 0x46),
          (7, 0x93), (8, 0x66), (9, 0x00),
          (12, 0x22), (13, 0xdf), (14, 0x2e), (15, 0x1e), (16, 0x96),
          (17, 0x23), (18, 0x29), (19, 0x99), (20, 0x07), (21, 0x7c),
          (22, 0x70), (23, 0x45), (24, 0x19), (25, 0x9f), (26, 0x47),
          (27, 0xcd), (28, 0x43), (29, 0xbf), (30, 0x6f), (31, 0x39),
          (32, 0xd8), (33, 0x2e), (34, 0x1e), (35, 0xfe), (36, 0x8b),
          (37, 0xda), (38, 0xd4), (39, 0xf1), (40, 0x35), (41, 0x77),
          (42, 0xac), (43, 0x74), (44, 0x8e), (45, 0xbc), (46, 0x07),
          (47, 0x83), (48, 0x18), (49, 0xd6), (50, 0x6e), (51, 0xce),
          (52, 0xfd), (53, 0x7c), (54, 0xe4), (55, 0x8e))
_T8F10 = {11865: "8aa10b00b35c34390280035e5e0d567abe5d3c9096232929077c7045199f474d43bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d72492dce3ae",
          11866: "1820d105b55c16292200a64665f876f196232929077c7045199f474d43bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a8f3cc6c9",
          11883: "fa167401d75c162922004b3ebf56040b9c5a183ffaf225fa077c7045199f474d43bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a",
          11893: "fa564117eb5c162922004b3ebf56040b37da675e3a260c767b3c27f2fdad79d443bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a",
          11941: "fa5641174b5d162922004b3ebf56040bfd5fd2b41aa2a6737b3c27f2fdad79d443bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a"}
_T8F1T = ("7858dbfcb155", "7858733ce157", "7858da7c13e2", "7858f67c30e2",
           "8858fb3cb39e", "b05865fc82b2", "b858cc3cb53c", "c058edfc53f9",
           "c0584a3ce0ff", "c0584a3ce1ff", "c858577c781b", "0059e23c9037",
           "00592f3c4038", "00592f3c4138", "10596a7c627e")
_T8F1C = ((0, 0xe9), (1, 0x45), (2, 0x52), (3, 0x84), (5, 0xdc),
          (6, 0x46), (7, 0x93), (8, 0x66), (9, 0x00), (12, 0x22),
          (13, 0xdf), (14, 0x2e), (15, 0x1e), (16, 0x96), (17, 0x23),
          (18, 0x29), (19, 0x99), (20, 0x07), (21, 0x7c), (22, 0x70),
          (23, 0x45), (24, 0x19), (25, 0x9f), (26, 0x47), (27, 0xcd),
          (28, 0x43), (29, 0xbf), (30, 0x6f), (31, 0x39), (32, 0xd8),
          (33, 0x2e), (34, 0x1e), (35, 0xfe), (36, 0x8b), (37, 0xda),
          (38, 0xd4), (39, 0xf1), (40, 0x35), (41, 0x77), (42, 0xac),
          (43, 0x74), (44, 0x8e), (45, 0xbc), (46, 0x07), (47, 0x83),
          (48, 0x18), (49, 0xd6), (50, 0x6e), (51, 0xce), (52, 0xfd),
          (53, 0x7c), (54, 0xe4), (55, 0x8e), (56, 0xc6), (57, 0xd8),
          (58, 0xb4), (59, 0x63))
_T8F2T = ("189405f07f8f3a3d", "980b055c6e57ba3d", "981005c86e6bba3d",
           "18e705147261ba3d", "9843048c70517a3e", "984304d071677a3e",
           "98430414737d7a3e", "182005846f2b7a3e", "18bd05c071a77a3e",
           "987104687e91fa3e", "186a057469271a3f", "186a05b86a3d1a3f",
           "187005087fa31a3f", "98a205b469571a3f", "9819048c6e293a3f",
           "98cf05c8799b9a3f")
_T8F2C = ((3, 0x5d), (5, 0x5c), (6, 0x16), (7, 0x29), (8, 0x22),
          (9, 0x00), (10, 0xa6), (11, 0x46), (12, 0x65), (18, 0x92),
          (19, 0x92), (20, 0x07), (21, 0x7c), (22, 0x70), (23, 0x45),
          (24, 0x19), (25, 0x9f), (26, 0x47), (27, 0x4d), (28, 0x43),
          (29, 0xbf), (30, 0x6f), (31, 0x39), (32, 0xd8), (33, 0x2e),
          (34, 0x1e), (35, 0x3e), (36, 0x8b), (37, 0xda), (38, 0xd4),
          (39, 0xf1), (40, 0x35), (41, 0x77), (42, 0xac), (43, 0x5c),
          (44, 0x8e), (45, 0xbc), (46, 0x07), (47, 0x83), (48, 0x18),
          (49, 0xd6), (50, 0x6e), (51, 0xee), (52, 0xee), (53, 0xd7),
          (54, 0xd7), (55, 0x24), (56, 0x98), (57, 0x5f), (58, 0x5f),
          (59, 0x5a), (60, 0x36), (61, 0x7c), (62, 0xc6), (63, 0xc9))
_T8F3T = ("d25f19e3ba4e3ef5", "15dd66537ae2d7f4", "32dc38e6ba4e3ef5",
           "c65ae3c47a250cf6", "e7db7bf8dac5dcf2", "785ba6dbfa250cf6",
           "05db134afa0c0cf4", "00db8713da0fa5f5", "8d5fb2af9acd71f4")
_T8F3C = ((0, 0xfa), (1, 0x16), (2, 0x74), (3, 0x01), (5, 0x5c),
          (6, 0x16), (7, 0x29), (8, 0x22), (9, 0x00), (10, 0x4b),
          (11, 0x3e), (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b),
          (24, 0x07), (25, 0x7c), (26, 0x70), (27, 0x45), (28, 0x19),
          (29, 0x9f), (30, 0x47), (31, 0x4d), (32, 0x43), (33, 0xbf),
          (34, 0x6f), (35, 0x39), (36, 0xd8), (37, 0x2e), (38, 0x1e),
          (39, 0x3e), (40, 0x8b), (41, 0xda), (42, 0xd4), (43, 0xf1),
          (44, 0x35), (45, 0x77), (46, 0xac), (47, 0x5c), (48, 0x8e),
          (49, 0xbc), (50, 0x07), (51, 0x83), (52, 0x18), (53, 0xd6),
          (54, 0x6e), (55, 0xee), (56, 0xee), (57, 0xd7), (58, 0xd7),
          (59, 0x24), (60, 0x98), (61, 0x5f), (62, 0x5f), (63, 0x5a))
_T8F4T = ("917ca462fdaf", "67bc85525db3", "167ce77d3db5", "fbfc40bb5db5",
           "6a7c23037db5", "cd3c33317db5", "5dfcf7afddb5", "a5fcd3405dbb",
           "32fca3b2bdbb", "1f7cc3f2ddbb", "e9fcf61ffdbb", "ff3c7490ddbd",
           "ff3c7590ddbd", "c93c5678ddc1", "99bc031bfdc3", "7b3c27f2fdad")
_T8F4B = ("5c37da675e3a260c76", "5d37dbac767a0d0c74",
           "5da65a37a97a10a575")
_T8F4C = ((0, 0xfa), (1, 0x56), (2, 0x41), (3, 0x17), (6, 0x16),
          (7, 0x29), (8, 0x22), (9, 0x00), (10, 0x4b), (11, 0x3e),
          (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b), (30, 0x79),
          (31, 0xd4), (32, 0x43), (33, 0xbf), (34, 0x6f), (35, 0x39),
          (36, 0xd8), (37, 0x2e), (38, 0x1e), (39, 0x3e), (40, 0x8b),
          (41, 0xda), (42, 0xd4), (43, 0xf1), (44, 0x35), (45, 0x77),
          (46, 0xac), (47, 0x5c), (48, 0x8e), (49, 0xbc), (50, 0x07),
          (51, 0x83), (52, 0x18), (53, 0xd6), (54, 0x6e), (55, 0xee),
          (56, 0xee), (57, 0xd7), (58, 0xd7), (59, 0x24), (60, 0x98),
          (61, 0x5f), (62, 0x5f), (63, 0x5a))
_T8F5C = ((0, 0xfa), (1, 0x56), (2, 0x41), (3, 0x17), (5, 0x5d),
          (6, 0x16), (7, 0x29), (8, 0x22), (9, 0x00), (10, 0x4b),
          (11, 0x3e), (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b),
          (16, 0xfd), (17, 0x5f), (18, 0xd2), (19, 0xb4), (20, 0x1a),
          (21, 0xa2), (22, 0xa6), (23, 0x73), (30, 0x79), (31, 0xd4),
          (32, 0x43), (33, 0xbf), (34, 0x6f), (35, 0x39), (36, 0xd8),
          (37, 0x2e), (38, 0x1e), (39, 0x3e), (40, 0x8b), (41, 0xda),
          (42, 0xd4), (43, 0xf1), (44, 0x35), (45, 0x77), (46, 0xac),
          (47, 0x5c), (48, 0x8e), (49, 0xbc), (50, 0x07), (51, 0x83),
          (52, 0x18), (53, 0xd6), (54, 0x6e), (55, 0xee), (56, 0xee),
          (57, 0xd7), (58, 0xd7), (59, 0x24), (60, 0x98), (61, 0x5f),
          (62, 0x5f), (63, 0x5a))
_T9HT = ("34fc5305bcd2", "4afc5b05bcd2", "babfb715bcd2", "d0bfbf15bcd2",
          "81fc8f9ddcd2", "7dfcab1efcd7", "d1bf7f3a1cd8", "6bfcdbe01cd8",
          "9abf8be11cd8", "4bfc3b195cd9", "edbf2779bcd9", "1afca35adcd9",
          "7ffcf713bcde", "45fce33ebcde", "5bfceb3ebcde", "2ebf8b43bcde")
_T9HB = ("7b3c27f2fdad", "917ca462fdaf", "67bc85525db3", "167ce77d3db5",
          "fbfc40bb5db5", "6a7c23037db5", "cd3c33317db5", "5dfcf7afddb5",
          "a5fcd3405dbb", "32fca3b2bdbb", "1f7cc3f2ddbb", "e9fcf61ffdbb",
          "ff3c7490ddbd", "ff3c7590ddbd", "c93c5678ddc1", "99bc031bfdc3")
_T9HC = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00), (6, 0x16),
          (7, 0x29), (8, 0xe2), (9, 0x36), (10, 0x15), (11, 0x74),
          (12, 0x01), (13, 0x58), (14, 0xf2), (15, 0xd1), (16, 0xbf),
          (17, 0x56), (18, 0x04), (19, 0x0b), (20, 0xc9), (21, 0x5f),
          (22, 0xd0), (23, 0x6e), (24, 0xfa), (25, 0x10), (26, 0xa5),
          (27, 0x75), (34, 0x79), (35, 0xd4), (42, 0xe2), (43, 0xe1),
          (44, 0x8b), (45, 0xda), (46, 0xd4), (47, 0xf1), (48, 0x35),
          (49, 0x77), (50, 0xac), (51, 0x5c), (52, 0x8e), (53, 0xbc),
          (54, 0x07), (55, 0x83), (56, 0x18), (57, 0xd6), (58, 0x6e),
          (59, 0xee), (60, 0xee), (61, 0xd7), (62, 0xd7), (63, 0x24),
          (64, 0x98), (65, 0x5f), (66, 0x5f), (67, 0x5a))
_T9DIP = {12213: "fa862e006b5f162922004b3ebf56040b8d5c8f89f70dd454077c7045199f474d43bf6f39d82e1e3e8bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a",
          12214: "fa5641176d5f162922004b3ebf56040b8d5c8f89f70dd464b73c51a59934c81db5fc673c5fd71d188bdad4f13577ac5c8ebc078318d66eeeeed7d724985f5f5a"}
_T9RT = ("32db129cf972", "815a94421973", "525e9d6a5973", "345d109d5973",
          "9559159d5973", "e25aeab89973", "f3ddeeb89973", "465b15c59973",
          "a6599b6bb973", "86df3d9ab973", "4b5f8a52f973", "8cdd3181f973",
          "cddb4e85f973", "a95c47c2f973", "f9d947c2f973", "ef5b34825974")
_T9RC = ((0, 0x01), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x5f),
          (6, 0x16), (7, 0x29), (8, 0xe2), (9, 0x2e), (10, 0x15),
          (11, 0x74), (12, 0x01), (13, 0x58), (14, 0xf2), (15, 0xd1),
          (16, 0xbf), (17, 0x56), (18, 0x04), (19, 0x0b), (20, 0x8d),
          (21, 0x5c), (22, 0x8f), (23, 0x89), (24, 0xf7), (25, 0x0d),
          (26, 0xd4), (27, 0x64), (28, 0xb7), (29, 0x3c), (30, 0x51),
          (31, 0xa5), (32, 0x99), (33, 0x34), (34, 0xc8), (35, 0x1d),
          (36, 0x65), (37, 0xbf), (38, 0x6b), (39, 0x3c), (40, 0x5f),
          (41, 0xd7), (42, 0x1d), (43, 0x18), (50, 0xc7), (51, 0xca),
          (52, 0x8e), (53, 0xbc), (54, 0x07), (55, 0x83), (56, 0x18),
          (57, 0xd6), (58, 0x6e), (59, 0xee), (60, 0xee), (61, 0xd7),
          (62, 0xd7), (63, 0x24), (64, 0x98), (65, 0x5f), (66, 0x5f),
          (67, 0x5a))
_T9D20 = {12231: "fa5641178f5f162922004b3ebf56040b8d5c8f89f70dd454b73c51a59934c85df3bfbb4cfaeea4994cddcf419a0591818ebc078318d66eeeeed7d724985f5f5a",
          12232: "faaea00b915f162922004b3ebf56040b8d5c8f89f70dd424b73c51a59934c89df3bfbb4cfaeea499fa5e9dfcb9f0fcfe8ebc078318d66eeeeed7d724985f5f5a",
          12241: "fa960abaa35f162922004b3ebf56040b8d5c8f89f70dd4b4b73c51a59934c8ddf3bfbb4cfaeea499c0dd8c9b792069bf853c68211c4aede6eed7d724985f5f5a"}
_T9D2AT = ("a5da9dfcb9f0fcfe", "115ca2fcb9f0fcfe", "37da5a9e192069ff",
           "d3dcffd719a8bcfd", "41dfab9e192069ff", "51de68fe39015cfe",
           "19dc3651d9f132ff", "ed5b3400997991fe")
_T9D2AC = ((0, 0xfa), (1, 0xae), (2, 0xa0), (3, 0x0b), (5, 0x5f),
          (6, 0x16), (7, 0x29), (8, 0x22), (9, 0x00), (10, 0x4b),
          (11, 0x3e), (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b),
          (16, 0x8d), (17, 0x5c), (18, 0x8f), (19, 0x89), (20, 0xf7),
          (21, 0x0d), (22, 0xd4), (23, 0x24), (24, 0xb7), (25, 0x3c),
          (26, 0x51), (27, 0xa5), (28, 0x99), (29, 0x34), (30, 0xc8),
          (31, 0x9d), (32, 0xf3), (33, 0xbf), (34, 0xbb), (35, 0x4c),
          (36, 0xfa), (37, 0xee), (38, 0xa4), (39, 0x99), (48, 0x8e),
          (49, 0xbc), (50, 0x07), (51, 0x83), (52, 0x18), (53, 0xd6),
          (54, 0x6e), (55, 0xee), (56, 0xee), (57, 0xd7), (58, 0xd7),
          (59, 0x24), (60, 0x98), (61, 0x5f), (62, 0x5f), (63, 0x5a))
_T9D2QT = ("053ce35e7c4a", "e3fc91785c4b", "1c7c87dabc4b", "f23c1806fc4d",
           "387c66dadc4e", "de3c80303c4f", "d9bc75533c4f", "963c76105c4f",
           "fc3c146a5c4f", "363cb6e3bc52", "94fcc3193c53", "27fce4213c53",
           "b17c27443c53", "f2fcf7443c53", "a1bcc6a57c54", "853c68211c4a")
_T9D2QB = ("c0dd8c9b792069bf", "ed5a770059015cbe", "abdfab24f9f132bf",
           "b0de060519b726be")
_T9D2QC = ((0, 0xfa), (1, 0x96), (2, 0x0a), (3, 0xba), (6, 0x16),
          (7, 0x29), (8, 0x22), (9, 0x00), (10, 0x4b), (11, 0x3e),
          (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b), (16, 0x8d),
          (17, 0x5c), (18, 0x8f), (19, 0x89), (20, 0xf7), (21, 0x0d),
          (22, 0xd4), (23, 0xb4), (24, 0xb7), (25, 0x3c), (26, 0x51),
          (27, 0xa5), (28, 0x99), (29, 0x34), (30, 0xc8), (31, 0xdd),
          (32, 0xf3), (33, 0xbf), (34, 0xbb), (35, 0x4c), (36, 0xfa),
          (37, 0xee), (38, 0xa4), (39, 0x99), (54, 0xed), (55, 0xe6),
          (56, 0xee), (57, 0xd7), (58, 0xd7), (59, 0x24), (60, 0x98),
          (61, 0x5f), (62, 0x5f), (63, 0x5a))
_T9S1T = ("dc4d553f4ee7", "dc4d1dbdc9e9", "5c4e5cfcf558", "dc51123e228f",
           "5c5278fbdc0b", "5c52e93ee30b", "5c526d7f5b0e", "5c52ef7cd256",
           "5c52a0bf4d59", "5c53a3bdd360", "5c56863c520c", "5c56a97eb411",
           "9c562f3b178e", "9c5787beae7d", "9c57f87e86e3", "9c58287f0feb")
_T9S1B = ("08a085441d997f50", "098c7b041d997f53", "0947e2741d19ff5a",
           "0b1d6a04dd993f5d", "086018749d19bf6f", "0b996914dd193f76",
           "0800c264dd99bf79", "09d64d64dd197f79", "08d841449d99bf7a",
           "0950a874dd993f7a", "0bd88e149d99bf95", "080f67449d993f99",
           "089387141d99ff99", "099d10549d197f99", "09df13749d19bf99",
           "0a1a97541d197fa3")
_T9S1C = ((1, 0x00), (2, 0x00), (3, 0x00), (6, 0x16), (7, 0x29),
          (8, 0xe2), (9, 0xf6), (12, 0x01), (13, 0x58), (14, 0xf2),
          (15, 0xd1), (16, 0xbf), (17, 0x56), (18, 0x04), (19, 0x0b),
          (20, 0x8d), (21, 0x5c), (22, 0x8f), (23, 0x89), (24, 0xf7),
          (25, 0x0d), (26, 0xd4), (28, 0xb7), (29, 0x3c), (30, 0x51),
          (31, 0xa5), (32, 0x99), (33, 0x34), (34, 0xc8), (36, 0xf3),
          (37, 0xbf), (38, 0xbb), (39, 0x4c), (40, 0xfa), (41, 0xee),
          (42, 0xa4), (44, 0xaf), (45, 0xdd), (46, 0xee), (47, 0x30),
          (48, 0xf9), (49, 0xf1), (50, 0x32), (54, 0x2a), (55, 0xe8),
          (57, 0x6a), (58, 0x37), (59, 0xe7), (64, 0x98), (65, 0x5f),
          (66, 0x5f), (67, 0x5a))
_T9D3P = {12561: "fa1674012362162922004b3ebf56040b8d5c8f89f70dd4a4b73c51a59934c85df3bfbb4cfaeea419a45c403136f86dba8ebc078318d66eeeeed7d724985f5f5a",
          12562: "fa9e69cb2562162922004b3ebf56040b8d5c8f89f70dd4c4b73c51a59934c85df3bfbb4cfaeea499a45c403136f86d32f8043024ecccbf8e1e7d7557985f5f5a"}
_T9D3T = ("626470df9bce", "6264cc5bfaeb", "a2640e5a2252", "a264625e5d52",
           "e264e35ce962", "e2643fd94780", "e264f45c019f", "e26466d9019f",
           "e2648dd843a0", "e264e1dc7ea0", "2265fc5938cd", "2265e75b3ccd",
           "62658edd9034", "a26585587081", "a265185a8588", "a265035c8988")
_T9D3C = ((0, 0x0c), (1, 0x00), (2, 0x00), (3, 0x00), (7, 0x91),
          (8, 0xa6), (9, 0xef), (10, 0x99), (11, 0xb6), (12, 0x12),
          (13, 0x80), (14, 0x25), (15, 0x1f), (16, 0xbf), (17, 0x56),
          (18, 0x04), (19, 0x0b), (20, 0x8d), (21, 0x5c), (22, 0x8f),
          (23, 0x89), (24, 0xf7), (25, 0x0d), (26, 0xd4), (27, 0xc4),
          (28, 0xb7), (29, 0x3c), (30, 0x51), (31, 0xa5), (32, 0x99),
          (33, 0x34), (34, 0xc8), (35, 0x5d), (36, 0xf3), (37, 0xbf),
          (38, 0xbb), (39, 0x4c), (40, 0xfa), (41, 0xee), (42, 0xa4),
          (43, 0x99), (44, 0xa4), (45, 0x5c), (46, 0x40), (47, 0x31),
          (48, 0x36), (49, 0xf8), (50, 0x6d), (51, 0x32), (52, 0xf8),
          (53, 0x04), (54, 0x30), (55, 0x24), (56, 0xec), (57, 0xcc),
          (58, 0xbf), (59, 0x8e), (60, 0xee), (61, 0x7f), (62, 0x78),
          (63, 0x57))
_T9D4T = ("e22e4627029f5e1da9", "62de56c701775c0d2b",
           "62de56c701b45c112b", "62de56c701065f112b",
           "a2f9d1c7019fdddc2b", "a27aea8701e15c71be",
           "a2f9d1c701a458e12b", "22c39fa701d6da1278",
           "e25094c701c9def9e2", "2297dca701ef59f987")
_T9D4C = ((0, 0x47), (1, 0xdf), (2, 0x8f), (3, 0x70), (10, 0x60),
          (11, 0xc9), (12, 0xbf), (13, 0x56), (14, 0x04), (15, 0x0b),
          (16, 0x8d), (17, 0x5c), (18, 0x8f), (19, 0x89), (20, 0xf7),
          (21, 0x0d), (22, 0xd4), (23, 0x24), (24, 0xb7), (25, 0x3c),
          (26, 0x51), (27, 0xa5), (28, 0x99), (29, 0x34), (30, 0xc8),
          (31, 0x5d), (32, 0xf3), (33, 0xbf), (34, 0xbb), (35, 0x4c),
          (36, 0xfa), (37, 0xee), (38, 0xa4), (39, 0x19), (40, 0xa4),
          (41, 0x5c), (42, 0x40), (43, 0x31), (44, 0x36), (45, 0xf8),
          (46, 0x6d), (47, 0x5a), (48, 0x66), (49, 0x3c), (50, 0xd3),
          (51, 0x96), (52, 0x98), (53, 0x9d), (54, 0xf9), (55, 0x57),
          (56, 0xee), (57, 0xbd), (58, 0x37), (59, 0x9d))
_T9T1T = ("00c4083cb4fa", "00c4edfc91fd", "80c4727cd71c", "00cb39fce6a9",
           "00ce063cd347", "00cf8fbc4302", "00cf8fbc4402", "00cf8e3ca58e",
           "00cfabbc18b0", "80d767bcf691", "80d88dbc634f", "80d8f4fc95d9",
           "80d9c8fc8595", "80d915fc3596", "00ddd6bc9526", "00ddadfce4cd")
_T9T1B = ("e2f9d10e275d8b77", "e221630d5a5e9c30", "2251940e77583103",
           "e221630d295f1d59")
_T9T1C = ((0, 0x07), (1, 0x00), (2, 0x00), (3, 0x00), (8, 0x47),
          (9, 0x98), (10, 0xf8), (11, 0x08), (15, 0xc0), (16, 0xc3),
          (17, 0x8d), (18, 0x5c), (19, 0x8f), (20, 0xf7), (21, 0x0d),
          (22, 0xd4), (23, 0x24), (24, 0xb7), (25, 0x3c), (26, 0x51),
          (27, 0xa5), (28, 0x99), (29, 0x34), (30, 0xc8), (31, 0x5d),
          (32, 0xf3), (33, 0xbf), (34, 0xbb), (35, 0x4c), (36, 0xfa),
          (37, 0xee), (38, 0xa4), (39, 0x19), (40, 0xa4), (41, 0x5c),
          (42, 0x40), (43, 0x31), (44, 0x36), (45, 0xf8), (46, 0x6d),
          (47, 0x5a), (48, 0x66), (49, 0x3c), (50, 0xd3), (51, 0x96),
          (52, 0x98), (53, 0x9d), (54, 0xf9), (55, 0x57), (56, 0xee),
          (57, 0xbd), (58, 0x37), (59, 0x9d))
_T9U1T = ("612ba5db0c5bd9", "612bf65b125bd9", "812efe5e39bbda",
           "012cb65d683bdb", "b12fcddcd73bdb", "1121335cd45bdb",
           "112184dcd95bdb", "1121d55cdf5bdb", "71265edd0f5bdb",
           "e12552da5c3bdd", "e125a35a623bdd", "312739dfea3bdd",
           "412709de5e3bdd", "712083dd1afbdd", "7120d45d20fbdd",
           "a1201a5d3afbdd")
_T9U1B = ("88083cb4fa", "88edfc91fd", "89727cd71c", "9639fce6a9",
           "9c063cd347", "9e8fbc4302", "9e8fbc4402", "9e8e3ca58e",
           "9eabbc18b0", "af67bcf691", "b18dbc634f", "b1f4fc95d9",
           "b3c8fc8595", "b315fc3596", "bad6bc9526", "baadfce4cd")
_T9U1C = ((0, 0x70), (1, 0x00), (2, 0x00), (3, 0x00), (6, 0x51),
          (7, 0x94), (8, 0xc7), (11, 0x8f), (12, 0x00), (14, 0x81),
          (15, 0x85), (16, 0xc3), (22, 0x40), (23, 0x4d), (24, 0xb7),
          (25, 0x3c), (26, 0x51), (27, 0xa5), (28, 0x99), (29, 0x34),
          (30, 0xc8), (31, 0x5d), (32, 0xf3), (33, 0xbf), (34, 0xbb),
          (35, 0x4c), (36, 0xfa), (37, 0xee), (38, 0xa4), (39, 0x19),
          (40, 0xa4), (41, 0x5c), (42, 0x40), (43, 0x31), (44, 0x36),
          (45, 0xf8), (46, 0x6d), (47, 0x5a), (48, 0x66), (49, 0x3c),
          (50, 0xd3), (51, 0x96), (52, 0x98), (53, 0x9d), (54, 0xf9),
          (55, 0x57), (56, 0xee), (57, 0xbd), (58, 0x37), (59, 0x9d),
          (60, 0xf5), (61, 0xde), (62, 0xae), (63, 0x36))
_T9V1D = "f4fd0807db64394f6300967cbf56040b8d5c8f89f70dd424b73c51a59934c85df3bfbb4cfaeea419a45c403136f86d5a663cd396989df957eebd379dec5dcba2"
_T9V10 = {12910: "07000000dd64394f0300f20803187bb200b63beabee79247b73c51a59934c85df3bfbb4cfaeea419a45c403136f86d5a663cd396989df957eebd379dec5dcba2b83c977e",
          12911: "70000000df64394f6300258f00634f1620ca3beabee7924731fcb4acfd0e83dcf3bfbb4cfaeea419a45c403136f86d5a663cd396989df957eebd379dec5dcba2b83c977e",
          12927: "03000000ff64394f0329798403187bb22090bbee981e5d51733c227fdef58a79f3bfbb4cfaeea419a45c403136f86d5a663cd396989df957eebd379dec5dcba2b83c977e",
          12937: "380000001365394f6329924700634f162090bbee981e5d51c57c81673e1d8c4bc0bfbf1d3eb64e9aa45c403136f86d5a663cd396989df957eebd379dec5dcba2b83c977e"}
_T9V1AT = ("453ce48a9d0f", "75fcd68b9d0f", "6e7cb0793d10", "cc7ce7b13d10",
           "d07ca3265d12", "f4fca4eefd17", "d9fcf62b3d18", "a93c31a13d18",
           "3dbc35ac3d18", "83bc90b11d1e", "83bc91b11d1e", "e17cd0e91d1e",
           "c7bcb390bd1e", "44fc5400bd20", "ddfc3101bd20")
_T9V1AC = ((0, 0x70), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x64),
          (6, 0x39), (7, 0x4f), (8, 0x63), (9, 0x00), (10, 0x25),
          (11, 0x8f), (12, 0x00), (13, 0x63), (14, 0x4f), (15, 0x16),
          (16, 0x20), (17, 0xca), (18, 0x3b), (19, 0xea), (20, 0xbe),
          (21, 0xe7), (22, 0x92), (23, 0x47), (30, 0x83), (31, 0xdc),
          (32, 0xf3), (33, 0xbf), (34, 0xbb), (35, 0x4c), (36, 0xfa),
          (37, 0xee), (38, 0xa4), (39, 0x19), (40, 0xa4), (41, 0x5c),
          (42, 0x40), (43, 0x31), (44, 0x36), (45, 0xf8), (46, 0x6d),
          (47, 0x5a), (48, 0x66), (49, 0x3c), (50, 0xd3), (51, 0x96),
          (52, 0x98), (53, 0x9d), (54, 0xf9), (55, 0x57), (56, 0xee),
          (57, 0xbd), (58, 0x37), (59, 0x9d), (60, 0xec), (61, 0x5d),
          (62, 0xcb), (63, 0xa2), (64, 0xb8), (65, 0x3c), (66, 0x97),
          (67, 0x7e))
_T9V1BT = ("093cd7ab7e798942", "52bcd7ab7e798942", "883c85061e030e3e",
           "043c6562fe1b8c4b", "fafc25227e2cdf27", "99fc459efe1b8c4b",
           "6a7c844e5eea2235", "4a7c420f5e7a8942", "993c71195e819639")
_T9V1BC = ((0, 0x03), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x65),
          (6, 0x39), (7, 0x4f), (8, 0x03), (9, 0x29), (10, 0x79),
          (11, 0x84), (12, 0x03), (13, 0x18), (14, 0x7b), (15, 0xb2),
          (16, 0x20), (17, 0x90), (18, 0xbb), (19, 0xee), (20, 0x98),
          (21, 0x1e), (22, 0x5d), (23, 0x51), (32, 0xf3), (33, 0xbf),
          (34, 0xbb), (35, 0x4c), (36, 0xfa), (37, 0xee), (38, 0xa4),
          (39, 0x19), (40, 0xa4), (41, 0x5c), (42, 0x40), (43, 0x31),
          (44, 0x36), (45, 0xf8), (46, 0x6d), (47, 0x5a), (48, 0x66),
          (49, 0x3c), (50, 0xd3), (51, 0x96), (52, 0x98), (53, 0x9d),
          (54, 0xf9), (55, 0x57), (56, 0xee), (57, 0xbd), (58, 0x37),
          (59, 0x9d), (60, 0xec), (61, 0x5d), (62, 0xcb), (63, 0xa2),
          (64, 0xb8), (65, 0x3c), (66, 0x97), (67, 0x7e))
_T9V1QT = ("88fc5b223eb6", "81fc43233eb6", "37bfcf011ebb", "cefcb7617ebb",
           "a1bf57667ebb", "53fcdb9bfec3", "34fcdbaebec8", "52bf6b50dec8",
           "b6fc57da3ec9", "23fc2b437eca", "82bf67f47eca", "4afc03f97eca",
           "57bfeb3b7ed6", "98fc2be51ed8", "aefc33e51ed8", "c0bfbf1d3eb6")
_T9V1QB = ("c57c81673e1d8c4b", "b37c074a3e1db330", "787c7400bee30847",
           "e33c1754be39472c")
_T9V1QN = "6c7cb338bee30847"
_T9V1QC = ((0, 0x38), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x65),
          (6, 0x39), (7, 0x4f), (8, 0x63), (9, 0x29), (10, 0x92),
          (11, 0x47), (12, 0x00), (13, 0x63), (14, 0x4f), (15, 0x16),
          (16, 0x20), (17, 0x90), (18, 0xbb), (19, 0xee), (20, 0x98),
          (21, 0x1e), (22, 0x5d), (23, 0x51), (38, 0x4e), (39, 0x9a),
          (40, 0xa4), (41, 0x5c), (42, 0x40), (43, 0x31), (44, 0x36),
          (45, 0xf8), (46, 0x6d), (47, 0x5a), (48, 0x66), (49, 0x3c),
          (50, 0xd3), (51, 0x96), (52, 0x98), (53, 0x9d), (54, 0xf9),
          (55, 0x57), (56, 0xee), (57, 0xbd), (58, 0x37), (59, 0x9d),
          (60, 0xec), (61, 0x5d), (62, 0xcb), (63, 0xa2), (64, 0xb8),
          (65, 0x3c), (66, 0x97), (67, 0x7e))
_T9W1T = ("3fdf5ce93a76", "a0db61e93a76", "eddc36059a76", "6d5f91139a76",
           "e05eae379a76", "475f4ed1da76", "5adaec3d5a77", "aade3d3e5a77",
           "40daf8289a77", "bddf012b9a77", "1a5dc125fa77", "a1db2a26fa77",
           "1e5ae327fa77", "945da258fa77", "f0dc5554ba78", "775bbf54ba78")
_T9W1B = ("c0bfbf1d3eb6", "88fc5b223eb6", "81fc43233eb6", "37bfcf011ebb",
           "cefcb7617ebb", "a1bf57667ebb", "53fcdb9bfec3", "34fcdbaebec8",
           "52bf6b50dec8", "b6fc57da3ec9", "23fc2b437eca", "82bf67f47eca",
           "4afc03f97eca", "57bfeb3b7ed6", "98fc2be51ed8", "aefc33e51ed8")
_T9W1C = ((0, 0x16), (1, 0x03), (2, 0x00), (3, 0x00), (6, 0x39),
          (7, 0x4f), (8, 0x63), (9, 0x00), (10, 0x63), (11, 0x4f),
          (12, 0x20), (13, 0x25), (14, 0x79), (15, 0x84), (16, 0x81),
          (17, 0xdc), (18, 0x75), (19, 0x4f), (20, 0x98), (21, 0x1e),
          (22, 0x5d), (23, 0x51), (24, 0x6c), (25, 0x7c), (26, 0xb3),
          (27, 0x38), (28, 0xbe), (29, 0xe3), (30, 0x08), (31, 0x47),
          (38, 0x4e), (39, 0x9a), (46, 0xdf), (47, 0xa6), (48, 0x66),
          (49, 0x3c), (50, 0xd3), (51, 0x96), (52, 0x98), (53, 0x9d),
          (54, 0xf9), (55, 0x57), (56, 0xee), (57, 0xbd), (58, 0x37),
          (59, 0x9d), (60, 0xec), (61, 0x5d), (62, 0xcb), (63, 0xa2),
          (64, 0xb8), (65, 0x3c), (66, 0x97), (67, 0x7e))
_T9X1D = "168947389367394f6300634f2090bbee981e5d916d7cc06f5a38f6c9f3bfbb4cfaeea419a45c403136f86d5a663cd396989df957eebd379dec5dcba2b83c977e"
_T9X10 = {13258: "1c0000009567394f0329c92303187bb22090bbee981e5d716d7cc06f5a38f649ddbfe76d1accea36fbdb80c8fd10b432663cd396989df957eebd379dec5dcba2b83c977e",
          13259: "160100009767394f6300634f80dc80c881dc754f981e5dd16d7cc06f5a38f6c9ddbfe76d1accea36dd923cc287a095a18f7c51259cdf997feebd379dec5dcba2b83c977e",
          13275: "0e000000b767394f0389e41103187bb22090bbee981e5db16d7cc06f5a38f6c9ddbfe76d1accea367cd972a4176939a8cd3c05759d480e5aeebd379dec5dcba2b83c977e",
          13285: "e1000000cb67394f63c92b5e00634f162090bbee981e5d516d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939983d49e411e496d7d1787f397dec5dcba2b83c977e"}
_T9X1AT = ("8afc46489cdf", "717c309fdcdf", "e93c0296fce2", "727ce5afbce3",
           "32fce18fdce3", "2efc83cadce6", "89bc95dd3ce7", "1fbcb2085ce7",
           "03bc76619ce8", "03bc77619ce8", "997c948c9ce8", "60fcb6f11cec",
           "85fc201c3cec", "943ce6727cec", "267c30957cec")
_T9X1AC = ((0, 0x16), (1, 0x01), (2, 0x00), (3, 0x00), (5, 0x67),
          (6, 0x39), (7, 0x4f), (8, 0x63), (9, 0x00), (10, 0x63),
          (11, 0x4f), (12, 0x80), (13, 0xdc), (14, 0x80), (15, 0xc8),
          (16, 0x81), (17, 0xdc), (18, 0x75), (19, 0x4f), (20, 0x98),
          (21, 0x1e), (22, 0x5d), (23, 0xd1), (24, 0x6d), (25, 0x7c),
          (26, 0xc0), (27, 0x6f), (28, 0x5a), (29, 0x38), (30, 0xf6),
          (31, 0xc9), (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d),
          (36, 0x1a), (37, 0xcc), (38, 0xea), (39, 0x36), (40, 0xdd),
          (41, 0x92), (42, 0x3c), (43, 0xc2), (44, 0x87), (45, 0xa0),
          (46, 0x95), (47, 0xa1), (54, 0x99), (55, 0x7f), (56, 0xee),
          (57, 0xbd), (58, 0x37), (59, 0x9d), (60, 0xec), (61, 0x5d),
          (62, 0xcb), (63, 0xa2), (64, 0xb8), (65, 0x3c), (66, 0x97),
          (67, 0x7e))
_T9X1BT = ("a63c4589ddf92d38", "5a3cb40e9d906b35", "6b7cd10e9d906b35",
           "547ca1b41ddcf23a", "06fc35c7dde9c327", "10fc02a25d31ba3d",
           "c83c9518bd14ee2f", "5c7c56c91d946b35", "017cb8b8dda0ab32")
_T9X1BC = ((0, 0x0e), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0x67),
          (6, 0x39), (7, 0x4f), (8, 0x03), (9, 0x89), (10, 0xe4),
          (11, 0x11), (12, 0x03), (13, 0x18), (14, 0x7b), (15, 0xb2),
          (16, 0x20), (17, 0x90), (18, 0xbb), (19, 0xee), (20, 0x98),
          (21, 0x1e), (22, 0x5d), (23, 0xb1), (24, 0x6d), (25, 0x7c),
          (26, 0xc0), (27, 0x6f), (28, 0x5a), (29, 0x38), (30, 0xf6),
          (31, 0xc9), (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d),
          (36, 0x1a), (37, 0xcc), (38, 0xea), (39, 0x36), (40, 0x7c),
          (41, 0xd9), (42, 0x72), (43, 0xa4), (44, 0x17), (45, 0x69),
          (46, 0x39), (47, 0xa8), (56, 0xee), (57, 0xbd), (58, 0x37),
          (59, 0x9d), (60, 0xec), (61, 0x5d), (62, 0xcb), (63, 0xa2),
          (64, 0xb8), (65, 0x3c), (66, 0x97), (67, 0x7e))
_T9X1QT = ("3d49e23ed28f", "3d4fc5bd503b", "3d511cfd2630",
           "bd5cb47c8b8b", "bd5e057cb58d", "bd64cafc842b",
           "bd640b3d963e", "bd6493bb9c3e", "bd667f7e2246",
           "bd6647fc9d48", "3d77093ebab5", "bd77e8bface7",
           "bd792ffb35ef", "3d7a01fc6e27", "3d7c21be2c44",
           "3d49787f397d")
_T9X1QB = ("e1672b5e5149b698e496d7", "e767635031c93638f89769",
           "e9680b2031c9b608ff96d7", "e7686b7d51c9b668891f3e")
_T9X1QN = "6e28fcc611c936280097d7"
_T9X1QC = ((1, 0x00), (2, 0x00), (3, 0x00), (6, 0x39), (7, 0x4f),
          (8, 0x63), (9, 0xc9), (12, 0x00), (13, 0x63), (14, 0x4f),
          (15, 0x16), (16, 0x20), (17, 0x90), (18, 0xbb), (19, 0xee),
          (20, 0x98), (21, 0x1e), (22, 0x5d), (24, 0x6d), (25, 0x7c),
          (26, 0xc0), (27, 0x6f), (28, 0x5a), (29, 0x38), (30, 0xf6),
          (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d), (36, 0x1a),
          (37, 0xcc), (38, 0xea), (40, 0x7c), (41, 0xd9), (42, 0x72),
          (43, 0xa4), (44, 0x17), (45, 0x69), (46, 0x39),
          (50, 0xe4), (51, 0x11), (55, 0xd1), (60, 0xec), (61, 0x5d),
          (62, 0xcb), (63, 0xa2), (64, 0xb8), (65, 0x3c), (66, 0x97),
          (67, 0x7e))
_T9Y1T = ("28932ada49d8", "28932ade49d8", "2893a8dd62df", "2893735e19e2",
           "a8939f5fca0e", "2894195e2a09", "6894ac5c202c", "68941ed9202c",
           "6894405cb0b3", "a894e6ddeee8", "a8940ddd30ea", "a894f8de34ea",
           "e894add98b00", "a895a8de6b51", "a895ab59247a", "e895ee58059d")
_T9Y1B = ("3d49787f397d", "3d49e23ed28f", "3d4fc5bd503b", "3d511cfd2630",
           "bd5cb47c8b8b")
_T9Y1C = ((0, 0x6e), (1, 0x0e), (2, 0x00), (3, 0x00), (7, 0xf3),
          (8, 0x87), (9, 0x96), (10, 0xfc), (11, 0xc6), (12, 0x00),
          (13, 0x63), (14, 0x4f), (15, 0x16), (16, 0x20), (17, 0x90),
          (18, 0xbb), (19, 0xee), (20, 0x98), (21, 0x1e), (22, 0x5d),
          (23, 0x11), (24, 0x6d), (25, 0x7c), (26, 0xc0), (27, 0x6f),
          (28, 0x5a), (29, 0x38), (30, 0xf6), (31, 0xc9), (32, 0xdd),
          (33, 0xbf), (34, 0xe7), (35, 0x6d), (36, 0x1a), (37, 0xcc),
          (38, 0xea), (39, 0x36), (40, 0x7c), (41, 0xd9), (42, 0x72),
          (43, 0xa4), (44, 0x17), (45, 0x69), (46, 0x39), (47, 0x28),
          (50, 0xe4), (51, 0x11), (52, 0x00), (53, 0x97), (54, 0xd7),
          (55, 0xd1), (64, 0xb8), (65, 0x3c), (66, 0x97), (67, 0x7e))
_T9Z1T = ("932ada49d8", "932ade49d8", "93a8dd62df", "93735e19e2",
           "939f5fca0e", "94195e2a09", "94ac5c202c", "941ed9202c",
           "94405cb0b3", "94e6ddeee8", "940ddd30ea", "94f8de34ea",
           "94add98b00", "95a8de6b51", "95ab59247a", "95ee58059d")
_T9Z1B = ("bd5e057cb58d", "bd64cafc842b", "bd640b3d963e",
           "bd6493bb9c3e", "bd667f7e2246", "bd6647fc9d48",
           "3d77093ebab5", "bd77e8bface7", "bd792ffb35ef",
           "3d7a01fc6e27", "3d7c21be2c44")
_T9Z1HI = (0x2, 0x2, 0x2, 0x2, 0xa, 0x2, 0x6, 0x6,
            0x6, 0xa, 0xa, 0xa, 0xe, 0xa, 0xa, 0xe)
_T9Z1LO = (0x8, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0x9, 0xa, 0xa)
_T9Z1C = ((0, 0x6e), (1, 0x0e), (2, 0x00), (3, 0x00), (7, 0xf3),
          (8, 0x87), (9, 0x96), (10, 0xfc), (11, 0xc6), (12, 0x00),
          (13, 0x63), (14, 0x4f), (15, 0x16), (16, 0x20), (17, 0x90),
          (18, 0xbb), (19, 0xee), (20, 0x98), (21, 0x1e), (22, 0x5d),
          (23, 0x11), (24, 0x6d), (25, 0x7c), (26, 0xc0), (27, 0x6f),
          (28, 0x5a), (29, 0x38), (30, 0xf6), (31, 0xc9), (32, 0xdd),
          (33, 0xbf), (34, 0xe7), (35, 0x6d), (36, 0x1a), (37, 0xcc),
          (38, 0xea), (39, 0x36), (40, 0x7c), (41, 0xd9), (42, 0x72),
          (43, 0xa4), (44, 0x17), (45, 0x69), (46, 0x39), (47, 0x28),
          (50, 0xe4), (51, 0x11), (52, 0x00), (53, 0x97),
          (54, 0xd7), (55, 0xd1), (64, 0xb8), (65, 0x3c), (66, 0x97),
          (67, 0x7e))
_T9A2D = "16491ee14b6a394f6300634f2090bbee981e5d516d7cc06f5a38f649ddbfe76d1acceab67cd972a41769396872bc31ab59b884b6eebd379dec5dcba2b83c977e"
_T9A20 = {13606: "850000004d6ae9378a93643800634f162090bbee981e5db16d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da36d9a56bb83c977e",
          13607: "530800004f6ae9378a134f860054f6642402b9eb981e5db16d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da83da7fd44fbc5697",
          13623: "420000006feaa7c2247b329c0037ea17050472d7981e5db16d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da0adf575591fc43e8",
          13624: "2100000071eaa7c2243d194e0014e05be403b9eb981e5db16d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da0adf57558b3cd6a3",
          13633: "f002000083eaa7c22401267ce4d6700abfe905bafcccd1156d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da0adf575517bc8077"}
_T9A2AT = ("5498bcf197", "57f5bc5300", "67d9fc42c7", "69adfc3283",
           "69fabce283", "6a3dbc1829", "6a55fc2029", "6a32fcd331",
           "7c60bcd3ce", "7dbbbc1074", "7f4f3c4017", "7fdc7cb030",
           "9190bcb2d5", "972f7cd435", "97073cc450")
_T9A2AC = ((0, 0x53), (1, 0x08), (2, 0x00), (3, 0x00), (5, 0x6a),
          (6, 0xe9), (7, 0x37), (8, 0x8a), (9, 0x13), (10, 0x4f),
          (11, 0x86), (12, 0x00), (14, 0xf6), (15, 0x64), (16, 0x24),
          (17, 0x02), (18, 0xb9), (19, 0xeb), (20, 0x98), (21, 0x1e),
          (22, 0x5d), (23, 0xb1), (24, 0x6d), (25, 0x7c), (26, 0xc0),
          (27, 0x6f), (28, 0x5a), (29, 0x38), (30, 0xf6), (31, 0x49),
          (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d), (36, 0x1a),
          (37, 0xcc), (38, 0xea), (39, 0xb6), (40, 0x7c), (41, 0xd9),
          (42, 0x72), (43, 0xa4), (44, 0x17), (45, 0x69), (46, 0x39),
          (47, 0xd8), (48, 0x72), (49, 0xbc), (50, 0x31), (51, 0xab),
          (52, 0x59), (53, 0xb8), (54, 0x84), (55, 0x76), (56, 0xce),
          (57, 0xf0), (58, 0x17), (59, 0xda), (60, 0x83), (61, 0xda),
          (62, 0x7f), (63, 0xd4))
_T9A2BT = ("14e05b9b7cc5be", "0bc44d63bc9393", "ff3d78797c987e",
           "caf507f8bc8453", "6580862d7c16f9", "8fb231133c156a",
           "2ae05bbbbc0652", "1ab53f793cf874")
_T9A2BC = ((0, 0x21), (1, 0x00), (2, 0x00), (3, 0x00), (5, 0xea),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x3d), (10, 0x19),
          (11, 0x4e), (12, 0x00), (16, 0xe4), (17, 0x03), (18, 0xb9),
          (19, 0xeb), (20, 0x98), (21, 0x1e), (22, 0x5d), (23, 0xb1),
          (24, 0x6d), (25, 0x7c), (26, 0xc0), (27, 0x6f), (28, 0x5a),
          (29, 0x38), (30, 0xf6), (31, 0x49), (32, 0xdd), (33, 0xbf),
          (34, 0xe7), (35, 0x6d), (36, 0x1a), (37, 0xcc), (38, 0xea),
          (39, 0xb6), (40, 0x7c), (41, 0xd9), (42, 0x72), (43, 0xa4),
          (44, 0x17), (45, 0x69), (46, 0x39), (47, 0xd8), (48, 0x72),
          (49, 0xbc), (50, 0x31), (51, 0xab), (52, 0x59), (53, 0xb8),
          (54, 0x84), (55, 0x76), (56, 0xce), (57, 0xf0), (58, 0x17),
          (59, 0xda), (60, 0x0a), (61, 0xdf), (62, 0x57), (63, 0x55))
_T9A2QT = ("c49fa4ed1c1ccd", "e4efb59526bccf", "04bfc77d57bccf",
           "24afaa8df23cd0", "c47fd50d4a7cd1", "246fe52d259cd1",
           "848fc975e59cd1", "e49fe1fde11cd2", "043fdb7589bcd4",
           "84bfb145d51cd6", "84cfb69dd51cd6", "442fd935593cd6",
           "24fffd7d579cd6", "c42fa945469cd6", "c43fae9d469cd6",
           "e4bfe905bafccc")
_T9A2QB = ("f0267c17bc8077", "634465863ce307", "d4821132bc2029",
           "2bc0a5a17c5024")
_T9A2QN = "d48211eb7ca52f"
_T9A2QC = ((1, 0x02), (2, 0x00), (3, 0x00), (6, 0xa7),
          (7, 0xc2), (8, 0x24), (9, 0x01), (14, 0x70),
          (15, 0x0a), (22, 0xd1), (23, 0x15), (24, 0x6d), (25, 0x7c),
          (26, 0xc0), (27, 0x6f), (28, 0x5a), (29, 0x38), (30, 0xf6),
          (31, 0x49), (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d),
          (36, 0x1a), (37, 0xcc), (38, 0xea), (39, 0xb6), (40, 0x7c),
          (41, 0xd9), (42, 0x72), (43, 0xa4), (44, 0x17), (45, 0x69),
          (46, 0x39), (47, 0xd8), (48, 0x72), (49, 0xbc), (50, 0x31),
          (51, 0xab), (52, 0x59), (53, 0xb8), (54, 0x84), (55, 0x76),
          (56, 0xce), (57, 0xf0), (58, 0x17), (59, 0xda), (60, 0x0a),
          (61, 0xdf), (62, 0x57), (63, 0x55))
_T9B2T = ("007c71bd5ee9", "ab7c21075eef", "753c55345eef", "aa3c03435eef",
           "73fc80135eff", "03bc4592beff", "cdfc80bfbeff", "b2fcd2fcdeff",
           "c6bc6546de05", "5ffc4247de05", "973c034bde05", "7c3cd0cdbe0b",
           "90fc354cfe14", "4e7c84d23e16", "4e7c85d23e16", "20fc70955e1c")
_T9B2B = ("e452bfe905bafccc", "c4539fa4ed1c1ccd", "e452efb59526bccf",
           "0453bfc77d57bccf", "2453afaa8df23cd0", "c4527fd50d4a7cd1",
           "24536fe52d259cd1", "84538fc975e59cd1", "e4539fe1fde11cd2",
           "04533fdb7589bcd4", "8453bfb145d51cd6", "8453cfb69dd51cd6",
           "44522fd935593cd6", "2453fffd7d579cd6", "c4532fa945469cd6",
           "c4533fae9d469cd6")
_T9B2C = ((0, 0xd4), (1, 0x20), (2, 0x00), (3, 0x00), (6, 0xa7),
          (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0x82), (11, 0x11),
          (14, 0x0d), (15, 0xa7), (22, 0xd1), (23, 0x15), (31, 0x9f),
          (32, 0xdd), (33, 0xbf), (34, 0xe7), (35, 0x6d), (36, 0x1a),
          (37, 0xcc), (38, 0xea), (39, 0xb6), (40, 0x7c), (41, 0xd9),
          (42, 0x72), (43, 0xa4), (44, 0x17), (45, 0x69), (46, 0x39),
          (47, 0xd8), (48, 0x72), (49, 0xbc), (50, 0x31), (51, 0xab),
          (52, 0x59), (53, 0xb8), (54, 0x84), (55, 0x76), (56, 0xce),
          (57, 0xf0), (58, 0x17), (59, 0xda), (60, 0x0a), (61, 0xdf),
          (62, 0x57), (63, 0x55), (64, 0xeb), (65, 0x7c), (66, 0xa5),
          (67, 0x2f))
_T9C20 = {13953: "0400000003eda7c28426c32909b0063b412077dd981e5db16d7cc06f5a38f649ddbfe76d1acceab67cd972a4176939d872bc31ab59b88476cef017da0adf5755343c8875",
          13954: "8702000005eda7c22401d660c1d4700aeeb658dbb8e5177aeafc1f9b41f7ef791acceab67cd972a4176939d872bc31ab59b88476cef017da0adf5755343c887583597191",
          13955: "8728000007eda7c22401d66041e7ffd8eeb658dbb8e5175ac1aae11404f96f321ef3ac6e7cd972a4176939d872bc31ab59b88476cef017da0adf5755343c887524559192",
          13971: "0a01000027eda7c22437d570006bb043c1dd166bb8e517badc3c3520fbac6cc37efc4b95bf2fdb707cd972a4176939d872bc31ab59b88476cef017da0adf5755343c8875",
          13981: "871200003beda7c22401d660c1e6a901eeb658dbb8e5179a7bbfa76267651b8edfd5700af988d6a7955f724c9b85968372bc31ab59b88476cef017da0adf5755343c8875"}
_T9C2AT = ("c1aa7eaf3b1ef3", "c112f9cf505ef4", "c1b87e0f5a5ef4",
           "e1b2f90ffbdef7", "c11e7f1f2f3ef9", "c17e7f07d79ef9",
           "e13e7ee794fe01", "e162f8877d7e05", "e18af92707de06",
           "c1047fdf115e07", "c196f8e7ab3e13", "c1307ecf795e13",
           "e1d8f83fdc5e13", "c1be7f3fe97e14", "c132f807a19e14")
_T9C2AC = ((0, 0x87), (1, 0x28), (2, 0x00), (3, 0x00), (5, 0xed),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6),
          (11, 0x60), (12, 0x41), (13, 0xe7), (14, 0xff), (15, 0xd8),
          (16, 0xee), (17, 0xb6), (18, 0x58), (19, 0xdb), (20, 0xb8),
          (21, 0xe5), (22, 0x17), (23, 0x5a), (25, 0xaa), (26, 0xe1),
          (27, 0x14), (35, 0x6e), (36, 0x7c), (37, 0xd9), (38, 0x72),
          (39, 0xa4), (40, 0x17), (41, 0x69), (42, 0x39), (43, 0xd8),
          (44, 0x72), (45, 0xbc), (46, 0x31), (47, 0xab), (48, 0x59),
          (49, 0xb8), (50, 0x84), (51, 0x76), (52, 0xce), (53, 0xf0),
          (54, 0x17), (55, 0xda), (56, 0x0a), (57, 0xdf), (58, 0x57),
          (59, 0x55), (60, 0x34), (61, 0x3c), (62, 0x88), (63, 0x75),
          (64, 0x24), (65, 0x55), (66, 0x91), (67, 0x92))
_T9C2BT = ("02fd4ba87f7ea2e7", "43fc135a1f8ca2e7", "7efc175a1f8ca2e7",
           "95fcc7d9bf12d1fa", "4afccb7c7f9446b8", "48bfe3353f6a7504",
           "98bf3359ff4c1ecb", "1abfbba83f5c35f1", "e2bf2f411f0797d4")
_T9C2BC = ((0, 0x0a), (1, 0x01), (2, 0x00), (3, 0x00), (5, 0xed),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x37), (10, 0xd5),
          (11, 0x70), (12, 0x00), (13, 0x6b), (14, 0xb0), (15, 0x43),
          (16, 0xc1), (17, 0xdd), (18, 0x16), (19, 0x6b), (20, 0xb8),
          (21, 0xe5), (22, 0x17), (24, 0xdc), (25, 0x3c), (26, 0x35),
          (27, 0x20), (28, 0xfb), (29, 0xac), (30, 0x6c), (31, 0xc3),
          (40, 0x7c), (41, 0xd9), (42, 0x72), (43, 0xa4), (44, 0x17),
          (45, 0x69), (46, 0x39), (47, 0xd8), (48, 0x72), (49, 0xbc),
          (50, 0x31), (51, 0xab), (52, 0x59), (53, 0xb8), (54, 0x84),
          (55, 0x76), (56, 0xce), (57, 0xf0), (58, 0x17), (59, 0xda),
          (60, 0x0a), (61, 0xdf), (62, 0x57), (63, 0x55), (64, 0x34),
          (65, 0x3c), (66, 0x88), (67, 0x75))
_T9C2QT = ("695d961fbb85", "065e344a5b86", "afdf01795b86", "c8df93a09b86",
           "4f5efda09b86", "135dc6b5fb87", "485c2d0fbb88", "745970c1bb88",
           "85dc74c1bb88", "255ac6c1bb88", "33da4eddfb88", "36de74e9fb88",
           "f65d6b531b8b", "1f5ba2861b8b", "3fdaa97f5b8b", "955f724c9b85")
_T9C2QB = ("bfa7628ef988d6a7", "fc3baace41b8a4a6", "fce74f3e44ab89a7")
_T9C2QN = "fcc738f67e710da6"
_T9C2QC = ((0, 0x87), (1, 0x12), (2, 0x00), (3, 0x00), (5, 0xed),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6),
          (11, 0x60), (12, 0xc1), (13, 0xe6), (14, 0xa9), (15, 0x01),
          (16, 0xee), (17, 0xb6), (18, 0x58), (19, 0xdb), (20, 0xb8),
          (21, 0xe5), (22, 0x17), (23, 0x9a), (28, 0x67),
          (29, 0x65), (30, 0x1b), (32, 0xdf), (33, 0xd5), (34, 0x70),
          (35, 0x0a), (46, 0x96), (47, 0x83), (48, 0x72), (49, 0xbc),
          (50, 0x31), (51, 0xab), (52, 0x59), (53, 0xb8), (54, 0x84),
          (55, 0x76), (56, 0xce), (57, 0xf0), (58, 0x17), (59, 0xda),
          (60, 0x0a), (61, 0xdf), (62, 0x57), (63, 0x55), (64, 0x34),
          (65, 0x3c), (66, 0x88), (67, 0x75))
_T9E20 = "87360100bbeda7c22401d660c1dd166b98a706842dbfd0dcfbfcef4f67651b065ff925c744ab89a77b7c62fb2cb41c84ddd5700a955b42bbcef017da0adf5755343c8875"
_T9E2T = ("695d961fbb85", "065e344a5b86", "afdf01795b86", "c8df93a09b86",
           "4f5efda09b86", "135dc6b5fb87", "485c2d0fbb88", "745970c1bb88",
           "85dc74c1bb88", "255ac6c1bb88", "33da4eddfb88", "36de74e9fb88",
           "f65d6b531b8b", "1f5ba2861b8b", "3fdaa97f5b8b")
_T9E2C = ((0, 0x87), (1, 0x12), (2, 0x00), (3, 0x00), (5, 0xed),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6),
          (11, 0x60), (12, 0xc1), (13, 0xe6), (14, 0xa9), (15, 0x01),
          (16, 0xee), (17, 0xb6), (18, 0x58), (19, 0xdb), (20, 0xb8),
          (21, 0xe5), (22, 0x17), (23, 0x9a), (24, 0xdb), (25, 0xfc),
          (26, 0xc7), (27, 0x38), (28, 0x67), (29, 0x65), (30, 0x1b),
          (31, 0xf6), (32, 0xdf), (33, 0xd5), (34, 0x70), (35, 0x0a),
          (36, 0x7e), (37, 0x71), (38, 0x0d), (39, 0xa6), (46, 0x96),
          (47, 0x83), (48, 0x72), (49, 0xbc), (50, 0x31), (51, 0xab),
          (52, 0x59), (53, 0xb8), (54, 0x84), (55, 0x76), (56, 0xce),
          (57, 0xf0), (58, 0x17), (59, 0xda), (60, 0x0a), (61, 0xdf),
          (62, 0x57), (63, 0x55), (64, 0x34), (65, 0x3c), (66, 0x88),
          (67, 0x75))
_T9E2QT = ("fb7cf848bcb15b", "db7c42aa3cb45b", "1b3c13ab44b45b",
           "1b3c14ab44b45b", "5b3c3602a4b55b", "1bbcb182bcb75b",
           "9b3c412854fe5b", "dbfce2a124195c", "7b7c78ac4c195c",
           "3b7c57dfe41c5c", "db7cc0388c275c", "fbfc226374275c",
           "3bbcf3637c275c", "db3c460bac435c", "9bbc61b644815c",
           "7b7c62fb84955b")
_T9E2QB = ("36845ff925c7a72c", "36249fd665f9a72d",
           "36847fe045a32732", "36e4fffa1d90a732",
           "b6449ffc3d092734", "b644ffe4d50fa734",
           "b6643fd1655ca73f", "36049fc4d5f22745",
           "b6845f9705172745", "b6845fc84d17a745",
           "b6845fa2651ca745", "b6a43fa3edd4a747",
           "b6c47fe34d972747", "36a47fdfb5362758",
           "b604ffb1256aa758")
_T9E2QN = "36e4ffa39dfaa75a"
_T9E2QC = ((0, 0x87), (2, 0x01), (3, 0x00), (6, 0xa7),
          (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6), (11, 0x60),
          (12, 0xc1), (13, 0xdd), (14, 0x16), (15, 0x6b), (16, 0x98),
          (17, 0xa7), (18, 0x06), (20, 0x2d), (21, 0xbf), (22, 0xd0),
          (23, 0xdc), (24, 0xfb), (25, 0xfc), (26, 0xef), (27, 0x4f),
          (28, 0x67), (29, 0x65), (30, 0x1b), (31, 0x06), (36, 0x44),
          (37, 0xab), (38, 0x89), (45, 0xb4), (46, 0x1c), (48, 0xdd),
          (49, 0xd5), (50, 0x70), (51, 0x0a), (54, 0x42),
          (55, 0xbb), (56, 0xce), (57, 0xf0), (58, 0x17), (59, 0xda),
          (60, 0x0a), (61, 0xdf), (62, 0x57), (63, 0x55), (64, 0x34),
          (65, 0x3c), (66, 0x88), (67, 0x75))
# T9F2 storm singles (literals, formula OPEN).
_T9F2S1 = "10000000bbefa7c284360da709b0063bc1dd166bb8e517badc3c3520fbac6cc30bfc83285b64fd767cd972a4176939d872bc31ab59b88476cef017da0adf5755343c8875"
_T9F2S2 = "87080000bdefa7c22401d660013e4e46eeb658dbb8e5179adc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755abca0ae8653cef017da0adf5755343c8875928efd9b"
_T9F2S3 = "87b60000bfefa7c22401d660c1dd166b98a706042dbfd0dc1bfc832867651b5efbdecf8d22ebb76bd7c7c958aed3e225c0416538ebbb85a70adf5755343c88753d61079c"
_T9F2S4 = "87060000dfefa7c22401d66041de18b4eeb658dbb8e5175adc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a9c5b9e4af0f7f820709abe2a250adf5755343c8875"
_T9F2S5 = "76680000f32f742a8813600d41de18b4eeb658dbb8e5175adc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a9c7b7441c0f7f82070d97b6dd66dde3caf343c8875"
# T9F2-B 15-row tab (b49,50,52,53,54,55), off 0..14.
_T9F2BT = ("416527be0fc2", "ad6528bf10a5", "d96590bd16f0",
           "ed6564bd9f57", "ed65a8fea257", "f165353f73c1",
           "f165fdbceec3", "f165fabffcd6", "8966587bb600",
           "896609be3103", "8966267f0451", "8966eefc7f53",
           "35677afbea4e", "356795bd664f", "39678b7c33bb")
_T9F2BC = ((0, 0x87), (1, 0xb6), (2, 0x00), (3, 0x00), (5, 0xef),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6),
          (11, 0x60), (12, 0xc1), (13, 0xdd), (14, 0x16), (15, 0x6b),
          (16, 0x98), (17, 0xa7), (18, 0x06), (19, 0x04), (20, 0x2d),
          (21, 0xbf), (22, 0xd0), (23, 0xdc), (24, 0x1b), (25, 0xfc),
          (26, 0x83), (27, 0x28), (28, 0x67), (29, 0x65), (30, 0x1b),
          (31, 0x5e), (32, 0xfb), (33, 0xde), (34, 0xcf), (35, 0x8d),
          (36, 0x22), (37, 0xeb), (38, 0xb7), (39, 0x6b), (40, 0xd7),
          (41, 0xc7), (42, 0xc9), (43, 0x58), (44, 0xae), (45, 0xd3),
          (46, 0xe2), (47, 0x25), (48, 0xc0), (51, 0x38), (56, 0x0a),
          (57, 0xdf), (58, 0x57), (59, 0x55), (60, 0x34), (61, 0x3c),
          (62, 0x88), (63, 0x75), (64, 0x3d), (65, 0x61), (66, 0x07),
          (67, 0x9c))
# T9F2-C 9-row tab (b48,49,50,51,56,57,58,59), off 0..8.
_T9F2CT = ("3bf110b9a5fb97f6", "3bf110b9faff9af6",
           "3bf110b9a63e13f9", "7b7441c00a7c6d76",
           "1bc3d7aae93c98d4", "5bb6dec38cfef070",
           "1b1f61ae99ffe0de", "7b7441c0283cb4c3",
           "dbcbedb1743f5be7")
_T9F2CC = ((0, 0x87), (1, 0x06), (2, 0x00), (3, 0x00), (5, 0xef),
          (6, 0xa7), (7, 0xc2), (8, 0x24), (9, 0x01), (10, 0xd6),
          (11, 0x60), (12, 0x41), (13, 0xde), (14, 0x18), (15, 0xb4),
          (16, 0xee), (17, 0xb6), (18, 0x58), (19, 0xdb), (20, 0xb8),
          (21, 0xe5), (22, 0x17), (23, 0x5a), (24, 0xdc), (25, 0x3c),
          (26, 0x35), (27, 0x20), (28, 0xfb), (29, 0xac), (30, 0x6c),
          (31, 0xc3), (32, 0x0b), (33, 0xfc), (34, 0x83), (35, 0x28),
          (36, 0x5b), (37, 0x64), (38, 0xfd), (39, 0x76), (40, 0xed),
          (41, 0xde), (42, 0xcf), (43, 0x8d), (44, 0xd7), (45, 0x75),
          (46, 0x5a), (47, 0x9c), (52, 0xf7), (53, 0xf8), (54, 0x20),
          (55, 0x70), (60, 0x0a), (61, 0xdf), (62, 0x57), (63, 0x55),
          (64, 0x34), (65, 0x3c), (66, 0x88), (67, 0x75))
# T9F2Q: 5B tab (b6,b60-63) m0..15 + b5 m-tab (+1 q>=1 m<6) + 8B words.
_T9F2QT = ("74885bf6db", "74af5a38dd", "74035f73dd", "7460d977dd",
           "740dde7204", "7511daed6b", "774adb89aa", "77785be4c0",
           "77785fe4c0", "77d5d9e8c0", "77cd5e2ac9", "78e659104e",
           "78abd84bf7", "79b8dea658", "791559ab58", "746dde3caf")
_T9F2Q5 = (0x6f, 0x6f, 0x6f, 0x6f, 0xaf, 0x6f, 0x30, 0x30,
           0x30, 0x30, 0x30, 0x30, 0x30, 0xb0, 0xb0, 0x30)
_T9F2QB = ("7b7441c0d97b6dd6", "fbcbedb1f1bba33c",
           "7b7641c0b77d6076", "fbc7d7aa383d75d0")
_T9F2QC = ((0, 0x76), (1, 0x68), (2, 0x00), (3, 0x00), (7, 0x2a),
          (8, 0x88), (9, 0x13), (10, 0x60), (11, 0x0d), (12, 0x41),
          (13, 0xde), (14, 0x18), (15, 0xb4), (16, 0xee), (17, 0xb6),
          (18, 0x58), (19, 0xdb), (20, 0xb8), (21, 0xe5), (22, 0x17),
          (23, 0x5a), (24, 0xdc), (25, 0x3c), (26, 0x35), (27, 0x20),
          (28, 0xfb), (29, 0xac), (30, 0x6c), (31, 0xc3), (32, 0x0b),
          (33, 0xfc), (34, 0x83), (35, 0x28), (36, 0x5b), (37, 0x64),
          (38, 0xfd), (39, 0x76), (40, 0xed), (41, 0xde), (42, 0xcf),
          (43, 0x8d), (44, 0xd7), (45, 0x75), (46, 0x5a), (47, 0x9c),
          (52, 0xf7), (53, 0xf8), (54, 0x20), (55, 0x70), (64, 0x34),
          (65, 0x3c), (66, 0x88), (67, 0x75))
# T9G2: 16x16 quiet, 6B tab (b10,11,b64-67) + b5[q] + F2QT-rot words.
_T9G2T = ("20c1a73c48ed", "40c3adbc6043", "40c3633c27cf",
          "a0c3c83cb431", "a0c3257c4038", "a0c3e5bc2853",
          "c0c3463ce0f4", "80c4ca3c3292", "80c999bcc1c1",
          "80cbaf3ce4fc", "a0cb8a3c48a4", "e0cbd6bc54a5",
          "20cce7bcc1a7", "c0ccdc3ca69d", "c0cc963c16c2",
          "e0d1727ce713")
_T9G2B5 = (0x30, 0x70, 0x70, 0x70, 0x70, 0xb1, 0x71, 0x31,
           0x31, 0x31, 0x31, 0x31, 0x31, 0x32, 0xb2, 0xb2)
_T9G2C = ((0, 0x60), (1, 0x67), (2, 0x07), (3, 0x00), (7, 0x2a),
          (8, 0x88), (9, 0x13), (12, 0x85), (13, 0xe4), (14, 0x8d),
          (15, 0x41), (16, 0x77), (17, 0x5b), (18, 0xac), (19, 0x6d),
          (20, 0xb8), (21, 0xe5), (22, 0x17), (23, 0x5a), (24, 0xdc),
          (25, 0x3c), (26, 0x35), (27, 0x20), (28, 0xfb), (29, 0xac),
          (30, 0x6c), (31, 0xc3), (32, 0x0b), (33, 0xfc), (34, 0x83),
          (35, 0x28), (36, 0x5b), (37, 0x64), (38, 0xfd), (39, 0x76),
          (40, 0xed), (41, 0xde), (42, 0xcf), (43, 0x8d), (44, 0xd7),
          (45, 0x75), (46, 0x5a), (47, 0x9c), (48, 0xfb), (49, 0x85),
          (50, 0xa7), (51, 0xbc), (52, 0xf7), (53, 0xf8), (54, 0x20),
          (55, 0x70), (56, 0x55), (57, 0x7f), (58, 0x76), (59, 0x51))
# T9H3 storm singles (literals, formula OPEN).
_T9H3S1 = "8600000073f2a7c224b7c577006bb043c1dd166bb8e5177adc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a4ca9bc3168fb1e1f04aecabff20adf5755343c8875"
_T9H3S2 = "64210000757224fea4016057c7b6f8cef5bb2dd6b8e5177adc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a4ca9bc3168fb1e1f04aecabff28f5c3ade627c1884"
_T9H3S3 = "64190200777224fea4016057a77e8befadddcfdc1c3a7ea1dc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a4ca9bc3168fb1e1f04aecabff28f5c3adef97c1884"
# T9H3-A 15-row tab (b16-21), off 0..14.
_T9H3AT = ("14ded83ffc3d", "d7dd6e7bfc3d", "3bdcdeef1c3f",
           "75de68f21c3f", "c65e6ef21c3f", "28dd40c51c43",
           "d35d57173c43", "745f15879c43", "b0dbd7db9c43",
           "015cdddb9c43", "3fdf840b1c45", "8fdc5700bc47",
           "8ddee52c3c48", "de5eeb2c3c48", "75da0a303c48")
_T9H3AC = ((0, 0x64), (1, 0x19), (2, 0x02), (3, 0x00), (5, 0x72),
          (6, 0x24), (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x60),
          (11, 0x57), (12, 0xa7), (13, 0x7e), (14, 0x8b), (15, 0xef),
          (22, 0x7e), (23, 0xa1), (24, 0xdc), (25, 0x3c), (26, 0x35),
          (27, 0x20), (28, 0xfb), (29, 0xac), (30, 0x6c), (31, 0xc3),
          (32, 0x0b), (33, 0xfc), (34, 0x83), (35, 0x28), (36, 0x5b),
          (37, 0x64), (38, 0xfd), (39, 0x76), (40, 0xed), (41, 0xde),
          (42, 0xcf), (43, 0x8d), (44, 0xd7), (45, 0x75), (46, 0x5a),
          (47, 0x4c), (48, 0xa9), (49, 0xbc), (50, 0x31), (51, 0x68),
          (52, 0xfb), (53, 0x1e), (54, 0x1f), (55, 0x04), (56, 0xae),
          (57, 0xca), (58, 0xbf), (59, 0xf2), (60, 0x8f), (61, 0x5c),
          (62, 0x3a), (63, 0xde), (64, 0xf9), (65, 0x7c), (66, 0x18),
          (67, 0x84))
# T9H3-B 10-row tab (b12,16-23), off 0..9.
_T9H3BT = ("e2207fa3b77dd23e07", "2298772116fd2bdbd8",
           "025c7535209d4ba2d5", "02c07bf9ea1d4ca2d5",
           "62c471e14b9d1317dc", "02e07ee784ddeadcc8",
           "4214761fc93d1456df", "62e06fb75d1dc209cc",
           "02f87e4b1bdd1317dc", "220c7759887d6f6cd2")
_T9H3BC = ((0, 0xc4), (1, 0x21), (2, 0x00), (3, 0x00), (5, 0x72),
          (6, 0x24), (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02),
          (11, 0x09), (13, 0xb7), (14, 0xf8), (15, 0xce), (24, 0xdc),
          (25, 0x3c), (26, 0x35), (27, 0x20), (28, 0xfb), (29, 0xac),
          (30, 0x6c), (31, 0xc3), (32, 0x0b), (33, 0xfc), (34, 0x83),
          (35, 0x28), (36, 0x5b), (37, 0x64), (38, 0xfd), (39, 0x76),
          (40, 0xed), (41, 0xde), (42, 0xcf), (43, 0x8d), (44, 0xd7),
          (45, 0x75), (46, 0x5a), (47, 0x4c), (48, 0xa9), (49, 0xbc),
          (50, 0x31), (51, 0x68), (52, 0xfb), (53, 0x1e), (54, 0x1f),
          (55, 0x04), (56, 0xae), (57, 0xca), (58, 0xbf), (59, 0xf2),
          (60, 0x8f), (61, 0x5c), (62, 0x3a), (63, 0xde), (64, 0xe7),
          (65, 0x7c), (66, 0x53), (67, 0xf9))
# T9H3Q: 4x16 tab (b24-30) + 8B block words (b1,12-15,20-22) + b5 rule.
_T9H3QT = ("5fbc61cbbfb8c9", "f77ce7ed1fc7c9", "433c652a5fc7c9",
           "fbbc71fdffccc9", "4c7cc02f3fcdc9", "e0bcc43a3fcdc9",
           "083c269adfcdc9", "e93c378c9ff8c9", "cefc90c9bff8c9",
           "9e7cc33edff8c9", "33fc60b33ff9c9", "f8bc36185ffbc9",
           "fe7c36605ffbc9", "833c807b9f00ca", "c47ca18f3f26ca",
           "2d3cb0055f26ca")
_T9H3QB = ("59826aef2f9eb8e0", "938296ae6b14cd79",
           "5902b3af329eb8e0", "7b027faf0965e746")
_T9H3QC = ((0, 0xc4), (2, 0x02), (3, 0x00), (6, 0x24), (7, 0xfe),
          (8, 0xa4), (9, 0x01), (10, 0x02), (11, 0x09), (16, 0xfd),
          (17, 0x16), (18, 0xdf), (19, 0x19), (23, 0x96), (31, 0x36),
          (32, 0x0b), (33, 0xfc), (34, 0x83), (35, 0x28), (36, 0x5b),
          (37, 0x64), (38, 0xfd), (39, 0x76), (40, 0xed), (41, 0xde),
          (42, 0xcf), (43, 0x8d), (44, 0xd7), (45, 0x75), (46, 0x5a),
          (47, 0x4c), (48, 0xa9), (49, 0xbc), (50, 0x31), (51, 0x68),
          (52, 0xfb), (53, 0x1e), (54, 0x1f), (55, 0x04), (56, 0xae),
          (57, 0xca), (58, 0xbf), (59, 0xf2), (60, 0x8f), (61, 0x5c),
          (62, 0x3a), (63, 0xde), (64, 0xe7), (65, 0x7c), (66, 0x53),
          (67, 0xf9))
# T9I1: 16x16 tab (b32-38) + H3QT-rot words + b28/29[q] + b5 rule.
_T9I1T = ("42fc7b6e9fddd4", "23fcbf739fddd4", "bdfc1b1abfddd4",
          "08fd7bb21fead4", "4dfcbbda3febd4", "13fca7055febd4",
          "d5fc97ec5febd4", "6abf271a5f0ad5", "15fc2b349f0bd5",
          "2bfc33349f0bd5", "f8fce393ff0bd5", "29fc97731f18d5",
          "99fc9b9b3f19d5", "5ffc87c63f19d5", "01fc7326bf19d5",
          "77bfaf35bf38d5")
_T9I1B5 = (0x73, 0x73, 0x73, 0x73, 0x73, 0x73, 0x73, 0x74,
           0x74, 0x74, 0x74, 0x74, 0x74, 0x74, 0x74, 0x75)
_T9I1W = ("c54d", "384e", "3a4e", "674e", "694e", "694e", "6e4e",
          "c44f", "c54f", "c64f", "c94f", "da4f", "da4f", "0450",
          "3151", "3251")
_T9I1C = ((0, 0xc4), (1, 0x61), (2, 0x22), (3, 0x00), (6, 0x24),
          (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02), (11, 0x09),
          (12, 0x02), (13, 0x0e), (14, 0xef), (15, 0x91), (16, 0xdd),
          (17, 0x31), (18, 0xdb), (19, 0xd8), (24, 0x7f), (25, 0x5b),
          (26, 0x7c), (27, 0x67), (30, 0xb6), (31, 0xe1), (39, 0x6f),
          (40, 0xed), (41, 0xde), (42, 0xcf), (43, 0x8d), (44, 0xd7),
          (45, 0x75), (46, 0x5a), (47, 0x4c), (48, 0xa9), (49, 0xbc),
          (50, 0x31), (51, 0x68), (52, 0xfb), (53, 0x1e), (54, 0x1f),
          (55, 0x04), (56, 0xae), (57, 0xca), (58, 0xbf), (59, 0xf2),
          (60, 0x8f), (61, 0x5c), (62, 0x3a), (63, 0xde), (64, 0xe7),
          (65, 0x7c), (66, 0x53), (67, 0xf9))
# T9J1 storm singles (literals, formula OPEN).
_T9J1S1 = "c40300002b7524fea4010209628bef0c747515a919b789f3dc3c3520fbac6cc30bfc83285b64fd76eddecf8dd7755a4ca9bc3168fb1e1f04aecabff28f5c3adee77c53f9"
_T9J1S2 = "c4eb02002d7524fea401020982aeae2239df8151b84d9cbffcf8edff8e5657d0c22dbe33b47b3f37d7755a4ca9bc3168fb1e1f04aecabff28f5c3adee77c53f98cbc2e62"
_T9J1S3 = "c4eb21002f7524fea401020982aeae2219b789b3df7c0746dcd1ea0a80fe8d0822dae23b9fdd617b3b4aa7c5a9bc3168fb1e1f04aecabff28f5c3adee77c53f9da7c1a73"
_T9J1S4 = "c4eb01004f7524fea401020982aeae2239df8151b84d9cbf5cf817ec8e5657e0fcb36b35c940d7b87c8bef0caf11dd4ba9bc3168fb1e1f04aecabff28f5c3adee77c53f9"
_T9J1S5 = "c4eb0100517524fea401020982aeae2239df81d1b84d9cbf5cf817ec8e5657e09cb998a4c940d7787c8bef0ccd68224ba9bc3168fb1e1f04aecabff28f5c3adee77c53f9"
# T9J1-A 15-row tab (b36-41), off 0..14.
_T9J1AT = ("d85b9b7f3b4a", "ffda0b9b7b4a", "02df31a77b4a",
           "63db36a77b4a", "ce5a70cb7b4a", "f0d936139b4c",
           "e85d53139b4c", "495a58139b4c", "fcd9c1679b4d",
           "0d5dc6679b4d", "805d8fa43b4f", "0e5b4ca63b4f",
           "1fde50a63b4f", "935e0400fb4f", "675c28d3fb4f")
_T9J1AC = ((0, 0xc4), (1, 0xeb), (2, 0x21), (3, 0x00), (5, 0x75),
          (6, 0x24), (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02),
          (11, 0x09), (12, 0x82), (13, 0xae), (14, 0xae), (15, 0x22),
          (16, 0x19), (17, 0xb7), (18, 0x89), (19, 0xb3), (20, 0xdf),
          (21, 0x7c), (22, 0x07), (23, 0x46), (24, 0xdc), (25, 0xd1),
          (26, 0xea), (27, 0x0a), (28, 0x80), (29, 0xfe), (30, 0x8d),
          (31, 0x08), (32, 0x22), (33, 0xda), (34, 0xe2), (35, 0x3b),
          (42, 0xa7), (43, 0xc5), (44, 0xa9), (45, 0xbc), (46, 0x31),
          (47, 0x68), (48, 0xfb), (49, 0x1e), (50, 0x1f), (51, 0x04),
          (52, 0xae), (53, 0xca), (54, 0xbf), (55, 0xf2), (56, 0x8f),
          (57, 0x5c), (58, 0x3a), (59, 0xde), (60, 0xe7), (61, 0x7c),
          (62, 0x53), (63, 0xf9), (64, 0xda), (65, 0x7c), (66, 0x1a),
          (67, 0x73))
# T9J1-B 8-row tab (b19,32-35,39,44-47), off 0..7.
_T9J1BT = ("51bcb6ec5f780c73154b", "511cb9f55f080c73154b",
           "d1bcb6e7ed68d16a2f4b", "d19cba3d62a84817e24a",
           "513cb76d26186d793c4b", "511cb9178e08f3dbee4a",
           "d1bcb9a652c8d26a2f4b", "51fcb95cdfe8af89084b")
_T9J1BC = ((0, 0xc4), (1, 0xeb), (2, 0x01), (3, 0x00), (5, 0x75),
          (6, 0x24), (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02),
          (11, 0x09), (12, 0x82), (13, 0xae), (14, 0xae), (15, 0x22),
          (16, 0x39), (17, 0xdf), (18, 0x81), (20, 0xb8), (21, 0x4d),
          (22, 0x9c), (23, 0xbf), (24, 0x5c), (25, 0xf8), (26, 0x17),
          (27, 0xec), (28, 0x8e), (29, 0x56), (30, 0x57), (31, 0xe0),
          (36, 0xc9), (37, 0x40), (38, 0xd7), (40, 0x7c), (41, 0x8b),
          (42, 0xef), (43, 0x0c), (48, 0xa9), (49, 0xbc), (50, 0x31),
          (51, 0x68), (52, 0xfb), (53, 0x1e), (54, 0x1f), (55, 0x04),
          (56, 0xae), (57, 0xca), (58, 0xbf), (59, 0xf2), (60, 0x8f),
          (61, 0x5c), (62, 0x3a), (63, 0xde), (64, 0xe7), (65, 0x7c),
          (66, 0x53), (67, 0xf9))
# T9J1Q: 4x16 tab (b2,b40-43,52,53) + b47 even/odd tabs + 7B words.
_T9J1QT = ("7cf8c8021d88", "bc786d102088", "3c7928e43888",
           "dcf921e58188", "7c794ee58188", "fcf947a98588",
           "1cf989b98588", "fc790a1bf888", "5c7961630989",
           "bcf9cfbc1389", "dc78645a5c89", "7c780ec95c89",
           "dc78a9825d89", "dc78ab825d89", "1c786c96eb89",
           "bcf83069ef89")
_T9J1Q7E = (0xfb, 0x4b, 0x9b, 0xab, 0x2b, 0x3b, 0x6b, 0x1b,
            0xdb, 0x3b, 0x1b, 0x5b, 0xab, 0xab, 0x3b, 0xeb)
_T9J1Q7O = (0xfa, 0x4a, 0x9a, 0xaa, 0x2a, 0x3a, 0x6a, 0x1a,
            0xda, 0x3a, 0x1a, 0x5a, 0xaa, 0xaa, 0x3a, 0xea)
_T9J1Q2 = (0x11, 0x11, 0x11, 0x11, 0x11, 0x10, 0x10, 0x10,
           0x10, 0x10, 0x11, 0x11, 0x11, 0x11, 0x11, 0x10)
_T9J1QB = ("31dedb22d46a2f", "b9dcb7f3baacfb",
           "bf599bcfd46a2f", "acdb551a5c17e2")
_T9J1QC = ((0, 0xc4), (1, 0xeb), (3, 0x00), (5, 0x75), (6, 0x24),
          (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02), (11, 0x09),
          (12, 0x82), (13, 0xae), (14, 0xae), (15, 0x22), (16, 0x39),
          (17, 0xdf), (18, 0x81), (19, 0x91), (20, 0xb8), (21, 0x4d),
          (22, 0x9c), (23, 0xbf), (24, 0xdc), (25, 0xd1), (26, 0xea),
          (27, 0x0a), (28, 0x2e), (29, 0xfc), (30, 0x0b), (31, 0xf6),
          (32, 0x3c), (33, 0x19), (34, 0xe8), (35, 0x1a), (48, 0x5f),
          (49, 0x5b), (50, 0x7c), (51, 0x67), (54, 0x0f), (55, 0x02),
          (56, 0xae), (57, 0xca), (58, 0xbf), (59, 0xf2), (60, 0x8f),
          (61, 0x5c), (62, 0x3a), (63, 0xde), (64, 0xe7), (65, 0x7c),
          (66, 0x53), (67, 0xf9))
# T9J2Q: 16x16 tab (b52,53,56-59) + 6B words (b44-49) + b5 rule.
_T9J2QT = ("ce1acffc202e", "ce1ac33e6c7c", "ee24c03ba0d5",
           "ee2562fbf67b", "6e26c27b46d6", "4e2be6bd7e19",
           "4e2b507d172c", "4e2b6b3f932c", "ce2bc4bea333",
           "ce2b86bb8f7e", "0e36b17ce82a", "ee37f53ef3dd",
           "ee37bdbc6ee0", "2e384afd3e4a", "ce3ca9bcd473",
           "ce3ce47df873")
_T9J2B5 = (0x75, 0x76, 0x76, 0x76, 0x76, 0x76, 0x76, 0x76,
           0x76, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77, 0x77)
_T9J2QB = ("3f7c6481bf03", "54bc36881f04", "993c14f21f07",
           "eafc90f23f10", "b23ca7f23f10", "f3fca354bf10",
           "86fcc45cbf10", "f13c850d1f1f", "adbcb0313f21",
           "d3fc675e7f22", "613c32ad9f2b", "353c87e49f2b",
           "6abc54c1bf2b", "6abc55c1bf2b", "033c36cb7f3d",
           "5e7c9834ff3d")
_T9J2QC = ((0, 0xc4), (1, 0xeb), (2, 0x01), (3, 0x01), (6, 0x24),
          (7, 0xfe), (8, 0xa4), (9, 0x01), (10, 0x02), (11, 0x09),
          (12, 0x82), (13, 0xae), (14, 0xae), (15, 0x22), (16, 0x19),
          (17, 0xb7), (18, 0x89), (19, 0xb3), (20, 0xdf), (21, 0x7c),
          (22, 0x07), (23, 0x46), (24, 0xdc), (25, 0xd1), (26, 0xea),
          (27, 0x0a), (28, 0x2e), (29, 0xfc), (30, 0x0b), (31, 0xf6),
          (32, 0x3c), (33, 0x19), (34, 0xe8), (35, 0x1a), (36, 0x94),
          (37, 0x5d), (38, 0x28), (39, 0x61), (40, 0x7c), (41, 0x1c),
          (42, 0x4d), (43, 0x64), (50, 0xf1), (51, 0x41), (54, 0x7c),
          (55, 0x67), (60, 0x8f), (61, 0x5c), (62, 0x3a), (63, 0xde),
          (64, 0xe7), (65, 0x7c), (66, 0x53), (67, 0xf9))
# T9K1 storm singles (literals, formula OPEN).
_T9K1S1 = "c4110000e37724fea4010209625b7c67747515a919b789b3df7c0746dcd1ea0a2efc0bf63c19e81a8a5ca24a789a9497a9bc3168fb1e1f04aecabff28f5c3adee77c53f9"
_T9K1S2 = "c4eb0700e57724fea401020982aeae2239df8151b84d9cbf5cf817ec8e5657e01cb94495c940d7a8988fa05dd3a4bc621b53d52b0e9bf7258f5c3adee77c53f9a07bd239"
_T9K1S3 = "40bc7e00e7f740e2e81b209082aeae2239df8151b84d9cbf5cf817ec8e5657e01cb94495c940d7a8988fa05dd3a4bc621b53d52b0e9bf725b9dd815ce77c53f9347cd239"
_T9K1S4 = "81b80700077886e5a937402062c647d0747515a919b789b3df7c0746dcd1ea0a2efc0bf63c19e81a8a5ca24a789a94575be05d1898aa5e71597e748ba6ddc545e77c53f9"
_T9K1S5 = "81b80700093821738934402062c647d0747515a919b789b3df7c0746dcd1ea0a2efc0bf63c19e81a8a5ca24a789a94575be05d1898aa5e71597e748b5ddbb348e77c53f9"
# T9K1-A 15-row tab (b5,6,56-59), off 0..14.
_T9K1AT = ("37418259ed29", "37414c5ae248", "3741f3db36b0",
           "3741b95872b0", "37416edfb3b1", "b7432edef23f",
           "b74392d9b9ee", "f7432bda2a6b", "f74352d96c6c",
           "b744f45e0795", "374671dc0d9d", "77469ed83903",
           "7846d9d961d2", "b846805bb639", "7847025f9c39")
_T9K1AC = ((0, 0x40), (1, 0xbc), (2, 0x7e), (3, 0x00), (7, 0xe2),
          (8, 0xe8), (9, 0x1b), (10, 0x20), (11, 0x90), (12, 0x82),
          (13, 0xae), (14, 0xae), (15, 0x22), (16, 0x39), (17, 0xdf),
          (18, 0x81), (19, 0x51), (20, 0xb8), (21, 0x4d), (22, 0x9c),
          (23, 0xbf), (24, 0x5c), (25, 0xf8), (26, 0x17), (27, 0xec),
          (28, 0x8e), (29, 0x56), (30, 0x57), (31, 0xe0), (32, 0x1c),
          (33, 0xb9), (34, 0x44), (35, 0x95), (36, 0xc9), (37, 0x40),
          (38, 0xd7), (39, 0xa8), (40, 0x98), (41, 0x8f), (42, 0xa0),
          (43, 0x5d), (44, 0xd3), (45, 0xa4), (46, 0xbc), (47, 0x62),
          (48, 0x1b), (49, 0x53), (50, 0xd5), (51, 0x2b), (52, 0x0e),
          (53, 0x9b), (54, 0xf7), (55, 0x25), (60, 0xe7), (61, 0x7c),
          (62, 0x53), (63, 0xf9), (64, 0x34), (65, 0x7c), (66, 0xd2),
          (67, 0x39))
# T9K1-B 8-row tab (b5-9,60-63), off 0..7.
_T9K1BT = ("7803af4934905b8635", "7803af4934a05d8635",
           "78f138c9349859eb11", "b89daf6933d4583b00",
           "38f238c934e159be30", "f8f16ca9336f5d32d0",
           "38f238c934d959eb31", "78a0ec09342dde64ee")
_T9K1BC = ((0, 0x81), (1, 0xb8), (2, 0x07), (3, 0x00), (10, 0x40),
          (11, 0x20), (12, 0x62), (13, 0xc6), (14, 0x47), (15, 0xd0),
          (16, 0x74), (17, 0x75), (18, 0x15), (19, 0xa9), (20, 0x19),
          (21, 0xb7), (22, 0x89), (23, 0xb3), (24, 0xdf), (25, 0x7c),
          (26, 0x07), (27, 0x46), (28, 0xdc), (29, 0xd1), (30, 0xea),
          (31, 0x0a), (32, 0x2e), (33, 0xfc), (34, 0x0b), (35, 0xf6),
          (36, 0x3c), (37, 0x19), (38, 0xe8), (39, 0x1a), (40, 0x8a),
          (41, 0x5c), (42, 0xa2), (43, 0x4a), (44, 0x78), (45, 0x9a),
          (46, 0x94), (47, 0x57), (48, 0x5b), (49, 0xe0), (50, 0x5d),
          (51, 0x18), (52, 0x98), (53, 0xaa), (54, 0x5e), (55, 0x71),
          (56, 0x59), (57, 0x7e), (58, 0x74), (59, 0x8b), (64, 0xe7),
          (65, 0x7c), (66, 0x53), (67, 0xf9))
# T9K1Q: 4x16 tab (b10,11,64-67) + 9B words (b5-9,60-63).
_T9K1QT = ("40b534fc80c0", "40b534fc81c0", "80b9a57ce0a0",
           "80b97d3cd0bb", "00d651fcc7e3", "00d66dfce4e3",
           "c0d75fbcd774", "00d829bc9000", "40d8323c28bd",
           "80d8787c128e", "00ddbdfcb360", "80f90dfcb3a6",
           "80f92a7c27c8", "40faaffcd431", "80fe6bfcb213",
           "80fe6fbcc813")
_T9K1QB = ("b8f338c934c0d847c0", "f8ef2be93380d84df6",
           "f8f338c93452de20d5", "f89faf6933cbda60fe")
_T9K1QC = ((0, 0x10), (1, 0x48), (2, 0x7b), (3, 0x00), (12, 0xc6),
          (13, 0x61), (14, 0x7c), (15, 0x04), (16, 0x5d), (17, 0x5d),
          (18, 0x45), (19, 0xea), (20, 0x19), (21, 0xb7), (22, 0x89),
          (23, 0xb3), (24, 0xdf), (25, 0x7c), (26, 0x07), (27, 0x46),
          (28, 0xdc), (29, 0xd1), (30, 0xea), (31, 0x0a), (32, 0x2e),
          (33, 0xfc), (34, 0x0b), (35, 0xf6), (36, 0x3c), (37, 0x19),
          (38, 0xe8), (39, 0x1a), (40, 0x8a), (41, 0x5c), (42, 0xa2),
          (43, 0x4a), (44, 0x78), (45, 0x9a), (46, 0x94), (47, 0x57),
          (48, 0x5b), (49, 0xe0), (50, 0x5d), (51, 0x18), (52, 0x98),
          (53, 0xaa), (54, 0x5e), (55, 0x71), (56, 0x59), (57, 0x7e),
          (58, 0x74), (59, 0x8b))
# T9K2Q: 16x16 tab (b1,2,3,13-15,20,21) + K1QT words + b5 rule.
_T9K2QT = ("88f90679ea52e3d8", "889f07f9def601d9",
           "c83c0671e3ee02d9", "083d06f9e51a02d9",
           "c8fb06d1ff1a11d9", "c8c507e9e6c229d9",
           "48980671ead62bd9", "489906f1e0762bd9",
           "c80b0679e98a5fd9", "48340769ea7a82d9",
           "88350741f77682d9", "88d707b1e30e82d9",
           "48d80729ebd682d9", "c86707d1e92a86d9",
           "880406f1d7c687d9", "480d0769dfeaa6d9")
_T9K2B5 = (0x78, 0x78, 0x78, 0x78, 0x79, 0x79, 0x79, 0x79,
           0x79, 0x79, 0x79, 0x79, 0x7a, 0x7a, 0x7a, 0x7a)
_T9K2QC = ((0, 0x10), (6, 0x04), (7, 0xaf), (8, 0x49), (9, 0x34),
          (12, 0xc6), (16, 0xdd), (17, 0xf8), (18, 0x08), (19, 0xda),
          (22, 0xc4), (23, 0x59), (24, 0xdf), (25, 0x7c), (26, 0x07),
          (27, 0x46), (28, 0xdc), (29, 0xd1), (30, 0xea), (31, 0x0a),
          (32, 0x2e), (33, 0xfc), (34, 0x0b), (35, 0xf6), (36, 0x3c),
          (37, 0x19), (38, 0xe8), (39, 0x1a), (40, 0x8a), (41, 0x5c),
          (42, 0xa2), (43, 0x4a), (44, 0x78), (45, 0x9a), (46, 0x94),
          (47, 0x57), (48, 0x5b), (49, 0xe0), (50, 0x5d), (51, 0x18),
          (52, 0x98), (53, 0xaa), (54, 0x5e), (55, 0x71), (56, 0x59),
          (57, 0x7e), (58, 0x74), (59, 0x8b), (60, 0xc1), (61, 0xd8),
          (62, 0xad), (63, 0xe9))
_T7CC = ((0, 0x75), (1, 0x01), (2, 0x00), (3, 0x00), (6, 0xc1),
         (7, 0x6b), (8, 0xfa), (9, 0xf6), (10, 0xcf),
         (11, 0x25), (12, 0x00), (13, 0xad), (14, 0xfc),
         (15, 0x22), (16, 0x39), (17, 0xcb), (18, 0xd3),
         (19, 0x8a), (20, 0x4d), (21, 0xdc), (22, 0xdb),
         (23, 0xd7), (24, 0x53), (25, 0x6d), (26, 0x21),
         (27, 0x3d), (33, 0x58), (34, 0x8b), (35, 0xc9),
         (41, 0x78), (42, 0xbf), (43, 0x06), (44, 0x2f),
         (45, 0xdf), (46, 0x31), (47, 0x6b), (48, 0x4e),
         (49, 0x25), (50, 0x88), (51, 0xe4), (52, 0x51),
         (53, 0x14), (54, 0x69), (55, 0x1b), (56, 0x4d),
         (57, 0xaf), (58, 0xaf), (59, 0x69))
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
    if len(pay) not in (44, 48, 52, 56, 60, 64, 68):
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
    if n <= 6644:  # T7C: quiet-256, tabs b36-40 + B3-walk + b5
        off = n - 6041
        if len(pay) != 60:
            return fail("T7C paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7C lencode")
        m = (off - 348) & 15
        k2 = (off - 348) >> 4
        if pay[5] != (0x51 + (off >= 359) + (off >= 487)):
            return fail("T7C b5")
        if pay[28:33].hex() != _T7B3T[k2]:
            return fail("T7C walk")
        if pay[36] != _T7CT36[m] or pay[37] != _T7CT37[m] or \
                pay[38] != _T7CT38[m] or pay[39] != _T7CT39[m] or \
                pay[40] != _T7CT40[m]:
            return fail("T7C tab")
        for b, v in _T7CC:
            if pay[b] != v:
                return fail("T7C const %d" % b)
        print("CLOSED T7C N=%d off=%d" % (n, off))
        return 0
    if n == 6645:  # solo 56B dip (off=604)
        if len(pay) != 56 or pay.hex() != _T7DIP604:
            return fail("T7DIP604")
        print("CLOSED T7DIP604 N=%d" % n)
        return 0
    if n <= 6647:  # T7D0: 2 post-dip singletons (off=605/606)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7D0[off - 605]:
            return fail("T7D0")
        print("CLOSED T7D0 N=%d off=%d" % (n, off))
        return 0
    if n <= 6662:  # T7D1: 15-row table b0/5/11/27/34/35/43
        off = n - 6041
        if len(pay) != 60:
            return fail("T7D1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7D1 lencode")
        cells = bytes((pay[0], pay[5], pay[11], pay[27], pay[34],
                       pay[35], pay[43])).hex()
        if cells != _T7D1T[off - 607]:
            return fail("T7D1 row")
        for b, v in _T7D1C:
            if pay[b] != v:
                return fail("T7D1 const %d" % b)
        print("CLOSED T7D1 N=%d off=%d" % (n, off))
        return 0
    if n == 6663:  # T7D2 singleton (off=622)
        if len(pay) != 60 or pay.hex() != _T7D2S:
            return fail("T7D2S")
        print("CLOSED T7D2S N=%d" % n)
        return 0
    if n <= 6672:  # T7D2: 9-row chatter table
        off = n - 6041
        if len(pay) != 60:
            return fail("T7D2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7D2 lencode")
        cells = bytes((pay[0], pay[11], pay[19], pay[26], pay[27],
                       pay[34], pay[35], pay[43], pay[48],
                       pay[49])).hex()
        if cells != _T7D2T[off - 623]:
            return fail("T7D2 row")
        for b, v in _T7D2C:
            if pay[b] != v:
                return fail("T7D2 const %d" % b)
        print("CLOSED T7D2 N=%d off=%d" % (n, off))
        return 0
    if n <= 6736:  # T7D3: 4x16 shared tab b48-51 + block words
        off = n - 6041
        if len(pay) != 60:
            return fail("T7D3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7D3 lencode")
        m = (off - 632) & 15
        q = (off - 632) >> 4
        if pay[48:52].hex() != _T7D3T[m]:
            return fail("T7D3 tab")
        blk = bytes((pay[0], pay[11], pay[19], pay[26], pay[27],
                     pay[34], pay[35], pay[43], pay[44], pay[45],
                     pay[46])).hex()
        if blk != _T7D3B[q]:
            return fail("T7D3 blk")
        for b, v in _T7D3C:
            if pay[b] != v:
                return fail("T7D3 const %d" % b)
        print("CLOSED T7D3 N=%d off=%d" % (n, off))
        return 0
    if n <= 6992:  # T7E: 16x16 walk D3T[0..15] + tab b55-59
        off = n - 6041
        if len(pay) != 60:
            return fail("T7E paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7E lencode")
        m = (off - 696) & 15
        q = (off - 696) >> 4
        if pay[5] != (0x54 + (off >= 743) + (off >= 871)):
            return fail("T7E b5")
        if pay[48:52].hex() != _T7D3T[q]:
            return fail("T7E walk")
        if pay[55:60].hex() != _T7ET[m]:
            return fail("T7E tab")
        for b, v in _T7EC:
            if pay[b] != v:
                return fail("T7E const %d" % b)
        print("CLOSED T7E N=%d off=%d" % (n, off))
        return 0
    if n <= 6995:  # T7G0: 3 transition literals (off=952..954)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7G0[off - 952]:
            return fail("T7G0")
        print("CLOSED T7G0 N=%d off=%d" % (n, off))
        return 0
    if n <= 7010:  # T7G1: 15-row table b5-9
        off = n - 6041
        if len(pay) != 60:
            return fail("T7G1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7G1 lencode")
        if pay[5:10].hex() != _T7G1T[off - 955]:
            return fail("T7G1 row")
        for b, v in _T7G1C:
            if pay[b] != v:
                return fail("T7G1 const %d" % b)
        print("CLOSED T7G1 N=%d off=%d" % (n, off))
        return 0
    if n == 7011:  # T7G2 singleton (off=970)
        if len(pay) != 60 or pay.hex() != _T7G2S:
            return fail("T7G2S")
        print("CLOSED T7G2S N=%d" % n)
        return 0
    if n <= 7020:  # T7G2: 9-row chatter table
        off = n - 6041
        if len(pay) != 60:
            return fail("T7G2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7G2 lencode")
        cells = bytes((pay[0], pay[5], pay[6], pay[7], pay[8],
                       pay[9], pay[10], pay[11])).hex()
        if cells != _T7G2T[off - 971]:
            return fail("T7G2 row")
        for b, v in _T7G2C:
            if pay[b] != v:
                return fail("T7G2 const %d" % b)
        print("CLOSED T7G2 N=%d off=%d" % (n, off))
        return 0
    if n <= 7084:  # T7G3: 4x16 shared tab b13-17 + block words
        off = n - 6041
        if len(pay) != 60:
            return fail("T7G3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7G3 lencode")
        m = (off - 980) & 15
        q = (off - 980) >> 4
        if pay[13:18].hex() != _T7G3T[m]:
            return fail("T7G3 tab")
        blk = bytes((pay[0], pay[5] - (q == 1 and off >= 999),
                     pay[6], pay[7], pay[8], pay[9], pay[10],
                     pay[11])).hex()
        if blk != _T7G3B[q]:
            return fail("T7G3 blk")
        for b, v in _T7G3C:
            if pay[b] != v:
                return fail("T7G3 const %d" % b)
        print("CLOSED T7G3 N=%d off=%d" % (n, off))
        return 0
    if n <= 7340:  # T7H: 16x16 walk G3T[0..15] + tab b20-23
        off = n - 6041
        if len(pay) != 60:
            return fail("T7H paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7H lencode")
        m = (off - 1044) & 15
        q = (off - 1044) >> 4
        if pay[5] != (0xf7 + (off >= 1127) + (off >= 1255)):
            return fail("T7H b5")
        if pay[13:18].hex() != _T7G3T[q]:
            return fail("T7H walk")
        if pay[20:24].hex() != _T7HT[m]:
            return fail("T7H tab")
        for b, v in _T7HC:
            if pay[b] != v:
                return fail("T7H const %d" % b)
        print("CLOSED T7H N=%d off=%d" % (n, off))
        return 0
    if n <= 7342:  # T7I0: 2 transition literals (off=1300/1301)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7I0[off - 1300]:
            return fail("T7I0")
        print("CLOSED T7I0 N=%d off=%d" % (n, off))
        return 0
    if n <= 7358:  # T7I1: 16-row table b28-32
        off = n - 6041
        if len(pay) != 60:
            return fail("T7I1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7I1 lencode")
        if pay[28:33].hex() != _T7I1T[off - 1302]:
            return fail("T7I1 row")
        for b, v in _T7I1C:
            if pay[b] != v:
                return fail("T7I1 const %d" % b)
        print("CLOSED T7I1 N=%d off=%d" % (n, off))
        return 0
    if n <= 7368:  # T7I2: 10-row chatter b28-34
        off = n - 6041
        if len(pay) != 60:
            return fail("T7I2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7I2 lencode")
        cells = bytes((pay[28], pay[29], pay[30], pay[31],
                       pay[32], pay[33], pay[34])).hex()
        if cells != _T7I2T[off - 1318]:
            return fail("T7I2 row")
        for b, v in _T7I2C:
            if pay[b] != v:
                return fail("T7I2 const %d" % b)
        print("CLOSED T7I2 N=%d off=%d" % (n, off))
        return 0
    if n <= 7432:  # T7I3: 64-body, 16-tabs b36-40
        off = n - 6041
        if len(pay) != 60:
            return fail("T7I3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7I3 lencode")
        m = (off - 1328) & 15
        q = (off - 1328) >> 4
        if pay[5] != (0xd9 + (off >= 1383)):
            return fail("T7I3 b5")
        if pay[28:35].hex() != _T7I3B[q]:
            return fail("T7I3 blk")
        if pay[36] != _T7I3T36[m] or pay[37] != _T7I3T37[m] or \
                pay[38] != _T7I3T38[m] or pay[39] != _T7I3T39[m] or \
                pay[40] != _T7I3T40[m]:
            return fail("T7I3 tab")
        for b, v in _T7I3C:
            if pay[b] != v:
                return fail("T7I3 const %d" % b)
        print("CLOSED T7I3 N=%d off=%d" % (n, off))
        return 0
    if n <= 7688:  # T7J: 16x16 band-run, tab + 8B block words
        off = n - 6041
        if len(pay) != 60:
            return fail("T7J paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7J lencode")
        m = (off - 1392) & 15
        q = (off - 1392) >> 4
        if pay[5] != (0xda + (off >= 1511) + (off >= 1639)):
            return fail("T7J b5")
        tab = bytes((pay[36], pay[37], pay[38], pay[39], pay[42],
                     pay[43])).hex()
        if tab != _T7JT[m]:
            return fail("T7J tab")
        blk = bytes((pay[0], pay[1], pay[2], pay[19], pay[26],
                     pay[27], pay[35], pay[40])).hex()
        if blk != _T7JB[q]:
            return fail("T7J blk")
        for b, v in _T7JC:
            if pay[b] != v:
                return fail("T7J const %d" % b)
        print("CLOSED T7J N=%d off=%d" % (n, off))
        return 0
    if n <= 7691:  # T7K0: 3 transition literals (off=1648..1650)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7K0[off - 1648]:
            return fail("T7K0")
        print("CLOSED T7K0 N=%d off=%d" % (n, off))
        return 0
    if n <= 7706:  # T7K1: 15-row table b48-52
        off = n - 6041
        if len(pay) != 60:
            return fail("T7K1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7K1 lencode")
        if pay[48:53].hex() != _T7K1T[off - 1651]:
            return fail("T7K1 row")
        for b, v in _T7K1C:
            if pay[b] != v:
                return fail("T7K1 const %d" % b)
        print("CLOSED T7K1 N=%d off=%d" % (n, off))
        return 0
    if n == 7707:  # T7K2 singleton (off=1666)
        if len(pay) != 60 or pay.hex() != _T7K2S:
            return fail("T7K2S")
        print("CLOSED T7K2S N=%d" % n)
        return 0
    if n <= 7716:  # T7K2a: 9-row table b48-54
        off = n - 6041
        if len(pay) != 60:
            return fail("T7K2a paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7K2a lencode")
        if pay[48:55].hex() != _T7K2AT[off - 1667]:
            return fail("T7K2a row")
        for b, v in _T7K2AC:
            if pay[b] != v:
                return fail("T7K2a const %d" % b)
        print("CLOSED T7K2a N=%d off=%d" % (n, off))
        return 0
    if n == 7717:  # T7K2 singleton2 (off=1676)
        if len(pay) != 60 or pay.hex() != _T7K2S2:
            return fail("T7K2S2")
        print("CLOSED T7K2S2 N=%d" % n)
        return 0
    if n <= 7720:  # T7K2b: 3-row table b46/47/55-59
        off = n - 6041
        if len(pay) != 60:
            return fail("T7K2b paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7K2b lencode")
        cells = bytes((pay[46], pay[47], pay[55], pay[56],
                       pay[57], pay[58], pay[59])).hex()
        if cells != _T7K2BT[off - 1677]:
            return fail("T7K2b row")
        for b, v in _T7K2BC:
            if pay[b] != v:
                return fail("T7K2b const %d" % b)
        print("CLOSED T7K2b N=%d off=%d" % (n, off))
        return 0
    if n <= 7732:  # T7K3a: 12-row table b46/55-59
        off = n - 6041
        if len(pay) != 60:
            return fail("T7K3a paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7K3a lencode")
        cells = bytes((pay[46], pay[55], pay[56], pay[57],
                       pay[58], pay[59])).hex()
        if cells != _T7K3AT[off - 1680]:
            return fail("T7K3a row")
        for b, v in _T7K3AC:
            if pay[b] != v:
                return fail("T7K3a const %d" % b)
        print("CLOSED T7K3a N=%d off=%d" % (n, off))
        return 0
    if n <= 7780:  # T7K3: 3x16 shared 7B tab b46/47/55-59
        off = n - 6041
        if len(pay) != 60:
            return fail("T7K3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7K3 lencode")
        m = (off - 1692) & 15
        q = (off - 1692) >> 4
        cells = bytes((pay[46], pay[47], pay[55], pay[56],
                       pay[57], pay[58], pay[59])).hex()
        if cells != _T7K3T[m]:
            return fail("T7K3 tab")
        if pay[48:55].hex() != _T7K3B[q]:
            return fail("T7K3 blk")
        for b, v in _T7K3C:
            if pay[b] != v:
                return fail("T7K3 const %d" % b)
        print("CLOSED T7K3 N=%d off=%d" % (n, off))
        return 0
    if n <= 8036:  # T7L: 16x16 walk K3T[0..15] + tab b56-59
        off = n - 6041
        if len(pay) != 60:
            return fail("T7L paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7L lencode")
        m = (off - 1740) & 15
        q = (off - 1740) >> 4
        if pay[5] != (0xfc + (off >= 1767) + (off >= 1895)):
            return fail("T7L b5")
        walk = bytes((pay[42], pay[43], pay[51], pay[52], pay[53],
                      pay[54], pay[55])).hex()
        if walk != _T7K3T[q]:
            return fail("T7L walk")
        if pay[56:60].hex() != _T7LT[m]:
            return fail("T7L tab")
        for b, v in _T7LC:
            if pay[b] != v:
                return fail("T7L const %d" % b)
        print("CLOSED T7L N=%d off=%d" % (n, off))
        return 0
    if n <= 8038:  # T7M0: 2 reframe literals (off=1996/1997)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7M0[off - 1996]:
            return fail("T7M0")
        print("CLOSED T7M0 N=%d off=%d" % (n, off))
        return 0
    if n <= 8054:  # T7M1: 16-row table b0/9-13
        off = n - 6041
        if len(pay) != 60:
            return fail("T7M1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7M1 lencode")
        cells = bytes((pay[0], pay[9], pay[10], pay[11], pay[12],
                       pay[13])).hex()
        if cells != _T7M1T[off - 1998]:
            return fail("T7M1 row")
        for b, v in _T7M1C:
            if pay[b] != v:
                return fail("T7M1 const %d" % b)
        print("CLOSED T7M1 N=%d off=%d" % (n, off))
        return 0
    if n == 8055:  # T7M2 singleton (off=2014)
        if len(pay) != 60 or pay.hex() != _T7M2S:
            return fail("T7M2S")
        print("CLOSED T7M2S N=%d" % n)
        return 0
    if n <= 8064:  # T7MB: 9-row bridge b5/13-19
        off = n - 6041
        if len(pay) != 60:
            return fail("T7MB paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7MB lencode")
        cells = bytes((pay[5], pay[13], pay[14], pay[15], pay[16],
                       pay[17], pay[18], pay[19])).hex()
        if cells != _T7MBT[off - 2015]:
            return fail("T7MB row")
        for b, v in _T7MBC:
            if pay[b] != v:
                return fail("T7MB const %d" % b)
        print("CLOSED T7MB N=%d off=%d" % (n, off))
        return 0
    if n <= 8128:  # T7RA: 4x16 regime-A tab b20-25 + blk b13-19
        off = n - 6041
        if len(pay) != 60:
            return fail("T7RA paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7RA lencode")
        m = (off - 2024) & 15
        q = (off - 2024) >> 4
        if pay[20:26].hex() != _T7RAT[m]:
            return fail("T7RA tab")
        if pay[13:20].hex() != _T7RAB[q]:
            return fail("T7RA blk")
        for b, v in _T7RAC:
            if pay[b] != v:
                return fail("T7RA const %d" % b)
        print("CLOSED T7RA N=%d off=%d" % (n, off))
        return 0
    if n <= 8384:  # T7RB: 16x16 walk RAT[0..15] + tab b28-32 + B/C/D
        off = n - 6041
        if len(pay) != 60:
            return fail("T7RB paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7RB lencode")
        m = (off - 2088) & 15
        q = (off - 2088) >> 4
        if pay[20:26].hex() != _T7RAT[q]:
            return fail("T7RB walk")
        if pay[28:33].hex() != _T7RBT[m]:
            return fail("T7RB tab")
        body = bytes((pay[0], pay[1], pay[2], pay[3], pay[5],
                      pay[6], pay[7], pay[8], pay[9], pay[10],
                      pay[11], pay[56])).hex()
        exp = _T7RBB[off >= 2151]
        if off >= 2279:
            exp = exp[:8] + "81" + exp[10:]
        if body != exp:
            return fail("T7RB body")
        for b, v in _T7RBC:
            if pay[b] != v:
                return fail("T7RB const %d" % b)
        print("CLOSED T7RB N=%d off=%d" % (n, off))
        return 0
    if n <= 8387:  # T7N0: 3 transition literals (off=2344..2346)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7N0[off - 2344]:
            return fail("T7N0")
        print("CLOSED T7N0 N=%d off=%d" % (n, off))
        return 0
    if n <= 8402:  # T7N1: 15-row table b28-31/35/40
        off = n - 6041
        if len(pay) != 60:
            return fail("T7N1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7N1 lencode")
        cells = bytes((pay[28], pay[29], pay[30], pay[31],
                       pay[35], pay[40])).hex()
        if cells != _T7N1T[off - 2347]:
            return fail("T7N1 row")
        for b, v in _T7N1C:
            if pay[b] != v:
                return fail("T7N1 const %d" % b)
        print("CLOSED T7N1 N=%d off=%d" % (n, off))
        return 0
    if n == 8403:  # T7N2 singleton (off=2362)
        if len(pay) != 60 or pay.hex() != _T7N2S:
            return fail("T7N2S")
        print("CLOSED T7N2S N=%d" % n)
        return 0
    if n <= 8412:  # T7N2: 9-row chatter table
        off = n - 6041
        if len(pay) != 60:
            return fail("T7N2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7N2 lencode")
        cells = bytes((pay[0], pay[1], pay[2], pay[26], pay[27],
                       pay[35], pay[40], pay[41], pay[42])).hex()
        if cells != _T7N2T[off - 2363]:
            return fail("T7N2 row")
        for b, v in _T7N2C:
            if pay[b] != v:
                return fail("T7N2 const %d" % b)
        print("CLOSED T7N2 N=%d off=%d" % (n, off))
        return 0
    if n == 8413:  # T7N3 singleton (off=2372)
        if len(pay) != 60 or pay.hex() != _T7N3S:
            return fail("T7N3S")
        print("CLOSED T7N3S N=%d" % n)
        return 0
    if n <= 8428:  # T7N3: 15-row table b40-45
        off = n - 6041
        if len(pay) != 60:
            return fail("T7N3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7N3 lencode")
        if pay[40:46].hex() != _T7N3T[off - 2373]:
            return fail("T7N3 row")
        for b, v in _T7N3C:
            if pay[b] != v:
                return fail("T7N3 const %d" % b)
        print("CLOSED T7N3 N=%d off=%d" % (n, off))
        return 0
    if n <= 8476:  # T7N4: 3x16 shared tab b40-45 + block words
        off = n - 6041
        if len(pay) != 60:
            return fail("T7N4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7N4 lencode")
        m = (off - 2388) & 15
        q = (off - 2388) >> 4
        if pay[40:46].hex() != _T7N4T[m]:
            return fail("T7N4 tab")
        blk = bytes((pay[5] - (q == 1 and off >= 2407), pay[30],
                     pay[31], pay[34], pay[35], pay[36], pay[37],
                     pay[38], pay[39])).hex()
        if blk != _T7N4B[q]:
            return fail("T7N4 blk")
        for b, v in _T7N4C:
            if pay[b] != v:
                return fail("T7N4 const %d" % b)
        print("CLOSED T7N4 N=%d off=%d" % (n, off))
        return 0
    if n <= 8732:  # T7O: 16x16 walk N4T[0..15] + tab b48-52
        off = n - 6041
        if len(pay) != 60:
            return fail("T7O paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T7O lencode")
        m = (off - 2436) & 15
        q = (off - 2436) >> 4
        if pay[5] != (0x82 + (off >= 2535) + (off >= 2663)):
            return fail("T7O b5")
        if pay[40:46].hex() != _T7N4T[q]:
            return fail("T7O walk")
        if pay[48:53].hex() != _T7OT[m]:
            return fail("T7O tab")
        for b, v in _T7OC:
            if pay[b] != v:
                return fail("T7O const %d" % b)
        print("CLOSED T7O N=%d off=%d" % (n, off))
        return 0
    if n <= 8734:  # 60-tier tail literals (off=2692/2693)
        off = n - 6041
        if len(pay) != 60 or pay.hex() != _T7TAIL[off - 2692]:
            return fail("T7TAIL")
        print("CLOSED T7TAIL N=%d off=%d" % (n, off))
        return 0
    if n <= 8750:  # T8HEAD: 16-row 64B head b50/51/59-63
        off = n - 8735
        if len(pay) != 64:
            return fail("T8HEAD paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8HEAD lencode")
        cells = bytes((pay[50], pay[51], pay[59], pay[60], pay[61],
                       pay[62], pay[63])).hex()
        if cells != _T8HT[off]:
            return fail("T8HEAD row")
        for b, v in _T8HC:
            if pay[b] != v:
                return fail("T8HEAD const %d" % b)
        print("CLOSED T8HEAD N=%d off=%d" % (n, off))
        return 0
    if n <= 8760:  # T8DIPW: wide dip 8751..8760 (60B lits)
        off = n - 8735
        if len(pay) != 60 or pay.hex() != _T8DIPW[off - 16]:
            return fail("T8DIPW")
        print("CLOSED T8DIPW N=%d off=%d" % (n, off))
        return 0
    if n <= 8824:  # T8R: 4x16 resume tab b60-63 + block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8R paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8R lencode")
        m = (off - 26) & 15
        q = (off - 26) >> 4
        if pay[60:64].hex() != _T8RT[m]:
            return fail("T8R tab")
        blk = bytes((pay[31], pay[39], pay[46], pay[47], pay[55],
                     pay[56], pay[57], pay[58], pay[59])).hex()
        if blk != _T8RB[q]:
            return fail("T8R blk")
        for b, v in _T8RC:
            if pay[b] != v:
                return fail("T8R const %d" % b)
        print("CLOSED T8R N=%d off=%d" % (n, off))
        return 0
    if n <= 9080:  # T8S1: 16x16 walk T8RT[0..15] + tab b8/13-17
        off = n - 8735
        if len(pay) != 64:
            return fail("T8S1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8S1 lencode")
        m = (off - 90) & 15
        q = (off - 90) >> 4
        if pay[5] != (0x04 + (off >= 97) + (off >= 225)):
            return fail("T8S1 b5")
        if pay[60:64].hex() != _T8RT[q]:
            return fail("T8S1 walk")
        tab = bytes((pay[8], pay[13], pay[14], pay[15], pay[16],
                     pay[17])).hex()
        if tab != _T8S1T[m]:
            return fail("T8S1 tab")
        for b, v in _T8S1C:
            if pay[b] != v:
                return fail("T8S1 const %d" % b)
        print("CLOSED T8S1 N=%d off=%d" % (n, off))
        return 0
    if n == 9081:  # solo 60B dip (off=346)
        if len(pay) != 60 or pay.hex() != _T8DIP346:
            return fail("T8DIP346")
        print("CLOSED T8DIP346 N=%d" % n)
        return 0
    if n <= 9084:  # T8P0: 3 post-dip literals (off=347..349)
        off = n - 8735
        if len(pay) != 64 or pay.hex() != _T8P0[off - 347]:
            return fail("T8P0")
        print("CLOSED T8P0 N=%d off=%d" % (n, off))
        return 0
    if n <= 9098:  # T8P1: 14-row table b5/16/20-24
        off = n - 8735
        if len(pay) != 64:
            return fail("T8P1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8P1 lencode")
        cells = bytes((pay[5], pay[16], pay[20], pay[21], pay[22],
                       pay[23], pay[24])).hex()
        if cells != _T8P1T[off - 350]:
            return fail("T8P1 row")
        for b, v in _T8P1C:
            if pay[b] != v:
                return fail("T8P1 const %d" % b)
        print("CLOSED T8P1 N=%d off=%d" % (n, off))
        return 0
    if n == 9099:  # T8P2 singleton (off=364)
        if len(pay) != 64 or pay.hex() != _T8P2S:
            return fail("T8P2S")
        print("CLOSED T8P2S N=%d" % n)
        return 0
    if n <= 9108:  # T8P2: 9-row table b24-30
        off = n - 8735
        if len(pay) != 64:
            return fail("T8P2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8P2 lencode")
        if pay[24:31].hex() != _T8P2T[off - 365]:
            return fail("T8P2 row")
        for b, v in _T8P2C:
            if pay[b] != v:
                return fail("T8P2 const %d" % b)
        print("CLOSED T8P2 N=%d off=%d" % (n, off))
        return 0
    if n == 9109:  # T8P3 singleton (off=374)
        if len(pay) != 64 or pay.hex() != _T8P3S:
            return fail("T8P3S")
        print("CLOSED T8P3S N=%d" % n)
        return 0
    if n <= 9124:  # T8P3: 15-row table b17-19/23/31/36/37
        off = n - 8735
        if len(pay) != 64:
            return fail("T8P3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8P3 lencode")
        cells = bytes((pay[17], pay[18], pay[19], pay[23],
                       pay[31], pay[36], pay[37])).hex()
        if cells != _T8P3T[off - 375]:
            return fail("T8P3 row")
        for b, v in _T8P3C:
            if pay[b] != v:
                return fail("T8P3 const %d" % b)
        print("CLOSED T8P3 N=%d off=%d" % (n, off))
        return 0
    if n <= 9172:  # T8P4: 3x16 shared 7B tab + 7B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8P4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8P4 lencode")
        m = (off - 390) & 15
        q = (off - 390) >> 4
        cells = bytes((pay[17], pay[18], pay[19], pay[23],
                       pay[31], pay[36], pay[37])).hex()
        if cells != _T8P4T[m]:
            return fail("T8P4 tab")
        if pay[24:31].hex() != _T8P4B[q]:
            return fail("T8P4 blk")
        for b, v in _T8P4C:
            if pay[b] != v:
                return fail("T8P4 const %d" % b)
        print("CLOSED T8P4 N=%d off=%d" % (n, off))
        return 0
    if n <= 9428:  # T8Q: 16x16 tab b36-41 + 7B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8Q lencode")
        m = (off - 438) & 15
        q = (off - 438) >> 4
        if pay[5] != (0x47 + (off >= 481) + (off >= 609)):
            return fail("T8Q b5")
        tab = bytes((pay[36], pay[37], pay[38], pay[39], pay[40],
                     pay[41])).hex()
        if tab != _T8QT[m]:
            return fail("T8Q tab")
        blk = bytes((pay[25], pay[26], pay[27], pay[30], pay[31],
                     pay[32], pay[33])).hex()
        if blk != _T8QB[q]:
            return fail("T8Q blk")
        for b, v in _T8QC:
            if pay[b] != v:
                return fail("T8Q const %d" % b)
        print("CLOSED T8Q N=%d off=%d" % (n, off))
        return 0
    if n == 9429:  # solo 60B dip (off=694)
        if len(pay) != 60 or pay.hex() != _T8DIP694:
            return fail("T8DIP694")
        print("CLOSED T8DIP694 N=%d" % n)
        return 0
    if n <= 9431:  # T8R0: 2 post-dip literals (off=695/696)
        off = n - 8735
        if len(pay) != 64 or pay.hex() != _T8R0[off - 695]:
            return fail("T8R0")
        print("CLOSED T8R0 N=%d off=%d" % (n, off))
        return 0
    if n <= 9446:  # T8R1: 15-row table b44-48
        off = n - 8735
        if len(pay) != 64:
            return fail("T8R1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8R1 lencode")
        if pay[44:49].hex() != _T8R1T[off - 697]:
            return fail("T8R1 row")
        for b, v in _T8R1C:
            if pay[b] != v:
                return fail("T8R1 const %d" % b)
        print("CLOSED T8R1 N=%d off=%d" % (n, off))
        return 0
    if n == 9447:  # T8R2 singleton (off=712)
        if len(pay) != 64 or pay.hex() != _T8R2S:
            return fail("T8R2S")
        print("CLOSED T8R2S N=%d" % n)
        return 0
    if n <= 9456:  # T8R2: 9-row table b44-50
        off = n - 8735
        if len(pay) != 64:
            return fail("T8R2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8R2 lencode")
        if pay[44:51].hex() != _T8R2T[off - 713]:
            return fail("T8R2 row")
        for b, v in _T8R2C:
            if pay[b] != v:
                return fail("T8R2 const %d" % b)
        print("CLOSED T8R2 N=%d off=%d" % (n, off))
        return 0
    if n == 9457:  # T8R3 singleton (off=722)
        if len(pay) != 64 or pay.hex() != _T8R3S:
            return fail("T8R3S")
        print("CLOSED T8R3S N=%d" % n)
        return 0
    if n <= 9472:  # T8R3: 15-row table b5/52-57
        off = n - 8735
        if len(pay) != 64:
            return fail("T8R3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8R3 lencode")
        cells = bytes((pay[5], pay[52], pay[53], pay[54], pay[55],
                       pay[56], pay[57])).hex()
        if cells != _T8R3T[off - 723]:
            return fail("T8R3 row")
        for b, v in _T8R3C:
            if pay[b] != v:
                return fail("T8R3 const %d" % b)
        print("CLOSED T8R3 N=%d off=%d" % (n, off))
        return 0
    if n <= 9520:  # T8R4: 3x16 shared 6B tab + 7B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8R4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8R4 lencode")
        m = (off - 738) & 15
        q = (off - 738) >> 4
        if pay[52:58].hex() != _T8R4T[m]:
            return fail("T8R4 tab")
        if pay[44:51].hex() != _T8R4B[q]:
            return fail("T8R4 blk")
        for b, v in _T8R4C:
            if pay[b] != v:
                return fail("T8R4 const %d" % b)
        print("CLOSED T8R4 N=%d off=%d" % (n, off))
        return 0
    if n <= 9776:  # T8S: 16x16 walk R4T[0..15] + tab b43/51/59-63
        off = n - 8735
        if len(pay) != 64:
            return fail("T8S paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8S lencode")
        m = (off - 786) & 15
        q = (off - 786) >> 4
        if pay[5] != (0x4a + (off >= 865) + (off >= 993)):
            return fail("T8S b5")
        if pay[52:58].hex() != _T8R4T[q]:
            return fail("T8S walk")
        tab = bytes((pay[43], pay[51], pay[59], pay[60], pay[61],
                     pay[62], pay[63])).hex()
        if tab != _T8ST[m]:
            return fail("T8S tab")
        for b, v in _T8SC:
            if pay[b] != v:
                return fail("T8S const %d" % b)
        print("CLOSED T8S N=%d off=%d" % (n, off))
        return 0
    if n <= 9779:  # T8T0: 3 reframe literals (off=1042..1044)
        off = n - 8735
        if len(pay) != 64 or pay.hex() != _T8T0[off - 1042]:
            return fail("T8T0")
        print("CLOSED T8T0 N=%d off=%d" % (n, off))
        return 0
    if n <= 9794:  # T8T1: 15-row table b60-63
        off = n - 8735
        if len(pay) != 64:
            return fail("T8T1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8T1 lencode")
        if pay[60:64].hex() != _T8T1T[off - 1045]:
            return fail("T8T1 row")
        for b, v in _T8T1C:
            if pay[b] != v:
                return fail("T8T1 const %d" % b)
        print("CLOSED T8T1 N=%d off=%d" % (n, off))
        return 0
    if n == 9795:  # T8T2 singleton (off=1060)
        if len(pay) != 64 or pay.hex() != _T8T2S:
            return fail("T8T2S")
        print("CLOSED T8T2S N=%d" % n)
        return 0
    if n <= 9804:  # T8T2: 9-row table b5-7/60-63
        off = n - 8735
        if len(pay) != 64:
            return fail("T8T2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8T2 lencode")
        cells = bytes((pay[5], pay[6], pay[7], pay[60], pay[61],
                       pay[62], pay[63])).hex()
        if cells != _T8T2T[off - 1061]:
            return fail("T8T2 row")
        for b, v in _T8T2C:
            if pay[b] != v:
                return fail("T8T2 const %d" % b)
        print("CLOSED T8T2 N=%d off=%d" % (n, off))
        return 0
    if n == 9805:  # T8T3 singleton (off=1070)
        if len(pay) != 64 or pay.hex() != _T8T3S:
            return fail("T8T3S")
        print("CLOSED T8T3S N=%d" % n)
        return 0
    if n <= 9820:  # T8T3: 15-row table b10/60-63
        off = n - 8735
        if len(pay) != 64:
            return fail("T8T3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8T3 lencode")
        cells = bytes((pay[10], pay[60], pay[61], pay[62],
                       pay[63])).hex()
        if cells != _T8T3T[off - 1071]:
            return fail("T8T3 row")
        for b, v in _T8T3C:
            if pay[b] != v:
                return fail("T8T3 const %d" % b)
        print("CLOSED T8T3 N=%d off=%d" % (n, off))
        return 0
    if n <= 9868:  # T8T4: 3x16 shared 5B tab + 7B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8T4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8T4 lencode")
        m = (off - 1086) & 15
        q = (off - 1086) >> 4
        cells = bytes((pay[10], pay[60], pay[61], pay[62],
                       pay[63])).hex()
        if cells != _T8T4T[m]:
            return fail("T8T4 tab")
        blk = bytes((pay[5] - (q == 2 and off >= 1121), pay[6],
                     pay[7], pay[56], pay[57], pay[58],
                     pay[59])).hex()
        if blk != _T8T4B[q]:
            return fail("T8T4 blk")
        for b, v in _T8T4C:
            if pay[b] != v:
                return fail("T8T4 const %d" % b)
        print("CLOSED T8T4 N=%d off=%d" % (n, off))
        return 0
    if n <= 10124:  # T8U: 16x16 walk T4T[0..15] + tab b1/12-15/20
        off = n - 8735
        if len(pay) != 64:
            return fail("T8U paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8U lencode")
        m = (off - 1134) & 15
        q = (off - 1134) >> 4
        if pay[5] != (0x4d + (off >= 1249) + (off >= 1377)):
            return fail("T8U b5")
        walk = bytes((pay[10], pay[60], pay[61], pay[62],
                      pay[63])).hex()
        if walk != _T8T4T[q]:
            return fail("T8U walk")
        tab = bytes((pay[1], pay[12], pay[13], pay[14], pay[15],
                     pay[20])).hex()
        if tab != _T8UT[m]:
            return fail("T8U tab")
        for b, v in _T8UC:
            if pay[b] != v:
                return fail("T8U const %d" % b)
        print("CLOSED T8U N=%d off=%d" % (n, off))
        return 0
    if n <= 10127:  # T8V0: 3 reframe literals (off=1390..1392)
        off = n - 8735
        if len(pay) != 64 or pay.hex() != _T8V0[off - 1390]:
            return fail("T8V0")
        print("CLOSED T8V0 N=%d off=%d" % (n, off))
        return 0
    if n <= 10142:  # T8V1: 15-row table b24-29
        off = n - 8735
        if len(pay) != 64:
            return fail("T8V1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8V1 lencode")
        if pay[24:30].hex() != _T8V1T[off - 1393]:
            return fail("T8V1 row")
        for b, v in _T8V1C:
            if pay[b] != v:
                return fail("T8V1 const %d" % b)
        print("CLOSED T8V1 N=%d off=%d" % (n, off))
        return 0
    if n == 10143:  # T8V2 singleton (off=1408)
        if len(pay) != 64 or pay.hex() != _T8V2S:
            return fail("T8V2S")
        print("CLOSED T8V2S N=%d" % n)
        return 0
    if n <= 10152:  # T8V2: 9-row chatter table
        off = n - 8735
        if len(pay) != 64:
            return fail("T8V2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8V2 lencode")
        cells = bytes((pay[21], pay[22], pay[23], pay[26], pay[27],
                       pay[28], pay[29], pay[30], pay[31])).hex()
        if cells != _T8V2T[off - 1409]:
            return fail("T8V2 row")
        for b, v in _T8V2C:
            if pay[b] != v:
                return fail("T8V2 const %d" % b)
        print("CLOSED T8V2 N=%d off=%d" % (n, off))
        return 0
    if n == 10153:  # T8V3 singleton (off=1418)
        if len(pay) != 64 or pay.hex() != _T8V3S:
            return fail("T8V3S")
        print("CLOSED T8V3S N=%d" % n)
        return 0
    if n <= 10168:  # T8V3: 15-row table b32-37
        off = n - 8735
        if len(pay) != 64:
            return fail("T8V3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8V3 lencode")
        if pay[32:38].hex() != _T8V3T[off - 1419]:
            return fail("T8V3 row")
        for b, v in _T8V3C:
            if pay[b] != v:
                return fail("T8V3 const %d" % b)
        print("CLOSED T8V3 N=%d off=%d" % (n, off))
        return 0
    if n <= 10216:  # T8V4: 3x16 shared 6B tab + 8B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8V4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8V4 lencode")
        m = (off - 1434) & 15
        q = (off - 1434) >> 4
        if pay[32:38].hex() != _T8V4T[m]:
            return fail("T8V4 tab")
        if pay[24:32].hex() != _T8V4B[q]:
            return fail("T8V4 blk")
        for b, v in _T8V4C:
            if pay[b] != v:
                return fail("T8V4 const %d" % b)
        print("CLOSED T8V4 N=%d off=%d" % (n, off))
        return 0
    if n <= 10472:  # T8W: 16x16 walk V4T[0..15] + tab b40-45
        off = n - 8735
        if len(pay) != 64:
            return fail("T8W paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8W lencode")
        m = (off - 1482) & 15
        q = (off - 1482) >> 4
        if pay[5] != (0x4f + (off >= 1505) + (off >= 1633)):
            return fail("T8W b5")
        if pay[32:38].hex() != _T8V4T[q]:
            return fail("T8W walk")
        if pay[40:46].hex() != _T8WT[m]:
            return fail("T8W tab")
        for b, v in _T8WC:
            if pay[b] != v:
                return fail("T8W const %d" % b)
        print("CLOSED T8W N=%d off=%d" % (n, off))
        return 0
    if n <= 10475:  # T8X0: 3 transition literals (off=1738..1740)
        off = n - 8735
        if len(pay) != 64 or pay.hex() != _T8X0[off - 1738]:
            return fail("T8X0")
        print("CLOSED T8X0 N=%d off=%d" % (n, off))
        return 0
    if n <= 10490:  # T8X1: 15-row table b48-53
        off = n - 8735
        if len(pay) != 64:
            return fail("T8X1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8X1 lencode")
        if pay[48:54].hex() != _T8X1T[off - 1741]:
            return fail("T8X1 row")
        for b, v in _T8X1C:
            if pay[b] != v:
                return fail("T8X1 const %d" % b)
        print("CLOSED T8X1 N=%d off=%d" % (n, off))
        return 0
    if n == 10491:  # T8X2 singleton (off=1756)
        if len(pay) != 64 or pay.hex() != _T8X2S:
            return fail("T8X2S")
        print("CLOSED T8X2S N=%d" % n)
        return 0
    if n <= 10500:  # T8X2: 9-row table b5/48-55
        off = n - 8735
        if len(pay) != 64:
            return fail("T8X2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8X2 lencode")
        cells = bytes((pay[5], pay[48], pay[49], pay[50], pay[51],
                       pay[52], pay[53], pay[54], pay[55])).hex()
        if cells != _T8X2T[off - 1757]:
            return fail("T8X2 row")
        for b, v in _T8X2C:
            if pay[b] != v:
                return fail("T8X2 const %d" % b)
        print("CLOSED T8X2 N=%d off=%d" % (n, off))
        return 0
    if n == 10501:  # T8X3 singleton (off=1766)
        if len(pay) != 64 or pay.hex() != _T8X3S:
            return fail("T8X3S")
        print("CLOSED T8X3S N=%d" % n)
        return 0
    if n <= 10516:  # T8X3: 15-row table b39/47/55-59
        off = n - 8735
        if len(pay) != 64:
            return fail("T8X3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8X3 lencode")
        cells = bytes((pay[39], pay[47], pay[55], pay[56],
                       pay[57], pay[58], pay[59])).hex()
        if cells != _T8X3T[off - 1767]:
            return fail("T8X3 row")
        for b, v in _T8X3C:
            if pay[b] != v:
                return fail("T8X3 const %d" % b)
        print("CLOSED T8X3 N=%d off=%d" % (n, off))
        return 0
    if n <= 10564:  # T8X4: 3x16 shared 7B tab + 6B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8X4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8X4 lencode")
        m = (off - 1782) & 15
        q = (off - 1782) >> 4
        cells = bytes((pay[39], pay[47], pay[55] - (q == 1),
                       pay[56], pay[57], pay[58],
                       pay[59])).hex()
        if cells != _T8X4T[m]:
            return fail("T8X4 tab")
        if pay[48:54].hex() != _T8X4B[q]:
            return fail("T8X4 blk")
        for b, v in _T8X4C:
            if pay[b] != v:
                return fail("T8X4 const %d" % b)
        print("CLOSED T8X4 N=%d off=%d" % (n, off))
        return 0
    if n <= 10820:  # T8Y: 16x16 tab b60-63 + 7B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8Y paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8Y lencode")
        m = (off - 1830) & 15
        q = (off - 1830) >> 4
        b5 = (0x52 + (off >= 1889) + (off >= 2017) +
              (m >= 6) * 0x40 + (m >= 13) * 0x40) & 0xff
        if pay[5] != b5:
            return fail("T8Y b5")
        if pay[60:64].hex() != _T8YT[m]:
            return fail("T8Y tab")
        blk = bytes((pay[39], pay[47], pay[55], pay[56], pay[57],
                     pay[58], pay[59])).hex()
        if blk != _T8YB[q]:
            return fail("T8Y blk")
        for b, v in _T8YC:
            if pay[b] != v:
                return fail("T8Y const %d" % b)
        print("CLOSED T8Y N=%d off=%d" % (n, off))
        return 0
    if n <= 10912:  # T8Z storm: 5 singles + Z1 15-row + Z2 9-row + Z3 15-row + Z4 3x16
        off = n - 8735
        if len(pay) != 64:
            return fail("T8Z paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8Z lencode")
        if n in _T8Z0:
            if pay.hex() != _T8Z0[n]:
                return fail("T8Z0 lit %d" % n)
            print("CLOSED T8Z0 N=%d off=%d" % (n, off))
            return 0
        if 10824 <= n <= 10838:
            m = off - 2089
            if bytes((pay[10], pay[11], pay[60], pay[61], pay[62],
                       pay[63])).hex() != _T8Z1T[m]:
                return fail("T8Z1 tab")
            for b, v in _T8Z1C:
                if pay[b] != v:
                    return fail("T8Z1 const %d" % b)
            print("CLOSED T8Z1 N=%d off=%d" % (n, off))
            return 0
        if 10840 <= n <= 10848:
            m = off - 2105
            if bytes((pay[0], pay[9], pay[10], pay[11], pay[60], pay[61],
                       pay[62], pay[63])).hex() != _T8Z2T[m]:
                return fail("T8Z2 tab")
            for b, v in _T8Z2C:
                if pay[b] != v:
                    return fail("T8Z2 const %d" % b)
            print("CLOSED T8Z2 N=%d off=%d" % (n, off))
            return 0
        if 10850 <= n <= 10864:
            m = off - 2115
            if bytes((pay[0], pay[1], pay[12], pay[13], pay[14], pay[15],
                       pay[16], pay[17])).hex() != _T8Z3T[m]:
                return fail("T8Z3 tab")
            for b, v in _T8Z3C:
                if pay[b] != v:
                    return fail("T8Z3 const %d" % b)
            print("CLOSED T8Z3 N=%d off=%d" % (n, off))
            return 0
        if 10865 <= n <= 10912:
            m = off - 2130
            q = (off - 2130) >> 4
            if bytes((pay[0], pay[1], pay[12], pay[13], pay[14], pay[15],
                       pay[16], pay[17])).hex() != _T8Z4T[m]:
                return fail("T8Z4 tab")
            if pay[5] != 0x54 + (off >= 2145):
                return fail("T8Z4 b5")
            blk = bytes((pay[9], pay[10], pay[11], pay[60], pay[61],
                         pay[62], pay[63])).hex()
            if blk != _T8Z4B[q]:
                return fail("T8Z4 blk")
            for b, v in _T8Z4C:
                if pay[b] != v:
                    return fail("T8Z4 const %d" % b)
            print("CLOSED T8Z4 N=%d off=%d" % (n, off))
            return 0
        return fail("T8Z gap %d" % n)
    if n <= 11168:  # T8A1: 16x16 tab b20-25 + 8B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8A1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8A1 lencode")
        m = (off - 2178) & 15
        q = (off - 2178) >> 4
        if pay[5] != 0x55 + (off >= 2273) + (off >= 2401):
            return fail("T8A1 b5")
        if bytes((pay[20], pay[21], pay[22], pay[23], pay[24],
                   pay[25])).hex() != _T8A1T[m]:
            return fail("T8A1 tab")
        blk = bytes((pay[0], pay[1], pay[12], pay[13], pay[14],
                     pay[15], pay[16], pay[17])).hex()
        if blk != _T8A1B[q]:
            return fail("T8A1 blk")
        for b, v in _T8A1C:
            if pay[b] != v:
                return fail("T8A1 const %d" % b)
        print("CLOSED T8A1 N=%d off=%d" % (n, off))
        return 0
    if n <= 11197:  # T8B1 storm: 5 singles + A 15-row + B 9-row
        off = n - 8735
        if len(pay) != 64:
            return fail("T8B1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8B1 lencode")
        if n in _T8B10:
            if pay.hex() != _T8B10[n]:
                return fail("T8B10 lit %d" % n)
            print("CLOSED T8B10 N=%d off=%d" % (n, off))
            return 0
        if 11172 <= n <= 11186:
            m = off - 2437
            if bytes((pay[32], pay[33], pay[34], pay[35], pay[36],
                       pay[37])).hex() != _T8B1AT[m]:
                return fail("T8B1A tab")
            for b, v in _T8B1AC:
                if pay[b] != v:
                    return fail("T8B1A const %d" % b)
            print("CLOSED T8B1A N=%d off=%d" % (n, off))
            return 0
        if 11188 <= n <= 11196:
            m = off - 2453
            if bytes((pay[32], pay[33], pay[34], pay[35], pay[36], pay[37],
                       pay[38], pay[39])).hex() != _T8B1BT[m]:
                return fail("T8B1B tab")
            for b, v in _T8B1BC:
                if pay[b] != v:
                    return fail("T8B1B const %d" % b)
            print("CLOSED T8B1B N=%d off=%d" % (n, off))
            return 0
        return fail("T8B1 gap %d" % n)
    if n <= 11260:  # T8B1Q: 4x16 tab b40-45 + 8B words, k15 early-edge
        off = n - 8735
        if len(pay) != 64:
            return fail("T8B1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8B1Q lencode")
        m = (off - 2463) & 15
        q = (off - 2463) >> 4
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[44],
                   pay[45])).hex() != _T8B1QT[m]:
            return fail("T8B1Q tab")
        blk = bytes((pay[32], pay[33], pay[34], pay[35], pay[36], pay[37],
                     pay[38], pay[39])).hex()
        exp = _T8B1QB[q] if m < 15 else _T8B1QB[q + 1]
        if blk != exp:
            return fail("T8B1Q blk")
        for b, v in _T8B1QC:
            if pay[b] != v:
                return fail("T8B1Q const %d" % b)
        print("CLOSED T8B1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 11516:  # T8C1: 16x16 tab b48-53 + 6B block words
        off = n - 8735
        if len(pay) != 64:
            return fail("T8C1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8C1 lencode")
        m = (off - 2526) & 15
        q = (off - 2526) >> 4
        if pay[5] != 0x57 + (off >= 2529) + (off >= 2657):
            return fail("T8C1 b5")
        if bytes((pay[48], pay[49], pay[50], pay[51], pay[52],
                   pay[53])).hex() != _T8C1T[m]:
            return fail("T8C1 tab")
        blk = bytes((pay[40], pay[41], pay[42], pay[43], pay[44],
                     pay[45])).hex()
        if blk != _T8C1B[q]:
            return fail("T8C1 blk")
        for b, v in _T8C1C:
            if pay[b] != v:
                return fail("T8C1 const %d" % b)
        print("CLOSED T8C1 N=%d off=%d" % (n, off))
        return 0
    if n <= 11545:  # T8D1 storm: 5 singles + A 15-row + B 9-row
        off = n - 8735
        if len(pay) != 64:
            return fail("T8D1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8D1 lencode")
        if n in _T8D10:
            if pay.hex() != _T8D10[n]:
                return fail("T8D10 lit %d" % n)
            print("CLOSED T8D10 N=%d off=%d" % (n, off))
            return 0
        if 11520 <= n <= 11534:
            m = off - 2785
            if bytes((pay[48], pay[49], pay[55], pay[56], pay[57], pay[58],
                       pay[59])).hex() != _T8D1AT[m]:
                return fail("T8D1A tab")
            for b, v in _T8D1AC:
                if pay[b] != v:
                    return fail("T8D1A const %d" % b)
            print("CLOSED T8D1A N=%d off=%d" % (n, off))
            return 0
        if 11536 <= n <= 11544:
            m = off - 2801
            if bytes((pay[1], pay[2], pay[23], pay[31], pay[39], pay[47],
                       pay[56], pay[57], pay[58], pay[59])).hex() != _T8D1BT[m]:
                return fail("T8D1B tab")
            for b, v in _T8D1BC:
                if pay[b] != v:
                    return fail("T8D1B const %d" % b)
            print("CLOSED T8D1B N=%d off=%d" % (n, off))
            return 0
        return fail("T8D1 gap %d" % n)
    if n <= 11593:  # T8D1Q: 3x16 tab b60-63 + 9B words, k15 early-edge
        off = n - 8735
        if len(pay) != 64:
            return fail("T8D1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8D1Q lencode")
        m = (off - 2811) & 15
        q = (off - 2811) >> 4
        if pay[5] != (0x1a if m in (0, 1, 2, 15) else
                       (0x5a, 0x9a, 0xda)[min((m // 3) - 1, 2)]):
            return fail("T8D1Q b5")
        if pay[60:64].hex() != _T8D1QT[m]:
            return fail("T8D1Q tab")
        blk = bytes((pay[1], pay[2], pay[23], pay[39], pay[47], pay[56],
                     pay[57], pay[58], pay[59])).hex()
        exp = _T8D1QB[q] if m < 15 else (_T8D1QB[q + 1] if q < 2
                                        else _T8D1QN)
        if blk != exp:
            return fail("T8D1Q blk")
        if pay[31] != (0x8d if n == 11593 else 0x0d):
            return fail("T8D1Q b31")
        for b, v in _T8D1QC:
            if pay[b] != v:
                return fail("T8D1Q const %d" % b)
        print("CLOSED T8D1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 11609:  # T8E1: 15-row (b5+b60-63) + single 11609
        off = n - 8735
        if len(pay) != 64:
            return fail("T8E1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8E1 lencode")
        if n == 11609:
            if pay.hex() != _T8E10:
                return fail("T8E10 lit")
            print("CLOSED T8E10 N=%d off=%d" % (n, off))
            return 0
        m = off - 2859
        if bytes((pay[5], pay[60], pay[61], pay[62],
                   pay[63])).hex() != _T8E1T[m]:
            return fail("T8E1 tab")
        for b, v in _T8E1C:
            if pay[b] != v:
                return fail("T8E1 const %d" % b)
        print("CLOSED T8E1 N=%d off=%d" % (n, off))
        return 0
    if n <= 11849:  # T8E1Q: 15x16 tab b60-63 + 4B words, k15 early-edge
        off = n - 8735
        if len(pay) != 64:
            return fail("T8E1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8E1Q lencode")
        m = (off - 2875) & 15
        q = (off - 2875) >> 4
        b5 = 0x1a
        if off >= 2913:
            b5 = 0x1b
        if off >= 2938:
            b5 = 0x5b
        if off >= 2986:
            b5 = 0x9b
        if off >= 3034:
            b5 = 0xdb
        if off >= 3041:
            b5 = 0xdc
        if pay[5] != b5:
            return fail("T8E1Q b5")
        if pay[10] != bytes.fromhex(_T8E1B10)[m]:
            return fail("T8E1Q b10")
        if pay[11] != (0x59 if m in (11, 12, 13, 14) else 0x58):
            return fail("T8E1Q b11")
        if pay[60:64].hex() != _T8E1QT[m]:
            return fail("T8E1Q tab")
        blk = bytes((pay[56], pay[57], pay[58], pay[59])).hex()
        exp = _T8E1QB[q] if m < 15 else (_T8E1QB[q + 1] if q < 14
                                        else _T8E1QN)
        if blk != exp:
            return fail("T8E1Q blk")
        for b, v in _T8E1QC:
            if pay[b] != v:
                return fail("T8E1Q const %d" % b)
        print("CLOSED T8E1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 11956:  # T8F tail: F1 15-row + F2 16-row + F3 9-row + F4 3blk + F5 15-row + 5 singles
        off = n - 8735
        if len(pay) != 64:
            return fail("T8F paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T8F lencode")
        if n in _T8F10:
            if pay.hex() != _T8F10[n]:
                return fail("T8F0 lit %d" % n)
            print("CLOSED T8F0 N=%d off=%d" % (n, off))
            return 0
        if 11850 <= n <= 11864:
            m = off - 3115
            if bytes((pay[10], pay[11], pay[60], pay[61], pay[62],
                       pay[63])).hex() != _T8F1T[m]:
                return fail("T8F1 tab")
            for b, v in _T8F1C:
                if pay[b] != v:
                    return fail("T8F1 const %d" % b)
            print("CLOSED T8F1 N=%d off=%d" % (n, off))
            return 0
        if 11867 <= n <= 11882:
            m = off - 3132
            if bytes((pay[0], pay[1], pay[2], pay[13], pay[14], pay[15],
                       pay[16], pay[17])).hex() != _T8F2T[m]:
                return fail("T8F2 tab")
            for b, v in _T8F2C:
                if pay[b] != v:
                    return fail("T8F2 const %d" % b)
            print("CLOSED T8F2 N=%d off=%d" % (n, off))
            return 0
        if 11884 <= n <= 11892:
            m = off - 3149
            if bytes((pay[16], pay[17], pay[18], pay[19], pay[20], pay[21],
                       pay[22], pay[23])).hex() != _T8F3T[m]:
                return fail("T8F3 tab")
            for b, v in _T8F3C:
                if pay[b] != v:
                    return fail("T8F3 const %d" % b)
            print("CLOSED T8F3 N=%d off=%d" % (n, off))
            return 0
        if 11894 <= n <= 11940:
            m = (off - 3159) & 15
            q = (off - 3159) >> 4
            if bytes((pay[24], pay[25], pay[26], pay[27], pay[28],
                       pay[29])).hex() != _T8F4T[m]:
                return fail("T8F4 tab")
            blk = bytes((pay[5], pay[16], pay[17], pay[18], pay[19],
                         pay[20], pay[21], pay[22], pay[23])).hex()
            exp = _T8F4B[q] if m < 15 else _T8F4B[q + 1]
            if q == 0 and m < 10:
                exp = "5c" + exp[2:]
            if q == 0 and 10 <= m < 15:
                exp = "5d" + exp[2:]
            if blk != exp:
                return fail("T8F4 blk")
            for b, v in _T8F4C:
                if pay[b] != v:
                    return fail("T8F4 const %d" % b)
            print("CLOSED T8F4 N=%d off=%d" % (n, off))
            return 0
        if 11942 <= n <= 11956:
            m = off - 3207
            if bytes((pay[24], pay[25], pay[26], pay[27], pay[28],
                       pay[29])).hex() != _T8F4T[m]:
                return fail("T8F5 tab")
            for b, v in _T8F5C:
                if pay[b] != v:
                    return fail("T8F5 const %d" % b)
            print("CLOSED T8F5 N=%d off=%d" % (n, off))
            return 0
        return fail("T8F gap %d" % n)
    if n <= 12212:  # T9HEAD: 16x16 tab b36-41 + 6B block words b28-33
        off = n - 11957
        if len(pay) != 68:
            return fail("T9HEAD paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9HEAD lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0x5d + (off >= 75) + (off >= 203):
            return fail("T9HEAD b5")
        if bytes((pay[36], pay[37], pay[38], pay[39], pay[40],
                   pay[41])).hex() != _T9HT[m]:
            return fail("T9HEAD tab")
        blk = bytes((pay[28], pay[29], pay[30], pay[31], pay[32],
                     pay[33])).hex()
        if blk != _T9HB[q]:
            return fail("T9HEAD blk")
        for b, v in _T9HC:
            if pay[b] != v:
                return fail("T9HEAD const %d" % b)
        print("CLOSED T9HEAD N=%d off=%d" % (n, off))
        return 0
    if n <= 12230:  # T9DIPR: 64B dip pair + R 16-row tab b44-49
        off = n - 11957
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9DIPR lencode")
        if n in _T9DIP:
            if len(pay) != 64:
                return fail("T9DIP paylen")
            if pay.hex() != _T9DIP[n]:
                return fail("T9DIP lit %d" % n)
            print("CLOSED T9DIP N=%d off=%d" % (n, off))
            return 0
        if len(pay) != 68:
            return fail("T9R paylen")
        m = off - 258
        if bytes((pay[44], pay[45], pay[46], pay[47], pay[48],
                   pay[49])).hex() != _T9RT[m]:
            return fail("T9R tab")
        for b, v in _T9RC:
            if pay[b] != v:
                return fail("T9R const %d" % b)
        print("CLOSED T9R N=%d off=%d" % (n, off))
        return 0
    if n <= 12304:  # T9D2 dip band: 3 singles + A 8-row + Q 4blk (paylen 64)
        off = n - 12231
        if len(pay) != 64:
            return fail("T9D2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9D2 lencode")
        if n in _T9D20:
            if pay.hex() != _T9D20[n]:
                return fail("T9D20 lit %d" % n)
            print("CLOSED T9D20 N=%d off=%d" % (n, off))
            return 0
        if 12233 <= n <= 12240:
            m = off - 2
            if bytes((pay[40], pay[41], pay[42], pay[43], pay[44], pay[45],
                       pay[46], pay[47])).hex() != _T9D2AT[m]:
                return fail("T9D2A tab")
            for b, v in _T9D2AC:
                if pay[b] != v:
                    return fail("T9D2A const %d" % b)
            print("CLOSED T9D2A N=%d off=%d" % (n, off))
            return 0
        m = (off - 11) & 15
        q = (off - 11) >> 4
        if pay[5] != 0x5f + (n >= 12288):
            return fail("T9D2Q b5")
        if bytes((pay[48], pay[49], pay[50], pay[51], pay[52],
                   pay[53])).hex() != _T9D2QT[m]:
            return fail("T9D2Q tab")
        blk = bytes((pay[40], pay[41], pay[42], pay[43], pay[44], pay[45],
                     pay[46], pay[47])).hex()
        exp = _T9D2QB[q] if m < 15 else _T9D2QB[q + 1]
        if blk != exp:
            return fail("T9D2Q blk")
        for b, v in _T9D2QC:
            if pay[b] != v:
                return fail("T9D2Q const %d" % b)
        print("CLOSED T9D2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 12560:  # T9S1: 16x16 tab b52,53,b60-63 + 8B block words
        off = n - 12305
        if len(pay) != 68:
            return fail("T9S1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9S1 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0x60 + (off >= 111) + (off >= 239):
            return fail("T9S1 b5")
        if bytes((pay[52], pay[53], pay[60], pay[61], pay[62],
                   pay[63])).hex() != _T9S1T[m]:
            return fail("T9S1 tab")
        blk = bytes((pay[0], pay[10], pay[11], pay[27], pay[35], pay[43],
                     pay[51], pay[56])).hex()
        if blk != _T9S1B[q]:
            return fail("T9S1 blk")
        for b, v in _T9S1C:
            if pay[b] != v:
                return fail("T9S1 const %d" % b)
        print("CLOSED T9S1 N=%d off=%d" % (n, off))
        return 0
    if n <= 12578:  # T9D3: 64B dip pair + R 16-row tab b5,6,b64-67
        off = n - 12561
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9D3 lencode")
        if n in _T9D3P:
            if len(pay) != 64:
                return fail("T9D3P paylen")
            if pay.hex() != _T9D3P[n]:
                return fail("T9D3P lit %d" % n)
            print("CLOSED T9D3P N=%d off=%d" % (n, off))
            return 0
        if len(pay) != 68:
            return fail("T9D3R paylen")
        m = off - 2
        if bytes((pay[5], pay[6], pay[64], pay[65], pay[66],
                   pay[67])).hex() != _T9D3T[m]:
            return fail("T9D3R tab")
        for b, v in _T9D3C:
            if pay[b] != v:
                return fail("T9D3R const %d" % b)
        print("CLOSED T9D3R N=%d off=%d" % (n, off))
        return 0
    if n <= 12588:  # T9D4: 10-row dip band tab b5-9,b60-63 (paylen 64)
        off = n - 12579
        if len(pay) != 64:
            return fail("T9D4 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9D4 lencode")
        if bytes((pay[5], pay[6], pay[7], pay[8], pay[9], pay[60], pay[61],
                   pay[62], pay[63])).hex() != _T9D4T[off]:
            return fail("T9D4 tab")
        for b, v in _T9D4C:
            if pay[b] != v:
                return fail("T9D4 const %d" % b)
        print("CLOSED T9D4 N=%d off=%d" % (n, off))
        return 0
    if n <= 12652:  # T9T1: 4x16 tab b13,14,b64-67 + 8B block words
        off = n - 12589
        if len(pay) != 68:
            return fail("T9T1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9T1 lencode")
        m = off & 15
        q = off >> 4
        if bytes((pay[13], pay[14], pay[64], pay[65], pay[66],
                   pay[67])).hex() != _T9T1T[m]:
            return fail("T9T1 tab")
        blk = bytes((pay[5], pay[6], pay[7], pay[12], pay[60], pay[61],
                     pay[62], pay[63])).hex()
        if blk != _T9T1B[q]:
            return fail("T9T1 blk")
        for b, v in _T9T1C:
            if pay[b] != v:
                return fail("T9T1 const %d" % b)
        print("CLOSED T9T1 N=%d off=%d" % (n, off))
        return 0
    if n <= 12908:  # T9U1: 16x16 tab b9,10,b17-21 + 5B block words
        off = n - 12653
        if len(pay) != 68:
            return fail("T9U1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9U1 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0x62 + (off >= 19) + (off >= 147):
            return fail("T9U1 b5")
        if bytes((pay[9], pay[10], pay[17], pay[18], pay[19], pay[20],
                   pay[21])).hex() != _T9U1T[m]:
            return fail("T9U1 tab")
        blk = bytes((pay[13], pay[64], pay[65], pay[66],
                     pay[67])).hex()
        if blk != _T9U1B[q]:
            return fail("T9U1 blk")
        for b, v in _T9U1C:
            if pay[b] != v:
                return fail("T9U1 const %d" % b)
        print("CLOSED T9U1 N=%d off=%d" % (n, off))
        return 0
    if n <= 12937:  # T9V1 storm: dip + 4 singles + A 15-row + B 9-row
        off = n - 11957
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9V1 lencode")
        if n == 12909:
            if len(pay) != 64:
                return fail("T9V1D paylen")
            if pay.hex() != _T9V1D:
                return fail("T9V1D lit")
            print("CLOSED T9V1D N=%d off=%d" % (n, off))
            return 0
        if len(pay) != 68:
            return fail("T9V1 paylen")
        if n in _T9V10:
            if pay.hex() != _T9V10[n]:
                return fail("T9V10 lit %d" % n)
            print("CLOSED T9V10 N=%d off=%d" % (n, off))
            return 0
        if 12912 <= n <= 12926:
            m = off - 955
            if bytes((pay[24], pay[25], pay[26], pay[27], pay[28],
                       pay[29])).hex() != _T9V1AT[m]:
                return fail("T9V1A tab")
            for b, v in _T9V1AC:
                if pay[b] != v:
                    return fail("T9V1A const %d" % b)
            print("CLOSED T9V1A N=%d off=%d" % (n, off))
            return 0
        if 12928 <= n <= 12936:
            m = off - 971
            if bytes((pay[24], pay[25], pay[26], pay[27], pay[28], pay[29],
                       pay[30], pay[31])).hex() != _T9V1BT[m]:
                return fail("T9V1B tab")
            for b, v in _T9V1BC:
                if pay[b] != v:
                    return fail("T9V1B const %d" % b)
            print("CLOSED T9V1B N=%d off=%d" % (n, off))
            return 0
        return fail("T9V1 gap %d" % n)
    if n <= 13000:  # T9V1Q: 4x16 tab b32-37 + 8B words, k15 early-edge
        off = n - 11957
        if len(pay) != 68:
            return fail("T9V1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9V1Q lencode")
        m = (off - 981) & 15
        q = (off - 981) >> 4
        if bytes((pay[32], pay[33], pay[34], pay[35], pay[36],
                   pay[37])).hex() != _T9V1QT[m]:
            return fail("T9V1Q tab")
        blk = bytes((pay[24], pay[25], pay[26], pay[27], pay[28], pay[29],
                     pay[30], pay[31])).hex()
        exp = _T9V1QB[q] if m < 15 else _T9V1QB[q + 1]
        if blk != exp:
            return fail("T9V1Q blk")
        for b, v in _T9V1QC:
            if pay[b] != v:
                return fail("T9V1Q const %d" % b)
        print("CLOSED T9V1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 13256:  # T9W1: 16x16 tab b40-45 + 6B block words b32-37
        off = n - 13001
        if len(pay) != 68:
            return fail("T9W1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9W1 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0x65 + (off >= 55) + (off >= 183):
            return fail("T9W1 b5")
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[44],
                   pay[45])).hex() != _T9W1T[m]:
            return fail("T9W1 tab")
        blk = bytes((pay[32], pay[33], pay[34], pay[35], pay[36],
                     pay[37])).hex()
        if blk != _T9W1B[q]:
            return fail("T9W1 blk")
        for b, v in _T9W1C:
            if pay[b] != v:
                return fail("T9W1 const %d" % b)
        print("CLOSED T9W1 N=%d off=%d" % (n, off))
        return 0
    if n <= 13285:  # T9X1 storm: dip + 4 singles + A 15-row + B 9-row
        off = n - 11957
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9X1 lencode")
        if n == 13257:
            if len(pay) != 64:
                return fail("T9X1D paylen")
            if pay.hex() != _T9X1D:
                return fail("T9X1D lit")
            print("CLOSED T9X1D N=%d off=%d" % (n, off))
            return 0
        if len(pay) != 68:
            return fail("T9X1 paylen")
        if n in _T9X10:
            if pay.hex() != _T9X10[n]:
                return fail("T9X10 lit %d" % n)
            print("CLOSED T9X10 N=%d off=%d" % (n, off))
            return 0
        if 13260 <= n <= 13274:
            m = off - 1303
            if bytes((pay[48], pay[49], pay[50], pay[51], pay[52],
                       pay[53])).hex() != _T9X1AT[m]:
                return fail("T9X1A tab")
            for b, v in _T9X1AC:
                if pay[b] != v:
                    return fail("T9X1A const %d" % b)
            print("CLOSED T9X1A N=%d off=%d" % (n, off))
            return 0
        if 13276 <= n <= 13284:
            m = off - 1319
            if bytes((pay[48], pay[49], pay[50], pay[51], pay[52], pay[53],
                       pay[54], pay[55])).hex() != _T9X1BT[m]:
                return fail("T9X1B tab")
            for b, v in _T9X1BC:
                if pay[b] != v:
                    return fail("T9X1B const %d" % b)
            print("CLOSED T9X1B N=%d off=%d" % (n, off))
            return 0
        return fail("T9X1 gap %d" % n)
    if n <= 13348:  # T9X1Q: 4x16 tab b48,49,b56-59 + 11B words, k15 edge
        off = n - 11957
        if len(pay) != 68:
            return fail("T9X1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9X1Q lencode")
        m = (off - 1329) & 15
        q = (off - 1329) >> 4
        if bytes((pay[48], pay[49], pay[56], pay[57], pay[58],
                   pay[59])).hex() != _T9X1QT[m]:
            return fail("T9X1Q tab")
        blk = bytes((pay[0], pay[5], pay[10], pay[11], pay[23], pay[31],
                     pay[39], pay[47], pay[52], pay[53], pay[54])).hex()
        exp = _T9X1QB[q] if m < 15 else _T9X1QB[q + 1]
        if q == 1 and 10 <= m < 15:
            exp = exp[:2] + "68" + exp[4:]
        if blk != exp:
            return fail("T9X1Q blk")
        for b, v in _T9X1QC:
            if pay[b] != v:
                return fail("T9X1Q const %d" % b)
        print("CLOSED T9X1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 13428:  # T9Y1: 5x16 tab b5,6,b60-63 + 6B block words
        off = n - 13349
        if len(pay) != 68:
            return fail("T9Y1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9Y1 lencode")
        m = off & 15
        q = off >> 4
        if bytes((pay[5], pay[6], pay[60], pay[61], pay[62],
                   pay[63])).hex() != _T9Y1T[m]:
            return fail("T9Y1 tab")
        blk = bytes((pay[48], pay[49], pay[56], pay[57], pay[58],
                     pay[59])).hex()
        if blk != _T9Y1B[q]:
            return fail("T9Y1 blk")
        for b, v in _T9Y1C:
            if pay[b] != v:
                return fail("T9Y1 const %d" % b)
        print("CLOSED T9Y1 N=%d off=%d" % (n, off))
        return 0
    if n <= 13604:  # T9Z1: 11x16 tab b6,b60-63 + 6B words + b5 HI/LO
        off = n - 13429
        if len(pay) != 68:
            return fail("T9Z1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9Z1 lencode")
        m = off & 15
        q = off >> 4
        lo = _T9Z1LO[q + 1] if m >= 11 and q < 10 else _T9Z1LO[q]
        if pay[5] != (_T9Z1HI[m] << 4) | lo:
            return fail("T9Z1 b5")
        if bytes((pay[6], pay[60], pay[61], pay[62],
                   pay[63])).hex() != _T9Z1T[m]:
            return fail("T9Z1 tab")
        blk = bytes((pay[48], pay[49], pay[56], pay[57], pay[58],
                     pay[59])).hex()
        if blk != _T9Z1B[q]:
            return fail("T9Z1 blk")
        for b, v in _T9Z1C:
            if pay[b] != v:
                return fail("T9Z1 const %d" % b)
        print("CLOSED T9Z1 N=%d off=%d" % (n, off))
        return 0
    if n <= 13633:  # T9A2 storm: dip + 5 singles + A 15-row + B 8-row
        off = n - 11957
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9A2 lencode")
        if n == 13605:
            if len(pay) != 64:
                return fail("T9A2D paylen")
            if pay.hex() != _T9A2D:
                return fail("T9A2D lit")
            print("CLOSED T9A2D N=%d off=%d" % (n, off))
            return 0
        if len(pay) != 68:
            return fail("T9A2 paylen")
        if n in _T9A20:
            if pay.hex() != _T9A20[n]:
                return fail("T9A20 lit %d" % n)
            print("CLOSED T9A20 N=%d off=%d" % (n, off))
            return 0
        if 13608 <= n <= 13622:
            m = off - 1651
            if bytes((pay[13], pay[64], pay[65], pay[66],
                       pay[67])).hex() != _T9A2AT[m]:
                return fail("T9A2A tab")
            for b, v in _T9A2AC:
                if pay[b] != v:
                    return fail("T9A2A const %d" % b)
            print("CLOSED T9A2A N=%d off=%d" % (n, off))
            return 0
        if 13625 <= n <= 13632:
            m = off - 1668
            if bytes((pay[13], pay[14], pay[15], pay[64], pay[65], pay[66],
                       pay[67])).hex() != _T9A2BT[m]:
                return fail("T9A2B tab")
            for b, v in _T9A2BC:
                if pay[b] != v:
                    return fail("T9A2B const %d" % b)
            print("CLOSED T9A2B N=%d off=%d" % (n, off))
            return 0
        return fail("T9A2 gap %d" % n)
    if n <= 13696:  # T9A2Q: 4x16 tab b12,b16-21 + 7B words, k15 edge
        off = n - 11957
        if len(pay) != 68:
            return fail("T9A2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9A2Q lencode")
        m = (off - 1677) & 15
        q = (off - 1677) >> 4
        if pay[5] != (0xeb if n >= 13696 else 0xea):
            return fail("T9A2Q b5")
        if pay[13] != (0xd6 if m in (1, 4, 11, 15) else 0xd7):
            return fail("T9A2Q b13")
        if bytes((pay[12], pay[16], pay[17], pay[18], pay[19], pay[20],
                   pay[21])).hex() != _T9A2QT[m]:
            return fail("T9A2Q tab")
        blk = bytes((pay[0], pay[10], pay[11], pay[64], pay[65], pay[66],
                     pay[67])).hex()
        exp = _T9A2QB[q] if m < 15 else (_T9A2QB[q + 1] if q < 3
                                        else _T9A2QN)
        if blk != exp:
            return fail("T9A2Q blk")
        for b, v in _T9A2QC:
            if pay[b] != v:
                return fail("T9A2Q const %d" % b)
        print("CLOSED T9A2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 13952:  # T9B2: 16x16 tab b24-29 + 8B block words + b30 rule
        off = n - 13697
        if len(pay) != 68:
            return fail("T9B2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9B2 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0xeb + (off >= 127) + (off >= 255):
            return fail("T9B2 b5")
        if pay[30] != 0x62 + (m >= 8):
            return fail("T9B2 b30")
        if bytes((pay[24], pay[25], pay[26], pay[27], pay[28],
                   pay[29])).hex() != _T9B2T[m]:
            return fail("T9B2 tab")
        blk = bytes((pay[12], pay[13], pay[16], pay[17], pay[18], pay[19],
                     pay[20], pay[21])).hex()
        if blk != _T9B2B[q]:
            return fail("T9B2 blk")
        for b, v in _T9B2C:
            if pay[b] != v:
                return fail("T9B2 const %d" % b)
        print("CLOSED T9B2 N=%d off=%d" % (n, off))
        return 0
    if n <= 13981:  # T9C2 storm: 5 singles + A 15-row + B 9-row
        off = n - 11957
        if len(pay) != 68:
            return fail("T9C2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9C2 lencode")
        if n in _T9C20:
            if pay.hex() != _T9C20[n]:
                return fail("T9C20 lit %d" % n)
            print("CLOSED T9C20 N=%d off=%d" % (n, off))
            return 0
        if 13956 <= n <= 13970:
            m = off - 1999
            if bytes((pay[24], pay[28], pay[29], pay[30], pay[31], pay[32],
                       pay[33])).hex() != _T9C2AT[m]:
                return fail("T9C2A tab")
            if pay[34] != (0xad if m >= 6 else 0xac):
                return fail("T9C2A b34")
            for b, v in _T9C2AC:
                if pay[b] != v:
                    return fail("T9C2A const %d" % b)
            print("CLOSED T9C2A N=%d off=%d" % (n, off))
            return 0
        if 13972 <= n <= 13980:
            m = off - 2015
            if bytes((pay[32], pay[33], pay[34], pay[35], pay[36], pay[37],
                       pay[38], pay[39])).hex() != _T9C2BT[m]:
                return fail("T9C2B tab")
            if pay[23] != (0xba if m == 5 else 0x9a):
                return fail("T9C2B b23")
            for b, v in _T9C2BC:
                if pay[b] != v:
                    return fail("T9C2B const %d" % b)
            print("CLOSED T9C2B N=%d off=%d" % (n, off))
            return 0
        return fail("T9C2 gap %d" % n)
    if n <= 14029:  # T9C2Q: 3x16 tab b40-45 + 8B words, k15 early-edge
        off = n - 11957
        if len(pay) != 68:
            return fail("T9C2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9C2Q lencode")
        m = (off - 2025) & 15
        q = (off - 2025) >> 4
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[44],
                   pay[45])).hex() != _T9C2QT[m]:
            return fail("T9C2Q tab")
        blk = bytes((pay[25], pay[26], pay[27], pay[31], pay[36], pay[37],
                     pay[38], pay[39])).hex()
        exp = _T9C2QB[q] if m < 15 else (_T9C2QB[q + 1] if q < 2
                                        else _T9C2QN)
        if blk != exp:
            return fail("T9C2Q blk")
        if pay[24] != (0xdb if n == 14029 else 0x7b):
            return fail("T9C2Q b24")
        for b, v in _T9C2QC:
            if pay[b] != v:
                return fail("T9C2Q const %d" % b)
        print("CLOSED T9C2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 14045:  # T9E2: 15-row tab b40-45 + single 14045
        off = n - 14030
        if len(pay) != 68:
            return fail("T9E2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9E2 lencode")
        if n == 14045:
            if pay.hex() != _T9E20:
                return fail("T9E20 lit")
            print("CLOSED T9E20 N=%d off=%d" % (n, off))
            return 0
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[44],
                   pay[45])).hex() != _T9E2T[off]:
            return fail("T9E2 tab")
        for b, v in _T9E2C:
            if pay[b] != v:
                return fail("T9E2 const %d" % b)
        print("CLOSED T9E2 N=%d off=%d" % (n, off))
        return 0
    if n <= 14300:  # T9E2Q: 15x16 tab b40-43,47,52,53 + 8B words, k15 edge; q15 ext
        off = n - 14046
        if len(pay) != 68:
            return fail("T9E2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9E2Q lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != 0xed + (off >= 34) + (off >= 162):
            return fail("T9E2Q b5")
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[47], pay[52],
                   pay[53])).hex() != _T9E2QT[m]:
            return fail("T9E2Q tab")
        blk = bytes((pay[1], pay[19], pay[32], pay[33], pay[34], pay[35],
                     pay[39], pay[44])).hex()
        exp = (_T9E2QB[q] if q < 15 else _T9E2QN) if m < 15 else (
            _T9E2QB[q + 1] if q < 14 else _T9E2QN)
        if blk != exp:
            return fail("T9E2Q blk")
        for b, v in _T9E2QC:
            if pay[b] != v:
                return fail("T9E2Q const %d" % b)
        print("CLOSED T9E2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 14329:  # T9F2: 3 singles + B 15-row + s14319 + C 9-row + s14329
        if len(pay) != 68:
            return fail("T9F2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9F2 lencode")
        _s = {14301: _T9F2S1, 14302: _T9F2S2, 14303: _T9F2S3,
              14319: _T9F2S4, 14329: _T9F2S5}
        if n in _s:
            if pay.hex() != _s[n]:
                return fail("T9F2S lit")
            print("CLOSED T9F2S N=%d" % n)
            return 0
        if n <= 14318:
            off = n - 14304
            if bytes((pay[49], pay[50], pay[52], pay[53], pay[54],
                       pay[55])).hex() != _T9F2BT[off]:
                return fail("T9F2B tab")
            for b, v in _T9F2BC:
                if pay[b] != v:
                    return fail("T9F2B const %d" % b)
            print("CLOSED T9F2B N=%d off=%d" % (n, off))
            return 0
        off = n - 14320
        if bytes((pay[48], pay[49], pay[50], pay[51], pay[56], pay[57],
                   pay[58], pay[59])).hex() != _T9F2CT[off]:
            return fail("T9F2C tab")
        for b, v in _T9F2CC:
            if pay[b] != v:
                return fail("T9F2C const %d" % b)
        print("CLOSED T9F2C N=%d off=%d" % (n, off))
        return 0
    if n <= 14392:  # T9F2Q: 3x16+15 tab b6,b60-63 + b5 + 8B words, k15 carry
        off = n - 14330
        if len(pay) != 68:
            return fail("T9F2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9F2Q lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != _T9F2Q5[m] + (q >= 1 and m < 6):
            return fail("T9F2Q b5")
        if bytes((pay[6], pay[60], pay[61], pay[62],
                   pay[63])).hex() != _T9F2QT[m]:
            return fail("T9F2Q tab")
        blk = bytes((pay[48], pay[49], pay[50], pay[51], pay[56],
                     pay[57], pay[58], pay[59])).hex()
        if blk != (_T9F2QB[q] if m < 15 else _T9F2QB[q + 1]):
            return fail("T9F2Q blk")
        for b, v in _T9F2QC:
            if pay[b] != v:
                return fail("T9F2Q const %d" % b)
        print("CLOSED T9F2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 14648:  # T9G2: 16x16 tab b10,11,b64-67 + b5[q] + F2QT-rot words
        off = n - 14393
        if len(pay) != 68:
            return fail("T9G2 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9G2 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != _T9G2B5[q] + (m >= 7 and q in (4, 12)):
            return fail("T9G2 b5")
        _f = _T9F2QT[(q + 15) & 15]
        if pay[6] != int(_f[0:2], 16):
            return fail("T9G2 b6")
        if bytes((pay[60], pay[61], pay[62], pay[63])).hex() != _f[2:]:
            return fail("T9G2 blk")
        if bytes((pay[10], pay[11], pay[64], pay[65], pay[66],
                   pay[67])).hex() != _T9G2T[m]:
            return fail("T9G2 tab")
        for b, v in _T9G2C:
            if pay[b] != v:
                return fail("T9G2 const %d" % b)
        print("CLOSED T9G2 N=%d off=%d" % (n, off))
        return 0
    if n <= 14676:  # T9H3: 3 singles + A 15-row + B 10-row
        if len(pay) != 68:
            return fail("T9H3 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9H3 lencode")
        _s = {14649: _T9H3S1, 14650: _T9H3S2, 14651: _T9H3S3}
        if n in _s:
            if pay.hex() != _s[n]:
                return fail("T9H3S lit")
            print("CLOSED T9H3S N=%d" % n)
            return 0
        if n <= 14666:
            off = n - 14652
            if bytes((pay[16], pay[17], pay[18], pay[19], pay[20],
                       pay[21])).hex() != _T9H3AT[off]:
                return fail("T9H3A tab")
            for b, v in _T9H3AC:
                if pay[b] != v:
                    return fail("T9H3A const %d" % b)
            print("CLOSED T9H3A N=%d off=%d" % (n, off))
            return 0
        off = n - 14667
        if bytes((pay[12], pay[16], pay[17], pay[18], pay[19],
                   pay[20], pay[21], pay[22],
                   pay[23])).hex() != _T9H3BT[off]:
            return fail("T9H3B tab")
        for b, v in _T9H3BC:
            if pay[b] != v:
                return fail("T9H3B const %d" % b)
        print("CLOSED T9H3B N=%d off=%d" % (n, off))
        return 0
    if n <= 14740:  # T9H3Q: 4x16 tab b24-30 + 9B block words
        off = n - 14677
        if len(pay) != 68:
            return fail("T9H3Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9H3Q lencode")
        m = off & 15
        q = off >> 4
        if bytes((pay[24], pay[25], pay[26], pay[27], pay[28],
                   pay[29], pay[30])).hex() != _T9H3QT[m]:
            return fail("T9H3Q tab")
        if pay[5] != (0x73 if (q == 3 or (q == 2 and m >= 11))
                        else 0x72):
            return fail("T9H3Q b5")
        blk = bytes((pay[1], pay[12], pay[13], pay[14], pay[15],
                     pay[20], pay[21], pay[22])).hex()
        if blk != _T9H3QB[q]:
            return fail("T9H3Q blk")
        for b, v in _T9H3QC:
            if pay[b] != v:
                return fail("T9H3Q const %d" % b)
        print("CLOSED T9H3Q N=%d off=%d" % (n, off))
        return 0
    if n <= 14996:  # T9I1: 16x16 tab b32-38 + H3QT words + b28/29 + b5
        off = n - 14741
        if len(pay) != 68:
            return fail("T9I1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9I1 lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != _T9I1B5[q] + (m >= 11 and q in (6, 14)):
            return fail("T9I1 b5")
        if bytes((pay[20], pay[21], pay[22],
                   pay[23])).hex() != _T9H3QT[q][0:8]:
            return fail("T9I1 blk")
        if bytes((pay[28], pay[29])).hex() != _T9I1W[q]:
            return fail("T9I1 w")
        if bytes((pay[32], pay[33], pay[34], pay[35], pay[36],
                   pay[37], pay[38])).hex() != _T9I1T[m]:
            return fail("T9I1 tab")
        for b, v in _T9I1C:
            if pay[b] != v:
                return fail("T9I1 const %d" % b)
        print("CLOSED T9I1 N=%d off=%d" % (n, off))
        return 0
    if n <= 15024:  # T9J1: 5 singles + A 15-row + B 8-row
        if len(pay) != 68:
            return fail("T9J1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9J1 lencode")
        _s = {14997: _T9J1S1, 14998: _T9J1S2, 14999: _T9J1S3,
              15015: _T9J1S4, 15016: _T9J1S5}
        if n in _s:
            if pay.hex() != _s[n]:
                return fail("T9J1S lit")
            print("CLOSED T9J1S N=%d" % n)
            return 0
        if n <= 15014:
            off = n - 15000
            if bytes((pay[36], pay[37], pay[38], pay[39], pay[40],
                       pay[41])).hex() != _T9J1AT[off]:
                return fail("T9J1A tab")
            for b, v in _T9J1AC:
                if pay[b] != v:
                    return fail("T9J1A const %d" % b)
            print("CLOSED T9J1A N=%d off=%d" % (n, off))
            return 0
        off = n - 15017
        if bytes((pay[19], pay[32], pay[33], pay[34], pay[35],
                   pay[39], pay[44], pay[45], pay[46],
                   pay[47])).hex() != _T9J1BT[off]:
            return fail("T9J1B tab")
        for b, v in _T9J1BC:
            if pay[b] != v:
                return fail("T9J1B const %d" % b)
        print("CLOSED T9J1B N=%d off=%d" % (n, off))
        return 0
    if n <= 15088:  # T9J1Q: 4x16 tab b2,b40-43,47,52,53 + 7B words
        off = n - 15025
        if len(pay) != 68:
            return fail("T9J1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9J1Q lencode")
        m = off & 15
        q = off >> 4
        if pay[2] != _T9J1Q2[m]:
            return fail("T9J1Q b2")
        if bytes((pay[40], pay[41], pay[42], pay[43], pay[52],
                   pay[53])).hex() != _T9J1QT[m]:
            return fail("T9J1Q tab")
        if pay[47] != (_T9J1Q7E[m] if q % 2 == 0 else _T9J1Q7O[m]):
            return fail("T9J1Q b47")
        blk = bytes((pay[36], pay[37], pay[38], pay[39], pay[44],
                     pay[45], pay[46])).hex()
        if blk != _T9J1QB[q]:
            return fail("T9J1Q blk")
        for b, v in _T9J1QC:
            if pay[b] != v:
                return fail("T9J1Q const %d" % b)
        print("CLOSED T9J1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 15344:  # T9J2Q: 16x16 tab b52,53,56-59 + 6B words + b5
        off = n - 15089
        if len(pay) != 68:
            return fail("T9J2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9J2Q lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != _T9J2B5[q] + (m == 15 and q in (0, 8)):
            return fail("T9J2Q b5")
        blk = bytes((pay[44], pay[45], pay[46], pay[47], pay[48],
                     pay[49])).hex()
        if blk != _T9J2QB[q]:
            return fail("T9J2Q blk")
        if bytes((pay[52], pay[53], pay[56], pay[57], pay[58],
                   pay[59])).hex() != _T9J2QT[m]:
            return fail("T9J2Q tab")
        for b, v in _T9J2QC:
            if pay[b] != v:
                return fail("T9J2Q const %d" % b)
        print("CLOSED T9J2Q N=%d off=%d" % (n, off))
        return 0
    if n <= 15372:  # T9K1: 5 singles + A 15-row + B 8-row
        if len(pay) != 68:
            return fail("T9K1 paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9K1 lencode")
        _s = {15345: _T9K1S1, 15346: _T9K1S2, 15347: _T9K1S3,
              15363: _T9K1S4, 15364: _T9K1S5}
        if n in _s:
            if pay.hex() != _s[n]:
                return fail("T9K1S lit")
            print("CLOSED T9K1S N=%d" % n)
            return 0
        if n <= 15362:
            off = n - 15348
            if bytes((pay[5], pay[6], pay[56], pay[57], pay[58],
                       pay[59])).hex() != _T9K1AT[off]:
                return fail("T9K1A tab")
            for b, v in _T9K1AC:
                if pay[b] != v:
                    return fail("T9K1A const %d" % b)
            print("CLOSED T9K1A N=%d off=%d" % (n, off))
            return 0
        off = n - 15365
        if bytes((pay[5], pay[6], pay[7], pay[8], pay[9], pay[60],
                   pay[61], pay[62], pay[63])).hex() != _T9K1BT[off]:
            return fail("T9K1B tab")
        for b, v in _T9K1BC:
            if pay[b] != v:
                return fail("T9K1B const %d" % b)
        print("CLOSED T9K1B N=%d off=%d" % (n, off))
        return 0
    if n <= 15436:  # T9K1Q: 4x16 tab b10,11,64-67 + 9B words
        off = n - 15373
        if len(pay) != 68:
            return fail("T9K1Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9K1Q lencode")
        m = off & 15
        q = off >> 4
        if bytes((pay[10], pay[11], pay[64], pay[65], pay[66],
                   pay[67])).hex() != _T9K1QT[m]:
            return fail("T9K1Q tab")
        blk = bytes((pay[5], pay[6], pay[7], pay[8], pay[9],
                     pay[60], pay[61], pay[62],
                     pay[63])).hex()
        if blk != _T9K1QB[q]:
            return fail("T9K1Q blk")
        for b, v in _T9K1QC:
            if pay[b] != v:
                return fail("T9K1Q const %d" % b)
        print("CLOSED T9K1Q N=%d off=%d" % (n, off))
        return 0
    if n <= 15692:  # T9K2Q: 16x16 tab b1-3,13-15,20,21 + K1QT words + b5
        off = n - 15437
        if len(pay) != 68:
            return fail("T9K2Q paylen")
        l10 = (((n << 1) | 1) & 0x3FF)
        if pay[4] != (l10 & 0xFF):
            return fail("T9K2Q lencode")
        m = off & 15
        q = off >> 4
        if pay[5] != _T9K2B5[q] + (m >= 3 and q in (3, 11)):
            return fail("T9K2Q b5")
        if bytes((pay[10], pay[11], pay[64], pay[65], pay[66],
                   pay[67])).hex() != _T9K1QT[q]:
            return fail("T9K2Q blk")
        if bytes((pay[1], pay[2], pay[3], pay[13], pay[14],
                   pay[15], pay[20], pay[21])).hex() != _T9K2QT[m]:
            return fail("T9K2Q tab")
        for b, v in _T9K2QC:
            if pay[b] != v:
                return fail("T9K2Q const %d" % b)
        print("CLOSED T9K2Q N=%d off=%d" % (n, off))
        return 0
    print("N out of scope", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
