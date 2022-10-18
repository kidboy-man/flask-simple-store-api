from marshmallow import Schema, fields


class PlainProductSchema(Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True, load_only=True)
    name = fields.String(required=True)
    image_url = fields.String(required=True)
    description = fields.String(required=True)
    sort = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class PlainCategorySchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    image_url = fields.String(required=True)
    sort = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ProductSchema(PlainProductSchema):
    category = fields.Nested(PlainCategorySchema(), dump_only=True)


class CategorySchema(PlainCategorySchema):
    products = fields.List(fields.Nested(PlainProductSchema()), dump_only=True)
