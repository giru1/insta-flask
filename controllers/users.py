def get_posts_by_user(user_name, posts):
    """
    Показываем все посты выбранного пользователя
    """
    post_user = []
    for post in posts:
        if post.get('poster_name') == user_name:
            post_user.append(post)
    return post_user
