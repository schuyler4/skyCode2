from flask import Flask
from pymongo import MongoClient
from secret import data_url
client = MongoClient(data_url)

app = Flask(__name__)

from views.basic import Home
from views.user import Sign_Up, Login

app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/signup', view_func=Sign_Up.as_view('sign_up'))
app.add_url_rule('/login', view_func=Login.as_view('login'))	

if __name__ == "__main__":
	app.run(debug=True);		