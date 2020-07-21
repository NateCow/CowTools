#===============================================================================
# cowPackagePlates.py
# Version: 1.0.0
# Last Updated: July 19, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# Takes list of shots and extracts plates for comp or roto, then copies them
# to a desginated folder.
# 
# Currently assumes Shot-based file hierarchy:
#   Shot_number
#       live_action
#           exr
#           jpg
#
#================================================================================

import re, os, shutil, glob, time, zipfile
import pyinputplus as pyip
from pathlib import Path

print("Cow Plate Packer\n")

projectCode = input('Please enter the project code: ')
vfxDir = input('\nPlease paste VFX directory: ')

# Convert input string to list using .split()
shots = input('\nPlease enter the shot numbers, separated by spaces: ').split(" ")
label = pyip.inputMenu(['main', 'DN'], prompt='\nPlease select main EXR plates for comp or denoised JPEG plates for roto:\n', numbered=True)
dest = input('\nPlease paste the output directory: ')
packageName = input('\nPlease provide a name for the zip file: ')
destFolder = Path(f'{dest}/{packageName}')

#TODO: Need to deal with more types of plates and possible versions.
if label == 'main':
    format = 'exr'
elif label == 'DN':
    format = 'jpg'


# Create master list with project code appended
shotList = [projectCode+'_'+s for s in shots]
fileName = [projectCode+'_'+s+'_plate_'+label for s in shots]
print(f'\nRetrieving {format} plates...')


for shot in shotList:

    print(f'Copying  {fileName} ...')
    
    target = Path(f'{vfxDir}/{shot}/live_action/{format}/')

    shutil.copytree(target, destFolder, dirs_exist_ok=True)

#TODO: Make this work:
#package = zipfile.ZipFile(f'{destFolder}/{packageName}.zip')
#package.close()

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
input('Press Enter to exit')