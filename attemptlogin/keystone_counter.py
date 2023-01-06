import os

os.chdir("/home/student/mycode/attemptlogin")

failure = 0
success = 0

with open("keystone.common.wsgi","r") as log:
    for line in log:
        if "Authorization failed" in line:
           failure += 1 
           print("Failed login from IP:", line.split(" ")[-1])
           with open("errors.txt","a") as error_file:
                error_file.write(line)
        elif "POST" or "GET" in line:
            success += 1
            with open("successful_login.txt","a") as success_file:
                success_file.write(line)
print("The number of failed attempts is", failure)
print("The number of successful logins is", success)