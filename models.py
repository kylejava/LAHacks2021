from keys import *
import requests
import json
from pprint import pprint



def findBusiness(choice , city):
    businesses = []
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'Bearer %s' % api_key}
    PARAMETERS = {
                    'term': ("Local " + choice),
                    'radius': 10000,
                    'location': city,
                    'limit': 10,
                    'offset': 1,

                    }
    response = requests.get(url = ENDPOINT , params = PARAMETERS, headers = HEADERS)
    business_data = response.json()
    for biz in business_data['businesses']:
        entry = {
            'name': biz['name'],
            'location': biz['location']['display_address'][0],
            'phone': biz['display_phone'],
            'image': biz['image_url']
        }
        businesses.append(entry)

    return businesses
