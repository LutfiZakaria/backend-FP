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

rulesitem_fields = {
    "id": fields.Integer,
    "merchant_id": fields.Integer,
    "item_id": fields.Integer,
    "supplier_type": fields.Integer,
    "supplier_amount":fields.Float,
    "supplier_bank_name":fields.String,
    "supplier_bank_account_number":fields.String,
    "supplier_bank_account_name":fields.String,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}

general_fields = {
    "id": fields.Integer,
    "merchant_id": fields.Integer,
    "tax_type":fields.Integer,
    "tax_amount":fields.Float,
    "gov_bank_account_number":fields.String,
    "marketplace_fee_type":fields.Integer,
    "marketplace_fee_amount":fields.Float,
    "marketplace_fee_bank_account_number": fields.String,
    "created_at": fields.DateTime(dt_format='rfc822'),
    "updated_at": fields.DateTime(dt_format='rfc822')
}