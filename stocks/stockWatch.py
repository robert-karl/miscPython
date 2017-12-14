# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 09:04:21 2017

@author: rinfi_000
"""
'''This is a small script to grab some stock information
from yahoo! finance on an automated schedule.'''

from urllib.request import urlopen
import re
from time import sleep
from datetime import datetime
import os.path
import numpy as np
from matplotlib import pyplot as plt

def getPrice(ticker):
    '''This sub-function will take as input the stock symbol as a string and
    returns the current price, as a float.'''
    websiteName = 'https://finance.yahoo.com/quote/{tic}?p={tic}'.format(tic=ticker.upper())
    
    htmlPage = urlopen(websiteName)
    htmlText = htmlPage.read().decode('utf-8')
    
    lookForStart = 'Price":{"raw":'
    lookForEnd = ',"fmt":'
    lookFor = lookForStart+'.*?'+lookForEnd
    #here's a clip from manual searching:
    '''Price":{"raw":47.785,"fmt":"47.78"}'''
    #Find the text
    priceSpot = re.search(lookFor,htmlText,re.IGNORECASE)
    price = priceSpot.group()
    #Remove the idenifiers
    price = re.sub(lookForStart,'',price)
    price = re.sub(lookForEnd,'',price)
    price = float(price)
    return price
def saveInfo(file,stk,prc,time):
    with open(file,'a') as saveLoc:
        #Prepare the time string for csv format
        time = re.sub(' ',',',time)
        time = re.sub(':',',',time)
        time = re.sub('/',',',time)
        lineLine = '{},{},{}\n'.format(stk,prc,time)
        saveLoc.writelines(lineLine)
        
    

tickerName = 'MU'
watchList = ['^DJI','^VIX','GC=F','dis']
saveFile = 'stocks.csv'
waitTime = 300 #in seconds
numQuery = 5 #number of times to query the website
if not os.path.isfile(saveFile):
    with open(saveFile,'w') as saveLoc:
        saveLoc.writelines('Stock,Price,Year,Month,Day,Hour,Minute,Second\n')
else:
    try:
        tryFile = open(saveFile,'a')
        tryFile.close()  
        #If we have permissions, then do the rest
        muP = getPrice(tickerName)
        for ii in range(0,numQuery):
            for stock in watchList:
                currentTime = datetime.now()
                dateFormat = '%Y %m/%d %H:%M:%S'
                currentTime = currentTime.strftime(dateFormat)
                currentPrice = getPrice(stock)
                print("{}: The price of {} is {}.".format(currentTime,stock.upper(),currentPrice))
                saveInfo(saveFile,stock.upper(),currentPrice,currentTime)
            if ii<numQuery-1:
                sleep(waitTime)        
    except PermissionError:
        print('Please close the file: {} and try again.'.format(saveFile))

