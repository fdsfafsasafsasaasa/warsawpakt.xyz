from flask import Blueprint

from paktsite import app

upload = Blueprint('upload', __name__, template_folder="templates/upload")