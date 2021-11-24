from flask import Flask
from pymysql import connections
from database.ConnectionFactory import ConnectionFactory

app = Flask(__name__) 

connection = ConnectionFactory(app)

from controllers import sellers 

#rodar nossa aplicacao

if __name__ == "__main__":
    app.run(debug=True)