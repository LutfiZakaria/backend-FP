from models import db
# Tempat Import Model Database #

class RulesItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer,db.ForeignKey('merchant.id', ondelete='CASCADE'),nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', ondelete = 'CASCADE'), nullable=False)
    supplier_type = db.Column(db.Integer, nullable=False)
    supplier_amount = db.Column(db.Float)
    supplier_bank_name = db.Column(db.String(50))
    supplier_bank_account_number = db.Column(db.String(50))
    supplier_bank_account_name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    
    def __repr__(self):
        return "<RulesItem %r>" % self.id