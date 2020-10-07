# Get All Products
@app.route('/product', methoods=['GET'])
def get_products():
    all_product = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)
    