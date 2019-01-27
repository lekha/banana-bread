"""Back-end server."""
import json
import random

from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)


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


@app.route('/')
def index():
    return 'Hello World'

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
    app.run(debug=True)
