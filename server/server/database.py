import pymysql

from server.auth import DB_AUTH 

def connection():
    return pymysql.connect(**DB_AUTH)


def fetch_foods():
    conn = connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    query = '''
        SELECT food.id, baker.name as owner, food.image_url
          FROM cafe.foods food
     LEFT JOIN cafe.bakers baker
            ON food.baker_id = baker.id
    '''
    cursor.execute(query)
    foods = list(cursor.fetchall())
    conn.close()
    return foods
