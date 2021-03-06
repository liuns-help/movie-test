#coding:utf-8
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

import pymysql

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root123@192.168.1.201:3306/movie"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.debug=True
db = SQLAlchemy(app)



from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404





