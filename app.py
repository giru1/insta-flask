from flask import Flask
from flask import render_template, request

from config import POSTS_FILE
from controllers.index import comments_post
from controllers.post import get_post_id, comments_user
from controllers.search import search_for_posts
from controllers.users import get_posts_by_user
from utils import read_json

app = Flask(__name__)

posts = read_json(POSTS_FILE)


@app.route('/')
def index():
    """
    Обработка главной страницы
    """
    posts_add_comment = comments_post()  # добавляем изменную структуру для вывода на главной страницы количества комментрариев
    return render_template('index.html', posts=posts_add_comment)


@app.route('/post/<int:id>')
def post(id):
    """
    Обработка страницы поста
    """
    post = get_post_id(id)
    comments = comments_user(id)
    comments_len = len(comments)
    return render_template('post.html', post=post, comments=comments, comments_len=comments_len)


@app.route('/search', methods=["GET", "POST"])
def search():
    """
    Обработка страницы поиска
    """
    word = request.args.get('tag')
    if word is None:
        word = ''
    posts_search = search_for_posts(word)
    posts_len = len(posts_search)
    return render_template('search.html', posts=posts_search, tag_name=word, posts_len=posts_len)


@app.route('/users/<user_name>')
def user(user_name):
    """
    Обработка страницы пользователя
    """
    user_posts = get_posts_by_user(user_name, posts)
    posts_len = len(user_posts)
    return render_template('user-feed.html', user_posts=user_posts, posts_len=posts_len, user_name=user_name)


if __name__ == '__main__':
    app.run()
