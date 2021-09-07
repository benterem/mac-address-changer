#!/usr/bin/env python


import subprocess
import sys

interface = sys.argv[1]
new_mac = sys.argv[2]

print(f"[+] Changing MAC address for {interface} to {new_mac}")

#subprocess.call(f"ifconfig {interface} down", shell=True)
#subprocess.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
#subprocess.call(f"ifconfig {interface} up", shell=True)

