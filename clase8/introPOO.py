# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 15:01:06 2018

@author: AstroEduardo
"""

AT=15e-6    #Access time 
MF= 140e6   #Modulation frecuency
BW=40e6     #Band Witch Df
AV=650      #Acouestic Velocity (m/s)
IW=403e-9   #Illuminatin wavlentght
#Tscan= 0.01 #Time scnanning



MR=[]
FF=linspace(1000,33000,100)

for FDS in FF:
    
    Tscan=1./FDS
    
    TBP=Tscan*BW
    print ("Resolucion maxima: ", TBP)
    
    Nspots=TBP*(1-(AT/(Tscan-AT)))
    print ("Resolucion real: ",Nspots)
    
    MR.append(Nspots*FDS)
plot (FF,MR)
show()