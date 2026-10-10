from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.route('/workshops', methods=['GET'])
def get_workshops():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM workshops")
        workshops = cursor.fetchall()
        return jsonify(workshops), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/workshops', methods=['POST'])
def create_workshop():
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO workshops (title, status) VALUES (%s, %s)"
        cursor.execute(query, (data['title'], data.get('status', 'Pending')))
        conn.commit()
        return jsonify({"message": "Workshop created", "id": cursor.lastrowid}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/workshops/<int:id>', methods=['PUT'])
def update_workshop(id):
    data = request.json
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE workshops SET title = %s, status = %s WHERE id = %s"
        cursor.execute(query, (data['title'], data['status'], id))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Workshop not found"}), 404
        return jsonify({"message": "Workshop updated"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/workshops/<int:id>', methods=['DELETE'])
def delete_workshop(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM workshops WHERE id = %s", (id,))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({"error": "Workshop not found"}), 404
        return jsonify({"message": "Workshop deleted"}), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/workshops/<int:id>', methods=['GET'])
def get_single_workshop(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM workshops WHERE id = %s", (id,))
        workshop = cursor.fetchone()
        if not workshop:
            return jsonify({"error": "Workshop not found"}), 404
        return jsonify(workshop), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)