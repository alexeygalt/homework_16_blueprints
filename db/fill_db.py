import json
from db.models import db, User, Offer, Order


def get_data(path):
    with open(path, 'r', encoding='utf-8') as file:
        result = json.load(file)
        return result


def fill_DB():
    db.drop_all()
    db.create_all()

    users_json = get_data('db/data/users.json')
    orders_json = get_data('db/data/orders.json')
    offers_json = get_data('db/data/offers.json')

    users = [User(**row) for row in users_json]
    orders = [Order(**row) for row in orders_json]
    offers = [Offer(**row) for row in offers_json]

    db.session.add_all(users)
    db.session.add_all(orders)
    db.session.add_all(offers)
    db.session.commit()


fill_DB()
