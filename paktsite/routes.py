from flask import render_template, abort, send_from_directory, request

from paktsite import app

@app.route("/")
def root():
    return render_template("public/index.html", ip=request.remote_addr)

@app.route("/upload")
def upload():
    if request.remote_addr == '47.183.192.96':
        return render_template("public/upload.html")
    else:
        abort(403)