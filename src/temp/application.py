from roastery import RoasteryApp
from endpoints.beans import Beans
from endpoints.users import Users

import os
import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

def get_application():
    app = RoasteryApp(__name__)
    
    app.add_endpoint(Beans)
    app.add_endpoint(Users)

    return app

application = get_application()

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0")