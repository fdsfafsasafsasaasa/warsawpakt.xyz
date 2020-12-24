from flask import render_template, abort, send_from_directory, request

from paktsite import app

@app.route("/")
def root():
    return render_template("public/index.html", ip=request.remote_addr)