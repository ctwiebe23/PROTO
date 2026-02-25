import sys
import time
from machine import Pin

while True:
    time.sleep(0.3)

    from_serial = sys.stdin.readline().strip()
    tokens = from_serial.split(" ")

    if len(tokens) == 0:
        continue

    match tokens[0]:
        case "STDOUT":
            sys.stdout.write("foo")
        case "PRINT":
            print("bar")
        case _:
            pass
