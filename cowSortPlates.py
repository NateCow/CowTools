#===============================================================================
# cowSortPlates.py
# Version: 1.1.0
# Last Updated: July 23, 2020
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
#           plate_name
#             exr
#               exr_sequence
#
# 2. Plate names lead with the same string as the individual shot directories
#================================================================================

import os, shutil, glob, time
from pathlib import Path

print("NateCow's Premiere Project Manager VFX Plate Mover 9000\n\n")

# Get the Premiere and VFX directories from user
sourcePath = input('Paste Premiere output directory (source): ')
#TODO: Input validation to make sure a valid directory has been provided.
vfxDir = input('\nPaste VFX directory (destination): ')
shotList = os.listdir(vfxDir)

os.chdir(sourcePath)
time.sleep(1)

print('\nHold onto your butts...\n')

# Test directories
# S:\Development\Automation\Transcoded_Brothers_Quarrel_Full_v05
# S:\Development\Automation\bro_vfx


for shot in shotList:

    frames = glob.glob(f'{shot}*')    
    
    if len(frames):
        fileName = frames[0].split('.')[0]
        newDir = f'{vfxDir}/{shot}/live_action/{fileName}/exr'
        os.mkdir(newDir)
        dest = Path(newDir) #TODO: Make sub-directories user controlled
        
        print(f'Moving  {fileName}  to  {dest}')

        for f in frames:
            shutil.move(f, dest)

message = "Job's done!"
print("-"*len(message) + "\n" + message + "\n")
input('Press Enter to exit')