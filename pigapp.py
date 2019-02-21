from pigweb import PigWeb
from wsgiref.simple_server import make_server
from blog.handler.user import user_router
from blog.handler.post import post_router

from blog import config


if __name__ == '__main__':

    application = PigWeb()
    PigWeb.register(user_router)
    PigWeb.register(post_router)

    server = make_server(config.WSIP, config.WSPORT, application)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()