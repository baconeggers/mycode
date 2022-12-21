#!/usr/bin/env python3

hostname = input("What value should we set for hostname? ")


## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    # these print statements run if hostname.lower has the correct value
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

# this runs the following print if the input doesn't match mtg
else:
    print("hostname does not match expected config")

# this prints regardless of the success/failure of the above
print("Exiting the script")
