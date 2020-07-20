#===============================================================================
# cowSortPlates
# Version: 1.0.0
# Last Updated: July 19, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# Looks at a folder of VFX plates as outputted by Premiere's Project Manager
# and sorts them into their respective folders in a user-specified directory.
# 
# Currently operating under two key assumptions:
# 1. A VFX directory as such:
#   Shot_number
#       live_action
#           exr
#
# 2. Plate names lead with the same string as the individual shot directories
#================================================================================

import re, os, shutil, glob, time
from pathlib import Path

print("NateCow's Premiere Project Manager VFX Plate Mover 9000\n\n")

# Get the Premiere and VFX directories from user
print('Paste Premiere output directory (source):')
sourcePath = input()
#TODO: Input validation to make sure a valid directory has been provided.
print('\nPaste VFX directory (destination):')
vfxDir = input()
shotList = os.listdir(vfxDir)

os.chdir(sourcePath)
time.sleep(1)

print('\nHold onto your butts...\n')
time.sleep(1)

# Test directories
# S:\Development\Automation\Transcoded_Brothers_Quarrel_Full_v05
# S:\Development\Automation\bro_vfx


for shot in shotList:

    frames = glob.glob(f'{shot}*')
    dest = Path(f'{vfxDir}/{shot}/live_action/exr') #TODO: Make sub-directories user controlled
    
    if len(frames):
        fileName = frames[0].split('.')[0]
        print(f'Moving  {fileName}  to  {dest}')

        for f in frames:
            shutil.move(f, dest)

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
print("Exiting...")
time.sleep(3)