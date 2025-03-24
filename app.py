from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Ruta para agregar un usuario
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                   (data['name'], data['email']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Usuario añadido!"}), 201

# Ruta para listar usuarios
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify({"users": users}), 200