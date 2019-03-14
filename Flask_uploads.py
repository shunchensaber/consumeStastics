from flask import Flask, url_for, request, redirect, render_template
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        #basepath = sys.path[0]     #根
        #upload_path = os.path.join(basepath, 'static', secure_filename(f.fi))
        upload_path = os.path.join('C:/', secure_filename(f.filename))
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload1.html')


if __name__=='__main__':
    app.run()


