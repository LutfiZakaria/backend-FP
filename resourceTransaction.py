from flask_restful import Resource, Api, reqparse, marshal, fields
from flask_jwt_extended import JWTManager,create_access_token,get_jwt_identity, jwt_required, get_jwt_claims, verify_jwt_in_request
from sqlalchemy import or_

from models import db
####### Tempat import Model#########
from modelTransaction import Transactions
####### Finish import Model#########

####### Tempat import Model#########
from marshalField import transaction_fields
####### Finish import Model#########

class ItemResources(Resource):
    # Untuk Menampilkan Item
    @jwt_required
    def get(self,id=None):

        my_identity = get_jwt_identity()

        qry = Item.query

        # Get Item by ID if ID exist.
        if id != None:
            qry = qry.filter_by(id = id).first()         
            return marshal(qry, item_fields), 200
        
        qry = qry.filter_by(merchant_id = my_identity).all()

        rows = []
        for row in qry:
            rows.append(marshal(row, item_fields))

        return rows, 200

    @jwt_required
    def post(self):
        merchant_id = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("item_name", type=str, location="json", required = True, help="Item must be string and exist")
        parser.add_argument("item_price", type=float, location="json", required = True, help="Item Price must be string and exist")
        args = parser.parse_args()
        
        add_item = Item(
            merchant_id = merchant_id,
            item_name = args['item_name'],
            item_price = args['item_price']
        )

        db.session.add(add_item)
        db.session.commit() 
        return {
            "message": "Add Item success",
            "item": marshal(add_item, item_fields)
        }, 200
    
    @jwt_required
    def put(self,id=None):
        merchant_id = get_jwt_identity()
        parser = reqparse.RequestParser()
        parser.add_argument("item_name", type=str, location="json", required = True, help="Item must be string and exist")
        parser.add_argument("item_price", type=float, location="json", required = True, help="Item Price must be string and exist")
        args = parser.parse_args()

        # Filter Item per item ID
        qry = Item.query.filter_by(id=id).first()
        if args['item_name'] != None:
            qry.item_name = args['item_name']
        if args['item_price'] != None:
            qry.item_price = args['item_price']
        
        qry.updated_at = db.func.current_timestamp()
        
        db.session.add(qry)
        db.session.commit() 
        return {
            "message": "Update Item success",
            "item": marshal(qry, item_fields)
        }, 200

    @jwt_required
    def delete(self,id=None):
        qry = Item.query.get(ident=id)

        if qry == None :
            return {"message":"Item Not Found"}, 404
            
        db.session.delete(qry)
        db.session.commit()

        return {"message":"Delete Item Successfull"}, 200