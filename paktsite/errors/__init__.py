from flask import Blueprint

from paktsite import app

errors = Blueprint('error', __name__, template_folder="templates")