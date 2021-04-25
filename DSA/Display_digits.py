# -*- coding: utf-8 -*-
"""
Dsiplays digits in ones, tens and hundereds
or as a dec, octal, binary no. 
--> done with a list

can do with a stack also
"""

import Stack

num = input("Enter Number: ")
num = int(num)
digits = []
base = 10

while num>0:
    rem = num % base
    digits.append(rem)
    num = num//base

for i in range(len(digits)):
    print(digits[-1-i])