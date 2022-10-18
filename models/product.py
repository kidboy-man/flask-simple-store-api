"""
category model
"""

from sqlalchemy.sql import func

from app import db


class Product(db.Model):
    __tablename__ = "product"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    category = db.relationship("Category", back_populates="products")
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    sort = db.Column(db.Integer)
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # TODO: implement soft delete
