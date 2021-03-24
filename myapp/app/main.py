import os
from flask import Flask, jsonify

app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    # return a json
    return jsonify({
        'status': 'OK',
    })

if __name__ == '__main__':
    #define the localhost ip and the port that is going to be used
    app.run(host='0.0.0.0', debug=os.getenv('FLASK_DEBUG'), port=os.getenv('PORT'))
