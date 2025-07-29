from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Replace with your actual PostgreSQL credentials
conn = psycopg2.connect(
    host="db.jpmhdydjycrojffhipxf.supabase.co",
    port=5432,
    database="postgres",
    user="postgres",
    password="french4477",
    sslmode="require"
)
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS registrations (
    id SERIAL PRIMARY KEY,
    fullname TEXT NOT NULL,
    age INT NOT NULL,
    phonenumber TEXT NOT NULL,
    email TEXT NOT NULL
);
""")
conn.commit()

@app.route("/")
def index():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    fullname = request.form["fullname"]
    age = request.form["age"]
    phonenumber = request.form["phonenumber"]
    email = request.form["email"]

    cursor.execute("""
        INSERT INTO registrations (fullname, age, phonenumber, email)
        VALUES (%s, %s, %s, %s)
    """, (fullname, age, phonenumber, email))
    conn.commit()

    return f"User {fullname} registered successfully!"

if __name__ == "__main__":
    app.run(debug=True)
