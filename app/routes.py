from app import app
from app.forms import IndexForm
from flask import redirect,render_template,url_for

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
    form=IndexForm()
    if form.validate_on_submit():
        return redirect(url_for("info"))
    return render_template("index.html",form=form)