#!/usr/bin/env python
# coding: utf-8

from flask import Flask, render_template, request, url_for
from tabulate import tabulate
import math
from math import *
import sympy as sp




app = Flask(__name__)

btitles = ['i', 'a', 'b', 'xi', 'f(xi)']
ntitles = ['i', 'x_i-1', 'x_i' ,'tolerance']
stitles = ['i', 'x_i-1', 'x_i-2', 'xi', 'tolerance']


@app.route("/num/bisec", methods=["POST","GET"])
def biseclander():
    return render_template("bisec.html")


@app.route("/num/newton", methods=["POST","GET"])
def newtonlander():
    return render_template("newton.html")


@app.route("/num/secant", methods=["POST","GET"])
def secantlander():
    return render_template("secant.html")



def func(expr, x): #evaluates a func., args: func, x substitute
    return eval(expr)



def dfunc(expr): #derivative of func in terms of x, args: func
    x = sp.Symbol('x')
    symfnu = str(sp.diff(func(expr, x)))
    return symfnu


def dfuncsub(expr, x): #evaluates the derivative of a func., args: func to deriv, x sub.
    return func(dfunc(expr), x)

@app.route("/num/calcbisec", methods=["POST","GET"])
def calcbisec():
    try:
        if request.method=="POST" and request.form['a'] != "" and request.form['b'] != "" and request.form['beqn'] != "" and request.form['btol'] != "" :
            eqn_input = str(request.form['beqn'])
            eqn_input = eqn_input.replace("^","**")
            a_input = float(request.form['a'])
            b_input = float(request.form['b'])
            approx = float(request.form['btol'])
            res = bisection(eqn_input,a_input,b_input,approx)
            zipp = zip(*res)
            table = tabulate(zipp, tablefmt='html', headers=btitles, floatfmt=".10f", numalign="center")
        else:
            return render_template('bisec.html')
            
        return render_template('bisec.html', table=table)
    except:
        return render_template('bisec.html')



def bisection(expr, af,bf,tol):
    a_list = []
    b_list = []
    xi_list = []
    fxi_list = [] 
    i_list = []
    i = 0
    a = af
    b = bf
    xi = (a+b)/2
    a_list.append(a)
    b_list.append(b)
    xi_list.append(xi)
    fxi_list.append(func(expr,xi))
    while (abs(b-a)>tol):
        if (func(expr,xi) < 0):
            b = xi
        else:
            a = xi
        i += 1
        xi = (a+b)/2
        a_list.append(a)
        b_list.append(b)
        xi_list.append(xi)
        fxi_list.append(func(expr,xi))
        i_list.append(i)

    return i_list,a_list, b_list, xi_list, fxi_list
 
@app.route("/num/calcnewton", methods=["POST","GET"])
def calcnewton():
    try:
        if request.method=="POST" and request.form['x0'] != "" and request.form['neqn'] != "" and request.form['napprox'] != "" :
            neqn_input = str(request.form['neqn'])
            neqn_input = neqn_input.replace("^","**")
            x0_input = float(request.form['x0'])
            napprox = float(request.form['napprox'])
            nres = newton_method(neqn_input,x0_input,napprox)
            nzipp = zip(*nres)
            ntable = tabulate(nzipp, tablefmt='html', headers=ntitles, floatfmt=".10f", numalign="center")
        else:
            return render_template('newton.html')
            
        return render_template('newton.html', ntable=ntable)
    except:
        return render_template('newton.html')




def newtonform(xn, fxn, dfxn):
    return xn - fxn/dfxn

def newton_method(expr, xn, tol):   #all the work is done here
    

    xnode_list = []
    oldxnode_list = []
    tol_list= []
    i_list = []
    i = 1
    fnsubxn = func(expr, xn)
    dfnsubxn = dfuncsub(expr, xn)
    old_xnode = 0
    xnode = newtonform(xn, fnsubxn, dfnsubxn)
    xnode_list.append(xnode)
    oldxnode_list.append(old_xnode)
    tol_list.append(abs(xnode-old_xnode))
    i_list.append(i)
    while( abs(xnode-old_xnode)> tol):
        old_xnode = xnode
        fnsubxn = func(expr, xnode)
        dfnsubxn = dfuncsub(expr, xnode)
        xnode = newtonform(xnode, fnsubxn, dfnsubxn)
        i+=1
        xnode_list.append(xnode)
        oldxnode_list.append(old_xnode)
        tol_list.append(abs(xnode-old_xnode))
        i_list.append(i)
        
        
    return i_list, xnode_list, oldxnode_list, tol_list



@app.route("/num/calcsecant", methods=["POST","GET"])
def calcsecant():
    try:
        if request.method=="POST" and request.form['sx0'] != "" and request.form['seqn'] != "" and request.form['sapprox'] != "" and request.form['sx1'] != "":
            seqn_input = str(request.form['seqn'])  
            seqn_input = seqn_input.replace("^","**")
            sx0_input = float(request.form['sx0'])
            sx1_input = float(request.form['sx1'])
            sapprox = float(request.form['sapprox'])
            sres = secant_method(seqn_input,sx0_input,sx1_input,sapprox)
            print(sres)
            szipp = zip(*sres)
            stable = tabulate(szipp, tablefmt='html', headers=stitles, floatfmt=".10f", numalign="center")
        else:
            return render_template('secant.html')
            
        return render_template('secant.html', stable=stable)
    except:
        return render_template('secant.html')


def secantform(xn,oldxn, fxn, oldfxn):
    return xn - (fxn*(xn-oldxn))/(fxn-oldfxn)


def secant_method(expr, oldoldxn, oldxn, tol):   #all the work is done here
   
    xnode_list = []
    oldxnode_list = []
    oldoldxnode_list = []
    tol_list= []
    i_list = []
    i = 2
    old_xnode = oldxn
    oldold_xnode = oldoldxn
    fnsuboldxn = func(expr, oldxn)
    fnsuboldoldxn = func(expr, oldoldxn)
    xnode = secantform(old_xnode, oldold_xnode, fnsuboldxn, fnsuboldoldxn)
    
    xnode_list.append(xnode)
    oldxnode_list.append(old_xnode)
    oldoldxnode_list.append(oldold_xnode)
    tol_list.append(abs(xnode-old_xnode))
    i_list.append(i)
    
    while( abs(xnode-old_xnode)> tol):
        oldold_xnode = old_xnode
        old_xnode = xnode
        
        fnsuboldxn = func(expr, old_xnode)
        fnsuboldoldxn = func(expr, oldold_xnode)

        xnode = secantform(old_xnode, oldold_xnode, fnsuboldxn, fnsuboldoldxn)
        
        i+=1
        xnode_list.append(xnode)
        oldxnode_list.append(old_xnode)
        oldoldxnode_list.append(oldold_xnode)
        tol_list.append(abs(xnode-old_xnode))
        i_list.append(i)
        
    return i_list, oldoldxnode_list, oldxnode_list, xnode_list, tol_list
    


@app.route("/num/", methods=["POST","GET"])
def index():
    return render_template("newindex.html")

if __name__=="__main__":
    app.run(debug=True)