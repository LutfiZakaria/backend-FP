from models import db

class TransactionDetail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id', ondelete='CASCADE'),nullable=False) 
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, default = 1)
    subTotal = db.Column(db.Float(50))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<TransactionDetail %r>" % self.id