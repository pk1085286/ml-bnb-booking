# Create a property search endpoint that allows guests to search for properties based on location, price, and availability
@app.route('/property/search', methods=['GET'])
def search_properties():
    location = request.args.get('location')
    price_min = request.args.get('price_min')
    price_max = request.args.get('price_max')
    date_start = request.args.get('date_start')
    date_end = request.args.get('date_end')
    properties = Property.query.filter(Property.address.contains(location)).filter(Pricing.price.between(price_min, price_max)).filter(Availability.date.between(date_start, date_end)).all()
    return jsonify({'properties': [property.to_dict() for property in properties]})
