from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route('/welcome/<name>')
def welcome(name):
   return 'Welcome %s' % name

@app.route('/api/v1/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('welcome',name = user))
   else:
      user = request.args.get('name')
      return redirect(url_for('welcome',name = user))

@app.route('/api/v1/register',methods=['POST'])
def register():
    name = data['name']
    email = data['email']
    password = data['password']

@app.route('/api/v1/offer',methods=['POST'])
def offer_a_ride():
    depart_location = data['depart_location']
    destination_location = data['depart_location']
    fare = data['fare']
    route = data['route']

@app.route('/api/v1/request',methods=['GET'])
def request_a_ride():
    route = data['route']
    fare = data['fare']
    depart_location = data['depart_location']
    destination_location = data['depart_location']
    driver = data['driver']

@app.route('/api/v1/total_rides',methods=['GET'])
def total_rides():
    route = data['route']
    fare = data['fare']
    depart_location = data['depart_location']
    destination_location = data['depart_location']
    driver = data['driver']

@app.route('/api/v1/admin',methods=['GET'])
def admin():
    name = data['name']
    password = data['password']


if __name__ == '__main__':
   app.run(debug = True)