# Get Single Products
@app.route('/product/<id>', methoods=['GET'])
def get_products(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)