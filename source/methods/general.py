from math import *
import sympy as sp


def func(expr, x): #evaluates a func., args: func, x substitute
    return eval(expr)



def dfunc(expr): #derivative of func in terms of x, args: func
    x = sp.Symbol('x')
    symfnu = str(sp.diff(func(expr, x)))
    return symfnu


def dfuncsub(expr, x): #evaluates the derivative of a func., args: func to deriv, x sub.
    return func(dfunc(expr), x)
