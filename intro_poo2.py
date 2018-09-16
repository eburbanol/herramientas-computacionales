# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 16:12:39 2018

@author: AstroEduardo
"""

from pylab import *

#AT=15e-6    #Access time 
#MF= 140e6   #Modulation frecuency
#BW=40e6     #Band Witch Df
AV=650      #Acouestic Velocity (m/s)
IW=403e-9   #Illuminatin wavlentght
#Tscan= 0.01 #Time scnanning



MR=[]
MR2=[]
MR3=[]
MR4=[]

FF=linspace(1000,33000,100)

for FDS in FF:
    AT=15e-6    #Access time 
    BW=40e6     #Band Witch Df
    
    Tscan=1./FDS
    
    TBP=Tscan*BW
    print ("Resolucion maxima: ", TBP)
    
    Nspots=TBP*(1-(AT/(Tscan-AT)))
    print ("Resolucion real: ",Nspots)
    
    MR.append(Nspots*FDS)
for FDS2 in FF:
    AT=25e-6    #Access time 
    BW=40e6     #Band Witch Df
    Tscan=1./FDS2
    
    TBP=Tscan*BW
    print ("Resolucion maxima: ", TBP)
    
    Nspots=TBP*(1-(AT/(Tscan-AT)))
    print ("Resolucion real: ",Nspots)
    
    MR2.append(Nspots*FDS2) 
for FDS3 in FF:
    AT=15e-6    #Access time 
    BW=60e6     #Band Witch Df
    Tscan=1./FDS3
    
    TBP=Tscan*BW
    print ("Resolucion maxima: ", TBP)
    
    Nspots=TBP*(1-(AT/(Tscan-AT)))
    print ("Resolucion real: ",Nspots)
    
    MR3.append(Nspots*FDS3) 
for FDS4 in FF:
    AT=20e-6    #Access time 
    BW=60e6     #Band Witch Df
    Tscan=1./FDS4
    
    TBP=Tscan*BW
    print ("Resolucion maxima: ", TBP)
    
    Nspots=TBP*(1-(AT/(Tscan-AT)))
    print ("Resolucion real: ",Nspots)
    
    MR4.append(Nspots*FDS4)     
plot (FF,MR) 
plot (FF,MR2) 
plot (FF,MR3) 
plot (FF,MR4) 

show()