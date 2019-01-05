from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelRulesItem import RulesItem
from modelMerchant import Merchant
from modelItem import Item
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import rulesitem_fields
####### Finish import Model#########

class RulesItemResources(Resource):
    # Untuk Menampilkan Item
    @jwt_required
    def get(self,id=None):
        pass
    
    # Merchant Posting Rules Setup untuk Item
    # Method Post disini hanya bertujuan untuk mengirimkan setup config di database
    @jwt_required
    def post(self):
        my_identity = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("item_id", type=int, location="json", help="Item ID must be linting and exist")
        parser.add_argument("supplier_type", type=int, location="json", help="Supplier Type intbe string and exist")
        parser.add_argument("supplier_amount", type=float, location="json", help="Supplier amount must be number and exist")
        parser.add_argument("supplier_bank_name", type=str, location="json", help="Bank Name must be string and exist")
        parser.add_argument("supplier_bank_account_number", type=str, location="json", help="Bank-account-number must be string and exist")
        parser.add_argument("supplier_bank_account_name", type=str, location="json", help="Bank account name mustbe string and exist")
        args = parser.parse_args()

        # Logic untuk mendapatkan transaction ID yang terakhir
        # Only support 1 barang 1 ID Transaksi
        
        add_rule_item = RulesItem(
            merchant_id = my_identity,
            item_id = args["item_id"],
            supplier_type = args["supplier_type"],
            supplier_amount = args["supplier_amount"],
            supplier_bank_name = args["supplier_bank_name"],
            supplier_bank_account_number = args["supplier_bank_account_number"],
            supplier_bank_account_name = args["supplier_bank_account_name"],
        )

        db.session.add(add_rule_item)
        db.session.commit()

        return {"message":"Add Rules Item Success"} , 200

        
        
    
    @jwt_required
    def put(self,id=None):
        pass

    @jwt_required
    def delete(self,id=None):
        pass