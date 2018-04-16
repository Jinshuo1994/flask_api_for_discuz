from decorators import *
from flask.ext.restful import Resource

class Logout(Resource):
    def post(self):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            try:
                data = jwt.decode(token, app.config['SECRET_KEY'])
                token_blacklist[token] = data['exp']
                return {"message" : "Log out successfully! Your token has expired"}
            except:
                return {'message': 'Token is invalid!'}, 401

        return {"message":"token missing"}