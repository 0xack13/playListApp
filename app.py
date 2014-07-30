import flask, flask.views
import os
import functools

app = flask.Flask(__name__)

class View(flask.views.MethodView):
	def get(self):
		return "Playlist App in Flask!";

app.add_url_rule('/', view_func=View.as_view('main'))

app.debug = True
app.run()
