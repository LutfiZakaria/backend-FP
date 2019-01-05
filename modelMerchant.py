from models import db
from werkzeug.security import generate_password_hash, check_password_hash

# Tempat Import Model Database #

class Merchant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable = False)
    bank_name = db.Column(db.String(50))
    bank_account = db.Column(db.String(50))
    bank_account_name = db.Column(db.String(50))
    status = db.Column(db.Boolean, default=1)
    created_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default= db.func.current_timestamp())
    # relationship
    rulesItem = db.relationship("RulesItem", backref="merchant", lazy=True)
    generalRuleInfo = db.relationship("GeneralRuleInfo", backref="merchant", lazy=True)
    Item = db.relationship("Item", backref="merchant", lazy=True)
    
    def __repr__(self):
        return "<Merchant %r>" % self.id