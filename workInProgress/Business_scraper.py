# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:04:21 2017

@author: rinfi_000
"""
'''This is a small script to grab some stock information
from business websites for Michelle on an automated schedule.'''

from urllib.request import urlopen
import re

     
def findInString(textBlock,startTag,endTag):
    names = []
    nameLocations = re.finditer(startTag,htmlText)
    for match in nameLocations:
        nameEnd = textBlock.find(endTag,match.start(),len(htmlText))
        names.append(textBlock[match.start()+len(startTag):nameEnd])
    return names

#websiteName = 'https://www.iapws.com/about/leadership/board-of-directors/'
#websiteName = "https://www2.deloitte.com/us/en/pages/technology/articles/meet-our-leaders-technology-services.html"
#websiteName = 'https://www.lockheedmartin.com/en-us/who-we-are/leadership-governance.html'
websiteName = 'https://www.raytheon.com/ourcompany/leadership'

htmlPage = urlopen(websiteName)
htmlText = htmlPage.read().decode('utf-8')

# Using the delimiter for headings in html, we can extract names
startTagName = '.pdf" target="_blank">'
endTagName = '</a></div>'
startTagTitle = '--label-hidden field--item"><p>'
endTagTitle = '</p></div>\n'

names = findInString(htmlText,startTagName,endTagName)
titles = findInString(htmlText,startTagTitle,endTagTitle)

for order in range(len(names)):
    print('{0} holds the title {1}'.format(names[order],titles[order]))
