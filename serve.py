import tornado.ioloop
import tornado.web
import json

class RandomNameHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.write("{\"first\":\"jebob\"}")

class NameHandler(tornado.web.RequestHandler):
    def post(self):
        self.set_header("Content-Type", "text/json")
        data = self.request.body.decode("utf-8")
        name_data = json.loads(data)
        self.write("You wrote " + data)

        with open("names.txt", "a") as myfile:
            myfile.write(json.dumps(name_data))

def make_app():
    return tornado.web.Application([
        (r"/api/name/random", RandomNameHandler),
        (r"/api/name", NameHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888,'0.0.0.0')
    tornado.ioloop.IOLoop.current().start()
