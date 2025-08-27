
from flask import Flask, jsonify
import pyodbc
import logging



app = Flask(__name__)
# Configure logging to file
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
app.logger.addHandler(logging.StreamHandler())
app.logger.setLevel(logging.ERROR)

def get_db_connection():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-P90FG3J;DATABASE=SF; Trusted_Connection=yes')
    return conn

@app.route('/gethomes', methods=['GET'])
def get_homes():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("{CALL GetHomes}")  # Executes stored procedure
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        app.logger.error(f"Error in /gethomes: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/gethomeAddresses', methods=['GET'])
def get_home_addresses():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("{CALL GetHomeAddresses}")  # Executes stored procedure
        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        cursor.close()
        conn.close()
        return jsonify(results)
    except Exception as e:
        app.logger.error(f"Error in /gethomeAddresses: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
