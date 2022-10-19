from http import HTTPStatus

from flask_smorest import Blueprint, abort

from models import Category
from schema import PlainCategorySchema

category_blueprint = Blueprint(
    "categories", __name__, description="Operation on Category"
)


@category_blueprint.route("/categories", methods=["GET"])
@category_blueprint.response(200, PlainCategorySchema(many=True))
def get_categories():
    status, result = Category().get_all()
    if not (status == HTTPStatus.OK):
        abort(status, result)
    return result


@category_blueprint.route("/categories/<int:category_id>", methods=["GET"])
@category_blueprint.response(200, PlainCategorySchema)
def get_category_by_id(category_id: int):
    status, result = Category.get_by_id(category_id)
    if not (status == HTTPStatus.OK):
        abort(status, result)
    return result


@category_blueprint.route("/categories", methods=["POST"])
@category_blueprint.arguments(PlainCategorySchema)
@category_blueprint.response(201, PlainCategorySchema)
def create_category(payload):
    status, result = Category().create(payload)
    if not (status == HTTPStatus.OK):
        abort(status, result)

    return result


@category_blueprint.route("/categories/<int:category_id>", methods=["PUT"])
@category_blueprint.arguments(PlainCategorySchema)
@category_blueprint.response(202, PlainCategorySchema)
def update_category(payload, category_id: int):
    status, result = Category().update(payload, category_id)
    if not (status == HTTPStatus.OK):
        abort(status, result)

    return result
