from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def showcook():
    return request.cookies.get('username')


if __name__ == '__main__':
    app.run()
