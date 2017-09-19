from bsddb import db

import additonalFunctions as AF
import click
from flask import Flask
from sqlite3 import dbapi2 as sqlite3


app = Flask(__name__)

DATABASE = 'email.db'
SECRET_KEY = 'development key'


def get_db():
    db = AF.get_db(app, DATABASE)
    return db


@app.teardown_appcontext
def close_DB():
    AF.close_DB()


def init_db():
    AF.init_db()


@app.cli.command('initdb')
def init_db_command():
    AF.initdb_command()


@app.route("/name/name=<name>")
def name(name):
    AF.hello()
    return "what is your name? \n is it " + name + "?"


@app.route("/email-signup/fname=<fname>&lname=<lname>&emailp1=<emailp1>&emailp2=<emailp2>&emailAccept=<emailAccept>")
def signup(fname, lname, emailp1, emailp2, emailAccept):
    print "name: " + fname + " " + lname
    print "email: " + emailp1 + "@" + emailp2
    print "Accept: " + emailAccept
    db = get_db()
    db.execute('select * from user')
    db.execute('insert into user (fname, lname, emailp1, emailp2, emailAccept) values (?, ?, ?, ?, ?)',
               [fname, lname, emailp1, emailp2, emailAccept])
    db.commit()
    return "Thanks for signing up " + fname


if __name__ == "__main__":
    app.run()
