from flask.views import MethodView
from flask import render_template, redirect, request, session, url_for
from models.base import db_session
from models.user import User
from sqlalchemy.sql import exists

class Sign_Up(MethodView):
	
	def get(self):
		return render_template('signup.html');

	def post(self):
		username = request.form['username']
		password = request.form['password']

		new_user = User(username, password)
		db_session.add(new_user)
		db_session.commit()

		session['loggedIn'] = True
		session['username'] = username
		return redirect('/')
	

class Login(MethodView):

	def get(self):
		return render_template('login.html')

	def post(self):
		username = request.form['username']
		password = request.form['password']

		user = db_session.query(User).filter(User.username == username, User.password == password)
		user_exists = db_session.query(user.exists()).scalar()

		if user_exists:
			session['loggedIn'] = True
			session['username'] = username
			return redirect('/')
		else:
			return redirect('/login')

class Logout(MethodView):
    	
	def get(self):
		if session['loggedIn']:
			session['loggedIn'] = False
			session['username'] = None

		return redirect('/')


class Profile(MethodView):
    
	def get(self):
		#username = session['username']
		logged_in = session['loggedIn']
		print(logged_in)
		#logged_in_username = session['username']

		#url_username = request.args.get('username')
		#print(url_username)
		#print(logged_in_username)

		if logged_in:
			return render_template('profile.html')
		else:
			return redirect('/login')

	def post(self):
		pass


