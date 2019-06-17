# coding : utf-8

#--------------------------------------------------------------------
#                           IMPORT
#--------------------------------------------------------------------

#Python libraries
import requests

class Link_API:
    """Allow to request openfoodfacts API"""

    def __init__(self):
        """Initialization of Link_API"""
        print("Link API Instanciated")

#--------------------------------------------------------------------
#                           METHODS
#--------------------------------------------------------------------

    def request(self, url):
        """Send a GET HTTP request and return the response in json format"""

        #We try to request openfoodfacts API
        try:
            r = requests.get(url)
            return r.json()

        except:
            print("Couldn't request openfoodfacts api!")

    

    def request_from_list(self, search_list):
        """Creates url from a list and then request each url"""

        dict_response = dict()
        dict_url = dict()

        #We create a dict associating an item to an url
        for item in search_list:
            dict_url[item] = "https://fr-en.openfoodfacts.org/category/"+item+".json"

        #We associate each item to the json response of the api
        for item, url in dict_url.items():
            r = requests.get(url)
            dict_response.update({item : r.json()})

        return dict_response
            