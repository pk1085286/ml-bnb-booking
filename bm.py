# Create a booking model that represents a booking made by a guest
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    date_start = db.Column(db.DateTime, nullable=False)
    date_end = db.Column(db.DateTime, nullable=False)

# Create a booking endpoint that allows guests to make a new booking
@app.route('/booking', methods=['POST'])
@token_required
def create_booking(current_user):
    data = request.get_json()
    property = Property.query.get
