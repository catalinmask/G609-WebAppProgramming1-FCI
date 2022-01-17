from flask import Flask, request
from flask_cors import CORS

from repository import create_user, connect, get_user_password
app=Flask(__name__)
CORS(app)
database="BazaProiect.db"
@app.route("/api/v1/signUp", methods=["POST"])
def signup():
    body = request.json #datele pe care le trimit in signup
    if not body: # daca nu trimit nimic
        error = {
            "error": "--Failed to create a new user. Empty body provided."
        }
        return error, 400

    try: 
        first_password = body["Password"]
        second_password = body["secondPassword"]
        if first_password != second_password:
            error = {
                "error": "--Failed to create user. Password mismatch."
            }
            return error, 400

        conn = connect(database)

        create_user(conn, body)
        conn.close()

        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to create a new user. Message: {e}"
        }
        return error, 500


@app.route("/api/v1/signIn", methods=["POST"])
def sign_in():
    try:
        body = request.json
        username = body.get("username")
        password = body.get("password")
        conn = connect(database)
        existing_password = get_user_password(conn, username)
        if existing_password is None or password != existing_password:
            error = {
                "error": "--Failed to sign in. Email or password are wrong."
            }
            return error, 401

        return '', 204
    except Exception as e:
        error = {
            "error": f"--Failed to sign in. Cause: {e}"
        }
        return error, 500


if __name__ == "__main__":
    app.run(debug=True, port=3004)