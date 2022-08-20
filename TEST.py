import flask
from flask import request, render_template
import psycopg2
import json

conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")

cur = conn.cursor()

postgres_delete_query_John = "DELETE FROM actor WHERE first_name='John' AND last_name='Philippi';"
postgres_delete_query_Manuel = "DELETE FROM actor WHERE first_name='Manuel' AND last_name='Eljuri';"
postgres_insert_query_John = "INSERT INTO actor (first_name, last_name) VALUES ('John', 'Philippi');"
postgres_insert_query_Manuel = "INSERT INTO actor (first_name, last_name) VALUES ('Manuel', 'Eljuri');"
postgres_select_query_actors = "SELECT * FROM actor WHERE actor_id > 200;"

cur.execute(postgres_insert_query_John)
conn.commit()
cur.execute(postgres_insert_query_Manuel)
conn.commit()
cur.execute(postgres_select_query_actors)
query_results = cur.fetchall()
print(query_results)

cur.execute(postgres_delete_query_John)
conn.commit()
cur.execute(postgres_select_query_actors)
query_results = cur.fetchall()
print(query_results)

cur.execute(postgres_delete_query_Manuel)
conn.commit()
cur.execute(postgres_select_query_actors)
query_results = cur.fetchall()
print(query_results)

cur.execute("""ALTER SEQUENCE actor_actor_id_seq RESTART WITH 201;""")
conn.commit()
cur.execute("""INSERT INTO actor (first_name, last_name) VALUES ('Philip', 'Savov');""")
conn.commit()
cur.execute(postgres_select_query_actors)
query_results = cur.fetchall()
print(query_results)

cur.execute("""DELETE FROM actor WHERE first_name='Philip' AND last_name='Savov';""")
conn.commit()
cur.execute("""ALTER SEQUENCE actor_actor_id_seq RESTART WITH 201;""")
conn.commit()

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()