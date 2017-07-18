"""
Author : Abhimanyu
Desc : Global Variables needed to accomadate system Changes
"""

class Gvars():
    #System Proxy Details
    https_proxy=""

    #API details
    APIBaseURL="https://api.plivo.com/"
    APIVersion="v1/"

    #API resource details
    searchingAPI="Account/%s/PhoneNumber/"
    buyingAPI="Account/%s/PhoneNumber/%s/"
    messageAPI="Account/%s/Message/"
    detailsAPI="Account/%s/Message/%s/"
    pricingAPI="Account/%s/Pricing/"
    accountDetailsAPI="Account/%s/"
