from app import app
from flask import render_template
from app.forms import UploadFileForm
from werkzeug.utils import secure_filename
import os




@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) # save file to static/files
        return "File has been uploaded!"
    return render_template('index.html', form=form)