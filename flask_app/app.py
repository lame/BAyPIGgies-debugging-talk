from uuid import uuid4

from flask import Flask, redirect, render_template
from flask_wtf.csrf import CSRFProtect

from .form import MyForm


app = Flask(__name__)
app.config["SECRET_KEY"] = str(uuid4())
csrf = CSRFProtect(app)


@app.route("/")
def root():
    form = MyForm()
    if form.validate_on_submit():
        return redirect("/success")
    return render_template("submit.html", form=form)


@app.route("/success")
def success():
    return "<p>Success! Hazaa!</p>"
