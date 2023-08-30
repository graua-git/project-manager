# General functions to perform CRUD operations on the database

from flask import jsonify
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='project_manager'
)
cursor = db.cursor(dictionary=True)

# ----------------------------------- CRUD -----------------------------------
def create(entry: dict, table: str) -> dict:
    """
    INSERT INTO Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    returns: response message from MySQL
    """
    try:
        entry_dict = parse_json(entry)
        sql = f"INSERT INTO {table} " + entry_dict['keys_str'] + " VALUES " + entry_dict['vals_str']
        cursor.execute(sql, entry_dict['vals_li'])
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def read(query_title: str, quantity: str = 'all') -> list:
    """
    SELECT Query
    query_title: Comment labeling the query in dml.sql
    returns: list of lists representing table
    quantity: "one" or "all"
    """
    query = get_query(query_title)
    try:
        # Query Database
        cursor.execute(query)
        table = cursor.fetchall()
        if quantity == "one":
            return table[0]
        else:
            return table
    except Exception as e:
            return jsonify({'error': str(e)}), 500

def get_query(query_title: str) -> str:
    """
    Gets query from dml.sql
    query_title: Comment labeling the query in dml.sql
    returns: query
    """
    with open("api/Blueprints/Database/dml.sql", 'r') as file:
        lines = file.readlines()
    found = False
    query_lines = []

    for line in lines:
        if query_title in line:
            found = True
        elif found and line.strip() == '':
            break
        elif found:
            query_lines.append(line.strip())

    return ' '.join(query_lines)[0:-1]
    

def read(query_title: str, quantity: str = 'all') -> list:
    """
    SELECT Query
    query_title: Comment labeling the query in dml.sql
    attributes: list of column names (str) in order
    returns: list of lists representing table
    quantity: "one" or "all"
    """
    query = get_query(query_title)
    try:
        # Query Database
        cursor.execute(query)
        table = cursor.fetchall()
        if quantity == "one":
            return table[0]
        else:
            return table
    except Exception as e:
            return jsonify({'error': str(e)}), 500
