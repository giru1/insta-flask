from config import POSTS_FILE
from utils import read_json

posts = read_json(POSTS_FILE)


def get_tag():
    """
    Обработка страницы поиск по тегу
    :return:
    """
    tag_name = ''
    select_posts = []

    for post in posts:
        if '#' + tag_name in post.get('content'):
            select_posts.append(post)

    return select_posts
