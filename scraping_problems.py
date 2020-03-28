import requests
from bs4 import BeautifulSoup

accept='text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8'
acceptEncoding='gzip, deflate, br'
acceptLanguage='en-US, en; q=0.5'
cookie='ffverifytimes=1; fflastactivity=0; fftab-history=calendar%2Cforums; ffsettingshash=c1cc05f4bc2c72fba054db520e06352e; fflastvisit=1585371911; ffdstonoff=1; fftimezoneoffset=-6; ffadon=1; __gads=ID=301618e0d651417d:T=1585371912:S=ALNI_MbN44mE7AAy1nrXhmvqaG7M_7vzig; _gid=GA1.2.69885615.1585371918; _ga=GA1.2.1633801945.1585371918'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363'
referer='https://www.forexfactory.com/calendar?day=Feb10.2019'
host='www.forexfactory.com'
connection='close'#'Keep-Alive'
upgrade='1'
head = {'User-Agent': useragent,'Referer':referer,'Host':host,'Connection':connection,'Accept-Encoding':acceptEncoding,'Accept-Language':acceptLanguage,'Accept':accept,'Cookie':cookie,'Upgrade-Insecure-Requests':upgrade}
page = requests.get("https://www.forexfactory.com/calendar?day=Feb10.2019",headers=head) #sample page
#print("content=",content)
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
