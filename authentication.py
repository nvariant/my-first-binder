## See https://documentation.uts.nlm.nih.gov/rest/authentication.html for full explanation

import requests

import lxml.html as lh
from lxml.html import fromstring



class Authentication:

   def __init__(self):
    self.apikey = "a3c76ec5-b11a-40b4-be82-43ecaddf112f"
    self.service="http://umlsks.nlm.nih.gov"
    self.auth_endpoint = "/cas/v1/api-key"
    self.uri="https://utslogin.nlm.nih.gov"

   def gettgt(self):
     params = {'apikey': self.apikey}
     h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
     r = requests.post(self.uri + self.auth_endpoint, data=params,headers=h)
     response = lh.fromstring(r.text)
     ## extract the entire URL needed from the HTML form (action attribute) returned - looks similar to https://utslogin.nlm.nih.gov/cas/v1/tickets/TGT-36471-aYqNLN2rFIJPXKzxwdTNC5ZT7z3B3cTAKfSc5ndHQcUxeaDOLN-cas
     ## we make a POST call to this URL in the getst method
     tgt = response.xpath('//form/@action')[0]

     return tgt

   def getst(self,tgt):

     params = {'service': self.service}
     h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
     r = requests.post(tgt,data=params,headers=h)
     st = r.text
     return st
     
auth = Authentication()
tgt = auth.gettgt()
st = auth.getst(tgt)
#print(st)

#print(auth.getmsh_sct())

def domap():
    baseURI = "https://uts-ws.nlm.nih.gov/rest"
    serv = "/crosswalk/current/source/MSH/"
    mui = "M0012177"
    targ = "?targetSource=SNOMEDCT_US"
    st = "ST-1287639-fDprXZeEOFnQ6foMGMpa-cas"
    ticket = "&ticket=" + st

    r = requests.get(baseURI + serv + mui + targ + ticket)
    print(r.text)

#domap()

#newurl = "https://uts-ws.nlm.nih.gov/rest/search/current?string=diabetes&ticket=" + st
#res = requests.get(url = newurl)
#print(res.text)

#testurl = "https://uts-ws.nlm.nih.gov/rest/crosswalk/current/source/MSH/M0012177?targetSource=SNOMEDCT_US&ticket=ST-1288479-fxiPQ377n972anRNnauX-cas"
#r = requests.get(testurl)
#print(r.text)




