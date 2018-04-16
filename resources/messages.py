import datetime
from decorators import *
from flask.ext.restful import Resource
import functools
import itertools

from exts import db

from models.models_member_forum import PreUcenterMember
from models.models_pm_dynamic import create_pre_ucenter_pm_message
from models.models_pm import PreUcenterPmMember, PreUcenterPmIndex


class MessageList(Resource):
    @token_required
    def get(self, *args, **kwargs):
        current_user = kwargs['current_user']
        plid_list = PreUcenterPmMember.query.filter(PreUcenterPmMember.uid == current_user.uid).all()

        output = []
        def get_message_list(pmid_record, table_id):
            PreUcenterPmMessages = create_pre_ucenter_pm_message(table_id % 10)
            message = db.session.query(PreUcenterPmMessages).filter_by(pmid=pmid_record.pmid).first()
            time_str = datetime.datetime.fromtimestamp(int(message.dateline)).isoformat()
            username = PreUcenterMember.query.filter(PreUcenterMember.uid == message.authorid).first().username
            message_data = {'uid' : message.authorid, 'username' : username,
                            'content' : message.message, 'dataline' : time_str}
            output.append(message_data)

        def get_pmid_list(plid_record):
            pmid_list = PreUcenterPmIndex.query.filter(PreUcenterPmIndex.plid == plid_record.plid).all()
            table_id = plid_record.plid
            map(functools.partial(get_message_list, table_id=table_id), pmid_list)
            map(get_message_list, pmid_list, itertools.repeat(table_id, len(pmid_list)))

        map(get_pmid_list, plid_list)

        return {"messages for %s" % current_user.username : output}