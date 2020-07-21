#===============================================================================
# cowPackagePlates.py
# Version: 0.1.0
# Last Updated: July 19, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# Takes list of shots and extracts plates for comp or roto, then compresses
# them into a zip file.
# 
# Currently assumes Shot-based file hierarchy:
#   Shot_number
#       live_action
#           exr
#           jpg
#
#================================================================================

import re, os, shutil, glob, time
from pathlib import Path

print("Cow Plate Packer\n")

projectCode = input('Please enter the project code: ')
vfxDir = input('\nPlease paste VFX directory: ')

# Convert input string to list
shots = input('Please enter the shot numbers, separated by spaces: ').split(" ")
dest = input('Please paste the output directory: ')

# Create master list with project code appended
shotList = [projectCode+'_'+s for s in shots]

print(shotList)

for shot in shotList:
    #TODO: Walk the directory tree to the jpg folder, glob files, copy them to dest.



