# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Decimal to Binary
result =[]

def decimal_to_binary(decimal):
    while (decimal  > 0):
        rem = int(decimal % 2)
        print (rem)
        result.append(rem)
        decimal = (decimal - rem) / 2
    print (''.join(str(e) for e in result[::-1]))

decimal = int(input("Enter the number in digital format: "))
decimal_to_binary(decimal)

#Binary to Decimal
def binary_to_decimal(binary):
    result_bin,dec = 0, 0
    n=0
    while (binary != 0):
        dec = binary % 10
        print("dec {}:".format(dec))
        binary = binary//10
        print("binary {}:".format(binary))
        result_bin = result_bin + dec * pow(2, n)
        print ("result_bin {}:".format(result_bin))
        n +=1
    print(result_bin)


binary = int(input("Enter the number in binary format: "))
binary_to_decimal(binary)