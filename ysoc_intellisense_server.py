from waitress import serve
from ysoc_intellisense_gui.wsgi import application

if __name__ == '__main__':
    serve(application,  port='8000')
    # serve(application,  port='443')
