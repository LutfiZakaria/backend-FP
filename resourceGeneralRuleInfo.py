from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelGeneralRuleInfo import GeneralRulesInfo
from modelMerchant import Merchant
from modelItem import Item
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import rulesitem_fields
####### Finish import Model#########

class GeneralRuleInfoResources(Resource):
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
        parser.add_argument("tax_type", type=int, location="json", help="Item ID must be linting and exist")
        parser.add_argument("tax_amount", type=float, location="json", help="Supplier amount must be number and exist")
        parser.add_argument("gov_bank_account_number", type=str, location="json", help="Government Bank account number must be string and exist")
        parser.add_argument("marketplace_fee_type", type=int, location="json", help="marketplace_fee Type intbe string and exist")
        parser.add_argument("marketplace_fee_amount", type=float, location="json", help="marketplace_fee amount must be number and exist")
        parser.add_argument("marketplace_fee_bank_account_number", type=str, location="json", help="Bank-account-number must be string and exist")
        args = parser.parse_args()

        # Logic untuk mendapatkan transaction ID yang terakhir
        # Only support 1 barang 1 ID Transaksi
        
        add_general_rule = GeneralRulesInfo(
            merchant_id = my_identity,
            tax_type = args["tax_type"],
            tax_amount = args["tax_amount"],
            gov_bank_account_number = args["gov_bank_account_number"],
            marketplace_fee_type = args["marketplace_fee_type"],
            marketplace_fee_amount = args["marketplace_fee_amount"],
            marketplace_fee_bank_account_number = args["marketplace_fee_bank_account_number"],
        )

        db.session.add(add_general_rule)
        db.session.commit()

        return {"message":"Add Rule General Info Success"} , 200

        
        
    
    @jwt_required
    def put(self,id=None):
        pass

    @jwt_required
    def delete(self,id=None):
        pass