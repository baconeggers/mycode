#!/user/bin/env python3

# create a small string
lilstring = "Atlas3 Research offeres classes on Python coding"
newlist = lilstring.split(" ") # this returns a list
print(newlist)

# create a list of strings
myiplist = ["192", "168", "0", "12"]
# set singleip as the result of joining the list myiplist around the "."
singleip = ".".join(myiplist)
print(singleip)

