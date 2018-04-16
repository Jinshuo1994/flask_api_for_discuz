import datetime
from decorators import *
from flask.ext.restful import Resource
from models.models_member_forum import PreForumPost

#for demo purpose, only return subject, message, authorid, author, useip, timeline.
#all the data in pre_forum_thread, pre_forum post can be returned
class PostList(Resource):
    @token_required
    def get(self, form_id, *args, **kwargs):
        posts = PreForumPost.query.filter(PreForumPost.fid == form_id).all()
        if not posts:
            return {"message" : "the forum does not exit or posts are empty"}

        output = []

        for post in posts:
            time_str = datetime.datetime.fromtimestamp(int(post.dateline)).isoformat()
            post_data = {'subject': post.subject, 'message': post.message, 'authorid': post.authorid,
                         'author' : post.author, 'useip': post.useip, 'timeline' : time_str}
            output.append(post_data)

        return {"posts" : output}