#!/usr/bin/env python3

# List of values we're using for this exercise
my_list = [ "192.168.0.5", 5060, "UP" ]


# returning the first value to stdout
print("The first item in the list (IP): " + my_list[0])

# returning the second value to stdout
print("The second item in the list (port): " + str(my_list[1]))

# returning the last value to stdout
print("The last item in the list (state): " + my_list[2])


# Challenge01: Given the following list, display only the IP addresses on screen

iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "SSH" ]

print("IP address list:\n", iplist[3], "\n",  iplist[4]) 
