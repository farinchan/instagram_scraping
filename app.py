import flask
from flask import request, jsonify
from flask_cors import CORS
from load import getprofile

app = flask.Flask(__name__)
CORS(app)


@app.route('/api/v1/profile', methods=['GET'])
def echo():
    username = request.args.get('username')
    if username is None:
        return jsonify({
            "status": "error",
            "message": "Username is required"
        })
    result = getprofile(username)
    return jsonify(result), result["status_code"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)