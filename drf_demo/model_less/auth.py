import json
import io
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from .models import userloc
import math
def getresponse(term,lat,lon):
	#term, location coords
	R = 6371
	radius = 2
	filename = 'config_secret.json'
	with io.open('/Users/thiyagesh/Desktop/yelp/drf-demo/drf_demo/model_less/config_secret.json') as cred:
    		creds = json.load(cred)
    		auth = Oauth1Authenticator(**creds)
    		client = Client(auth)
	params = {
    		'term': term,
    		'lang': 'fr'
		}
	result = []
	lat = float(lat)
	lon = float(lon) 
	x1 = lon - math.degrees((radius*math.cos(math.radians(lat)))/R)
	x2 = lon + math.degrees((radius*math.cos(math.radians(lat)))/R)
	y1 = lat + math.degrees(radius/R)
	y2 = lat - math.degrees(radius/R)
	print "Original:",lat,lon
	print "Next:",lat-0.001,lon+0.001
	response = client.search_by_bounding_box(
    		lat+0.01,
		lon-0.01,
		lat-0.01,
		lon+0.01,
    		**params
		)
	#response = client.search_by_coordinates(lat, long, **params)
	for i in response.businesses: 
		result.append(i.name) 
	if len(result) != 0:
		return result
	else:
		return None	 

