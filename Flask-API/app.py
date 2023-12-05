from flask import Flask, render_template

app = Flask(__name__,static_url_path="/static")

import os


@app.route("/")
def base():
    return render_template("base.html")


@app.route("/add") # POST handler/endpoint
def add():
    return render_template("add.html")


@app.route("/delete") # DELETE handler/endpoint
def delete():
    return render_template("delete.html")


@app.route("/menu")  # GET handler/endpoint
def menu():
    return render_template("menu.html")


@app.route("/reports")  # GET handler/endpoint
def reports():
    return render_template("reports.html")


@app.route("/update")  # PUT/PATCH handler/endpoint
def update():
    return render_template("update.html")


@app.route("/read")  # GET handler/endpoint
def read():
    return render_template("read.html")
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")