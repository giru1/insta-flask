from config import POSTS_FILE, COMMENTS_FILE
from utils import read_json

posts = read_json(POSTS_FILE)
def get_post_id(id):
    """
    Показываем пост на основании выбранного id
    """


    for post in posts:
        if post['pk'] == int(id):
            return post
    return None




def comments_user(id):
    """
    Показываем комментарии к посты на основании выбранного id
    """
    all_comments = read_json(COMMENTS_FILE)
    comments = [comment for comment in all_comments if comment['post_id'] == int(id)]
    return comments
