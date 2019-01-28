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


class User(object):
    def __init__(
            self, id=None, name=None, email=None, avatar=None, tokens=None):
        self.id = id
        self.name = name
        self.email = email
        self.avatar = avatar
        self.tokens = tokens

        self.is_authenticated = id is not None
        self.is_active = id is not None
        self.is_anonymous = id is None
    
    def get_id(self):
        return self.id


USERS = {
    -1: User(),
}


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

def load_user_from_state(state, url):
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
        email = user_data['email']
        user = load_user_from_email(email)
        if user is None:
            id = user_data['id']
            new_user = User(
                id,
                user_data['name'],
                email,
                user_data['picture'],
                json.dumps(token),
            )
            USERS[id] = new_user
            user = new_user
        return user 

def load_user_from_id(user_id):
    return USERS.get(user_id)

def load_user_from_email(email):
    for user in USERS.values():
        if user.email == email:
            final_user = user
            break
    else:
        final_user = None
    return final_user
