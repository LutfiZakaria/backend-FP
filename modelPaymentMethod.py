from models import db

from modelTransactionDetail import TransactionDetail

class PaymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(50), nullable = False)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    #Relationship to another Table
    transaction_detail = db.relationship("TransactionDetail", backref="paymentmethod", lazy=True)

    def __repr__(self):
        return "<PaymentMethod %r>" % self.id