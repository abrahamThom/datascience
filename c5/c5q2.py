import requests
from bs4 import BeautifulSoup
def getdata(url):
 r = requests.get(url)
 return r.content
htmldata = getdata("https://sjcetpalai.ac.in")
soup = BeautifulSoup(htmldata,'html.parser')
print("SJC23MCA-20485 : PRINCE THOMAS")
print("Batch : MCA 2023-25")
links = soup.find_all("a")
print("Total number of links : ",len(links))
for link in links:
 if link.get("href") != "":
    print("Link :",link.get("href"),"Text :",link.string)