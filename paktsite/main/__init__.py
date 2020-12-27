from flask import Blueprint

from paktsite import app

main = Blueprint('/', __name__, template_folder="templates/main")

print("importing main routes")