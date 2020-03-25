
from methods.general import func, dfuncsub

def newton_method(expr, xn, tol):   #all the work is done here
    
    def newtonform(xn, fxn, dfxn):
        return xn - fxn/dfxn


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
