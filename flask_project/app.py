from flask import Flask, jsonify, request, url_for, redirect

app = Flask(__name__)

# Equivalent to the one in app.run(debug=True)
# app.config['DEBUG'] = True
# Only you know!!!
# app.config['SECRET_KEY'] = 'This is a secret'


# ------------------------------------------Set-up------------------------------------------------

# Step 1: set up vene (https://flask.palletsprojects.com/en/1.1.x/installation/#install-create-env)
# Step 2: EXPORT/SET FLASK_APP=app.py; EXPORT/SET FLASK_ENV=development; flask run
#         OR
#         if main block with app.run(debug=True); python app.py
# Quit the venv ==> deactivate


# ---------------------------------------Basic Examples------------------------------------------------

# the url route of the page
# <name> is like a placehold, need to be put in the func as parameter
# so the route should be server/name in order to have return
@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!<h1>'.format(name)


# if no name input, then default is Chesed and path is /home
@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'Chesed'})
# if change string to int, then string type vars cannnot be used;
# but put string here, we could use both int and string
@app.route('/home/<string:name>', methods=['GET', 'POST'])
def homepage(name):
    # return '<h1>You are on the home page!<h1>'
    # The only difference is the font size
    # return 'You are on the home page!'
    return '<h1>Hello {}! You are on the home page<h1>'.format(name)


@app.route('/json')
def home():
    # return '<h1>You are on the home page!<h1>'
    # The only difference is the font size
    return jsonify({'key': 'value'})


# the path will be .../query?name=Chesed&location=Toronto
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {} from {}. You are on the query page!<h1>'.format(name, location)


####################################################################################

# First form
@app.route('/theform1')
def theform1():
    # when click on 'Submit', will go to ../process page
    return '''<form method="POST" action="/process">
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" name="Submit">
           <form>'''


# only want to accept POST request: only the user submits the form
# can go the ../process page
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return 'Hello {}. You are from {}. Submitted successfully'.format(name, location)


# Second form: equivalent to the first form just head on the different pages after submit
@app.route('/theform2', methods=['GET', 'POST'])
def theform2():
    # if users directly go to ../theform2, they will only see the form
    if request.method == 'GET':
        return '''<form method="POST" action="/theform2">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" name="Submit">
               <form>'''
    else:
        # when click on 'Submit', will go to ../theform page as well and see the result
        name = request.form['name']
        location = request.form['location']
        return 'Hello {}. You are from {}. Submitted successfully'.format(name, location)


#####################################################################################

# redirect
@app.route('/redirect_form', methods=['GET', 'POST'])
def redirect_form():
    # if users directly go to ../redirect_form, they will only see the form
    if request.method == 'GET':
        return '''<form method="POST" action="/redirect_form">
                    <input type="text" name="name">
                    <input type="text" name="location">
                    <input type="submit" name="Submit">
               <form>'''
    else:
        name = request.form['name']
        location = request.form['location']

        # return redirect user to ../home after submit, it will use default name
        # return redirect(url_for('homepage')): url_for('function name')
        # return redirect(url_for('homepage', name=name))

        # since location is not valid para in the homepage function, it will be
        # appended as query, i.e. ../home?location=Toronto
        return redirect(url_for('homepage', name=name, location=location))


if __name__ == '__main__':
    app.run(debug=True)
