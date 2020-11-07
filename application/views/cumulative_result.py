from application import db, api
from application.models.cumulative_result import CumulativeResult
from application.models.user import User
from application.schemata.cumulative_result import CumulativeResultSchema
from flask import Blueprint, request, Response, make_response, render_template, redirect
from flask_restful import Resource
import datetime

cumulative_bp = Blueprint("cumulative", __name__, url_prefix='/cumulative-result')
cumulative_schema = CumulativeResultSchema()
session = db.session
api = api(cumulative_bp)
headers = {'Content-Type': 'application/json'}


class Cumulative(Resource):

    def get(self, id):
        user = User.query.filter(User.google_id == id).all()

        if not user:
            return redirect('/authorize')

        # record = CumulativeResult.query.filter(CumulativeResult.google_id == id).all()
        record = CumulativeResult.query.all()

        # return cumulative_schema.dumps(record, many=True)
        return render_template('homepage/rank.html', placeholder=record)

    def post(self, id=None):
        data = request.json
        print("cumul  "+ str(data))
        google_id = data.get('google_id')
        kind = data.get('kind')
        count = data.get('count')

        # old_result = CumulativeResult.query.filter(CumulativeResult.google_id == google_id and CumulativeResult.kind == kind).one()

        # CumulativeResult.query.filter(CumulativeResult.google_id == google_id and CumulativeResult.kind == kind).delete()
        # session.commit()

        # new_result = CumulativeResult(google_id=google_id, times=(old_result.get_times() + 1), cumulative_count=(old_result.get_count() + int(count)), kind=kind)

        # session.add(new_result)
        # session.commit()

        return "register complete!"


api.add_resource(Cumulative, '/')


# class AllUsers(Resource):
#     def get(self):
#         user = User.query.get(request.args.get('id'))
#         if not user.admin:
#             return Response("No Authority", 401, mimetype='application/json')
#         result = User.query.all()
#         return make_response(render_template('user/multiple_user_result.html', title="전체 사용자 정보", result=result, id=str(user.id), user=user), 200, headers)
#         # return Response(user_schema.dumps(result, many=True), 200, mimetype='application/json')
#
#     def post(self):
#         data = request.form.to_dict()
#         user = register.run(data)
#
#         return make_response(render_template('user/specific_user_result.html', title="생성된 사용자", result=user, request_user=user, id=str(user.id)), 201, headers)
#
#
# class SpecificUser(Resource):
#     def get(self, id):
#         data = request.args
#
#         target_user = User.query.get(id)
#         request_user = User.query.get(data.get('id'))
#
#         if not request_user.admin and data.get('id') != id:
#             return Response(user_schema.dumps(request_user), 401, mimetype='application/json')
#         if not target_user:
#             return Response(user_schema.dumps(target_user), 400, mimetype='application/json')
#
#         if id == data.get('id'):
#             return make_response(render_template('user/specific_user_result.html', title='사용자 정보', result=target_user, request_user=request_user, id=str(request_user.id)), 200, headers)
#         else:
#             target_id = data.get('사용자 번호')
#             result = [target_user]
#             return make_response(render_template('user/select_specific_user.html', title='사용자 정보', result=result, target_id=str(target_id), id=str(request_user.id)), 200, headers)
#
#     def put(self, id):
#         data = request.form
#         target_user = User.query.get(id)
#         request_user = User.query.get(data['id'])
#
#         if request_user.admin: # 사용자가 관리자일 경우
#             if target_user.admin and request_user.id != target_user.id: # 수정하려고 하는 대상이 관리자이고 자기 자신이 아닌 경우
#                 return Response(user_schema.dumps(target_user), 400, mimetype='application/json')
#             else: # 수정하려고 하는 대상이 일반 사용자이거나, 자기 자신일 경우
#                 if data.get('google_id'):
#                     target_user.google_id = data['google_id']
#                 if data.get('ko_name'):
#                     target_user.ko_name = data['ko_name']
#                 if data.get('en_name'):
#                     target_user.en_name = data['en_name']
#                 if data.get('entry_date'):
#                     target_user.entry_date = datetime.datetime.strptime(data['entry_date'], '%Y-%m-%d %H:%M:%S')
#                 if data.get('admin'):
#                     target_user.admin = data['admin']
#
#         else: # 사용자가 일반 사용자일 경우
#             if id != data['id']: # 수정하려고 하는 대상이 자기 자신이 아닌 경우
#                 return Response("No Authority", 400, mimetype='application/json')
#             elif id == data['id']: # 수정하교 하는 대상이 자기 자신일 경우
#                 if data.get('google_id'):
#                     target_user.google_id = data['google_id']
#                 if data.get('en_name'):
#                     target_user.en_name = data['en_name']
#                 if data.get('ko_name'):
#                     target_user.ko_name = data['ko_name']
#                 if data.get('entry_date'):
#                     target_user.entry_date = datetime.datetime.strptime(data['entry_date'], '%Y-%m-%d %H:%M:%S')
#                 if data.get('admin'): # 일반 사용자는 admin 수정 불가
#                     return Response("No Authority", 401, mimetype='application/json')
#
#         session.commit()
#         return Response(user_schema.dumps(target_user), 200, mimetype='application/json')
#
#     def delete(self, id):
#
#         request_user = User.query.get(request.form['id'])
#
#         if not request_user.admin:
#             return Response(user_schema.dumps(request_user), 401, mimetype='application/json')
#
#         target_user = User.query.get(id)
#         if not target_user or target_user.admin:  # 삭제하려는 대상이 존재하지 않는 경우
#             return Response(user_schema.dumps(target_user), 400, mimetype='application/json')
#
#         db.session.delete(target_user)
#         db.session.commit()
#         return Response(user_schema.dumps(request_user), 200, mimetype='application/json')
#
#     def post(self, id=None):
#         data = request.form
#         user = User.query.all()
#         target_id = "temp" if not data.get('사용자 번호') else data.get('사용자 번호')
#
#         return make_response(render_template('user/select_specific_user.html', title="회원 선택", result=user, id=str(data.get('id')), target_id=target_id), 200, headers)
#
# api.add_resource(AllUsers, '/')
# api.add_resource(SpecificUser, '/<string:id>')