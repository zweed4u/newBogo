#!/usr/bin/env python2.7
#https://www.alovestorygame.com/
import json, requests
session=requests.session()
first=raw_input('First name: ')
last=raw_input('Last name: ')
cell=raw_input('Cell Phone: (eg. 15858675309) ')
zipcode=raw_input('Zip code: ')
email=raw_input('eMail: ')
headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'api.alovestorygame.com',
    'Origin':'https://www.alovestorygame.com',
    'Referer':'https://www.alovestorygame.com/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}

payload={
    "f":first,
    "l":last,
    "m":cell,
    "s":"false",
    "z":zipcode,
    "e":email
}

r=session.post('https://api.alovestorygame.com/us/reg',data=json.dumps(payload),headers=headers)
print r.content
