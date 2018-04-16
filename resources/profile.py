from decorators import *
from flask.ext.restful import Resource
from models.models_member_forum import PreCommonMemberProfile


class MemberProfile(Resource):
    @token_required
    def get(self, *args, **kwargs):
        profile = PreCommonMemberProfile.query.filter(PreCommonMemberProfile.uid == kwargs['current_user'].uid).first()
        member_profile = {'realname': profile.realname, 'gender': profile.gender, 'username': kwargs['current_user'].username}
        return  {'profile' : member_profile}