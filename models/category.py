"""
category model
"""

from sqlalchemy.sql import func

from app import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    sort = db.Column(db.Integer)
    products = db.relationship("Product", back_populates="category", lazy="dynamic")
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # TODO: implement soft delete
