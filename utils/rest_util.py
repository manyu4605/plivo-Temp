import json
import requests

class send_rest():
    def __init__(self , *args , **kwargs):
        self.url = ''
        self.headers = {}
        self.verify = False
        self.data = {}

    def set_url(self,url):
        self.url = url

    def set_headers(self,headers):
        self.headers = headers

    def set_data(self,data):
        self.data = data
        
    def get(self):
        try :
            response = requests.get(url=self.url,data=json.dumps(self.data),headers=self.headers,verify=self.verify,proxies={'https':''})
            print response.status_code,
        except Exception as e:
            print "Sending Rest(get) .. [FAILED]"
            print e.__doc__
            return -1

        return(response.status_code,response.__dict__["_content"])

    def put(self):
        try :
            response = requests.put(url=self.url,data=json.dumps(self.data),headers=self.headers,verify=self.verify,proxies={'https':''})
            print response.status_code,
        except Exception as e:
            print "Sending Rest(put) .. [FAILED]"
            print e.__doc__
            return -1

        return (response.status_code,response.__dict__["_content"])


    def delete(self):
        try :
            response = requests.delete(url=self.url,data=json.dumps(self.data),headers=self.headers,verify=self.verify,proxies={'https':''})
            print response.status_code,
        except Exception as e:
            print "Sending Rest(delete) .. [FAILED]"
            print e.__doc__
            return -1

        return (response.status_code,response.__dict__["_content"])


    def post(self):
        try :
            response = requests.post(url=self.url,data=json.dumps(self.data),headers=self.headers,verify=self.verify,proxies={'https':''})
            print response.status_code,
        except Exception as e:
            print "Sending Rest(post) .. [FAILED]"
            print e.__doc__
            return -1

        return (response.status_code,response.__dict__["_content"])


