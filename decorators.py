from flask import request
from functools import wraps
import jwt
from exts import app
from common.blacklist import token_blacklist
from models.models_member_forum import PreUcenterMember

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token in token:
            return {'message' : 'Token is missing!'}, 401, {'WWW-Authenticate': 'Basic realm="Login required!"'}

        if token in token_blacklist.keys():
            return {'message' : 'Token submitted is an expired one!'}

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = PreUcenterMember.query.filter_by(username=data['username']).first()
        except:
            return {'message' : 'Token is invalid! Log in first please!'}, 401
        if current_user:
            print data['username']

        kwargs['current_user'] = current_user
        return f(*args, **kwargs)

    return decorated