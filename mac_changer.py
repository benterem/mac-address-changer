#!/usr/bin/env python


import subprocess
import sys

interface = sys.argv[1]
new_mac = sys.argv[2]

print(f"[+] Changing MAC address for {interface} to {new_mac}")

#subprocess.call("ifconfig wlan0 down", shell=True)
#subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
#subprocess.call("ifconfig wlan0 up", shell=True)

