
from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

def get_db_connection():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=SF;UID=username;PWD=password')
    return conn

@app.route('/gethomes', methods=['GET'])
def get_homes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL GetHomes}")  # Executes stored procedure
    columns = [column for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    cursor.close()
    conn.close()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
