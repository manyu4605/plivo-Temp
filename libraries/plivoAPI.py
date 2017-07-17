import sys
sys.path.insert(0,'../')
from rest_util import SendRest
from globalVariables import Gvars

class PlivoAPI():

    def __init__(self,auth_id,auth_token):
        self.base_url = Gvars.APIBaseURL
        self.base_api_version = Gvars.APIVersion
        self.auth = auth_id
        self.restAPI = SendRest(auth_id,auth_token)
        self.headers = {'content-type': 'application/json'}

    def searching(self,country_iso,pattern):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.searchingAPI%(self.auth)
        self.restAPI.data = {"country_iso":country_iso,"pattern":pattern}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def buying(self,number):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.buyingAPI%(self.auth,number)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.post()

    def message(self,src,dst,text):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.messageAPI%(self.auth)
        self.restAPI.data = {
                             "src":src,
                             "dst":dst,
                             "text":text
                            }
        self.restAPI.headers = self.headers
        return self.restAPI.post()

    def details(self,uuid):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.detailsAPI%(self.auth,uuid)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def pricing(self,country_iso):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.pricingAPI%(self.auth)
        self.restAPI.data = {"country_iso":country_iso}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


    def account_details(self):
        self.restAPI.url = self.base_url + self.base_api_version + Gvars.accountDetailsAPI%(self.auth)
        self.restAPI.data = {}
        self.restAPI.headers = self.headers
        return self.restAPI.get()


a = PlivoAPI("MAMDA3OTQ5NGI1OWE4NG","NWY4NmQzZGNhYWM2YTFiMmJmZDRjMTgwMmRlMmZj")
#print a.searching("US",7692225329)
#print a.buying(17692225329)
#print a.message(17692225329,17692225328,"Hello World !")

#print a.details("12149129-8de6-4f6c-9db2-03a2637ff780")
#print a.pricing("US")
print a.account_details()
