from flask_app import app
from flask import Flask, render_template, redirect, session, request
from flask_app.models.team import Team
from flask_app.models.user import User

@app.route('/addGame/')
def addGame():
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id': session['user_id']
    }
    theUser = User.getOne(data)
    return render_template('addGame.html', user= theUser)

@app.route('/createGame/', methods=['post'])
def createGame():
    data= {
        'team1': request.form['team1'],
        'team2': request.form['team2'],
        'finalScore': request.form['finalScore'],
        'gameInfo': request.form['gameInfo'],
        'gameDate': request.form['gameDate'],
        'user_id': session['user_id']
    }
    Team.save(data)
    return redirect('/dashboard/')

@app.route('/viewGame/<int:team_id>/view/')
def viewGame(team_id):
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id': team_id
    }
    mygame=Team.getOne(data)
    return render_template('viewGame.html', game=mygame)


@app.route('/editGame/<int:team_id>/edit/')
def editGame(team_id):
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id': team_id
    }
    return render_template('editGame.html', game=Team.getOne(data))

@app.route('/updateGame/<int:team_id>/update/',methods=['POST'])
def updateGame(team_id):
    data= {
        'id': team_id,
        'team1': request.form['team1'],
        'team2': request.form['team2'],
        'finalScore': request.form['finalScore'],
        'gameInfo': request.form['gameInfo'],
        'gameDate': request.form['gameDate']
        
    }
    Team.update(data)
    return redirect(f'/viewGame/{team_id}/view/')

@app.route('/deleteGame/<int:team_id>/delete/')
def deleteGame(team_id):
    if 'user_id' not in session:
        return redirect('/')
    data= {
        'id': team_id
    }
    Team.delete(data)
    return redirect('/dashboard/')
