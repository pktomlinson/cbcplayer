#!/usr/bin/python3

import subprocess

getvolume = subprocess.check_output(['mpc', 'volume'])
getvolume = getvolume.decode("utf-8")
x = len(getvolume) - 1
getvolume = getvolume[0:x]
print(getvolume[8:x-1])

