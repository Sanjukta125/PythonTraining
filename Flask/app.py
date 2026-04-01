from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 1️⃣ Configure MySQL Database (UPDATE password & database name before running)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Admin%40123@localhost/flask_db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 2️⃣ Initialize SQLAlchemy
db = SQLAlchemy(app)

# 3️⃣ Define a Model (Table)
class User(db.Model):
    __tablename__ = "users"  # Table name in MySQL
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# 4️⃣ Create Tables (if they don't exist yet)
with app.app_context():
    db.create_all()

# 5️⃣ Route to Add User (POST)
@app.route("/add-user", methods=["POST"])
def add_user():
    try:
        data = request.json
        if not data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing name or email"}), 400

        new_user = User(name=data["name"], email=data["email"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 6️⃣ Route to Get All Users (GET)
@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)

if __name__ == "__main__":
    app.run( port=8000,debug=True)
