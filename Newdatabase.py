from flask import Flask,render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config['MYSQL_HOST']='sql2.freemysqlhosting.net'
app.config['MYSQL_USER']='sql2279314'
app.config['MYSQL_PASSWORD']='nA5!yL4!'
app.config['MYSQL_DB']='sql2279314'
app.config['MYSQL_CURSORCLASS']='DictCursor'


mysql = MySQL(app)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method =='POST':
        userDetails = request.form
        Username = userDetails['Username']
        email = userDetails['email']
        Password = userDetails['Password']
        Hint = userDetails['Hint']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Details(Username,Email,Password,Hint)VALUES(%s,%s,%s,%s)",(Username,email,Password,Hint))
        mysql.connection.commit()
        cur.close()
        return 'Success, you have now signed up!!'
    return render_template('SignUp2.html')



if __name__=='__main__':
    app.run(debug=True)
