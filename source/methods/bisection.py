from methods.general import func

def bisection_method(expr, af,bf,tol):
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
 