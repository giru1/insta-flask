import pprint

from config import COMMENTS_FILE, POSTS_FILE
from utils import read_json

comments = read_json(COMMENTS_FILE)
posts = read_json(POSTS_FILE)


def comments_post():
    """
    Функция для добавления добавляем изменной структуру
    для вывода на главной страницы количества комментрариев
    """
    # for post in posts:
    #     post['comments'] = []
    for comment in comments:
        counter = 0
        for post in posts:
            post['comments'] = 0

            if post['pk'] == comment['post_id']:
                # print(post['pk'], comment['post_id'])
                # print(post['comments'])
                # print(comment['comment'])
                counter += 1
                # print(len(post['comments']))
            post['comments'] = counter
            print(counter)
    return posts

