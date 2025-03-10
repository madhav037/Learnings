from flask import redirect, request, url_for
from app import app

@app.route('/')
def home():
    return "Hello from Home page!"

@app.route('/contact')
def contact():
    return "Hello from contact page!"

@app.route('/about')
def about():
    return "<h1>Hello from about page!</h1>"

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))
    
@app.route('/success/<name>')
def success(name):
    return "welcome %s" % name
        