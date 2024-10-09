# main.py
from flask import Flask
from api.like_api import like_api

app = Flask(__name__)

# Register the like API blueprint
app.register_blueprint(like_api, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
