#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - strings test true"""

ipchk = input("What IP Address would you Like to set? ")

# a string tests as True
if ipchk == "192.168.70.1":
    print("This is an invalid IP Address.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
    print("You did not provide an input, please try again.")


