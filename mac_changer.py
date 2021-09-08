#!/usr/bin/env python


import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface whose MAC address will be changed")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    
    if not options.new_mac:
        parser.error("[-] Please specify a new MAC address, use --help for more info")
    
    return options

def change_mac(interface, new_mac):
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def check_mac_address(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    search_result = re.search(br"ether ((\w\w:?){6})", ifconfig_result)
    
    if search_result:
        return search_result.group(1).decode()
    else:
        print("[-] could not read MAC address.")
        


options = get_arguments()

mac_add_before = check_mac_address(options.interface)

change_mac(options.interface, options.new_mac)
mac_add_after = check_mac_address(options.interface)

if mac_add_after == options.new_mac:
    print(f"[+] MAC address was succesfully changed to {mac_add_after}")
else:
    print(f"[-] Fail. MAC address unchanged. MAC address = {mac_add_after}")
