#!/usr/bin/env python3
"""test_aead_units.py -- proto unit tests (no oracle, synthetic blobs)."""
import hashlib
import hmac
import os
import struct
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "..", "proto"))
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

    def test_id_trunc_boundary(self):
        full = b"AEA1" + bytes([5, 0, 0, 0]) + struct.pack("<I", 0) + bytes(144)
        with self.assertRaises(aead.FmtErr):
            aead.archive_id(full[:155])
        self.assertEqual(aead.archive_id(full[:156]), hashlib.sha256(full[:156]).digest())
        withauth = b"AEA1" + bytes([5, 0, 0, 0]) + struct.pack("<I", 12) + bytes(12 + 144)
        with self.assertRaises(aead.FmtErr):
            aead.archive_id(withauth[:167])
        self.assertEqual(aead.archive_id(withauth[:168]), hashlib.sha256(withauth[:168]).digest())

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

    def test_read_key_file_forms(self):
        import tempfile
        raw32 = bytes(range(32))
        cases = [(raw32, raw32),  # raw binary passthrough
                 (b"hex:" + raw32.hex().encode() + b"\n", raw32),  # hex: + NL
                 (b"base64:QUJD", b"ABC"),  # base64:
                 (b"\xff\xfe\x00key", b"\xff\xfe\x00key"),  # non-ascii raw
                 (raw32 + b"\n", raw32 + b"\n")]  # raw+NL NOT stripped (err-key32nl)
        for content, want in cases:
            with tempfile.NamedTemporaryFile(delete=False) as fh:
                fh.write(content)
                path = fh.name
            try:
                self.assertEqual(aead.read_key_file(path), want)
            finally:
                os.unlink(path)

    def test_dec_ver(self):
        key80 = bytes(range(80))
        data, salt = b"payload-data", b"salty"
        tag = aead.mac(key80[:32], data, salt)
        # 80B key: verify + AES-CTR roundtrip
        dec = aead.dec_ver(key80, data, salt, tag)
        enc = aead.dec_ver(key80, dec, salt, aead.mac(key80[:32], dec, salt))
        self.assertEqual(enc, data)
        # 32B key: verify only, data passthrough
        self.assertEqual(aead.dec_ver(key80[:32], data, salt, tag), data)
        # tampered tag / data raise
        with self.assertRaises(aead.FmtErr):
            aead.dec_ver(key80, data, salt, b"\x00" * 32)
        with self.assertRaises(aead.FmtErr):
            aead.dec_ver(key80, data + b"x", salt, tag)

    def test_scrypt_matches_hashlib(self):
        for n in (1024, 16384):
            self.assertEqual(aead.scrypt_key("pw", b"salt1234", n),
                             hashlib.scrypt(b"pw", salt=b"salt1234",
                                            n=n, r=8, p=1, dklen=32))

    def test_enc_ver_mirrors_dec_ver(self):
        key80 = bytes(range(80))
        data, salt = b"payload-data", b"salty"
        stored, tagm = aead.enc_ver(key80, data, salt)
        self.assertEqual(aead.dec_ver(key80, stored, salt, tagm), data)
        self.assertNotEqual(stored, data)  # CTR applied for 80B keys
        stored32, tag32 = aead.enc_ver(key80[:32], data, salt)
        self.assertEqual(stored32, data)  # 32B keys: identity + MAC
        self.assertEqual(aead.dec_ver(key80[:32], stored32, salt, tag32), data)

    def test_parse_size(self):
        self.assertEqual(aead.parse_size("1m"), 1 << 20)
        self.assertEqual(aead.parse_size("64k"), 64 << 10)
        self.assertEqual(aead.parse_size("16"), 16)
        self.assertEqual(aead.parse_size("0"), 0)
        with self.assertRaises(aead.FmtErr):
            aead.parse_size("bogus")

    def test_encrypt_self_roundtrip(self):
        # API-level, no oracle: profile 1 + profile 5 + empty, fixed salt
        key32 = bytes(range(32))
        salt = bytes(0xAB for _ in range(32))
        blob = aead.encrypt_aea(b"hello", 1, symkey=key32, alg="none",
                                checksum="sha256", padding="none", salt=salt)
        self.assertEqual(aead.decrypt_aea(blob, symkey=key32), b"hello")
        blob5 = aead.encrypt_aea(b"hello", 5, password="pw-20-bytes-long-ok!!",
                                 alg="none", checksum="none", padding="none",
                                 salt=salt)
        self.assertEqual(aead.decrypt_aea(blob5, password="pw-20-bytes-long-ok!!"), b"hello")
        empty = aead.encrypt_aea(b"", 1, symkey=key32, alg="none",
                                 checksum="none", padding="none", salt=salt)
        self.assertEqual(aead.decrypt_aea(empty, symkey=key32), b"")
        padded = aead.encrypt_aea(b"hello", 1, symkey=key32, alg="none",
                                  checksum="sha256", padding=16, salt=salt)
        self.assertEqual(aead.decrypt_aea(padded, symkey=key32), b"hello")

    def test_encrypt_rejects(self):
        key32 = bytes(range(32))
        with self.assertRaises(aead.FmtErr):
            aead.encrypt_aea(b"x", 9, symkey=key32)
        with self.assertRaises(aead.FmtErr):
            aead.encrypt_aea(b"x", 1)
        with self.assertRaises(aead.FmtErr):
            aead.encrypt_aea(b"x", 1, symkey=key32, alg="bogus")
        with self.assertRaises(aead.FmtErr):
            aead.encrypt_aea(b"x", 1, symkey=key32, padding="adaptive")
        with self.assertRaises(aead.FmtErr):
            aead.encrypt_aea(b"x", 1, symkey=key32, checksum="bogus")


if __name__ == "__main__":
    unittest.main()
