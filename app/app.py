from database import db, migrate
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.views.templates_views import app_views
from app.models.entities.users import User
from app.models.entities.comments import Comments
from app.models.entities.garbage import Garbage
from app.models.entities.cooperative import Cooperative
from app.models.entities.comment_likes import CommentLikes
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


def _register_blueprint(_app: Flask):
    _app.register_blueprint(app_views)


app = Flask(__name__, template_folder="./app/templates", static_folder="./templates")
CORS(app)
app.config.from_object('settings')
app.config['FLASK_ADMIN_SWATCH'] = 'Slate'
admin = Admin(app, name='EcoHub', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Comments, db.session))
admin.add_view(ModelView(Garbage, db.session))
admin.add_view(ModelView(Cooperative, db.session))
admin.add_view(ModelView(CommentLikes, db.session))
JWTManager(app)
db.init_app(app)
migrate.init_app(app, db)
_register_blueprint(app)
