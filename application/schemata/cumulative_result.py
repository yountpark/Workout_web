from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from application.models.cumulative_result import *


class CumulativeResultSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CumulativeResult
