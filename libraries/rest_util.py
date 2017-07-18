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
    """
    :Mandatory Param: Auth_id
    :Mandatory Param: Auth_token
    """
        self.url = ''
        self.headers = {}
        self.data = {}
        self.auth_id = auth_id
        self.auth_token = auth_token
        self.proxy = Gvars.https_proxy

    def get(self):
    """
    For GET operation
    Passes data as query params
    :returns code , data when Success:
    :return -1 -1 , when Failure:
    """
        try :
            response = requests.get(url=self.url, params=self.data,\
                                    headers=self.headers,auth=(self.auth_id,self.auth_token)\
                                    ,proxies={'https':self.proxy})
            return (response.status_code, json.loads(response.text))
        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1

    def put(self):
    """
    For PUT operation
    Passes data as Json
    :returns code , data when Success:
    :return -1 -1 , when Failure:
    """
        try :
            response = requests.put(url=self.url, data=json.dumps(self.data),\
                                    headers=self.headers, verify=False,\
                                    proxies={'https':''})
            return (response.status_code, json.loads(response.text))

        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1

    def delete(self):
    """
    For DELETE operation
    Passes data as query params
    :returns code , data when Success:
    :return -1 -1 , when Failure:
    """

        try :
            response = requests.delete(url=self.url, params=self.data,\
                                       headers=self.headers,auth=(self.auth_id,self.auth_token)\
                                       ,proxies={'https':self.proxy})
            return (response.status_code, json.loads(response.text))

        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1


    def post(self):
    """
    For POST operation
    Passes data as Json
    :returns code , data when Success:
    :return -1 -1 , when Failure:
    """
        try :
            response = requests.post(url=self.url, data=json.dumps(self.data),\
                                     headers=self.headers,auth=(self.auth_id,self.auth_token),\
                                     proxies={'https':self.proxy})
            return (response.status_code,json.loads(response.text))
        except Exception as e:
            print "INFO:%s , error:%s"%(self.__dict__ ,e.__doc__)
            return -1,-1
