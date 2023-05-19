from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost:3306/test_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////testdb.db'

db = SQLAlchemy(app)














if __name__=="__main__":
    app.run(debug=True)



