# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:47:26 2024

@author: Van Anh
"""
a = float(input("nhap so a:"))
b = float(input("nhap so b:"))
A = ((a**0.5-b**0.5)/(a**0.25-b**0.25))-((a**0.5+(a*b)**0.25)/(a**0.25+b**0.25))
print("Gia tri bieu thuc la:", A)