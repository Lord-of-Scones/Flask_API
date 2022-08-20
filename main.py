import flask
from flask import request, render_template
import psycopg2

firstname = ""
lastname = ""

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/postgres/json', methods=['GET'])
@app.route('/api/postgres/actor', methods=['GET'])
@app.route('/api/postgres/actor/filterup', methods=['GET'])
@app.route('/api/postgres/actor/filterdown', methods=['GET'])
@app.route('/api/postgres/insert_actor', methods=['GET'])
@app.route('/api/postgres/delete_actor', methods=['GET'])
def actor():

    #Displays information about actors on paths provided below
    if request.path == '/api/postgres/actor':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM actor WHERE actor_id=%s ORDER BY actor_id asc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:
                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("first_name") :
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            firstname = request.args.get("first_name")

            cur.execute("SELECT * FROM actor WHERE first_name=%s ORDER BY actor_id asc;", (firstname,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:
                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("last_name"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            lastname = request.args.get("last_name")

            cur.execute("SELECT * FROM actor WHERE last_name=%s ORDER BY actor_id asc;", (lastname,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:
                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()
        else:
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            cur.execute("SELECT * FROM actor ORDER BY actor_id asc;")
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:

                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

    #Used to display all data above or below a given ID value
    if request.path == '/api/postgres/actor/filterup':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM actor WHERE actor_id >= %s ORDER BY actor_id asc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:
                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

    if request.path == '/api/postgres/actor/filterdown':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM actor WHERE actor_id <= %s ORDER BY actor_id desc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th>Id Number</th><th>First Name</th><th>Last Name</th><th>Last Updated</th></thead><body>"
            for value in query_results:
                html_table += f"<tr><td>{value[0]}</td><td>{value[1]}</td><td>{value[2]}</td><td>{value[3]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

    #Inserts an actor from parameters being passed in by the user
    if request.path == '/api/postgres/insert_actor':
        if request.args.get("first_name") and request.args.get("last_name"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            firstname = request.args.get("first_name")
            lastname = request.args.get("last_name")

            cur.execute("INSERT INTO actor (first_name, last_name) VALUES (%s, %s);", (firstname, lastname))
            conn.commit()

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

            return "INSERT SUCCESS"

        else:
            return "This api expects first_name and last_name values to be present"

    # Deletes an actor from parameters being passed in by the user
    if request.path == '/api/postgres/delete_actor':
        if request.args.get("first_name") and request.args.get("last_name"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            firstname = request.args.get("first_name")
            lastname = request.args.get("last_name")

            cur.execute("DELETE FROM actor WHERE first_name=%s AND last_name=%s;", (firstname, lastname))
            conn.commit()

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

            return "DELETE SUCCESS"

        else:
            return "This api expects first_name and last_name values to be present"




@app.route('/api/postgres/address', methods=['GET'])
@app.route('/api/postgres/address/filterup', methods=['GET'])
@app.route('/api/postgres/address/filterdown', methods=['GET'])
@app.route('/api/postgres/insert_address', methods=['GET'])
@app.route('/api/postgres/delete_address', methods=['GET'])

def address():
    if request.path == '/api/postgres/address':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM address WHERE address_id=%s ORDER BY address_id asc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("address"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            address = request.args.get("address")

            cur.execute("SELECT * FROM address WHERE address=%s ORDER BY address_id asc;", (address,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("address2"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            address2 = request.args.get("address2")

            cur.execute("SELECT * FROM address WHERE address2=%s ORDER BY address_id asc;", (address2,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("district"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            district = request.args.get("district")

            cur.execute("SELECT * FROM address WHERE district=%s ORDER BY address_id asc;", (district,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

        elif request.args.get("city_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            city_id = request.args.get("city_id")

            cur.execute("SELECT * FROM address WHERE city_id=%s ORDER BY address_id asc;", (city_id,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()
        elif request.args.get("postal_code"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            postal_code = request.args.get("postal_code")

            cur.execute("SELECT * FROM address WHERE postal_code=%s ORDER BY address_id asc;", (postal_code,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()
        elif request.args.get("phone"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            phone = request.args.get("phone")

            cur.execute("SELECT * FROM address WHERE phone=%s ORDER BY address_id asc;", (phone,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()
        else:
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            cur.execute("SELECT * FROM address ORDER BY address_id asc;")
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

    # Used to display all data above or below a given ID value
    if request.path == '/api/postgres/address/filterup':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres",
                                    password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM address WHERE address_id >= %s ORDER BY address_id asc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

    if request.path == '/api/postgres/address/filterdown':
        if request.args.get("filter_id"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres",
                                    password="mysecretpassword")
            cur = conn.cursor()

            id_value = request.args.get("filter_id")

            cur.execute("SELECT * FROM address WHERE address_id<=%s ORDER BY address_id desc;", (id_value,))
            query_results = cur.fetchall()
            html_table = "<table><thead><th style=padding:10px>Address Id </th><th style=padding:10px>Address</th><th style=padding:10px>Address 2</th><th style=padding:10px>District</th><th style=padding:10px>City Id</th><th style=padding:10px>Postal Code</th><th style=padding:10px>Phone</th><th style=padding:10px>Last Update</thead><body>"
            for value in query_results:
                html_table += f"<tr><td style=padding:10px>{value[0]}</td><td style=padding:10px>{value[1]}</td><td style=padding:10px>{value[2]}</td><td style=padding:10px>{value[3]}</td><td style=padding:10px>{value[4]}</td><td style=padding:10px>{value[5]}</td><td style=padding:10px>{value[6]}</td><td style=padding:10px>{value[7]}</td></tr>"
            html_table += "</tbody><table>"
            return html_table

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()

    #Inserts an actor from parameters being passed in by the user
    if request.path == '/api/postgres/insert_address':
        if request.args.get("address") and request.args.get("address2") and request.args.get("district") and request.args.get("city_id") and request.args.get("postal_code") and request.args.get("phone"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            address = request.args.get("address")
            address2 = request.args.get("address2")
            district = request.args.get("district")
            city_id = request.args.get("city_id")
            postal_code = request.args.get("postal_code")
            phone = request.args.get("phone")


            cur.execute("INSERT INTO address (address, address2, district, city_id, postal_code, phone) VALUES (%s, %s, %s, %s, %s, %s);", (address, address2, district, city_id, postal_code, phone))
            conn.commit()

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

            return "INSERT SUCCESS"

        else:
            return "This api expects first_name and last_name values to be present"

    # Deletes an actor from parameters being passed in by the user
    if request.path == '/api/postgres/delete_address':
        if request.args.get("address") and request.args.get("address2") and request.args.get("district") and request.args.get("city_id") and request.args.get("postal_code") and request.args.get("phone"):
            conn = psycopg2.connect(host="localhost", port=5432, database="dvdrental", user="postgres", password="mysecretpassword")
            cur = conn.cursor()

            address = request.args.get("address")
            address2 = request.args.get("address2")
            district = request.args.get("district")
            city_id = request.args.get("city_id")
            postal_code = request.args.get("postal_code")
            phone = request.args.get("phone")

            cur.execute("DELETE FROM address WHERE address=%s AND address2=%s AND district=%s AND city_id=%s AND postal_code=%s AND phone=%s;", (address, address2, district, city_id, postal_code, phone))
            conn.commit()

            # Close the cursor and connection to so the server can allocate
            # bandwidth to other requests
            cur.close()
            conn.close()

            return "DELETE SUCCESS"

        else:
            return "This api expects first_name and last_name values to be present"

app.run(port=5001)



