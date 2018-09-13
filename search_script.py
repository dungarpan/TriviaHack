from bs4 import BeautifulSoup as soup
from urllib.request import urlopen 

def search(url):
	uclient= urlopen(url)
	page_html=uclient.read()
	uclient.close()
	page_soup=soup(page_html,"html.parser")
	#res=soup.find_all("div", class_="Z0LcW")
	api_key= 'AIzaSyDGVTDLw_kRF4XhJrup8Mbyh3-Jx9A0dR0'