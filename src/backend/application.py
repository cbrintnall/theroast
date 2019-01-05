from core import RoasteryApp

def get_app(*args, **kwargs):
    return RoasteryApp()

application = get_app()

if __name__ == '__main__':
    application.run(debug=True)
