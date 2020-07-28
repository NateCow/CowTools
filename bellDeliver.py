import os, shutil, glob, time
import pyinputplus as pyip
from pathlib import Path
from datetime import datetime

print('Molto Bella VFX Delivery\n')

shotNames = {
    'bell_001_001': 'MOLTO_BELLA_REEL_001_shot_1',
    'bell_001_020': 'VFX_Reel_1_phone',
    'bell_003_020': 'VFX_Reel_3_phone',
    'bell_005_020': 'VFX_Reel_5_Bathroom',
    'bell_005_000': 'VFX_Reel_5_BG_Plate',
    'bell_005_001': 'VFX_Reel_5_sunrise_1',
    'bell_005_010': 'VFX_Reel_5_sunrise_10',
    'bell_005_011': 'VFX_Reel_5_sunrise_11',
    'bell_005_012': 'VFX_Reel_5_sunrise_12',
    'bell_005_013': 'VFX_Reel_5_sunrise_13',
    'bell_005_002': 'VFX_Reel_5_sunrise_2',
    'bell_005_003': 'VFX_Reel_5_sunrise_3',
    'bell_005_004': 'VFX_Reel_5_sunrise_4',
    'bell_005_005': 'VFX_Reel_5_sunrise_5',
    'bell_005_006': 'VFX_Reel_5_sunrise_6',
    'bell_005_007': 'VFX_Reel_5_sunrise_7',
    'bell_005_008': 'VFX_Reel_5_sunrise_8',
    'bell_005_009': 'VFX_Reel_5_sunrise_9'
}

today = datetime.today().strftime('%Y%m%d')
vfxDir = Path(f'S:/Projects/bell/vfx')
deliveryFolder = Path(f'S:/Projects/bell/vfx/_Delivery')

#TODO: Ask for shot numbers.

#TODO: List files in /shot/comp directory.

#TODO: Glob mov's, use [-1] to grab latest version. Set it up to ask for version later.

#TODO: Copy file to _Delivery/today.

#TODO: Rename according to shotNames dictionary.

