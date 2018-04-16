import time
from decorators import *
from flask_restful import reqparse
from flask.ext.restful import Resource
from common.util import generate_password
import random
from validate_email import validate_email

from exts import db
from models.models_member_forum import PreCommonMember, PreUcenterMember

parser = reqparse.RequestParser()

class Register(Resource):
    def post(self):
        parser.add_argument('username', required=True, help='username cannot be empty')
        parser.add_argument('password', required=True, help='password cannot be empty')
        parser.add_argument('email', required=True, help='password cannot be empty')
        args = parser.parse_args()
        username = args.get('username')
        orginal_password = args.get('password')
        email = args.get('email')
        regip = request.remote_addr
        regdate = int(time.time())

        user = PreUcenterMember.query.filter(PreUcenterMember.username == username).first()



        if user:
            return {'message': 'username has already been registered, try another one'}

        if len(orginal_password) < 6:
            return {'message': 'password must be no less than 6 characters'}

        if not validate_email(email):
            return {'message': 'email format is invalid'}

        # generate 6 digit Hexadecimal number as salt
        salt = ''
        for _ in range(1, 7):
            salt = salt + format(random.randint(0, 15), 'x')

        password = generate_password(orginal_password, salt)
        new_user = PreUcenterMember(username=username, password=password, email=email, regip=regip, regdate=regdate, salt=salt)
        db.session.add(new_user)

        #although pre_common_member is not used to login, this schema need to be updated. Otherwise, an account activation is prompted
        #when loging in the webiste using browser.
        new_user_common = PreCommonMember(username=username, password=password, email=email, regdate=regdate)
        db.session.add(new_user_common)
        db.session.commit()

        return {'message' : '%s is registered successfully. You can use it to sign up now.' % username}