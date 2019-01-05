from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelTransaction import Transactions
from modelTransactionDetail import TransactionDetail
from modelItem import Item
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import transaction_fields
####### Finish import Model#########

class TransactionDetailResources(Resource):
    # Untuk Menampilkan Item
    @jwt_required
    def get(self,id=None):
        pass
    
    # Buyer Melakukan transaksi dan terecord dalam Database Kita
    # Merchant hanya dapat melihat transaksi yang sesuai dengan merchant ID
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("item_id", type=int, location="json", help="Payment Method must be linting and exist")
        parser.add_argument("quantity", type=int, location="json", help="Shipment Method intbe string and exist")
        parser.add_argument("status", type = bool, location="json")
        args = parser.parse_args()

        # Logic untuk mendapatkan transaction ID yang terakhir
        # Only support 1 barang 1 ID Transaksi
        add_trx = Transactions()
        db.session.add(add_trx)
        db.session.commit()

        qry = Transactions.query.order_by(desc(Transactions.created_at)).first()
        trx_id = qry.id

        
        # Perhitungan SubTotal
        qry = Item.query.filter_by(id = args["item_id"]).first()
        subTotal = float(args['quantity'])*qry.item_price

        add_trx_detail = TransactionDetail(
            item_id = args["item_id"],
            transaction_id = trx_id,
            quantity = args["quantity"],
            subTotal = subTotal,
            status = args["status"]
        )

        db.session.add(add_trx_detail)
        db.session.commit()

        return {"message":"Add Detail Transaction Success"} , 200

        
        
    
    @jwt_required
    def put(self,id=None):
        pass

    @jwt_required
    def delete(self,id=None):
        pass