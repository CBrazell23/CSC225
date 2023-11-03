# Implements operations on binary numbers.
# CSC 225, Assignment 1
# Given code, Winter '20


def add(addend_a, addend_b):
    """
    Add two 8-bit, two's complement binary numbers; ignore carries/overflows.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param addend_a: A bitstring representing the first number
    :param addend_b: A bitstring representing the second number
    :return: A bitstring representing the sum
    """
    carry = '0'
    str = ""
    for i in range(7, -1, -1):
        num = addend_a[i] + addend_b[i] + carry
        if((num[0] == '1' and num[1] == '1') or (num[1] == '1' and num[2] == '1') or (num[0] == '1' and num[2] == '1')):
            carry = '1'
        else:
            carry = '0'
        if(num[0] == '1' and num[1] == '1' and num[2] == '1'):
            str += '1'
        elif(num[0] == '1' and num[1] == '0' and num[2] == '0'):
            str += '1'
        elif(num[0] == '0' and num[1] == '1' and num[2] == '0'):
            str += '1'
        elif (num[0] == '0' and num[1] == '0' and num[2] == '1'):
            str += '1'
        else:
            str += '0'
        addend_a = addend_a[:len(addend_a)]
        addend_b = addend_b[:len(addend_b)]
    return str[::-1]

def negate(number):
    """
    Negate an 8-bit, two's complement binary number.
    TODO: Implement this function. Do *not* convert the number to decimal.

    :param number: A bitstring representing the number to negate
    :return: A bistring representing the negated number
    """
    str = ""
    for x in number:
        if x == '1':
            str += '0'
        else:
            str += '1'
    num = 7
    fin = ""
    while str[num] != '0':
        if num < 0:
            pass
        else:
            fin += '0'
            num -= 1
    fin += '1'
    num -= 1
    for i in range(num, -1, -1):
        fin += str[i]
    return fin[::-1]


def subtract(minuend, subtrahend):
    """
    Subtract one 8-bit, two's complement binary number from another.
    TODO: Implement this function. Do *not* convert the numbers to decimal.

    :param minuend: A bitstring representing the number from which to subtract
    :param subtrahend: A bitstring representing the number to subtract
    :return: A bitstring representing the difference
    """
    negatedNum = negate(subtrahend)
    return add(minuend, negatedNum)

def binary_to_decimal(number):
    """
    Convert an 8-bit, two's complement binary number to decimal.
    TODO: Implement this function.

    :param number: A bitstring representing the number to convert
    :return: An integer, the converted number
    """
    num = 7
    dec = 0
    while num > -1:
        if(number[num] == '1'):
            dec += 1 * (2 ** (7 - num))
        num -= 1
    return dec


def decimal_to_binary(number):
    """
    Convert a decimal number to 8-bit, two's complement binary.
    TODO: Implement this function.

    :param number: An integer, the number to convert
    :return: A bitstring representing the converted number
    :raise OverflowError: If the number cannot be represented with 8 bits
    """
    str = ""
    num = 7
    while(num > -1):
        if number >= (2 ** num):
            str += '1'
            number -= (2 ** num)
        else:
            str += '0'
        num -= 1
    return str
