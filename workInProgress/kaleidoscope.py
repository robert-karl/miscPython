# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 15:41:49 2019

Kaleidoscope

This program creates a kaleidoscope image and plots it

The options for the user are:
    What image to load
    How far to shift left-right or up-down
    The number of slices in the final image
    The number of pixels in the image
    
@author: rinfi_000
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage as ndi
from scipy import misc
from os import path as path
from matplotlib.animation import FuncAnimation

def pickImage():
    ''' Selects the image from the filesystem and loads it to the workspace'''
    # Load image from file
    #pathImage = r"C:\Users\rinfi_000\Pictures\ScienceArt";
    pathImage = r"C:\Users\rinfi_000\Pictures\Wallpapers";
    fileName = r'Mayan_Groudon_Kyorge_Rayquaza.jpg';
    fullFile = path.join(pathImage,fileName);
    imageBase = misc.imread(fullFile);
    return imageBase

def shiftImage(image,shiftY,shiftX):
    '''shifts the image by the prescribed amounts and returns the shifted image
    '''
    image = np.roll(image,shiftY,axis=0);
    image = np.roll(image,shiftX,axis=1);
    return image;

def getCenter(image,Nim):
    '''Takes the central Nim by Nim square from the center of the image.'''
    Ny,Nx,Nc = image.shape;
    # Ensure that these are even numbers
    Ny+=Ny%2;
    Nx+=Nx%2;
    if Ny>Nim and Nx>Nim:
        image = image[int(Ny/2-Nim/2):int(Ny/2+Nim/2),int(Nx/2-Nim/2):int(Nx/2+Nim/2),:];
    return image

def makeWedge(Nim,Nslice):
    '''Creates the wedge shaped mask that is used to select the region to 
    reflect and rotate.'''
    xx,yy = np.meshgrid(np.linspace(-Nim/2,Nim/2,Nim),np.linspace(-Nim/2,Nim/2,Nim));
    
    limAngle = yy/xx < np.tan(2*np.pi/Nslice);
    limZeroY = yy>0;
    limZeroX = xx>0;
    
    limAll = limAngle*limZeroY*limZeroX;
    if Nc>1:
        limAll
    limAll = np.reshape(limAll,[Nim,Nim,1]); # Makes it a 3D array for better compatibility
    return limAll

def makeKaleido(imageBase,wedgeMask,Nslice,Nc):
    '''Takes the image and the wedge mask and reflects and rotates to make the 
    kaleidoscope image.'''
    # Prepare the image
    kaleido = np.zeros([Nim,Nim,Nc]);
    wedge = np.zeros([Nim,Nim,Nc]);
                      
    wedge = imageBase*wedgeMask;
    wedge = wedge + np.flipud(wedge);
    wedgeRot = np.zeros([Nim,Nim,Nc]);
    # Reflect the sections
    for slice in range(int(Nslice/2)):
        angle = slice*360/Nslice*2;
        wedgeRot += ndi.rotate(wedge,angle,reshape=False);
    kaleido=wedgeRot;
    
    # Clean up the image for RGB usage
    kaleido=(kaleido-np.min(kaleido))/(np.max(kaleido)-np.min(kaleido)) ;
    return kaleido


# Parameters to tune
# Final size of the image (square)
Nim = 400;
# Amount to shift the base image by
shiftY = 150; #units of pixels
shiftX = 210; 
# Number of slices in the kaleidoscope image
Nslice = 20;

# Select the image
imageBase = pickImage();
Nc = imageBase.shape[2]; # Determine how many color channels there are.

# Set up the figure
im = plt.imshow(np.ones([Nim,Nim]));
# Shift the image
imageBase = shiftImage(imageBase,shiftY,shiftX);             
# Select sub-region of the image
imageBase = getCenter(imageBase,Nim);
# Create the wedge
wedgeMask = makeWedge(Nim,Nslice);
# Create kaleidoscope image
kaleido = makeKaleido(imageBase,wedgeMask,Nslice,Nc);
# Make the plot
im.set_array(kaleido);
