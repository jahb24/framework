import tornado.ioloop
import tornado.web

class HolaMundo(tornado.web.RequestHandler):
    def get(self):
        self.write("Hola, profe")

    def post(self):
        user = self.get_argument("username")
        passwd = self.get_argument("password")
        self.write("Your username is %s and password is %s" % (user, passwd))

def make_app():
    return tornado.web.Application([
        (r"/", HolaMundo),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()