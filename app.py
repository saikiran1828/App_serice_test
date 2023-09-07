# app.py

from flask import Flask, jsonify
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

# PostgreSQL database configuration
db_config = {
    'dbname': 'sustainability_db_dev_postgsql',
    'user': 'sustainability_ey_rwuser',
    'password': 'EY@RW123#',
    'host': '10.17.33.134',
    'port': '5432'
}

@app.route('/test-db')
def test_db_connection():
    try:
        # Attempt to connect to the PostgreSQL database
        conn = psycopg2.connect(**db_config)
        conn.close()
        return jsonify({"message": "Database connection successful!"}), 200
    except OperationalError as e:
        return jsonify({"message": "Database connection error: " + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
