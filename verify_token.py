import firebase_admin
from firebase_admin import auth
from firebase_admin.auth import InvalidIdTokenError

from models import UserModel

firebase_admin.initialize_app()

def retrieve_user(req):
    token = req.headers.get('Authorization')
    print(token, 'token got from header')
    if token is None:
        return None
    token = token.replace('Bearer ', '')
    try:
        decoded_token = auth.verify_id_token(token)
        print(decoded_token, 'decoded token')
        user = UserModel(decoded_token['uid'], decoded_token['email'], decoded_token['picture'], decoded_token['name'])
        return user
    except Exception as err:
        print(err)
        return None