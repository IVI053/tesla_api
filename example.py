#!/usr/bin/env python3

from tesla_api import TeslaApiClient

client = TeslaApiClient()

vehicles = client.list_vehicles()

for v in vehicles:
	print('%s\t%s (%s)\t%s' % (v.id,v.display_name,v.vin,v.state))
