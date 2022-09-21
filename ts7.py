from flask import Flask, render_template
from ts6 import *

s = starter("dan")

app = Flask(__name__)

def reverse(x):
    items = list(x.items())
    y = {k: v for k, v in reversed(items)}
    return y


@app.route("/")
def nach():
    return "Это ответ на 7 таск (начальная страница)"

@app.route("/report")
def table():
    return render_template("table.html",tables=s)

@app.route("/report/drivers")
def drivers():
    return render_template("drivers.html",tables=s)

@app.route('/report/drivers/driver_id=<string:about>')
def about(about:str):
    return render_template("dn.html",dn=about,tables=s)

@app.route("/report/drivers/order=desc")
def order():
    return render_template("table_ord.html",tables=reverse(s))

if __name__ == '__main__':
    app.run(debug=True)