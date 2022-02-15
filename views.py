from app import app
import controllers.functions as


SETTINGS_FILE = 'static/settings.json'
CANDIDATE_FILE = 'static/candidates.json'


menu = {'Главная': '/',
        'Список': '/list',
        'Поиск': '/search',
        'Скилы': '/skill'}


@app.route('/')
def index_url():
    return functions.settings_json(SETTINGS_FILE, menu)


# @app.route('/', methods=["POST", "GET"])
# def index_url():
#     return functions.candidate_info(CANDIDATE_FILE)


# @app.route('/list')
# def list_candidates():
#     return functions.list_url(menu, CANDIDATE_FILE)
#
#
# @app.route('/search/')
# def search():
#     return functions.search_url(menu, CANDIDATE_FILE)
#
#
#
# @app.route('/skill')
# def skill():
#     return functions.skill_url(menu, CANDIDATE_FILE)

