from flask import Flask
from flask_cors import CORS 

"""
Kör appen enligt följande:
    1. Öppna en terminal och installera requirements med
        pip install -r requirements.txt
    2. Ändra PORT-konstanten till rätt portnummer enligt lista på itslearning
    3. Starta appen i terminalen med
        python app.py
    4. Besök sidan på nätet med https://kursens.server.fi:80xx
"""

PORT=5000
app = Flask(__name__)
CORS(app) # Tillåt cross-origin requests

@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True, ssl_context=(
        '/etc/letsencrypt/fullchain.pem', 
        '/etc/letsencrypt/privkey.pem'
    ))
