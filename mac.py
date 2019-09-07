#!/usr/bin/env python 


import subprocess
import optparse
import re

print(" "*30 + "-"*28)  
print(" "*30 + "|" + "  Welcome To Mac Changer  " + "|")
print(" "*30 + "-"*28)

def Get_Arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i","--interface", dest="interface",help="Interface to change mac address")
	parser.add_option("-m","--mac", dest="mac_to_spoof",help="mac address to change")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("	Please specify the interface you want to change mac ,use -h or --help to know how to use")
	elif not options.mac_to_spoof:
		parser.error("	Please specify the new mac address ,use -h or --help to know how to use")
	return options

def Changing_Mac(interface,mac_to_spoof):
	subprocess.call(["ifconfig" , interface , "down"])
	subprocess.call(["ifconfig" , interface , "hw" , "ether" , mac_to_spoof ])
	subprocess.call(["ifconfig" , interface , "up"])
	print("Trying To change you mac address")
	

def Current_Mac(interface):
	mac_result = subprocess.check_output(["ifconfig",interface])	
	result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",mac_result)
	
	if result:
		return result.group(0)
	else:
		print("[*] Couldnot read mac address ,interface doesnt have mac")

		print("[*] Couldnot read mac address ,interface doesnt have mac")

options =  Get_Arguments()



previous_mac = Current_Mac(options.interface)
print("[*] Current Mac:: " + previous_mac)

Changing_Mac(options.interface,options.mac_to_spoof)


current_mac = Current_Mac(options.interface)
if current_mac == options.mac_to_spoof:
	print("[*] Mac Address has been changed succesfully from " + previous_mac +  " to " + current_mac )
else:
	print("[*] Cant Able to change Mac")










