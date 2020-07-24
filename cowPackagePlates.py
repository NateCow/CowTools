#===============================================================================
# cowPackagePlates.py
# Version: 1.1.2
# Last Updated: July 23, 2020
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
#           plate_name
#             exr
#               exr_sequence
#             jpg
#               jpg_sequence
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


#TODO: Comp should copy the entire shot directory. See about not utilizing an exr/jpg folder under live_action
if format.lower() == 'exr':
    label = 'main'
elif format.lower() == 'jpg':
    label = 'DN'


# Create master list with project code appended
shotList = [projectCode+'_'+s for s in shots]
filename = [projectCode+'_'+s+'_plate_'+label for s in shots]

packageFolder = Path(f'{vfxDir}/_Packages/{packageName}')


print(f'\nRetrieving {format} plates...')


for shot in shotList:
    
    shotName = shot+'_plate_'+label
    print(f'Copying  {shotName} ...')
    
    target = Path(f'{vfxDir}/{shot}/live_action/{shotName}/{format.lower()}')
    destFolder = Path(f'{packageFolder}/{shotName}')
    shutil.copytree(target, destFolder, dirs_exist_ok=True)

"""
if format.lower() == 'jpg':
    copyJPGs()
elif format.lower() == 'exr':
    copyEXRs()
"""

#TODO: Make this work:
#package = zipfile.ZipFile(f'{destFolder}/{packageName}.zip')
#package.close()

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
print(f'Plates copied to: {packageFolder}')
input('\nPress Enter to exit and open directory...')

os.system(f'start {packageFolder}')