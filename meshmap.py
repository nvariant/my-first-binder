import json

comstr = '''
tocui = '{"pageSize":25,"pageNumber":1,"result":{"classType":"searchResults","results":[{"ui":"C0022949","rootSource":"MTH","uri":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0022949","name":"lactose"}]}}'
tocui_dict = json.loads(tocui)
resdict = dict(tocui_dict['result'])['results'][0]['ui']
print(resdict)
'''

tosct = '{"pageSize":25,"pageNumber":1,"pageCount":1,"result":[{"classType":"Atom","ui":"A3531690","suppressible":"false","obsolete":"false","rootSource":"SNOMEDCT_US","termType":"FN","code":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/source/SNOMEDCT_US/47703008","concept":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0022949","sourceConcept":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/source/SNOMEDCT_US/47703008","sourceDescriptor":"NONE","attributes":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/AUI/A3531690/attributes","parents":"NONE","ancestors":null,"children":"NONE","descendants":null,"relations":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/AUI/A3531690/relations","name":"Lactose (substance)","language":"ENG","contentViewMemberships":[]},{"classType":"Atom","ui":"A29510920","suppressible":"false","obsolete":"false","rootSource":"SNOMEDCT_US","termType":"FN","code":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/source/SNOMEDCT_US/423291009","concept":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/CUI/C0022949","sourceConcept":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/source/SNOMEDCT_US/423291009","sourceDescriptor":"NONE","attributes":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/AUI/A29510920/attributes","parents":"NONE","ancestors":null,"children":"NONE","descendants":null,"relations":"https://uts-ws.nlm.nih.gov/rest/content/2020AB/AUI/A29510920/relations","name":"Product containing lactose (medicinal product)","language":"ENG","contentViewMemberships":[]}]}'

tosct_dict = json.loads(tosct)
reslist = tosct_dict['result']
conlist = []
for li in reslist:
    SCTID = (dict(li)['sourceConcept']).split"/"[-1]
    FSN = (dict(li)['name'])
    con = SCTID + '|' + FSN
    conlist.append(con)
print(conlist)
