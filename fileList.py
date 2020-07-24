#===============================================================================
# fileList.py
# Version: 1.0.0
# Last Updated: July 22, 2020
# Author: Nathaniel Caauwe
# www.NateCow.com
#===============================================================================

#===============================================================================
# Looks at a folder given and writes a list of the files to a text file
#===============================================================================

import os

print('\nThis tool will create and open a text file with a list of files in a directory.')
directory = input('\nPlease paste the filepath: ')

files = os.listdir(directory)

report = open(f'{directory}/_files.txt', 'w')
report.write('\n'.join(files))
report.close()
os.system(f'start {directory}/_files.txt')