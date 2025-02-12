# модуль для расчетов операций

import cmath
from fractions import Fraction
from re import U


def Calc_block(data):
    left_value, oper, right_value = data
    if oper == '+':
        result = sum(left_value, right_value)
    if oper == '-':
        result = sub(left_value, right_value)
    if oper == '*':
        result = mult(left_value, right_value)
    if (oper =='/') and (right_value != 0):
        result = div(left_value, right_value)
    else:
        result = 'Ошибка деления на 0!'
    return res


def sum(left_value, right_value):
    return left_value + right_value


def sub(left_value, right_value):
    return left_value - right_value


def mult(left_value, right_value):
    return left_value * right_value


def div(left_value, right_value):
    return left_value / right_value