from models import db
# Tempat Import Model Database #

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer, db.ForeignKey('merchant.id', ondelete='CASCADE'),nullable=False)
    item_name = db.Column(db.String(50), nullable=False)
    item_price = db.Column(db.Float(50), nullable=False)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    # relationship
    rulesItem = db.relationship("RulesItem", backref="item", lazy=True)
    Item = db.relationship("TransactionDetail", backref="item", lazy=True)
    
    def __repr__(self):
        return "<Merchant %r>" % self.id