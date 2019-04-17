# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Decimal to Binary
result =[]

def decimal_to_binary(decimal):
    print ("Hello")
    while (decimal  > 0):
        rem = int(decimal % 2)
        print (rem)
        result.append(rem)
        decimal = (decimal - rem) / 2
    print (''.join(str(e) for e in result[::-1]))

decimal = int(input("Enter the number in digital format: "))
decimal_to_binary(decimal)

#Binary to Decimal

