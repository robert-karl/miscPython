# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:38:30 2019

A sequel to the downloader, this function changes the names of a group of files 
from v#.pdf to Harvard_Classics_vol#.pdf

@author: rinfi_000
"""

import os
import glob

path2file = r'C:\Users\rinfi_000\Documents\eBooks\HarvardClassics'
source = os.path.join(path2file,'v{}.pdf')

dest = os.path.join(path2file,'Harvard_Classics_vol{}.pdf')

for filename in glob.glob(os.path.join(path2file,'v*.pdf')):
    # use the \v and the .pdf to identify which number the file is. 
    firstChar = filename.index(r'\v')
    lastChar = filename.index('.pdf')
    keep = filename[firstChar+2:lastChar]
    # Make a new filename
    newFilename = os.path.join(filename[0:firstChar],'Harvard_Classics_vol{}.pdf'.format(keep))
    
    # Change the name, keeping the number
    os.rename(filename,newFilename)
