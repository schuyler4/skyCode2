from flask import Flask, session
from secret import data_url
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '()SDYFUHISDJUHF&**UI&^*&^YUHJ'

from views.basic import Home
from views.user import Sign_Up, Login, Logout

app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/signup', view_func=Sign_Up.as_view('sign_up'))
app.add_url_rule('/login', view_func=Login.as_view('login'))	
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))

if __name__ == "__main__":
	app.run(debug=True);		