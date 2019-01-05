from models import db

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method_id = db.Column(db.Integer, db.ForeignKey('payment_method.id', ondelete='CASCADE'), nullable = False)
    shipment_method_id = db.Column(db.Integer, db.ForeignKey('shipment_method.id', ondelete='CASCADE'), nullable = False)
    insurance_method_id = db.Column(db.Integer, db.ForeignKey('insurance_method.id', ondelete='CASCADE'), nullable = False, default = 1)
    shipment_price = db.Column(db.Float, default = 100)
    insurance_price = db.Column(db.Float, default = 0)
    total = db.Column(db.Float)
    payment_status = db.Column(db.Integer, nullable = True)
    receiver_address = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Transactions %r>" % self.id