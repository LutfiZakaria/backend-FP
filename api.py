import sys, json
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########
from resourceMerchant import MerchantResources
from resourceLogin import LoginResources
from resourceItem import ItemResources
from resourceTransaction import TransactionResources
from resourceTransactionDetail import TransactionDetailResources
from resourceGeneralRuleInfo import GeneralRuleInfoResources
from resourceRulesItem import RulesItemResources
############## Finish import resources ##################


######### Tempat untuk Membuat Endpoint ################
api.add_resource(MerchantResources, "/api/merchant", "/api/merchant/<int:id>")
api.add_resource(LoginResources, "/api/merchant/login")
api.add_resource(ItemResources, "/api/merchant/item", "/api/merchant/item/<int:id>")
api.add_resource(TransactionResources, "/api/merchant/trx", "/api/merchant/trx/<int:id>")
api.add_resource(TransactionDetailResources, "/api/merchant/trx_detail", "/api/merchant/trx_detail/<int:id>")
api.add_resource(GeneralRuleInfoResources, "/api/merchant/general", "/api/merchant/generalrule/<int:id>")
api.add_resource(RulesItemResources, "/api/merchant/ruleitem", "/api/merchant/ruleitem/<int:id>")
################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)