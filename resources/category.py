# from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from databases.db import db
from models import Category
from schema import CategorySchema, PlainCategorySchema

category_blueprint = Blueprint(
    "categories", __name__, description="Operation on Category"
)


@category_blueprint.route("/categories")
class CategoryController(MethodView):
    def get(self):
        pass

    @category_blueprint.arguments(PlainCategorySchema)
    @category_blueprint.response(201, PlainCategorySchema)
    def post(self, payload):
        category = Category(**payload)

        try:
            db.session.add(category)
            db.session.commit()
        except Exception as e:
            abort(500, message=str(e))


@category_blueprint.route("/categories/<int:category_id>")
@category_blueprint.response(200, CategorySchema)
class GetCategory(MethodView):
    def get(self, category_id):
        pass
