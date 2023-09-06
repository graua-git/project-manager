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

def read(query: str, quantity: str = 'all') -> list:
    """
    SELECT Query
    query_title: SQL query
    returns: list of lists representing table
    quantity: "one" or "all"
    """
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

def update(entry: dict, table: str, id: int) -> dict:
    """
    UPDATE Query
    entry: JSON Object representing row to insert
    table: table to insert object into
    id: id# of object to update
    returns: response message from MySQL
    """
    try:
        id_name = table.lower()[:-1] + "_id"
        end = f" WHERE {id_name} = {id}"
        sql = f"UPDATE {table} SET "
        for key, val in entry.items():
            if isinstance(val, str):
                val = "'" + val + "'"
            sql += str(key) + " = " + str(val) + ", "
        sql = sql[:-2] + end
        print(sql)
        cursor.execute(sql)
        db.commit()
        return jsonify({'message': "Record updated successfully"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def delete(query: str, id: int) -> dict:
    """
    DELETE Query
    query: SQL query
    returns: list of lists representing table
    """
    try:
        # Query Database
        cursor.execute(query.format(id=id))
        db.commit()
        return jsonify({'message': str(cursor.rowcount) + " record(s) deleted"}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ----------------------------- Helper Functions -----------------------------
def parse_json(entry: dict) -> dict:
    """
    Parses JSON object into strings to use for queries
    entry: JSON Object representing row
    returns: dict
        keys_str: string representing keys "(key1, key2, key3, ...)"
        vals_str: string representing values as %s "(%s, %s, %s, ...)"
        vals_li: list of values [val1, val2, val3, ...]
    """
    keys_str, vals_str = "(", "("
    keys_li, vals_li = [], []
    for key, val in entry.items():
        keys_str += key + ", "
        vals_str += "%s, "
        vals_li.append(val)
    keys_str = keys_str[:-2] + ")"
    vals_str = vals_str[:-2] + ")"
    return {
            'keys_str': keys_str, 
            'vals_str': vals_str,
            'vals_li': vals_li
            }
