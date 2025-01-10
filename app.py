from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db,bcrypt
from views import views
from auth import auth

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key="secretkey"

#Initialize the database
db.init_app(app)
bcrypt.init_app(app)


#Register the Blueprint
app.register_blueprint(views)
app.register_blueprint(auth)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)