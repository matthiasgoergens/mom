#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from tests.speed import report

setups = [
    "from mom.codec.base58 import b58decode, b58encode; import os; b = b58encode(os.urandom(60))",
    "from mom.codec.base58 import _b58decode, b58encode; import os; b = b58encode(os.urandom(60))",
    None,
    "from mom.codec.base62 import b62decode, b62encode; import os; b = b62encode(os.urandom(60))",
    "from mom.codec.base62 import _b62decode, b62encode; import os; b = b62encode(os.urandom(60))",
    None,
    "from mom.builtins import integer_byte_length; n=1<<4096",
    "from mom.builtins import _integer_byte_length; n=1<<4096",
    "from mom.builtins import _integer_byte_length_1; n=1<<4096",
    None,
    "from mom.builtins import integer_bit_length; n=1<<4096",
    "from mom.builtins import _integer_bit_length; n=1<<4096",
    "from mom.builtins import _integer_bit_length_1; n=1<<4096",
    None,
    "from mom.codec.integer import integer_to_bytes; n=1<<4096",
    "from mom.codec.integer import _long_to_bytes; n=1<<4096",
    "from mom.codec.integer import _integer_to_bytes_a; n=1<<4096",
    "from mom.codec.integer import _integer_to_bytes_python_rsa; n=1<<4096",
    "from mom.codec.integer import _integer_to_bytes_array_based; n=1<<4096",
    None,
    "import os; from mom.codec.integer import bytes_to_integer; b = os.urandom(4003)",
    "import os; from mom.codec.integer import _bytes_to_integer; b = os.urandom(4003)",
]
statements = [
    "b58decode(b)",
    "_b58decode(b)",
    None,
    "b62decode(b)",
    "_b62decode(b)",
    None,
    "integer_byte_length(n)",
    "_integer_byte_length(n)",
    "_integer_byte_length_1(n)",
    None,
    "integer_bit_length(n)",
    "_integer_bit_length(n)",
    "_integer_bit_length_1(n)",
    None,
    "integer_to_bytes(n)",
    "_long_to_bytes(n)",
    "_integer_to_bytes_a(n)",
    "_integer_to_bytes_python_rsa(n)",
    "_integer_to_bytes_array_based(n)",
    None,
    "bytes_to_integer(b)",
    "_bytes_to_integer(b)",
]


def main(setups, statements):
    print("Python %s" % sys.version)
    for setup, statement in zip(setups, statements):
        if setup is None or statement is None:
            print("")
        else:
            report(statement, setup)
    print("\n%s" % ("-" * 100))

if __name__ == "__main__":
    main(setups, statements)

