"""
just for testing the api
"""
from flask_restful import Resource


class Message(Resource):
    """
    Operation for message
    """

    def get(self, message: str):
        """
        get what u say:D
        """
        return {"message": message}
