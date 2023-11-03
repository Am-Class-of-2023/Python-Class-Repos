import http.client
import json
from math import exp



conn = http.client.HTTPSConnection("domain-checker7.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "0f80a1a2b3mshff351b87adf8c66p141e84jsn3924b604aa9a",
    'X-RapidAPI-Host': "domain-checker7.p.rapidapi.com"
}

# user enters domain
domainEntered = input("Enter Domain Here: ")
print("")

# request from api
conn.request("GET", "/whois?domain=" + domainEntered, headers=headers)

res = conn.getresponse()
data = res.read()
jsonResponse = json.loads(data.decode('utf-8'))
domainDic = jsonResponse

# print(jsonResponse)


# data
domainData = domainDic.get('domain')
avaliabledata = str(domainDic.get('avaliable'))
ownerdata = domainDic.get('registrar')
expirationdata = domainDic.get('expires_at')
registrardata = domainDic.get('registrar')


# Data display
print("Data For",domainData)
print("-" * (len(domainData) + 8))
if len(ownerdata) == 0:
    avaliabledata = True
    print("Domain is avaliable")
else:
    avaliabledata = False
    print("Avaliability:", avaliabledata)
    print("Owner of domain:", ownerdata)
    print("Expires:", expirationdata)
    print("Domain maintained at:", registrardata)

