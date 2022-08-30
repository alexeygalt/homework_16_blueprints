from flask import Blueprint, jsonify, request
from db.models import db, Offer

offers_blueprint = Blueprint('offers_blueprint', __name__)


@offers_blueprint.route('/offers', methods=['GET', 'POST'])
def get_all_offers():
    if request.method == 'GET':
        result = []
        offers = Offer.query.all()
        for offer in offers:
            result.append(offer.offers_to_dict())
        return jsonify(result)

    if request.method == 'POST':
        update_data = request.get_json()
        new_offer = Offer(
            order_id=update_data.get('order_id'),
            executor_id=update_data.get('executor_id')

        )
        db.session.add(new_offer)
        db.session.commit()
        return jsonify({'Offer': 'created'})


@offers_blueprint.route('/offers/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_one_offer(pk):
    offer = Offer.query.get(pk)
    if not offer:
        return jsonify({'ValueError': 'offer not found'})
    if request.method == 'GET':
        return jsonify(offer.offers_to_dict())
    if request.method == 'PUT':
        update_data = request.get_json()
        offer.order_id = update_data.get('order_id')
        offer.executor_id = update_data.get('executor_id')
        db.session.add(offer)
        db.session.commit()
        return jsonify({f'Offer {pk}': 'updated'})
    if request.method == 'DELETE':
        db.session.delete(offer)
        db.session.commit()
        return jsonify({f'Offer {pk}': 'deleted'})

