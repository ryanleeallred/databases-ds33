# Step 0 - import sqlite3
import sqlite3
import queries as q
import pandas as pd

# DB Connection
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# make a cursor and execute the query
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    results = curs.fetchall()
    return results

# only run the lines inside the if statement
# if we are running the file as a script
if __name__ == '__main__':
    conn = connect_to_db()
    results = execute_q(conn, q.name_and_hp)
    df = pd.DataFrame(results, columns=['character_name', 'hit_points'])
    df.to_csv('characters.csv', index=False)
    print(df.head())