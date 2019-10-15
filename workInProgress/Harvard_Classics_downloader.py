# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:03:57 2019

This program scrapes the website /www.myharvardclassics.com and downloads all 
of the harvard classics collection to a local directory. Currently that 
directory is hard coded internally. This can be changed to make it user 
supplied

@author: rinfi_000
"""

import urllib.request as ul
import shutil as sh
import os

# Get the pdf from the download site
def getPDF(URL,path2file,fileNum):
    file_name = 'v{0}.pdf'.format(fileNum)
    fullfile = os.path.join(path2file,file_name)
    with ul.urlopen(URL) as response, open(fullfile,'wb+') as output_file:
        sh.copyfileobj(response,output_file)
    fileNum = fileNum+1
    return fileNum

# Establish the target directory
path2file = r'C:\Users\rinfi_000\Documents\eBooks\HarvardClassics'
# In order to name the files sequentially, this counter is employed
fileNum = 1


# The website's organization is not super intuitive, so this is done in a 
# piecemeal fashion
URLuse = 'http://www.myharvardclassics.com/downloads/20120212/download'
fileNum = getPDF(URLuse,path2file,fileNum)

for num in range(1,14):
    URLuse = 'http://www.myharvardclassics.com/downloads/20120212_{0}/download'.format(num)
    fileNum = getPDF(URLuse,path2file,fileNum)

URLuse = 'http://www.myharvardclassics.com/downloads/20120213/download'
fileNum = getPDF(URLuse,path2file,fileNum)

for num in range(1,36):
    URLuse = 'http://www.myharvardclassics.com/downloads/20120213_{0}/download'.format(num)
    fileNum = getPDF(URLuse,path2file,fileNum)
    
URLuse = 'http://www.myharvardclassics.com/downloads/20120605/download'
fileNum = getPDF(URLuse,path2file,fileNum)

URLuse = 'http://www.myharvardclassics.com/downloads/20120605_1/download'
fileNum = getPDF(URLuse,path2file,fileNum)
    

        