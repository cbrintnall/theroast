from flask import Blueprint

def generate_blueprint(endpoint_cls):
    # Take classname and lowercase it
    url = endpoint_cls.__name__.lower()
    view_blueprint = Blueprint(url, __name__)
    view_blueprint.add_url_rule("/", 
                                url, 
                                endpoint_cls.as_view(url))
    view_blueprint.add_url_rule("/<string:uid>", 
                                "{}_id".format(url), 
                                endpoint_cls.as_view(url))
    return view_blueprint