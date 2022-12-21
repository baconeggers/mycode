#!/usr/bin/env python3

# importing code to assist in our program
import shutil
import os

# changing the present working directory
os.chdir('/home/student/mycode/')

# moving selected file to new directory
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user to change name of kerrigan.obj
xname = input('What is the new name for kerrigan.obj?')

# rename kerrigan.obj
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)
