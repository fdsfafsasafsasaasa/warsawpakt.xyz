from paktsite import app

from flask import render_template


@app.errorhandler(500)
def err_500(*args):
    return render_template("errors/500.html")


@app.errorhandler(401)
def err_401(*args):
    return render_template("errors/401.html")

@app.errorhandler(404)
def err_404(*args):
    return render_template("errors/404.html")