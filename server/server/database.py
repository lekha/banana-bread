import pymysql

from server.auth import DB_AUTH 

def connection():
    return pymysql.connect(**DB_AUTH)


def fetch_user_by_id(id):
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = '''
        SELECT id, user_id, name, email, avatar, tokens
          FROM cafe.users
         WHERE id = %(id)s
    '''
    params = {'id': id}
    cursor.execute(query, params)
    results = cursor.fetchall()
    if results:
        user = results[0]
    else:
        user = None
    conn.close()
    return user

def fetch_user(user_id):
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = '''
        SELECT id, user_id, name, email, avatar, tokens
          FROM cafe.users
         WHERE user_id = %(user_id)s
    '''
    params = {'user_id': user_id}
    cursor.execute(query, params)
    results = cursor.fetchall()
    if results:
        user = results[0]
    else:
        user = None
    conn.close()
    return user

def set_user(user):
    conn = connection()
    cursor = conn.cursor()
    query = '''
        INSERT IGNORE cafe.users (user_id, name, email, avatar, tokens)
               VALUES (%(user_id)s, %(name)s, %(email)s, %(avatar)s, %(tokens)s)
    '''
    cursor.execute(query, user.db_dict())
    conn.commit()
    id = fetch_user(user.user_id)['id']    
    conn.close()
    return id

def fetch_foods():
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = '''
        SELECT food.id, baker.name as baker, baker.id as baker_id,
               food.image_url
          FROM cafe.foods food
     LEFT JOIN cafe.bakers baker
            ON food.baker_id = baker.id
    '''
    cursor.execute(query)
    foods = list(cursor.fetchall())
    conn.close()
    return foods

def fetch_voted_foods(user):
    query_1 = '''
        SELECT food.id
          FROM cafe.votes vote
     LEFT JOIN cafe.foods food
            ON vote.winner_baker_id = food.baker_id
         WHERE vote.user_id = %(user_id)s
    '''
    query_2 = '''
        SELECT food.id
          FROM cafe.votes vote
     LEFT JOIN cafe.foods food
            ON vote.loser_baker_id = food.baker_id
         WHERE vote.user_id = %(user_id)s
    '''
    params = {'user_id': user.id}
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query_1, params)
    voted_foods_1 = {x for (x,) in cursor.fetchall()}
    cursor.execute(query_2, params)
    voted_foods_2 = {x for (x,) in cursor.fetchall()}
    conn.close()
    return voted_foods_1.union(voted_foods_2)

def fetch_selected_foods(user):
    conn = connection()
    cursor = conn.cursor()
    query = '''
        SELECT food_id
          FROM cafe.selected_foods
         WHERE is_selected = 1
           AND user_id = %(user_id)s
    '''
    params = {'user_id': user.id}
    cursor.execute(query, params)
    selected_foods = {x for (x,) in cursor.fetchall()}
    conn.close()
    return selected_foods

def set_selected_foods(user_id, foods):
    conn = connection()
    cursor = conn.cursor()
    query = '''
         INSERT INTO cafe.selected_foods (user_id, food_id, is_selected)
              VALUES (%(user_id)s, %(food_id)s, %(is_selected)s)
    ON DUPLICATE KEY UPDATE is_selected=VALUES(is_selected)
    '''
    def _param(user, food, is_selected):
        return {
            'user_id': user,
            'food_id': food,
            'is_selected': is_selected,
        }
    params = [_param(user_id, food['id'], food['selected']) for food in foods]
    for param in params:
        cursor.execute(query, param)
    conn.commit()
    conn.close()

def fetch_categories():
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = '''
        SELECT id, name, superlative
          FROM cafe.categories
    '''
    cursor.execute(query)
    categories = list(cursor.fetchall())
    conn.close()
    return categories

def fetch_votes(user):
    query = '''
        SELECT category_id, winner_baker_id, loser_baker_id
          FROM cafe.votes
         WHERE user_id = %(user_id)s
    '''
    params = {'user_id': user.id}
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query, params)
    votes = list(cursor.fetchall())
    conn.close()
    return votes

def set_votes(user, category, winner, loser):
    query = '''
        INSERT INTO cafe.votes (user_id, category_id, winner_baker_id,
                    loser_baker_id)
             VALUES (%(user_id)s, %(category_id)s, %(winner_id)s, %(loser_id)s)
    '''
    params = {
        'user_id': user.id,
        'category_id': category['id'],
        'winner_id': winner['baker_id'],
        'loser_id': loser['baker_id'],
    }
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    conn.close()
