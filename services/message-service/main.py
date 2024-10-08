from flask import Flask
from api.message_api import message_api

app = Flask(__name__)

# Register the message blueprint
app.register_blueprint(message_api, url_prefix='/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
