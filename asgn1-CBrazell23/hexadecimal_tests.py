# Tests operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given tests, Winter '20

import unittest
import hexadecimal as hx


class TestHexadecimal(unittest.TestCase):
    def test01_binary_to_hex(self):
        msg = "Testing basic binary-to-hex conversion"
        self.assertEqual(hx.binary_to_hex("0000010100011010"), "0x051A", msg)
        self.assertEqual(hx.binary_to_hex("0010010100111010"), "0x253A", msg)

    def test02_hex_to_binary(self):
        msg = "Testing basic hex-to-binary conversion"
        self.assertEqual(hx.hex_to_binary("0x051A"), "0000010100011010", msg)
        self.assertEqual(hx.hex_to_binary("0xFFFF"), "1111111111111111", msg)
        self.assertEqual(hx.hex_to_binary("0x142A"), "0001010000101010", msg)


if __name__ == "__main__":
    unittest.main()
