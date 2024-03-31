from flask import Blueprint

search_engine = Blueprint("search_engine", __name__)


@search_engine.route("/")
def search():
    return
