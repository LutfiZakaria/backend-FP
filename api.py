import sys, json
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########
from resourceMerchant import MerchantResources
from resourceLogin import LoginResources
from resourceItem import ItemResources
############## Finish Style ##################


############## Finish import resources ##################


######### Tempat untuk Membuat Endpoint ################
api.add_resource(MerchantResources, "/api/merchant", "/api/merchant/<int:id>")
api.add_resource(LoginResources, "/api/merchant/login")
api.add_resource(ItemResources, "/api/merchant/item", "/api/merchant/item/<int:id>")

################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)