#!/usr/bin/env python3

""" RZFeeser@alta3.com | Alta3 Research
    using the csv library to work with csv data"""

import csv
import os

os.chdir("/home/student/mycode/credmaker/")

try:
    user_input = int(input("If you would like to manually input data, press 1\nOtherwise, press 2: "))
    if user_input == 1:
        outFile = open("admin.rc","a")
        osAUTH = input("What is the OS_AUTH_URL? ")
        print("export OS_AUTH_URL=" + osAUTH, file=outFile)

        print("export OS_IDENTITY_API_VERSION=3", file=outFile)

        osPROJ = input("What is the OS_PROJECT_NAME? ")
        print("export OS_PROJECT_NAME=" + osPROJ, file=outFile)

        osPROJDOM = input("What is the OS_PROJECT_DOMAIN_NAME? ")
        print("export OS_PROJECT_DOMAIN_NAME=" + osPROJDOM, file=outFile)

        osUSER = input("What is the OS_USERNAME? ")
        print("export OS_USERNAME=" + osUSER, file=outFile)

        osUSERDOM = input("What is the OS_USER_DOMAIN_NAME? ")
        print("export OS_USER_DOMAIN_NAME=" + osUSERDOM, file=outFile)

        osPASS = input("What is the OS_PASSWORD? ")
        print("export OS_PASSWORD=" + osPASS, file=outFile)
        outFile.close()
    
    elif user_input == 2:
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
except:
    print("That was not a valid option, please try again.")
print("admin.rc files created!")