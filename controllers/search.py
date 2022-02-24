from config import POSTS_FILE
from utils import read_json


def search_for_posts(tag_name):
    """
    Поиск постов по ключевому слову
    """

    posts = read_json(POSTS_FILE)
    select_posts = []
    for post in posts:
        if tag_name in post['content']:
            select_posts.append(post)
    return select_posts
