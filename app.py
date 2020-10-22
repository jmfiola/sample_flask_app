from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hey, we have Flask in a Docker container!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
