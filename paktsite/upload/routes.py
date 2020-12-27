from flask import app, render_template, abort, send_from_directory, request
from werkzeug.utils import redirect, secure_filename

import os

from paktsite.upload import upload
from paktsite import app

DISALLOWED_FILE_EXTENSIONS = {
    "py",
    "html",
    "js",
    "sh",
    "bash"
}

@upload.route("/", methods=["GET", "POST"])
def uploadFile():
    if request.method == "GET":
        return render_template("upload.html", files=os.listdir(app.config["UPLOAD_FOLDER"]))
    elif request.method == "POST":
        file = request.files['file']
        if file.filename == "":
            abort(400)
        if file.filename.split(".")[1] in DISALLOWED_FILE_EXTENSIONS:
            abort(400)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename)))
        return redirect(f"/uploads/{file.filename}")

@upload.route("/uploads/<filename>")
def downloadFile(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename=filename)
