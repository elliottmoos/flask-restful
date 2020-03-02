from flask import Flask, g, jsonify
from flask_restful import Resource, Api
import models

from auth import auth
import config
from resources.courses import courses_api
from resources.reviews import reviews_api
from resources.users import users_api

app = Flask(__name__)
app.register_blueprint(courses_api, url_prefix='/api/v1')
app.register_blueprint(reviews_api, url_prefix='/api/v1')
app.register_blueprint(users_api, url_prefix='/api/v1')

@app.route('/api/v1/users/token', methods=['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token': token.decode('ascii')})

if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG, port=config.PORT, host=config.HOST)