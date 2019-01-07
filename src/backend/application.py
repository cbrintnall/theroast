from roastery import RoasteryApp
from mongo_thingy import connect

from utils.application import register_methodview
from endpoints.beans import Beans

def get_application():
    app = RoasteryApp(__name__)
    connect("mongodb://localhost/test")

    @app.errorhandler(Exception)
    def handle_error(e):
        return {"Error": str(e)}

    register_methodview(app, Beans)

    return app

application = get_application()

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0")