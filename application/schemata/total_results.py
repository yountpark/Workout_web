from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from application.models.total_results import *


class TotalResultsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TotalResults
