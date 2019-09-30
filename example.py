#!/usr/bin/env python3

# Request account data interactively
# No credentials saved!
from tesla_api.passwordmanager import Interactive
pwmgr = Interactive()

# It's also possible - but NOT RECOMMENDED - to provide account data in code.
# You should NOT USE it, as it is unsave!
# It is possible to drive your car with is data!
#from tesla_api.passwordmanager import Hardcoded
#pwmgr = Hardcoded('account','password')

from tesla_api import TeslaApiClient
client = TeslaApiClient(pwmgr)

vehicles = client.list_vehicles()

for v in vehicles:
	print('%s\t%s (%s)\t%s' % (v.id,v.display_name,v.vin,v.state))
