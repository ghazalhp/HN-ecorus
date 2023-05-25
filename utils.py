import requests

from config import Config


def get_story_comment(story_id: int):
    URL = Config.HN_URL + str(story_id) + ".json?print=pretty"
    r = requests.get(url=URL)
    data = r.json()
    comments = []
    print(data)
    if 'kids' not in data:
        return []
    for kid in data['kids']:
        URL = Config.HN_URL + str(kid) + ".json?print=pretty"
        r = requests.get(url=URL)
        item = r.json()
        if item['type'] == "comment":
            comments.append(item)
    return comments


def get_top_stories():
    URL = Config.HN_TOP_STORY_URL
    r = requests.get(url=URL)
    data = r.json()
    print(len(data))
    return data[0:Config.TOP_STORIES_NUMBER]


def first_comments(number, comments):
    print("first_comments")
    comments = sorted(comments, key=lambda k: k.get('time', 0))

    return comments[0:number]
