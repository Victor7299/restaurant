from flask import Blueprint, jsonify, request
from rest_app.crud.models import Product

api = Blueprint(
    'api',
    __name__,
    url_prefix='/api'
)

@api.get('/products')
def products():
    q = request.args.get('q')
    products = Product.query.filter(Product.name.contains(q)).all()
    data = []
    for product in products:
        product_info = {}
        product_info['name'] = product.name
        product_info['price'] = product.price
        data.append(product_info)
    print(products)
    return jsonify({'products': data})