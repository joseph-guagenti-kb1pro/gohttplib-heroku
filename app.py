import os
from gohttp import route, run

@route('/')
def index(w, req):
    w.write("%s %s %s\n" % (req.method, req.host, req.url))
    w.write("Hello, world (and Hans2 :).\n")

run(host='', port=os.environ.get('PORT', 5000))
