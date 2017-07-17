"""
================================================================================
Author: Abhimanyu Singh

Description: This File contains requests library wrapper for CRUD operations
================================================================================
"""
import sys
sys.path.insert(0,'../')
from globalVariables import Gvars
import json
import requests


class SendRest():

    def __init__(self, auth_id , auth_token):
        self.url = ''
        self.headers = {'content-type': 'application/json'}
        self.data = {}
        self.auth_id = auth_id
        self.auth_token = auth_token
        self.proxy = Gvars.https_proxy

    def get(self):
        try :
            response = requests.get(url=self.url, params=self.data,\
                                    headers=self.headers,auth=(self.auth_id,self.auth_token)\
                                    ,proxies={'https':self.proxy})
        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1
        return(response.status_code, response.content)

    def put(self):
        try :
            response = requests.put(url=self.url, data=json.dumps(self.data),\
                                    headers=self.headers, verify=False,\
                                    proxies={'https':''})
        except Exception as e:
            print "PUT opertaion failed info :\n\
                   URL : %s\n\
                   DATA: %s\n\
                   HEADERS: %s\n\
                   ERROR: %s\
                  "%(self.url,headers, data,e.__doc__)

            return -1,-1

        return (response.status_code, response.__dict__["_content"])


    def delete(self):
        try :
            response = requests.delete(url=self.url, params=self.data,\
                                       headers=self.headers,auth=(self.auth_id,self.auth_token)\
                                       ,proxies={'https':self.proxy})

        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1

        return(response.status_code, response.content)


    def post(self):
        try :
            response = requests.post(url=self.url, data=json.dumps(self.data),\
                                     headers=self.headers,auth=(self.auth_id,self.auth_token),\
                                     proxies={'https':self.proxy})
            print response.url
        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1

        return (response.status_code,response.__dict__["_content"])

def main ():
    myCaller = SendRest('MAMDA3OTQ5NGI1OWE4NG','NWY4NmQzZGNhYWM2YTFiMmJmZDRjMTgwMmRlMmZj')
    myCaller.url = "https://api.plivo.com/v1/Account/MAMDA3OTQ5NGI1OWE4NG/PhoneNumber/"
    myCaller.data = {"country_iso":"US","pattern":76922}
    print myCaller.get()

#main()


