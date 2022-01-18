from functools import wraps
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import datetime

from repository import create_user, connect, get_user_password
app=Flask(__name__)
app.config["JWT_SECRET_KEY"] = 'manancarichard'
jwt = JWTManager(app)


#def token_required(f): #Ruta de verificare daca am TOKEN
#   @wraps(f)
#    def decorated(*args, **kwargs):
#        token=request.args.get('token')
#        if not token:
#            return jsonify({'messege':'Token is missing!'}),403
#        try:
#            data=jwt.decode(token, app.config['SECRET_KEY'])
#        except:
#            return jsonify({'messege':'Token is invalid'}),403
#        return f(*args, **kwargs)






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


@app.route("/api/v1/signIn", methods=["POST","GET"])
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
        #token=jwt.encode({'username':username, 'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        # return jsonify({'token':token}), 200
        access_token = create_access_token(identity=username)
        print(access_token)
        res = {"access_token":access_token}
        return res
    except Exception as e:
        error = {
            "error": f"--Failed to sign in. Cause: {e}"
        }
        return error, 500

@app.route("/api/v1/Account",methods=["GET"])
@jwt_required() #Verifica daca are token altfel nu intra pe pagina
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == "__main__":
    app.run(debug=True, port=3004)