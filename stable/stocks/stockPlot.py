# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 13:14:59 2017

@author: rinfi_000
"""
import csv
import numpy as np
from matplotlib import pyplot as plt

def getInfo(fileName,ticker):
    '''This function takes a file (csv) of stock information and a ticker 
    abbreviation to look for (a string) and returns all of the time and 
    price information about that stock from the file.
    Inputs: 
        fileName, ticker
    Outputs:
        fillTime, fullPrice'''
    ticker = ticker.upper()
    fullPrice = np.array([])
    fullTime = np.array([])
    with open(fileName,'r') as dataFile:
        fileReader = csv.reader(dataFile)
        next(fileReader)
        for stock,price,year,month,day,hour,minute,second in fileReader:
            time = float(second)+60*float(minute)+60*60*float(hour)
            price = float(price)
            if stock.upper()==ticker:
                fullPrice = np.append(fullPrice,price)
                fullTime = np.append(fullTime,time)
    return (fullTime,fullPrice)

fileName = 'stocks.csv'
stockList = np.array(['^DJI','^VIX','GC=F','DIS'])
timeArray = np.array([])
priceArray = np.array([])
for ticker in stockList:
    (tempTime,tempPrice) = getInfo(fileName,ticker)
    plt.plot(tempTime,tempPrice)

plt.legend(stockList)
plt.xlabel('time (sec)')
plt.ylabel('price ($)')
plt.savefig('stockPlot.png')
plt.show()