from flask import Blueprint, jsonify, request
from db.models import db, Order

orders_blueprint = Blueprint('orders_blueprint', __name__)


@orders_blueprint.route('/orders', methods=['GET', 'POST'])
def get_all_orders():
    if request.method == 'GET':
        result = []
        orders = Order.query.all()
        for order in orders:
            result.append(order.orders_to_dict())
        return jsonify(result)
    if request.method == 'POST':
        upload_order = request.get_json()
        new_order = Order(
            name=upload_order.get('name'),
            description=upload_order.get('description'),
            start_date=upload_order.get('start_date'),
            end_date=upload_order.get('end_date'),
            address=upload_order.get('address'),
            price=upload_order.get('price'),
            customer_id=upload_order.get('customer_id'),
            executor_id=upload_order.get('executor_id')

        )
        db.session.add(new_order)
        db.session.commit()
        return jsonify(new_order.orders_to_dict())


@orders_blueprint.route('/orders/<int:pk>', methods=['GET', 'PUT', 'DELETE'])
def get_one_order(pk):
    order = Order.query.get(pk)
    if not order:
        return jsonify({'ValueError': 'order not found'})
    if request.method == 'GET':
        return jsonify(order.orders_to_dict())
    if request.method == 'PUT':
        upload_date = request.get_json()
        order.name = upload_date.get('name')
        order.description = upload_date.get('description')
        order.start_date = upload_date.get('start_date')
        order.end_date = upload_date.get('end_date')
        order.address = upload_date.get('address')
        order.price = upload_date.get('price')
        order.customer_id = upload_date.get('customer_id')
        order.executor_id = upload_date.get('executor_id')
        db.session.add(order)
        db.session.commit()
        return jsonify(order.orders_to_dict())
    if request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return jsonify({f'Order {pk}': 'deleted'})

    
