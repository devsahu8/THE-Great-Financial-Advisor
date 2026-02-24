from app import app
from app.forms import IndexForm
from flask import redirect,render_template,url_for
from app.get_data import lower,middle,upper

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    form=IndexForm()
    if form.validate_on_submit():
        amount=form.amount.data
        if amount<=5000:
            return redirect(url_for("lower_fun",amount=amount))
        elif amount>=500000:
            return redirect(url_for("upper_fun",amount=amount))
        else:
            return redirect(url_for("middle_fun",amount=amount))
    return render_template("index.html",form=form)

@app.route("/lower_fun/<int:amount>")
def lower_fun(amount):
    data=lower(amount)
    return render_template("lower.html",data=data)

@app.route("/middle_fun/<int:amount>")
def middle_fun(amount):
    data=middle(amount)
    return render_template("middle.html",data=data)

@app.route("/upper_fun/<int:amount>")
def upper_fun(amount):
    data=upper(amount)
    return render_template("upper.html",data=data)