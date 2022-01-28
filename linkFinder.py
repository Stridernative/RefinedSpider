from urllib.request import urlopen
from bs4 import BeautifulSoup
#import csv


#The main URL first Scrape point
url_to_scrape = 'https://www.apple.com/retail/storelist/'

#Request page info & close page
request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

html_soup = BeautifulSoup(page_html, 'html.parser')

store_list = html_soup.find_all('div', class_="address-lines")

#open & Create CSV
#file = open('addresses.csv', 'w')
#writer = csv.writer(file)

#write header rows
#header = ['Address']
#writer.writerow(header)

#First Scrape data array
stores =[]

#Gather each stores href link
for store in store_list:
    store_location = store.find('a')
    store_link = (store_location.get('href'))
    stores.append(store_link)
    print(str('https://www.apple.com') + (store_link)
)

#Gather each individual stores address
#for address in stores:
    #address_url_scrape = 'https://www.apple.com' + str(address)
   # request_page = urlopen(address_url_scrape)
  # page_html = request_page.read()
  #  request_page.close()
  #  html_soup_address = BeautifulSoup(page_html, 'html.parser')

   # address_list = html_soup_address.find('address').text

 #   print(address_list)
   # writer.writerow([address_list])


#file.close()

