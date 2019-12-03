from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from api.dblogic import dbluser
from api.containers.cuser import CUser
import yaml

app = Flask(__name__)
conf = yaml.load(open('api/db.yaml'))

mysql_uri = ''.join(['mysql://',
             conf['mysql_user'],
             ':',
             conf['mysql_password'],
             '@',
             conf['mysql_host'],
             '/',
             conf['mysql_db']])

print (mysql_uri)
app.config['SQLALCHEMY_DATABASE_URI'] = mysql_uri

db = SQLAlchemy(app)

@app.route('/')
def index():
    str = "flask"
    return json.dumps(str)


@app.route('/user/<uuid>', methods=['GET'])
def user_get(uuid):
    user = dbluser.get_user_uuid(uuid)
    return json.dumps(user)


if __name__ == '__main__':
    app.run()

