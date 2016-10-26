from flask.views import MethodView
from flask import render_template


class Sign_Up(MethodView):
	
	def get(self):
		return render_template('user.html');

	def post(self):
		pass


class Login(MethodView):

	def get(self):
		return render_template('login.html')

	def post(self):
		pass