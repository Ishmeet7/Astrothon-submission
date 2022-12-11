# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GUJuGeIvOhPII2UO8w4jwhNjPPJUf6OF
"""
#installing and importing packages
pip install astropy

from astropy.cosmology import WMAP9 as cosmo
from astropy import units as u

#taking value of scale factor as input
scale_factor=float(input("Enter the value of scale factor:"))  

#calculation of redshift,z
z=(1/scale_factor)-1
#taking distance of galaxy from planet as input
dist=float(input("Enter distance of galaxy from planet:"))   #enter distance in million years i.e.if distance is 5 million light years enter just 5

#h0=hubble's constant
#calculating hubble's constant
h0=cosmo.H(z)

#age=age of universe  
#calculating age of universe
age=cosmo.age(z)  

#size=size of universe
taking size of universe as input
size_univ=float(input("Enter size of the universe observer is in:"))  #if distance is 5 million light years enter just 5

#calculating distance upto which galaxy can be seen
distance=size_univ-dist

#calculating rs=speed of recession of galaxy        
rs=d*h0

#conversion of megaparsec to km
x = 1.0 * u.megaparsec
y=x.to(u.km) 

#calculating time(t) upto which galaxy can be seen 
t=(distance*y)/rs
print("Time period(in seconds) to know  about a galaxy is: "+ str(t))

#conversion of units
x = 1.0 * u.megaparsec
y=x.to(u.km)
print(y)
