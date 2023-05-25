#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask
from flask_restful import Resource, Api

from config import Config
from utils import get_top_stories, get_story_comment, first_comments, most_used_words_in_comments

app = Flask(__name__)
api = Api(app)


class TopComments(Resource):
    def get(self):
        top_stories = get_top_stories(Config.TOP_COMMENTS_STORY_NUMBER)
        all_story_comments = []
        for story_id in top_stories:
            all_story_comments.extend(get_story_comment(story_id=story_id,nested=False))
        return json.dumps(first_comments(Config.TOP_COMMENTS_COMMENTS_NUMBER, all_story_comments))


api.add_resource(TopComments, '/comments')


class MostUsedWords(Resource):
    def get(self):
        top_stories = get_top_stories(Config.MOST_USED_WORDS_STORY_NUMBER)
        all_story_comments = []
        for story_id in top_stories:
            all_story_comments.extend(get_story_comment(story_id=story_id,nested=False))
        comments = first_comments(Config.MOST_USED_WORDS_COMMENTS_NUMBER, all_story_comments)
        return json.dumps(most_used_words_in_comments(Config.MOST_USED_WORDS_WORDS_NUMBER, comments))


api.add_resource(MostUsedWords, '/words')


class MostUsedWordsNestedComments(Resource):
    def get(self):
        top_stories = get_top_stories(Config.NESTED_COMMENTS_STORY_NUMBER)
        all_story_comments = []
        for story_id in top_stories:
            all_story_comments.extend(get_story_comment(story_id=story_id,nested=True))
        return json.dumps(most_used_words_in_comments(Config.NESTED_COMMENTS_WORDS_NUMBER, all_story_comments))

api.add_resource(MostUsedWordsNestedComments, '/words/nestedcomments')


if __name__ == '__main__':
    app.run(debug=True)
