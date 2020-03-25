from methods.general import func

def secant_method(expr, oldoldxn, oldxn, tol):   #all the work is done here
   
    def secantform(xn,oldxn, fxn, oldfxn):
        return xn - (fxn*(xn-oldxn))/(fxn-oldfxn)

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
    
