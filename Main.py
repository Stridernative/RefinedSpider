import requests
import csv ,operator
import json


url = "https://www.apple.com/rsp-web/store-search?locale=en_US&sc=false"

payload={}
headers = {
  'authority': 'www.apple.com',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
  'accept': 'application/json, text/plain, */*',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.apple.com/retail/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'dssid2=e9ff214d-18b2-4a81-a0f6-32b102ec9b54; dssf=1; as_sfa=Mnx1c3x1c3x8ZW5fVVN8Y29uc3VtZXJ8aW50ZXJuZXR8MHwwfDE; pxro=1; as_tex=~1~|433415:1:1646917679:USA|5oBaTDAI632YArOVRNck2XV77H9vv7UtpE5nZu6VG9A; geo=US; as_pcts=YV_zabrg0+4BZdAAO3UEKFZL6f5gH0G7zsb8vkNzn-IUl54Qi-FN3wZP1pjvf467d:V4fhYT4SYeDkC803dcNDZgOz3PE9GRo6AC8QbvS; s_cc=true; s_fid=0ABDE6F70B11B24E-3A2AE86A963182B4; s_vi=[CS]v1|30FA2FAD353EFB09-60001B9B59469802[CE]; as_dc=ucp1; mk_epub=%7B%22btuid%22%3A%22rmomkd%22%2C%22prop57%22%3A%22www.us.retailstore%22%7D; s_sq=appleglobal%252Capplestoreww%3D%2526c.%2526a.%2526activitymap.%2526page%253Dretail%252520-%252520list%252520store%252520search%252520%252528us%252529%2526link%253Dcaliforniaunited%252520states%252520-%252520-%252520find%252520a%252520store%2526region%253Dfind%252520a%252520store%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dretail%252520-%252520list%252520store%252520search%252520%252528us%252529%2526pidt%253D1%2526oid%253DfunctionIr%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DA'
}

response = requests.request("GET", url, headers=headers, data=payload)
stores = json.loads(response.text)

print(response.text)

with open('AppleLocations.csv', mode='w') as CSVFile:
    writer = csv.writer(CSVFile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow([
      "storeName",
      "address1",
      "city",
      "stateCode",
      "postal",
      "latitude",
      "longitude"
    ])




    for store in stores['results']:
      row = []
      store_name = store["storeName"]
      address = store["address"]["address1"]
      city = store["address"]["city"]
      state = store["address"]["stateCode"]
      postal = store["address"]["postal"]
      latitude = store["geolocation"]["latitude"]
      longitude = store["geolocation"]["longitude"]

      row.append(store_name)
      row.append(address)
      row.append(city)
      row.append(state)
      row.append(postal)
      row.append(latitude)
      row.append(longitude)
      writer.writerow(row)



#testing out sorting CSV not working
# error: list index out of range
#unsure why ??????
#data = csv.reader(open('AppleLocations.csv'),delimiter=',')

#data = sorted(data, key=operator.itemgetter(0))

#print('After sorting:')
