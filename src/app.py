from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():

    return "index"


@app.route('/login')
def login():

    return "login"


@app.route('/register')
def register():
    return "register"


@app.route('/login', methods=['POST'])
def login_api():
    return "login api"


@app.route('/register', methods=['POST'])
def register_api():
    return "register api"


@app.route('/perfil/:<int:id>', methods=['GET'])
def profile_api(id):
    return "Profile api"


@app.errorhandler(404)
def not_found(error):
    return "Error: {}".format(error.code)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, processes=0)
