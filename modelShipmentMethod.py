from models import db

from modelTransaction import Transactions

class ShipmentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shipment_method = db.Column(db.String(50), nullable = False)
    shipment_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    #Relationship to another Table
    transaction = db.relationship("Transactions", backref="shipmentmethod", lazy=True)

    def __repr__(self):
        return "<ShipmentMethod %r>" % self.id