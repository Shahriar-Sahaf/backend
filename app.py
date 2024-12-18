from flask import Flask
from flask_login import LoginManager
from config import Config
from controllers.auth_controller import auth_bp
from controllers.main_controller import main_bp
from models import db, User

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)