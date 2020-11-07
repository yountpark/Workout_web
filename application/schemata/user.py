from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from application.models.user import *


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
