# -*- coding: utf-8 -*-
"""
Created on Tue May 11 23:02:32 2021

@author: shweta
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 21:51:19 2020

@author: win10
"""
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class FlowerSpecies(BaseModel):
    Sepal_Length: float   
    Sepal_Width: float 
    Petal_Length: float 
    Petal_Width: float 
   