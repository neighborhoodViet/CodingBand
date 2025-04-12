# Configurations for the application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///appdatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

appDB = SQLAlchemy(app)  # creates a database instance

