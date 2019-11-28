from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import migrate

app = Flask(__name__)
app.config["SECRET_KEY"] = "478223b132a12560b5e7a4188e7cbddc3ab37d58fa71328c8c8fb17e42f754c7"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost/fr_data_base"
db = SQLAlchemy(app)

from website import routes