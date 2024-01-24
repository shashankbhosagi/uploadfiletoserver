from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']='mysecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

from app import routes