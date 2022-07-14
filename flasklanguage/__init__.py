from flask import Flask


app = Flask(__name__)

from flasklanguage import routes
from flasklanguage.errors.handlers import errors
app.register_blueprint(errors)
