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
from server.auth import load_user_from_id
from server.auth import load_user_from_state


app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.session_protection = 'strong'


FOODS = [
    {
        'owner': 'Lekha',
        'image_url': 'https://www.simplyrecipes.com/wp-content/uploads/2014/08/banana-bread-vertical-c-1200.jpg',
        'selected': False,
    },
    {
        'owner': 'Mike K',
        'image_url': 'https://images-gmi-pmc.edge-generalmills.com/c23f59e1-1a55-4ba7-91de-71ca24e197fe.jpg',
        'selected': False,
    },
    {
        'owner': 'Danielle',
        'image_url': 'https://www.landolakes.com/RecipeManagementSystem/media/Recipe-Media-Files/Recipes/Retail/x17/20643-walnut-banana-bread-600x600.jpg?ext=.jpg',
        'selected': False,
    },
]

SUPERLATIVES = ['prettier', 'tastier', 'better textured']


@login_manager.user_loader
def load_user(user_id):
    return load_user_from_id(user_id)


@app.route('/')
@login_required
def index():
    return 'Hello World'

@app.route('/login')
def login():
    if current_user.is_authenticated:
        request.args.get('next')
        return redirect(next or '/')

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
        user = load_user_from_state(session['oauth_state'], request.url)
        login_user(user)
        return(redirect('/'))
    return 'Could not fetch your information.'

@app.route('/api/selected_role', methods=['POST'])
def api_selected_role():
    role = json.loads(request.data)['role']
    return ''

@app.route('/api/foods')
def api_foods():
    return jsonify(FOODS)

@app.route('/api/selected_food', methods=['POST'])
def api_selected_food():
    foods = json.loads(request.data)['foods']
    return ''

@app.route('/api/vote')
def api_vote():
    food1, food2 = random.sample(FOODS, 2)
    vote =  {
        'superlative': random.choice(SUPERLATIVES),
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
