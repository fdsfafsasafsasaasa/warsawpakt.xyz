from flask import render_template, abort, send_from_directory, request, url_for
from flask.helpers import send_file
from werkzeug.utils import redirect, secure_filename

from paktsite import app

import os

DISALLOWED_FILE_EXTENSIONS = {
    "py",
    "html",
    "js",
    "sh",
    "bash"
}

@app.route("/")
def root():
    return render_template("public/index.html", ip=request.remote_addr)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template("public/upload.html", files=os.listdir(app.config["UPLOAD_FOLDER"]))
    elif request.method == "POST":
        file = request.files['file']
        if file.filename == "":
            abort(400)
        if file.filename.split(".")[1] in DISALLOWED_FILE_EXTENSIONS:
            abort(400)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename)))
        return redirect(f"/uploads/{file.filename}")

@app.route("/uploads/<filename>")
def download(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename)

@app.errorhandler(500)
def err_500():
    return render_template("errors/500.html")


@app.errorhandler(401)
def err_401():
    return render_template("errors/401.html")

@app.errorhandler(404)
def err_404():
    return render_template("errors/404.html")
