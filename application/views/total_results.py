from application import db, api
from application.models.user import User
from application.models.total_results import TotalResults
from application.schemata.total_results import TotalResultsSchema
from flask import Blueprint, request, Response, make_response, render_template, redirect, url_for, session
from flask_restful import Resource
import datetime

total_bp = Blueprint("total", __name__, url_prefix='/')
total_schema = TotalResultsSchema()
api = api(total_bp)
headers = {'Content-Type': 'application/json'}


class TotalResult(Resource):

    def get(self):

        if 'google_id' not in session:
            return redirect(url_for('google_api.authorize'))
        else:
            google_id = session['google_id']

        result = TotalResults.query.filter(TotalResults.google_id == google_id).all()
        return make_response(render_template('homepage/record.html', user_name=google_id, hello=result))

    def post(self, id=None):

        data = request.json
        
        if 'google_id' not in session:
            return redirect(url_for('google_api.authorize'))
        else:
            google_id = session['google_id']

        exercise_result = TotalResults(google_id=google_id, time=datetime.datetime.now(), count=data.get('count'), kind=data.get('kind'))
        db.session.add(exercise_result)
        db.session.commit()

        return "register complete!"


api.add_resource(TotalResult, '/record')
