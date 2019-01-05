from flask_restful import fields

merchant_fields = {
    "id": fields.Integer,
    "fullname": fields.String, 
    "email": fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

merchantfull_fields = {
    "id": fields.Integer,
    "fullname": fields.String, 
    "email": fields.String,
    "bank_name": fields.String,
    "bank_account": fields.String,
    "bank_account_name": fields.String,
    "address":fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}


item_fields = {
    "id":fields.Integer,
    "merchant_id":fields.Integer,
    "item_name":fields.String,
    "item_price":fields.Float,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

transaction_fields = {
    "id": fields.Integer,
    "payment_method_id": fields.Integer,
    "shipment_method_id": fields.Integer,
    "insurance_method_id": fields.Integer,
    "paymentmethod.payment_method":fields.String,
    "shipmentmethod.shipment_method":fields.String,
    "shipment_price": fields.String,
    "insurancemethod.insurance_method":fields.String,
    "insurance_price": fields.String,
    "total": fields.Float,
    "payment_status": fields.String,
    "receiver_name": fields.String,
    "receiver_phone": fields.String,
    "receiver_address": fields.String,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

transactiondetail_fields = {
    "id": fields.Integer,
    "transaction_id": fields.Integer,
    "item_id": fields.String,
    "Item.item_name": fields.String,
    "quantity": fields.String,
    "subTotal": fields.Float,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

po_fields = {
    "id": fields.Integer,
    "supplierID": fields.Integer,
    "suppliers.name": fields.String,
    "userPOID": fields.Integer,
    "packagePOID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name": fields.String,
    "packages.Category.category":fields.String,
    "quantity": fields.Integer,
    "buyingPricePerPackage": fields.Float,
    "totalPrice": fields.Float,
    "notes" : fields.String,
    "status":fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

sale_fields = {
    "id": fields.Integer,
    "userSalesID": fields.Integer,
    "customerSalesID": fields.Integer,
    "customers.fullname": fields.String,
    "packageSalesID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name": fields.String,
    "packages.Category.category":fields.String,
    "quantity": fields.Integer,
    "sellingPricePerPackage": fields.Float,
    "totalPrice":fields.Float,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

actualstock_fields = {
    "id": fields.Integer,
    "userActualStocksID": fields.Integer,
    "packageActualStocksID": fields.Integer,
    "actual_stock": fields.Integer,
    "packages.package_name": fields.String,
    "packages.Items.item":fields.String,
    "notes": fields.String,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

packagetrack_fields = {
    "id": fields.Integer,
    "POID": fields.Integer,
    "salesID": fields.Integer,
    "packageID": fields.Integer,
    "packages.Items.item":fields.String,
    "packages.package_name":fields.String,
    "code": fields.String,
    "status": fields.Boolean,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

subuser_fields = {
    "id": fields.Integer,
    "userID": fields.Integer,
    "fullname": fields.String,
    "email": fields.String,
    "username": fields.String,
    "apiKey": fields.String,
    "phone_number": fields.String,
    "subuser_type": fields.String,
    "status": fields.Boolean,
    "created_at": fields.String,
    "updated_at": fields.String
}