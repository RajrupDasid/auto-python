"""TED TALK DOWNLOADER WITH PYTHON"""
import requests #getting content of the TED Talk page
from bs4 import BeautifulSoup #web scraping
import re #Regular pattern or expression matching
#from urllib.request import urlretrieve 
#for downloading mp4
import sys #for argument parsing

#Exception Handeling
if len(sys.argv)>1:
    url=sys.argv[1]
else:
    sys.exit("Error: While entering the URL | Please specify a correct one")
#url=input("Enter your desired TED Talk url for apply download")

r= requests.get(url)
print("Processing Download")

soup=BeautifulSoup(r.content,features="lxml")
for val in soup.findAll("script"):
    if (re.search("talkPage.init",str(val))) is not None:
        result=str(val)
result_mp4=re.search("(?P<url>https?://[\^s]+)(mp4)",result).group("url")
mp4_url=result_mp4.split( '"' )[0]
print("Downloading desire video from ....."+mp4_url)
file_name=mp4_url.split("/")[len(mp4_url.split("/"))-1].split('?')[0]
print("Store the video in ...."+ file_name)
r=requests.get(mp4_url)
with open(file_name,'wb') as f:
    f.write(r.content)

#alternative method
#urlretrive(mp4,file_name)
print("Download Process finished")

