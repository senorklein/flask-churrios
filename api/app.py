from flask import Flask, json
from flask_mysqldb import MySQL

import yaml

from containers.user import User
from lib import userlib

app = Flask(__name__)
conf = yaml.load(open('api/db.yaml'))

mysql = MySQL(app)


@app.route('/')
def index():
    str = "flask"
    return json.dumps(str)


@app.route('/user/<uuid>', methods=['GET'])
def user_get(uuid):
    # test data
    test = {"uuid" : uuid,
           "name" : "test",
           "email" : "test@test.com"}

    cur = mysql.connection.cursor()

    userlib.get_user_by_uuid(cur, uuid)

    user = User(test, test.keys())
    if user['name'] == 'test':
        print("This is a test user: " + user['name'])

    return json.dumps(user)


if __name__ == '__main__':
    app.run()

