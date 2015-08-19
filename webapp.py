from flask import Flask, render_template, request, url_for
from pymongo import MongoClient

#Mongo Settings
client = MongoClient('db', 27017) # db is the hostname for the mongodb daemon. Need to link the db container to this container and create a local alias in etc/hosts.
db = client.test_database
collection = db.test_collection
posts = db.posts

# Initialize the Flask application
app = Flask(__name__)
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
	if posts.count()!=0:
		N=posts.count()
		return render_template('form_submit.html', messages=posts.find().sort('_id')[N-1]['name'])
	else:
		return render_template('form_submit.html', messages="There are no messages :)")

@app.route('/hello/', methods=['POST'])
def hello():
    name=request.form['yourname']
    posts.insert_one(dict(name=name))
    return render_template('form_action.html', name=name)

if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000"),
        debug=True,
  )
