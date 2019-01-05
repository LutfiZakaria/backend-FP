from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_, desc

from models import db
####### Tempat import Model#########
from modelTransaction import Transactions
from modelInsuranceMethod import InsuranceMethod
from modelShipmentMethod import ShipmentMethod
from modelPaymentMethod import PaymentMethod
from modelTransactionDetail import TransactionDetail
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import transaction_fields
####### Finish import Model#########

class TransactionResources(Resource):
    # Untuk Menampilkan Item
    @jwt_required
    def get(self,id=None):
        pass

    # Buyer Melakukan transaksi dan terecord dalam Database Kita
    # Merchant hanya dapat melihat transaksi yang sesuai dengan merchant ID
    def put(self, id=None):
        parser = reqparse.RequestParser()
        parser.add_argument("payment_method_id", type=int, location="json", help="Payment Method must be linting and exist")
        parser.add_argument("shipment_method_id", type=int, location="json", help="Shipment Method intbe string and exist")
        parser.add_argument("insurance_method_id", type=int, location="json", help="Insurance Method must be string and exist")
        parser.add_argument("receiver_name", type=str, location="json", required = True, help="Receiver must be string and exist")
        parser.add_argument("receiver_phone", type=str, location="json", required = True, help="Receiver must be string and exist")
        parser.add_argument("receiver_address", type=str, location="json", required = True, help="Receiver must be string and exist")
        parser.add_argument("payment_status", type=str, location="json")
        args = parser.parse_args()
        
        # Perhitungan Shipment Price
        # Apabila User tidak input maka secara default Kerry Express
        qryShipment = ShipmentMethod.query
        if args["shipment_method_id"] != None:
            qryShipment = qryShipment.filter_by(id=args["shipment_method_id"]).first()
            shipment_price = qryShipment.shipment_price
        else :
            qryShipment = qryShipment.filter_by(id=1).first()
            shipment_price = qryShipment.shipment_price

        # Perhitungan insurance Price
        # Apabila User tidak input maka secara default No insurance
        qryinsurance = InsuranceMethod.query
        if args["insurance_method_id"] != None:
            qryinsurance = qryinsurance.filter_by(id=args["insurance_method_id"]).first()
            insurance_price = qryinsurance.insurance_price
        else :
            qryinsurance = qryinsurance.filter_by(id=1).first()
            insurance_price = qryinsurance.insurance_price
        
        #Perhitungan Total Transaksi
        qryTotal = Transactions.query.order_by(desc(Transactions.created_at)).first()
        trx_id = qryTotal.id
        qryTotal  = TransactionDetail.query.filter_by(transaction_id = trx_id).all()
        total = 0
        for row in qryTotal:
            total = total + row.subTotal
        
        qry = Transactions.query.filter_by(id = id).first()
        if args['payment_method_id'] is not None:
            qry.payment_method_id = args['payment_method_id']
        if args['shipment_method_id'] is not None:
            qry.shipment_method_id = args['shipment_method_id']
            qry.shipment_price = shipment_price
        if args['insurance_method_id'] is not None:
            qry.insurance_method_id = args['insurance_method_id']
            qry.insurance_price = insurance_price
        if args['receiver_name'] is not None:
            qry.receiver_name = args['receiver_name']
        if args['receiver_phone'] is not None:
            qry.receiver_phone = args['receiver_phone']
        if args['receiver_address'] is not None:
            qry.receiver_address = args['receiver_address']
        if args['payment_status'] is not None:
            qry.payment_status = args['payment_status']
        
        # Penggatian Total
        qry.total = total + insurance_price + shipment_price

        db.session.add(qry)
        db.session.commit() 
        return {
            "message": "Add transaction success",
            "transaction": marshal(qry, transaction_fields)
        }, 200
    
    @jwt_required
    def post(self):
        pass

    @jwt_required
    def delete(self,id=None):
        pass