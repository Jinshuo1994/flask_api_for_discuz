
import datetime
from decorators import *
from flask_restful import reqparse
from flask.ext.restful import Resource
from common.util import generate_password

from models.models_member_forum import PreUcenterMember

parser = reqparse.RequestParser()

class Login(Resource):
    def post(self):
        parser.add_argument('username', required=True, help='must input your username')
        parser.add_argument('password', required = True, help = 'must input your password')
        args = parser.parse_args()
        username = args.get('username')
        original_password = args.get('password')

        user = PreUcenterMember.query.filter(PreUcenterMember.username == username).first()

        if not user:
            return {'message' : 'cannot find the user, please register first!'}

        #encrypt method: md5(md5(password) + salt)
        salt = user.salt;

        password = generate_password(original_password, salt)

        if user.password == password:
            token = jwt.encode(
                {'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                app.config['SECRET_KEY'])


            return {'token': token.decode('UTF-8')}

        return 'username or password wrong!', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'}

