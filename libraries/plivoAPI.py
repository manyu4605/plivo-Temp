"""
Author : Abhimanyu Singh
Desc : APIs for interaction with Plivo Cloud
"""

import sys
sys.path.insert(0,'../')
from rest_util import SendRest
from globalVariables import Gvars

class PlivoAPI():

    """
    Test Library for interacting with Pilvo APIs
    """

    def __init__(self,auth_id,auth_token):
        """
        :return: None
        """
        self.base_url = Gvars.APIBaseURL
        self.base_api_version = Gvars.APIVersion
        self.auth = auth_id
        self.restAPI = SendRest(auth_id,auth_token)
        self.headers = {'content-type': 'application/json'}

    def searching(self,country_iso,pattern):
        """
        Invoke Pilvo searching API
        :param country_iso:Country Code Ex. US
        :param pattern: startng pattern
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version +\
                           Gvars.searchingAPI%(self.auth)
        self.restAPI.data = {"country_iso":country_iso,"pattern":pattern}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def buying(self,number):
        """
        Invoke Pilvo buying API
        :param number: Phone Number to buy
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version + \
                           Gvars.buyingAPI%(self.auth,number)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.post()

    def message(self,src,dst,text):
        """
        Invoke Pilvo message API
        :param src: Source Phone Number
        :param dst: Destination Phone Number
        :param text: Message Text
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version +\
                           Gvars.messageAPI%(self.auth)
        self.restAPI.data = {
                             "src":src,
                             "dst":dst,
                             "text":text
                            }
        self.restAPI.headers = self.headers
        return self.restAPI.post()

    def details(self,uuid):
        """
        Invoke Pilvo detail API
        :param uuid: UUID returned from Message API
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version +\
                           Gvars.detailsAPI%(self.auth,uuid)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def pricing(self,country_iso):
        """
        Invoke Pilvo pricing API
        :param country_iso:Country Code Ex. US
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version +\
                           Gvars.pricingAPI%(self.auth)
        self.restAPI.data = {"country_iso":country_iso}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def account_details(self):
        """
        Invoke Pilvo account Detail API
        :return: Code , Json Response
        """
        self.restAPI.url = self.base_url + self.base_api_version +\
                           Gvars.accountDetailsAPI%(self.auth)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.get()
