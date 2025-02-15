from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET').encode()
csrf = CSRFProtect(app)



@app.route('/')
def index():
    return render_template('index.html'), 200


@app.route('/login')
def login():
    return render_template('login.html'), 200


@app.route('/register')
def register():
    return "register"


@app.route('/profile')
def perfil_user():
    return "template user"




# api

@app.route('/login', methods=['POST'])
def login_api():
    return "login api"


@app.route('/register', methods=['POST'])
def register_api():
    return "register api"


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


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=0)
