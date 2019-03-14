from flask import Flask, url_for, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        return "欢迎你的到来"


if __name__=='__main__':
    app.run()


