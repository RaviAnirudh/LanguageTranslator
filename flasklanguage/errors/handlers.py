from flask import Blueprint
from flask.templating import render_template

errors=Blueprint('errors',__name__)

@errors.app_errorhandler(500)
def error_500(e):
    return render_template('errors/500.html'),500

@errors.app_errorhandler(404)
def error_404(e):
    return render_template('errors/404.html'),404
