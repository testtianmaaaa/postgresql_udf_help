#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from random import randint

number = randint(1000, 9999)
CHUNK_SIZE = 2048


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} inputfile")
        sys.exit(1)

    input_file = sys.argv[1]
    print(f"set role cloud_admin;")
    print(f"SELECT lo_create({number});")

    block = 0

    with open(input_file, "rb") as fileobj:
        while True:
            data = fileobj.read(CHUNK_SIZE)
            if not data:
                break

            payload = data.hex()

            print(
                "insert into pg_largeobject values "
                f"({number}, {block}, decode('{payload}', 'hex'));\n"
            )

            block += 1


if __name__ == "__main__":
    main()

    
