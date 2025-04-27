from flask import Flask, jsonify, request
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)

@app.route("/author")
def author():
    author = {
        "name": "Alisa",
        "course": 4,
        "age": 21,
    }
    return jsonify(author)

@app.route('/sum')
def runner():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})

@app.route("/")
def server_info():
    return "My server"


if __name__ == "__main__":
    app.run(debug=True, port=5000)

def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000

if __name__ == "__main__":
    app.run(debug=True, port=get_port())




