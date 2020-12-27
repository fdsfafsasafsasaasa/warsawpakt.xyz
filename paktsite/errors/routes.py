from paktsite.errors import errors

from flask import render_template


@errors.errorhandler(500)
def err_500(*args):
    return render_template("errorss/500.html")


@errors.errorhandler(401)
def err_401(*args):
    return render_template("errorss/401.html")

@errors.errorhandler(404)
def err_404(*args):
    return render_template("errorss/404.html")