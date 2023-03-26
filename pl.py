# Create a property model that represents a property listing
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    photos = db.relationship('Photo', backref='property', lazy=True)
    availability = db.relationship('Availability', backref='property', lazy=True)
    pricing = db.relationship('Pricing', backref='property', lazy=True)
    amenities = db.Column(db.String(500), nullable=False)
    house_rules = db.Column(db.String(500), nullable=False)
    cancellation_policy = db.Column(db.String(500), nullable=False)

# Create a property endpoint that allows hosts to create a new property listing
@app.route('/property', methods=['POST'])
@token_required
def create_property(current_user):
    data = request.get_json()
    new_property = Property(name=data['name'], description=data['description'], address=data['address'], amenities=data['amenities'], house_rules=data['house_rules'], cancellation_policy=data['cancellation_policy'], owner=current_user)
    db.session.add(new_property)
    db.session.commit()
    return jsonify({'message': 'New property created!'})
