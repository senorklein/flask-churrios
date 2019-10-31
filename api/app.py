from flask import Flask, json

import yaml

from containers.user import User

app = Flask(__name__)
db = yaml.load(open('api/db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']


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

    user = User(test, test.keys())
    if user['name'] == 'test':
        print("This is a test user: " + user['name'])

    return json.dumps(user)


if __name__ == '__main__':
    app.run()

