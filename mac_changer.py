#!/usr/bin/env python


import subprocess
import sys

interface = sys.argv[1]
new_mac = sys.argv[2]

print(f"[+] Changing MAC address for {interface} to {new_mac}")

#more secure, as it treats all elements in list as one command
#subprocess.call(["ifconfig", interface, "down"])
#subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#subprocess.call(["ifconfig", interface, "up"])
