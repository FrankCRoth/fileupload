import os
from re import U
import app_config
from flask import Flask, render_template, flash, request, redirect, url_for, abort, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config.from_object(app_config)

class UploadException(Exception):
    pass

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            _save_file(request.files['file'])
            flash('Successfully uploaded file', 'info')
        except UploadException as e:
            flash('File type not supported')
            

        #upload_file = request.files['file']
        #filename = secure_filename(upload_file.filename)
        #if filename != '':
        #    file_ext = os.path.splitext(filename)[1]
        #    if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
        #        flash('File type %s not supported' % file_ext, 'error')
        #        return redirect(url_for('index')) 
        #    upload_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        #    flash('Successfully uploaded file %s' % filename, 'info')
        return redirect(url_for('index')) 
    return render_template('index.html')

app.route('/api/upload')
def upload():
    json_data = request.get_json()
    filename = json_data['filename']
    try:
        _save_file(filename)
        return jsonify('Success upload')
    except UploadException as e:
        return jsonify('Error')

def _save_file(upload_file):
    if upload_file == '':
        raise UploadException('No file specified.')
    filename = secure_filename(upload_file.filename)
    file_ext = os.path.splitext(filename)[1]
    if file_ext.lower() not in app.config['UPLOAD_EXTENSIONS']:
        raise UploadException('Not support file extension')
    upload_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    
