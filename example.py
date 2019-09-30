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

# new style 2.x.x with defined password manager
client = TeslaApiClient(pwmgr)

# old 1.x.x style with hardcoded account data
# NOT RECOMMENDED any more!
#client = TeslaApiClient('account','password')

# to use multiple accounts the tokenfile can be specified
client2 = TeslaApiClient(pwmgr,tokenfile='token2.json')

vehicles = client.list_vehicles()

for v in vehicles:
    print('%s\t%s (%s)\t%s' % (v.id,v.display_name,v.vin,v.state))

