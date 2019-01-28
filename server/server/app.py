"""Back-end server."""
import json
import random

from flask import Flask
from flask import jsonify
from flask import redirect
from flask import request
from flask import session
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import LoginManager

from server.auth import Config
from server.auth import auth_url_and_state
from server.auth import dict_to_user
from server.auth import user_data_from_state
from server.auth import user_data_to_user
from server.database import fetch_foods
from server.database import fetch_selected_foods
from server.database import fetch_superlatives
from server.database import fetch_user
from server.database import fetch_user_by_id
from server.database import set_selected_foods
from server.database import set_user


app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    return dict_to_user(fetch_user_by_id(user_id))


@app.route('/')
@login_required
def index():
    return 'Hello World'

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(request.args.get('next') or '/')

    auth_url, state = auth_url_and_state()
    session['oauth_state'] = state
    return redirect(auth_url)

@app.route('/oauth2callback')
def callback():
    if current_user is not None and current_user.is_authenticated:
        return redirect('/')
    elif 'error' in request.args:
        if request.args.get('error') == 'access denied':
            return 'You denied access.'
        else:
            return 'Error encountered.'
    elif 'code' not in request.args and 'state' not in request.args:
        return(redirect('/login'))
    else:
        user_data = user_data_from_state(session['oauth_state'], request.url)
        user = dict_to_user(fetch_user(user_data['id']))
        if user is None:
            user = user_data_to_user(user_data)
            user.id = set_user(user)
        login_user(user)
        return(redirect('/'))
    return 'Could not fetch your information.'

@app.route('/api/selected_role', methods=['POST'])
def api_selected_role():
    role = json.loads(request.data)['role']
    return ''

@app.route('/api/foods')
@login_required
def api_foods():
    foods = fetch_foods()
    selected_foods = fetch_selected_foods(current_user.id)
    for food in foods:
        if food['id'] in selected_foods:
            food['selected'] = True
        else:
            food['selected'] = False
    return jsonify(foods)

@app.route('/api/selected_food', methods=['POST'])
@login_required
def api_selected_food():
    foods = json.loads(request.data)['foods']
    set_selected_foods(current_user.id, foods)
    return ''

@app.route('/api/vote')
@login_required
def api_vote():
    all_foods = fetch_foods()
    selected = fetch_selected_foods(current_user.id)
    filtered = [food for food in all_foods if food['id'] in selected]
    food1, food2 = random.sample(filtered, 2)
    vote =  {
        'superlative': random.choice(fetch_superlatives()),
        'food1': food1,
        'food2': food2,
    }
    return jsonify(vote)

@app.route('/api/vote_result', methods=['POST'])
def api_vote_result():
    results = json.loads(request.data)
    return ''


if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc')
