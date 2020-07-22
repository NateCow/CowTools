#===============================================================================
# cowPackagePlates.py
# Version: 1.0.1
# Last Updated: July 21, 2020
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

import os, shutil, glob, time
import pyinputplus as pyip
from pathlib import Path

print("Cow Plate Packer\n")

projectCode = input('Please enter the project code: ')
vfxDir = input('Please paste VFX directory: ')

# Convert input string to list using .split()
shots = input('Please enter the shot numbers, separated by spaces: ').split(" ")
format = pyip.inputMenu(['EXR', 'JPG'], prompt='Please select the type of plates you need:\n', numbered=True)
packageName = input('Please provide a name for the zip file: ')
destFolder = Path(f'{vfxDir}/_Packages/{packageName}')

#TODO: Need to deal with more types of plates and possible versions.
if format.lower() == 'exr':
    label = 'main'
elif format.lower() == 'jpg':
    label = 'DN'


# Create master list with project code appended
shotList = [projectCode+'_'+s for s in shots]
fileName = [projectCode+'_'+s+'_plate_'+label for s in shots]
print(f'\nRetrieving {format} plates...')


for shot in shotList:

    print(f'Copying  {fileName[0]} ...')
    
    target = Path(f'{vfxDir}/{shot}/live_action/{format}/')

    shutil.copytree(target, destFolder, dirs_exist_ok=True)

#TODO: Make this work:
#package = zipfile.ZipFile(f'{destFolder}/{packageName}.zip')
#package.close()

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
print(f'Plates copied to: {destFolder}')
input('\nPress Enter to exit and open directory...')

os.system(f'start {destFolder}')