#!/usr/bin/python3
for ch in range(97, 123):
    if chr(ch) not in ['q', 'e']:
        print("{}".format(chr(ch)), end='')
