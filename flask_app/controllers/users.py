from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.user import User
from flask_app.models.team import Team

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect('/dashboard')
    return render_template('index.html')

@app.route('/createUser/', methods=['post'])
def createUser():
    data= {
        'firstName': request.form['firstName'],
        'lastName': request.form['lastName'],
        'email': request.form['email']
    }

    id = User.save(data)
    session['user_id']= id
    return redirect('/dashboard/')

@app.route('/login/', methods=['post'])
def login():
    data= {
        'email': request.form['email']
    }

    id = User.getOneForLogin(data)
    print(id)
    session['user_id']= id
    return redirect('/dashboard/')

@app.route('/dashboard/')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id' : session['user_id']
    }
    theUser= User.getOne(data)
    theGames= Team.getAll()
    userGames = Team.AllTeams(data)
    return render_template('dashboard.html', user = theUser, games=theGames, myGames=userGames)

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')