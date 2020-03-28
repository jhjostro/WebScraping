import requests
from bs4 import BeautifulSoup
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'}
page = requests.get("https://www.forexfactory.com/calendar?day=Feb2.2018",headers=head) #sample page
content = page.content
soup = BeautifulSoup(content,"html.parser")
table = soup.find_all("tr",{"class":"calendar_row"})
time=99
for item in table:
    currency=item.find_all("td", {"class":"calendar__currency"})[0].text #currency
    time_entry=item.find_all("td", {"class":"calendar__time"})[0].text #time (may have more than one entry)
    #if( str.len(time_entry)=0 ):  #empty string for time
    #        time_entry=time
    print( "currency="+currency ) #Currency
    print( "time_entry=",time_entry ) #Time Eastern
