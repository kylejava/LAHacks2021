from keys import *
import requests
import json
from pprint import pprint



def findBusiness(choice , city):
    businesses = []
    counter = 1
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
            'name': (str(counter) + ". "  + biz['name']),
            'location': biz['location']['display_address'][0] + " "+biz['location']['display_address'][1] ,
            'phone': biz['display_phone'],
            'image': biz['image_url'],
            'rating': biz['rating']
        }
        counter +=1
        businesses.append(entry)

    return businesses
