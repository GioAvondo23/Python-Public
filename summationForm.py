#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:43:24 2024

@author: gio_avondo
"""
import math
from math import comb
import numpy as np


def formula(degree):
    if degree == 0:
        final0 = np.zeros(6)
        final0[0] = 1
        return final0
    
    k = degree + 1
    right = np.zeros(6)
    for i in range(1,k+1):
        right[i-1] = comb(k,i)
    
    for i in range(1,k):
        right = np.subtract(right, float(comb(k,i-1)) *formula(i-1))
    right = right/k
    return right

def formula2(degree):
    k = degree + 1
    right = formula(degree)
    r2 = list(right)
    count = 0
    for i in right:
        r2[count] = i.as_integer_ratio()
        count += 1
    return r2
print(formula(4))


