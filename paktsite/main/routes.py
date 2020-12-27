from paktsite.main import main

from flask import render_template, request

@main.route("/")
def root():
    return render_template("main/index.html", ip=request.remote_addr)