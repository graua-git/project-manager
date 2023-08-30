from flask import jsonify
import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='project_manager'
)
cursor = db.cursor(dictionary=True)

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
