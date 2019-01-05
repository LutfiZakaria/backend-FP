from models import db
# Tempat Import Model Database #

class GeneralRulesInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.Integer,db.ForeignKey('merchant.id', ondelete='CASCADE'),nullable=False)
    tax_type = db.Column(db.Integer, nullable=False)
    tax_amount = db.Column(db.Float)
    gov_bank_account_number = db.Column(db.String(50))
    marketplace_fee_type = db.Column(db.Integer)
    marketplace_fee_amount = db.Column(db.Float)
    marketplace_fee_bank_account_number = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())

    def __repr__(self):
        return "<GeneralRulesInfo %r>" % self.id