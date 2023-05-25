import string

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


def get_top_stories(number):
    URL = Config.HN_TOP_STORY_URL
    r = requests.get(url=URL)
    data = r.json()
    print(len(data))
    return data[0:number]


def first_comments(number, comments):
    print("first_comments")
    comments = sorted(comments, key=lambda k: k.get('time', 0))

    return comments[0:number]


def parse_comment_text(text):
    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation))
    text_without_html_tags = text_without_punctuation.replace('<p>', ' ')
    words = []
    for word in text_without_html_tags.split(" "):
        if word.isalpha():
            words.append(word)
    return words


def most_used_words_in_comments(number,comments):
    words_count = {}
    for item in comments:
        words = parse_comment_text(item['text'])
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1
    return sorted(words_count.items(), key=lambda x: x[1], reverse=True)[0:number]