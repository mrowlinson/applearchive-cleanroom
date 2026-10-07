#!/usr/bin/env python3
"""test_aead_units.py -- proto unit tests (no oracle, synthetic blobs)."""
import hashlib
import hmac
import struct
import sys
import unittest

sys.path.insert(0, "proto")
import aead


def manual_hkdf(size, ikm, info, salt=b""):
    prk = hmac.digest(salt or bytes(32), ikm, "sha256")
    out, prev, n = b"", b"", (size + 31) // 32
    for i in range(1, n + 1):
        prev = hmac.digest(prk, prev + info + bytes([i]), "sha256")
        out += prev
    return out[:size]


class Units(unittest.TestCase):
    def test_hkdf_matches_manual(self):
        for size, ikm, info, salt in [(32, b"k", b"AEA_RHEK", b"salt"),
                                      (80, b"x" * 32, b"AEA_SK\x01\x00\x00\x00", b""),
                                      (64, b"s" * 32, b"AEA_SCRYPT", b"")]:
            self.assertEqual(aead.hkdf(size, ikm, info, salt),
                             manual_hkdf(size, ikm, info, salt))

    def test_mac_shape(self):
        m = aead.mac(b"K" * 32, b"data", b"salt")
        self.assertEqual(m, hmac.digest(b"K" * 32, b"salt" + b"data" + struct.pack("<Q", 4), "sha256"))

    def test_id_shape(self):
        blob = b"AEA1" + bytes([5, 0, 0, 0]) + struct.pack("<I", 0) + bytes(144)
        self.assertEqual(aead.archive_id(blob), hashlib.sha256(blob[:156]).digest())
        blob2 = b"AEA1" + bytes([1, 0, 0, 0]) + struct.pack("<I", 4) + b"ABCD" + bytes(144)
        self.assertEqual(aead.archive_id(blob2), hashlib.sha256(blob2[:160]).digest())

    def test_rejects(self):
        with self.assertRaises(aead.FmtErr):
            aead.decrypt_aea(b"XXXX" + bytes(200))
        with self.assertRaises(aead.FmtErr):
            aead.decrypt_aea(b"AEA1" + bytes([9, 0, 0, 0]) + bytes(200))
        with self.assertRaises(aead.FmtErr):
            aead.decrypt_aea(b"AEA1" + bytes([5, 0, 0, 0]) + struct.pack("<I", 0) + bytes(100))
        with self.assertRaises(aead.FmtErr):
            aead.archive_id(b"short")

    def test_keyvalue_forms(self):
        self.assertEqual(aead.parse_key_value("hex:" + "ab" * 32), bytes.fromhex("ab" * 32))
        import base64
        raw = bytes(range(32))
        self.assertEqual(aead.parse_key_value("base64:" + base64.b64encode(raw).decode()), raw)
        with self.assertRaises(aead.FmtErr):
            aead.parse_key_value("ab" * 32)

    def test_codec_dispatch(self):
        import zlib
        self.assertEqual(aead.decomp("-", b"q", 1), b"q")
        self.assertEqual(aead.decomp("z", zlib.compress(b"hi"), 2), b"hi")
        with self.assertRaises(aead.FmtErr):
            aead.decomp("Q", b"q", 1)
        self.assertEqual(aead.cksum(0, b"q"), b"")
        m1 = aead.cksum(1, b"q")
        self.assertEqual(len(m1), 8)
        self.assertEqual(m1, aead.cksum(1, b"q"))
        self.assertNotEqual(m1, aead.cksum(1, b"qq"))
        self.assertEqual(aead.murmur64a(b""), aead.murmur64a(b""))


if __name__ == "__main__":
    unittest.main()
