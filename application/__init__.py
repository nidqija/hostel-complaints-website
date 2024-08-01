from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
app.config['UPLOADED_FOLDER'] = '../application/static/facilitiesform'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'png', 'jpeg'}
bcrypt = Bcrypt(app)
migrate = Migrate(app , db)
app.app_context().push()
login_manager = LoginManager(app)



from application import routes


