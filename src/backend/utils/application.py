from flask import Blueprint

def register_methodview(app, endpoint):
    # Take classname and lowercase it
    url = "{}".format(endpoint.__name__.lower())
    view_blueprint = Blueprint(url, __name__)
    view_blueprint.add_url_rule("/", url, endpoint.as_view(url))
    view_blueprint.add_url_rule("/<string:version>", "{}_id".format(url), endpoint.as_view(url))
    app.register_blueprint(view_blueprint, url_prefix="/{}".format(url))