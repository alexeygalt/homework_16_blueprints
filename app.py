# from db.models import app
from flask import Flask
from db.fill_db import fill_DB
from offers_routs.views import offers_blueprint
from orders_routs.view import orders_blueprint
from users_routs.view import users_blueprint

app = Flask(__name__)

fill_DB()

app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)

if __name__ == '__main__':
    app.run()
