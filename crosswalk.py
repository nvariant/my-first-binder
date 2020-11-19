import requests
import json

import lxml.html as lh
from lxml.html import fromstring
import time


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

   def getst(self):
     tgt = self.gettgt()
     params = {'service': self.service}
     h = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain", "User-Agent":"python" }
     r = requests.post(tgt,data=params,headers=h)
     st = r.text
     return st

class MeshMapper:

    def __init__(self, auth):
        self.auth = auth

    def getcui(self, mui):
        tgt = self.auth.gettgt()
        ticket = self.auth.getst(tgt)
        mshtocuipre = "https://uts-ws.nlm.nih.gov/rest/search/2020AB?string="
        mshtocuisuff = "&sabs=MSH&searchType=exact&inputType=sourceUi&ticket="
        fullurl = mshtocuipre + mui + mshtocuisuff + ticket
        r = requests.get(fullurl)
        #print(fullurl)
        tocui_json = json.loads(r.text)
        cui = dict(tocui_json['result'])['results'][0]['ui']
        return cui

    def getsct(self, cui):
        tgt = self.auth.gettgt()
        ticket = self.auth.getst(tgt)
        cuitosctpre = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/"
        cuitosctsuff = "/atoms?sabs=SNOMEDCT_US&ttys=PT&ticket="
        fullurl = cuitosctpre + cui + cuitosctsuff + ticket
        r = requests.get(fullurl)
        #print(fullurl)
        tosct_json = json.loads(r.txt)
        reslist = tosct_dict['result'] #often more than one SCTID for a cui
        conlist = []
        for li in reslist:
            sctid = (dict(li))['sourceConcept'].split("/")[-1]
            fsn = (dict(li)['name'])
            con = sctid + '|' + fsn
            conlist.append(con)
        return conlist

    def mapmuis(self, muilist):
        outlist = []
        for m in muilist:
            cui = getcui(mui)
            time.sleep(0.021)
            sct = getsct(cui)
            tine.sleep(0.021)
            entry = mui +'||' + sct
            outlist.append(entry)
            return outlist

    def readMesh(self, filename):
        with open(filename, 'r') as fi:
            lines = fi.readlines()
            p = re.compile('M\d*')
            for line in lines:
                m =  match(p, line) 
            








comstr = '''
mui = "M0012177" auth = Authorization() mm = MeshMapper(auth) a = Authentication() print(a.getst()) print() #c = Crosswalk(a) #print(c.getmsh_sct(mui))
'''

#fullURL = "https://uts-ws.nlm.nih.gov/rest/crosswalk/current/source/HPO/HP:0001947?targetSource=SNOMEDCT_US&ticket=ST-933001-RZOTsGNzxG2faVkfnoFn-cas"

#msh-to-CUI fullURL= "https://uts-ws.nlm.nih.gov/rest/search/2020AB?string=M0012177&sabs=MSH&searchType=exact&inputType=sourceUi&ticket=ST-1069274-xJtOurtNZjdPsDbNIs1k-cas"

#CUI-to-SCT PT
#fullURL = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0022949/atoms?sabs=SNOMEDCT_US&ttys=PT&ticket=ST-1073741-D2UQobTwap5IBCUjEfA9-cas"

#CUI-to-SCT FSN
#fullURL = "https://uts-ws.nlm.nih.gov/rest/content/current/CUI/C0022949/atoms?sabs=SNOMEDCT_US&ttys=FN&ticket=ST-1832213-ba0vh9LFQwhP7LtP5fIJ-cas"

comstr2 = '''
baseURI ="https://uts-ws.nlm.nih.gov/rest"
serv = "/crosswalk/current/source/MSH/"
targ = "?targetSource=SNOMEDCT_US"
ticket = "&ticket=ST-946570-BLkvTxW35gmVPnezdmJX-cas"
fullURL = baseURI + serv + mui + targ + ticket
r = requests.get(fullURL)
print(fullURL)
print(r.text)
'''


