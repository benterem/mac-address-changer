#!/usr/bin/env python


import subprocess
import optparse


parser = optparse.OptionParser()


parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC address will be changed")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

parser.parser_args()


parser.add_option(

interface = sys.argv[1]
new_mac = sys.argv[2]

print(f"[+] Changing MAC address for {interface} to {new_mac}")

#more secure, as it treats all elements in list as one command
#subprocess.call(["ifconfig", interface, "down"])
#subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
#subprocess.call(["ifconfig", interface, "up"])
