from flask import request
from flask_jwt_extended import decode_token

from app.exceptions.generic_exc import NotFoundError
from app.models import UserModel


def get_user_from_token():
    token = request.headers.get("Authorization").split()[-1]
    decoded_jwt = decode_token(token)
    user_id = decoded_jwt.get("sub")
    user: UserModel = UserModel.query.get(user_id)

    if not user:
        raise NotFoundError(request = "user")

    return user
