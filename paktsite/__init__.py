from flask import Flask

app = Flask(__name__)

import paktsite.views

app.config["UPLOAD_FOLDER"] = "paktsite/static/uploads/" 