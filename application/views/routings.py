from flask import Blueprint, request, Response, make_response, render_template, redirect, session, url_for
from flask import current_app
from flask_cors import CORS
from application import db

route_bp = Blueprint("routs", __name__, url_prefix='/')

@route_bp.route('hello')
def world():
    return "Hello World"

@route_bp.route('/index')
def index():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/index.html', user_name=user_name)


@route_bp.route('/rank')
def rank():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/rank.html', user_name=user_name)


@route_bp.route('/record')
def record():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/record.html', user_name=user_name)


@route_bp.route('/runninglive')
def runninglive():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/runninglive.html', user_name=user_name)


@route_bp.route('/runningvideo')
def runningvideo():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/runningvideo.html', user_name=user_name)


@route_bp.route('/squatlive')
def squatelive():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/squatlive.html', user_name=user_name)


@route_bp.route('/squatvideo')
def squatvideo():

    if 'user_name' in session:
        user_name = session['user_name']
    else:
        user_name = None

    return render_template('/homepage/squatvideo.html', user_name=user_name)

@route_bp.route('/exercise_end', methods=['POST', 'GET'])
def exercise_end():
    print("ok?")
    # data = request.form['data']
    # name = request.form['test']
    # count = data['count']
    print(request.json)
    print(request.json['count'])
    # count = request.form['count']
    # print('name : '+name)
    # print('count : '+count)
    return redirect(url_for('routs.index'))

