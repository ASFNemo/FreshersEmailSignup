from flask import Flask
from sqlite3 import dbapi2 as sqlite3
from additonalFunctions import DB


app = Flask(__name__)

DATABASE = 'freshers-email.db'
SECRET_KEY = 'development key'

def getDBClass():
	print("yooo")
	db = DB(dbName=DATABASE)
	return 

@app.route("/")
def hello():
	return "hello"

@app.route("/email-signup/fname=<fname>&lname=<lname>&email<email>&emailAccept=<emailAccept>")
def signup(fname, lname, email, emailAccept):
    print "name: " + fname + " " + lname
    print "email: " + emailp1 + "@" + emailp2
    print "Accept: " + emailAccept
    db = getDBClass()
    print ("here")
    db.addFresher(fname, lname, email, emailAccept)
    return "Thanks for signing up " + fname


@app.route("/name=<name>")
def appConnectionTest(name):
	print ("Hello " + name)
	
if __name__ == "__main__":
    app.run()
