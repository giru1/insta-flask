from config import COMMENTS_FILE, POSTS_FILE
from utils import read_json

comments = read_json(COMMENTS_FILE)
posts = read_json(POSTS_FILE)


def comments_post():
    """
    Функция для добавления добавляем изменной структуру
    для вывода на главной страницы количества комментрариев
    """
    for post in posts:
        post['comments'] = 0
        for comment in comments:
            if post['pk'] == comment['post_id']:
                post['comments'] += 1
    return posts

