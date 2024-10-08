from flask import Flask
from api.user_api import user_api
from persistence.user_persistence import init_db

app = Flask(__name__)
app.register_blueprint(user_api, url_prefix='/')

@app.before_first_request
def initialize_database():
    init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)