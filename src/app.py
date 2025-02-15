from multiprocessing import Value
from re import I
from urllib import response
from flask import Flask, flash, jsonify, redirect, request, render_template
from flask_pymongo import PyMongo
# from flask_wtf import FlaskForm
# from flask_wtf.csrf import CSRFProtect, CSRFError
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET').encode()
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
mongo = PyMongo(app)
# csrf = CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/login')
def login():
    return render_template('login.html'), 200


@app.route('/register')
def register():
    return render_template('register.html'), 200


@app.route('/profile')
def perfil_user():
    return "template user"


# api

@app.route('/login', methods=['POST'])
def login_api():

    email = request.form['email']
    password = request.form['password']

    try:
        cursor = mongo.db.users.find_one({"email": email})
        if not cursor:
            raise ("No existe")

        if cursor['password'] != generate_password_hash(password):
            raise ('Error de contraseña')

    except Exception as e:
        flash(e)
        return render_template('login.html'), 401

    return render_template('login.html'), 200  # in the future to profile


@app.route('/register', methods=['POST'])
def register_api():
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password)

    try:
        id = mongo.db.users.insert_one(
            {'email': email, 'password': hashed_password})
        if not id:
            raise Exception('Error al insertar usuario')

        id = str(id).split("'")[1]
        response = {
            "id": id,
            "password": hashed_password,
            "email": email
        }

        return render_template('perfil.html'), 201

    except Exception as e:
        flash(e)
        return render_template('register.html')


@app.route('/perfil/<int:id>', methods=['GET', 'PUT', 'PATCH'])
def profile_api(id):

    if request.method == 'PUT':
        return "Update all param of perfil de {}".format(id)

    if request.method == 'PATCH':
        return " Update on param of profile de {}".format(id)

    return "Profile api de {}".format(id)


@app.errorhandler(404)
def not_found(error):
    return "Error: {}".format(error.code)


# @app.errorhandler(CSRFError)
# def csrf_error(error):
#     flash('Error de formulario')
#     path = request.path.split('/')[1]
#     print(path)

#     return redirect(url_for(path))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=0)
