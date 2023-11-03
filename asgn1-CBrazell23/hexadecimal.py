# Implements operations on hexadecimal numbers.
# CSC 225, Assignment 1
# Given code, Winter '20'

def binary_to_hex(number):
    """
    Convert a 16-bit binary number to hexadecimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: A hexadecimal string, the converted number
    """
    num1 = number[0:4]
    num2 = number[4:8]
    num3 = number[8:12]
    num4 = number[12:16]

    fin1 = 0
    for i in range(len(num1)):
        if(num1[3 - i] == '1'):
            fin1 += 1 * (2 ** i)

    fin2 = 0
    for i in range(len(num2)):
        if (num2[3 - i] == '1'):
            fin2 += 1 * (2 ** i)

    fin3 = 0
    for i in range(len(num3)):
        if (num3[3 - i] == '1'):
            fin3 += 1 * (2 ** i)

    fin4 = 0
    for i in range(len(num4)):
        if (num4[3 - i] == '1'):
            fin4 += 1 * (2 ** i)

    fin1 = hex(fin1)
    fin2 = hex(fin2)
    fin3 = hex(fin3)
    fin4 = hex(fin4)

    return "0x" + fin1 + fin2 + fin3 + fin4

def hex(num):
    if(num == 10):
        return 'A'
    elif(num == 11):
        return 'B'
    elif(num == 12):
        return 'C'
    elif(num == 13):
        return 'D'
    elif(num == 14):
        return 'E'
    elif(num == 15):
        return 'F'
    elif(num == 9):
        return '9'
    elif(num == 8):
        return '8'
    elif (num == 7):
        return '7'
    elif (num == 6):
        return '6'
    elif (num == 5):
        return '5'
    elif (num == 4):
        return '4'
    elif (num == 3):
        return '3'
    elif (num == 2):
        return '2'
    elif (num == 1):
        return '1'
    elif (num == 0):
        return '0'


def unhex(num):
    if(num == 'A'):
        return 10
    elif(num == 'B'):
        return 11
    elif(num == 'C'):
        return 12
    elif(num == 'D'):
        return 13
    elif(num == 'E'):
        return 14
    elif(num == 'F'):
        return 15
    elif(num == '9'):
        return 9
    elif (num == '8'):
        return 8
    elif (num == '7'):
        return 7
    elif (num == '6'):
        return 6
    elif (num == '5'):
        return 5
    elif (num == '4'):
        return 4
    elif (num == '3'):
        return 3
    elif (num == '2'):
        return 2
    elif (num == '1'):
        return 1
    elif (num == '0'):
        return 0


def hex_to_binary(number):
    """
    Convert a hexadecimal number to 16-bit binary.
    TODO: Implement this function.

    :param number: A hexadecimal string, the number to convert
    :return: A bitstring representing the converted number
    """
    number = number[2:]
    arr = [0] * len(number)
    for i in range(len(number)):
        arr[i] = unhex(number[i])
    finArr = [0] * len(number)
    for i in range(len(number)):
        finArr[i] = hexToBinHelp(arr[i])
    fin = ""
    for x in finArr:
        fin += x
    return fin

def hexToBinHelp(number):
    str = ""
    num = 3
    while (num > -1):
        if number >= (2 ** num):
            str += '1'
            number -= (2 ** num)
        else:
            str += '0'
        num -= 1
    return str
