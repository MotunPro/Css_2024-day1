# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:04:08 2024

@author: motunrayobadejo
"""

import pandas

file = pandas.read_csv("diab_data.csv")
print(file)

print (file.info())

print (file.describe())

file = pandas.read_csv("iris.csv")

print (file)

print (file.info())
print (file.describe())
"""
epal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000
"""

file = pandas.read_csv("insurance_data.csv", skiprows=5)

print(file)

file = pandas.read_csv("housing_data.csv")
print(file)
column_names = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N"]
file1 = pandas.read_csv("housing_data.csv","column_names")
print("file1")


