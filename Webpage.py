
from flask import Flask, render_template, request
import pymysql

db = pymysql.connect('database-1.ceuicflk6aqm.ap-northeast-2.rds.amazonaws.com',
'admin', 'Admin1234')

cursor = db.cursor()

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])

def getdata():
    usrname = request.form['username']
    emailid = request.form['email_id']

    database = "USE employee;"

    cursor.execute(database)

    sql = "INSERT INTO employee VALUES(%s,%s)"

    cursor.execute(sql, (usrname, emailid))
    db.commit()
    return render_template('pass.html', n=usrname, em=emailid)


if __name__ == '__main__':
    app.run(debug=True)


