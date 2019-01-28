import pymysql

from server.auth import DB_AUTH 

def connection():
    return pymysql.connect(**DB_AUTH)


def fetch_foods():
    conn = connection()
    cursor = conn.cursor()
    query = '''
        SELECT food.id, baker.name, food.image_url
          FROM cafe.foods food
     LEFT JOIN cafe.bakers baker
            ON food.baker_id = baker.id
    '''
    cursor.execute(query)
    foods = []
    columns = ['id', 'owner', 'image_url']
    for row in cursor:
        foods.append(dict(zip(columns, row)))
    conn.close()
    print(foods)
    return foods
