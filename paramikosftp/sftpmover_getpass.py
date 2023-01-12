#!/usr/bin/env python3

# import paramiko so we can talk SSH
import paramiko
import os
import getpass

def movethemfiles(sftp, fileloc):
    # iterate across the files within directory
    try:
        for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
            if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is not a directory
                sftp.put("/home/student/filestocopy/"+x, fileloc +x) # move file to target location
    except Exception as err:
        print("There was an error moving the files!", err)
def main():
    # where to connect to
    t = paramiko.Transport("10.10.2.3",22) #ip and port of bender

    # how to connect
    t.connect(username="bender",password=getpass.getpass()) # notice the password references getpass

    # make an SFTP connection object
    sftp = paramiko.SFTPClient.from_transport(t)

    fileloc = input("Where on the remote host should the files go?\n")

    movethemfiles(sftp, fileloc)

    # close the connection
    sftp.close()


if __name__ == "__main__":
    main()