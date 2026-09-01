from flask import Flask, app, render_template, request,redirect, url_for
import os

app = Flask(__name__)


# Home route
@app.route('/', methods=['GET', 'POST'])
def home():

    #button action handling
    if request.method == 'POST':
        button_value = request.form.get('login-action')
        if button_value == 'login':
            return redirect(url_for("login"))
    return render_template("home.html")