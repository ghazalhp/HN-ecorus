#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from flask_restful import Resource, Api

from config import Config
from utils import get_top_stories, get_story_comment, first_comments

app = Flask(__name__)
api = Api(app)



class TopComments(Resource):
    def get(self):
        print("here")
        top_stories = get_top_stories()
        all_story_comments = []
        for story_id in top_stories:
            all_story_comments.extend(get_story_comment(story_id=story_id))
        return json.dumps(first_comments(Config.TOP_COMMENTS_NUMBER, all_story_comments))

api.add_resource(TopComments, '/comments')

if __name__ == '__main__':
    app.run(debug=True)