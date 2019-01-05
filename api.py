import sys, json
from configs import app
from configs import manager
from configs import api

###### Tempat Untuk Import Resource #########

############## Finish Style ##################

# Import resource untuk api subusers

############## Finish import resources ##################


######### Tempat untuk Membuat Endpoint ################


api.add_resource(PackageTrackDetail, "/api/users/track", "/api/users/track/<int:id>")
# api.add_resource()
# Endpoint untuk api subusers
################# Finished Endpoint ################

if __name__ == '__main__':
    try:
        if  sys.argv[1] == 'db':
            manager.run()
        else:
            app.run(debug=True, host = '0.0.0.0', port = 5000)
    except  IndexError as p:
        app.run(debug=True, host = '0.0.0.0', port = 5000)