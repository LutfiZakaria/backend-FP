from models import db

class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float)
    payment_status = db.Column(db.Integer, nullable = True)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<Transactions %r>" % self.id