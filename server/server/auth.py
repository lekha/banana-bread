import json
import os

from requests_oauthlib import OAuth2Session


class Auth(object):
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    REDIRECT_URI = (
        os.environ.get('REDIRECT_URI') or
        'http://localhost:8080/oauth2callback'
    )
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')


DB_AUTH = {
    'host': os.environ.get('DB_HOST'),
    'user': os.environ.get('DB_USER'),
    'passwd': os.environ.get('DB_PASSWORD'),
    'db': 'cafe'
}


class User(object):
    def __init__(
            self, id=None, name=None, email=None, avatar=None, tokens=None):
        self.id = None
        self.user_id = id
        self.name = name
        self.email = email
        self.avatar = avatar
        self.tokens = tokens

        self.is_authenticated = id is not None
        self.is_active = id is not None
        self.is_anonymous = id is None
    
    def get_id(self):
        return self.id

    def db_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'avatar': self.avatar,
            'tokens': self.tokens,
        }


def dict_to_user(user_dict):
    if user_dict is None:
        return

    copied_dict = user_dict.copy()
    del copied_dict['user_id']
    copied_dict['id'] = user_dict['user_id']
    user = User(**copied_dict)
    user.id = user_dict['id']
    return user


def google_auth(state=None, token=None):
    if token:
        session = OAuth2Session(Auth.CLIENT_ID, token=token)
    elif state:
        session = OAuth2Session(
            Auth.CLIENT_ID,
            state=state,
            redirect_uri=Auth.REDIRECT_URI,
        )
    else:
        session = OAuth2Session(
            Auth.CLIENT_ID,
            redirect_uri=Auth.REDIRECT_URI,
            scope=Auth.SCOPE,
        )
    return session

def auth_url_and_state():
    auth = google_auth()
    auth_url, state = auth.authorization_url(
        Auth.AUTH_URI, access_type='offline')
    return auth_url, state

def user_data_from_state(state, url):
    auth_with_state = google_auth(state=state)
    token = auth_with_state.fetch_token(
        Auth.TOKEN_URI,
        client_secret=Auth.CLIENT_SECRET,
        authorization_response=url,
    )
    auth_with_token = google_auth(token=token)
    response = auth_with_token.get(Auth.USER_INFO)
    if response.status_code == 200:
        user_data = response.json()
        user_data['token'] = token
        return user_data

def user_data_to_user(user_data):
    user = User(
        user_data['id'],
        user_data['name'],
        user_data['email'],
        user_data['picture'],
        json.dumps(user_data['token']),
    )
    return user

def load_user_from_email(email):
    for user in USERS.values():
        if user.email == email:
            final_user = user
            break
    else:
        final_user = None
    return final_user
