
from flask import Flask, render_template, request, url_for
from tabulate import tabulate
from math import *
from methods.bisection import bisection_method
from methods.secant import secant_method
from methods.newton import newton_method
from methods.general import func, dfunc, dfuncsub
from methods.trapezoidal import trapezoidal
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


@app.route("/num/trapezoid", methods=["POST","GET"])
def trapezoidlander():
    return render_template("trapezoidal.html")


@app.route("/num/calcbisec", methods=["POST","GET"])
def calcbisec():
#try:
    if request.method=="POST" and request.form['a'] != "" and request.form['b'] != "" and request.form['beqn'] != "" and request.form['btol'] != "" :
        eqn_input = str(request.form['beqn'])
        eqn_input = eqn_input.replace("^","**")
        a_input = float(request.form['a'])
        b_input = float(request.form['b'])
        approx = float(request.form['btol'])
        res = bisection_method(eqn_input,a_input,b_input,approx)
        zipp = zip(*res)
        table = tabulate(zipp, tablefmt='html', headers=btitles, floatfmt=".10f", numalign="center")
    else:
        return render_template('bisec.html')
        
    return render_template('bisec.html', table=table)
#except:
    #return render_template('bisec.html')



@app.route("/num/calcnewton", methods=["POST","GET"])
def calcnewton():
# try:
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
# except:
#     return render_template('newton.html')


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




@app.route("/num/calctrapezoid", methods=["POST","GET"])
def calctrapezoid():
    if request.method=="POST" and request.form['equation'] != "" and request.form['lowerinterval'] != "" and request.form['higherinterval'] != "" and request.form['n'] != "":
        eqn_input = request.form['equation']
        eqn_input = eqn_input.replace("^","**")
        lowerinterval = float(request.form['lowerinterval'])
        higherinterval = float(request.form['higherinterval'])
        n = int(request.form['n'])
        res = trapezoidal(eval("lambda x:" + eqn_input), lowerinterval, higherinterval, n)
    else:
        return render_template('trapezoidal.html')
        
    return render_template('trapezoidal.html', table=res)



@app.route("/num", methods=["POST","GET"])
def index():
    return render_template("newindex.html")

if __name__=="__main__":
    app.run(debug=True)