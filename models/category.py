"""
category model
"""
from __future__ import annotations

from http import HTTPStatus
from typing import List, Tuple

from sqlalchemy.exc import NoResultFound
from sqlalchemy.sql import func

from app import db


class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255))
    sort = db.Column(db.Integer)
    products = db.relationship(
        "Product", back_populates="category", lazy="dynamic"
    )  # noqa
    created_at = db.Column(
        db.DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    # TODO: implement soft delete

    @classmethod
    def create(cls, payload) -> Tuple[int, Category]:
        new_category = Category(**payload)
        try:
            db.session.add(new_category)
            db.session.commit()
        except Exception as e:
            return HTTPStatus.INTERNAL_SERVER_ERROR, str(e)
        finally:
            db.session.close()

        return HTTPStatus.OK, payload

    @classmethod
    def update(cls, payload, category_id) -> Tuple[int, Category]:
        category = None
        try:
            category = (
                db.session.query(Category).filter_by(id=category_id).one()
            )  # noqa
        except NoResultFound as e:
            return HTTPStatus.NOT_FOUND, str(e)

        try:
            category.name = payload["name"] or category.name
            category.image_url = payload["image_url"] or category.image_url
            category.sort = payload["sort"] or category.sort
            db.session.commit()
        except Exception as e:
            return HTTPStatus.INTERNAL_SERVER_ERROR, str(e)
        finally:
            db.session.close()

        return HTTPStatus.OK, category

    @classmethod
    def get_by_id(cls, category_id) -> Tuple[int, Category]:
        category = None
        try:
            category = (
                db.session.query(Category).filter_by(id=category_id).one()
            )  # noqa
        except NoResultFound as e:
            return HTTPStatus.NOT_FOUND, str(e)
        except Exception as e:
            return HTTPStatus.INTERNAL_SERVER_ERROR, str(e)
        finally:
            db.session.close()

        return HTTPStatus.OK, category

    @classmethod
    def get_all(cls) -> Tuple[int, List[Category]]:
        categories = None
        try:
            categories = db.session.query(Category).all()
        except Exception as e:
            return HTTPStatus.INTERNAL_SERVER_ERROR, str(e)
        finally:
            db.session.close()

        return HTTPStatus.OK, categories
