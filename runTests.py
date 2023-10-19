#!/usr/bin/python3

import sys
import subprocess

for instance in range(1000) :
    subprocess.check_call(['python','testingServer.py'],\
            stdout=sys.stdout, stderr=subprocess.STDOUT)