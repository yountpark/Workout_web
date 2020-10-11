from flask import Flask, redirect, url_for, session, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, pprint
from flask_migrate import Migrate
from flask_restful import Api
from application.views.google_api import print_index_table
from flask_socketio import SocketIO
import os


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()
api = Api
socketio = SocketIO()

def create_app(mode='dev'):

    app = Flask(__name__)

    from application.config import config_name
    app.config.from_object(config_name[mode])

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)


    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

    from application.views.google_api import google_api_bp
    from application.views.user import user_bp
    from application.views.cumulative_result import cumulative_bp
    from application.views.routings import route_bp
    app.register_blueprint(google_api_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(cumulative_bp)
    app.register_blueprint(route_bp)

    @app.route('/playing')
    def input_video():
        return render_template('cam.html')

    @app.route('/')
    def init():
        return render_template('homepage/index.html', user_name=None)

    @app.route('/main')
    def main():
        if 'google_id' not in session and 'user_name' not in session:
            return redirect(url_for('google_api.authorize'))

        google_id = session['google_id']
        user_name = session['user_name']

        return render_template('homepage/index.html', user_name=user_name)

    @app.route('/test')
    def test():
        return render_template('cam.html')

    @app.route('/my_model/<path:path>')
    def send_file(path):
        return send_from_directory('my_model', path)

    @socketio.on('myconnect')
    def handle_connect(data):
        print(data['count'])
    return app



