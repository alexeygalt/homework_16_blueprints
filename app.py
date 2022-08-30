from db.models import app
from db.fill_db import fill_DB
from offers_routs.views import offers_blueprint
from orders_routs.view import orders_blueprint
from users_routs.view import users_blueprint


fill_DB()

app.register_blueprint(users_blueprint)
app.register_blueprint(orders_blueprint)
app.register_blueprint(offers_blueprint)

app.run()

