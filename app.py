#!/usr/local/anaconda3/bin/python3

import os
import json
from flask import Flask
from flask import render_template, make_response, request
from flask_sqlalchemy import SQLAlchemy
import pymysql
from datetime import datetime



app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True




pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test2'
db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

class File(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)

    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    content = db.Column(db.Text)
    category = db.relationship('Category',
        backref=db.backref('articles', lazy='dynamic'))

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<Article %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<Category %r>' % self.name

db.create_all()

java = Category('Java')
python = Category('Python')
file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool!')
file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool!')
db.session.add(java)
db.session.add(python)
db.session.add(file1)
db.session.add(file2)
db.session.commit()

db_output = File.query.all()

@app.route('/')
def index():
    return render_template('index.html',file_list=db_output)


@app.route('/files/<file_id>')
def file(file_id):
    s = file_id.strip('<>')
    query_result = File.query.filter_by(id=s).first()
    if query_result:
        return render_template('file.html',filename=query_result)
    else:
        return render_template('404.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(port=3000)
