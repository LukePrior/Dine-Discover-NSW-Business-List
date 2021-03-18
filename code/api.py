import ast
import re
import requests
import time
from datetime import date
import csv

file = open("dict.txt", "r")

contents = file.read()
dictionary = ast.literal_eval(contents)

file.close()

postcode = ""
suburb = ""
voucher = "CSE" #CSG

today = date.today()

for key in dictionary:
    postcode = key
    for i in dictionary[key]:
        suburb = i
        suburb = re.sub(r"\s+", '%20', suburb)
        api = "https://mybusiness.service.nsw.gov.au/api/crsb/dine-and-discover/business-finder?suburb=" + suburb + "&postCode=" + postcode + "&voucherType=" + voucher
        fetch = requests.get(api)
        response = fetch.json()
        for i in response:
            fields = [i['name'], i['address'], i['latitude'], i['longitude'], i['phone'], i['website'], today.strftime("%d/%m/%Y")]
            with open('dine.csv', 'a', newline="") as fd:
                writer = csv.writer(fd)
                writer.writerow(fields)
        time.sleep(1)
