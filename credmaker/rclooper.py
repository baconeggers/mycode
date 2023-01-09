#!/usr/bin/env python3

""" RZFeeser@alta3.com | Alta3 Research
    using the csv library to work with csv data"""

import csv
import os

os.chdir("/home/student/mycode/credmaker/")


with open("csv_users.txt","r") as csvfile:
    # counter to create unique file names
    i = 0
    # loop across our open file line by line
    for row in csv.reader(csvfile):
        i += 1
        filename = f"admin.rc{i}"

        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

print("admin.rc files created!")