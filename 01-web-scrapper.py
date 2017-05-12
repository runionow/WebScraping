from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

# Example 1:

try:
    url = urlopen("https://salesforce.com")
except HTTPError:
    print('Please Check the URL and Try Again')

bsObj = BeautifulSoup(url.read(), 'lxml')

found = bsObj.find_all('p',{'class':'item-intro'})

for item in found:
    print(item.get_text())

# Example 2:

try:
    url = urlopen("http://pythonscraping.com/pages/page3.html")
except HTTPError as e:
    print("Message : {}").format(e)

bsObj = BeautifulSoup(url.read(),'lxml')

found = bsObj.find('table',{'id':'giftList'}).tr.next_siblings

for item1 in found:
    print(item1)