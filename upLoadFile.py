from flask import Flask, request
app = Flask(__name__)


@app.route("/upload", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        file.save('/download/file')
        return "文件接收成功"

