from flask import Flask, request
from flask_cors import CORS 

PORT=8341

app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/", methods = ['GET', 'POST'])
def hello():
    return { 'greeting': "hello, flask-JSON",
'method' : request.method}

@app.route("/test", methods = ['GET', 'POST'])
def test():
    return { "msg": "testing",
'method' : request.method}
    

@app.route("/ip")
def ip():

    ip = request.remote_addr
    return { "ip": ip }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))
