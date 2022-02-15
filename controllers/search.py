from config import POSTS_FILE
from utils import read_json

posts = read_json(POSTS_FILE)


def search_for_posts(tag_name):
    """
    Поиск постов по ключевому слову
    """
    select_posts = []
    for post in posts:
        if tag_name in post['content']:
            select_posts.append(post)
    return select_posts
