from flask import Flask
from .controllers.view_controller import bp as view_bp

app = Flask(__name__)
app.secret_key = "thIsIsfakesearchengIne"
app.register_blueprint(view_bp)


app.jinja_env.globals.update(
    zip=zip,
    enumerate=enumerate,
)