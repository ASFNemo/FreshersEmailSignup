import psycopg2

class DB(object):
 
    def __init__(self):
        print("opening a new DB object")
        print("booo")
        self.connection = psycopg2.connect(database="testdb", user="asherfischbaum", password="123")

        print("database opened successfully")

        cursor = self.connection.cursor()
        print("cursor setting worked")
        cursor.execute("CREATE TABLE IF NOT EXISTS freshers(" +
                        "ID     SERIAL  PRIMARY KEY," + 
                        "FNAME  TEXT    NOT NULL,"+
                        "SNAME  TEXT    NOT NULL," +
                        "EMAIL  TEXT    NOT NULL    UNIQUE," +
                        "EMAILACCEPT BOOL NOT NULL)"   )

        print("TABLE successfully CREATED ")

        self.connection.commit()

    def addFresher(fname, sname, email, emailAccept):
        print("adding fresher")
        cursor = self.connection.cursor()
        print ("connected")
        cursor.execute("INSERT INTO freshers (FNAME, SNAME, EMAIL, EMAILACCEPT)"+
                        "(\'" + FNAME + "\', \'" + SNAME + "\', \'" +  EMAIL + "\', \'" +  EMAILACCEPT + "\')")
        print("statement ok")
        self.connection.commit()
        print("done")



def randomprint(self):
    print("randomprint")
