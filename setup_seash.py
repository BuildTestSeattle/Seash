
"""
# !/usr/bin/python

<Program>
  setup_seash.py 
  
<Date Started>
  July 5th, 2014

<Author>
  Chintan Choksi

<Purpose>
  This script does a git check-out of all the dependent repositories of Seash to the home directory.
  
<Usage>
  How to run this program:
  1. Clone the seash repository to local machine, and run this script
  2. Run this script: 
  seash user$ python setup_seash.py
   
"""


import commands
import subprocess
import os
import sys

"""
==========================================================================================
if not os.path.exists('target/'):
    os.makedirs('target/')
   
I have kept this in comment as it's still to be decided whether to create a new target 
folder or check-out the repositories in current working directories
==========================================================================================
"""    
pr = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/seattlelib_v2" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr.communicate()
print str(out)

pr1 = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/clearinghouse" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr1.communicate()
print str(out)

pr2 = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/portability" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr2.communicate()
print str(out)

pr3 = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/repy_v2" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr3.communicate()
print str(out)

pr4 = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/repy_v1" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr4.communicate()
print str(out)

pr5 = subprocess.Popen( "/usr/bin/git clone https://github.com/SeattleTestbed/dist -b git-aware-buildscripts" , cwd = os.getcwd(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE )
(out, error) = pr5.communicate()
print str(out)



