#!/usr/bin/python

import requests
import sys

print "************ OSCP - LM Cracker	             ************"
print "************ By Robert Kugler / @robertchrk   ************"

if len(sys.argv)<2:
	print "Usage: python crack.py lm_hashes.txt"
	sys.exit()
    

print ""
print ("Checking the hashes in ... "+sys.argv[1])
print ""
print ""

with open(sys.argv[1]) as f:
  for line in f:
    r = requests.post("http://cracker.offensive-security.com/insert.php", data={'hash': line.rstrip(), 'type': 'lm', 'method': 'table', 'priority':'insert_here'})
    print("Hash:"+line +"---"+r.content.replace('<META HTTP-EQUIV="Refresh" CONTENT="8;URL=/">',''))
