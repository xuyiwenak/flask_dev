import sys
sys.path.insert(0,'/home/sszj/xuyiwen/flask/examples/blueprintexample')
#sys.path.insert(0,'/home/sszj/xuyiwen/flask/examples/blueprintexample/hello_world')
from flask import Flask, Blueprint
#from blueprintexample.simple_page import simple_page
from simple_page.simple_page import simple_page
#from hello_world.hello_world import hello_world
#import hello_world
#import simple_page
#from blueprintexample.hello_world import hello_world
#hello_world = Blueprint('hello_world', __name__, template_folder='templates')
app = Flask(__name__)
app.register_blueprint(simple_page)
# Blueprint can be registered many times
#simple_page = Blueprint('simple_page', __name__, template_folder='templates')
app.register_blueprint(simple_page, url_prefix='/pages')

#app.register_blueprint(hello_world.hello_world)
#app.register_blueprint(hello_world.hello_world, url_prefix='/hello')
if __name__=='__main__':
  app.run(debug="true", host="103.244.235.249")
