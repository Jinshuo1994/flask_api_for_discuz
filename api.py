from flask_restful import Api
from exts import db

from decorators import *

from resources.login import Login
from resources.register import Register
from resources.posts import PostList
from resources.profile import MemberProfile
from resources.messages import MessageList
from resources.logout import Logout

api = Api(app)

db.init_app(app)

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(Logout, '/logout')
api.add_resource(PostList, '/forum/<form_id>')
api.add_resource(MemberProfile, '/profile')
api.add_resource(MessageList, '/messages')




if __name__ == '__main__':
    app.run(debug=True)