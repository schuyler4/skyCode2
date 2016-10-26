from flask.views import MethodView
from flask import render_template


class Home(MethodView):

	def get(self):
		return render_template('home.html')

	def post(self):
		pass


class Page_Not_Found(MethodView):

	def get(self):
		return render_templatel('404.html')


class Server_Error(MethodView):
	
	def get(self):
		return render_templatel('500.html')