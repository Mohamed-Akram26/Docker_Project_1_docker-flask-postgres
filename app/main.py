from flask import Flask
import psycopg2
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route('/')
def home():
    return "Welcome to Dockerized Flask App!"

@app.route('/db')
def check_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return "Database connected successfully!"
    except Exception as e:
        return f"Error connecting to DB: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
