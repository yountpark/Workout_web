from application import db, api
from application.models.cumulative_result import CumulativeResult
from application.models.user import User
from application.schemata.cumulative_result import CumulativeResultSchema
from flask import Blueprint, request, Response, make_response, render_template, redirect, session, url_for
from flask_restful import Resource
from sqlalchemy import and_
import datetime

cumulative_bp = Blueprint("cumulative", __name__, url_prefix='/')
cumulative_schema = CumulativeResultSchema()
api = api(cumulative_bp)


class Cumulative(Resource):

    def get(self):

        if 'google_id' not in session:
            return redirect(url_for('google_api.authorize'))
        else:
            user_name = session['user_name']

        result = CumulativeResult.query.all()

        return make_response(render_template('homepage/rank.html', user_name=user_name, hi=cumulative_schema.dumps(result, many=True)))

    def post(self, id=None):
        
        data = request.json
        
        if 'google_id' not in session:
            return redirect(url_for('google_api.authorize'))
        else:
            google_id = session['google_id']
        
        kind = data.get('kind')
        count = data.get('count')

        try:
            old_result = CumulativeResult.query.filter(and_(CumulativeResult.google_id == google_id, CumulativeResult.kind == kind)).one()
            CumulativeResult.query.filter(and_(CumulativeResult.google_id == google_id, CumulativeResult.kind == kind)).\
                update(
                        {
                            CumulativeResult.times : (old_result.get_times() + 1), 
                            CumulativeResult.cumulative_count : (old_result.get_count() + int(count))
                        }
                    )
            db.session.commit()
        except:
            new_result = CumulativeResult(google_id=google_id, times= 1, cumulative_count=(int(count)), kind=kind)

            db.session.add(new_result)
            db.session.commit()

        return "register complete!"


api.add_resource(Cumulative, '/ranking')
