from configs import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

######### Tempat untuk Import Model ########
from modelMerchant import Merchant
from modelItem import Item
from modelRulesItem import RulesItem
from modelPaymentMethod import PaymentMethod
from modelInsuranceMethod import InsuranceMethod
from modelShipmentMethod import ShipmentMethod
from modelTransaction import Transactions
from modelTransactionDetail import TransactionDetail
from modelGeneralRuleInfo import GeneralRulesInfo

######### Finish Import Model ########