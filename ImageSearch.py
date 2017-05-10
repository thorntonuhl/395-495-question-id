from bs4 import BeautifulSoup
from PIL import Image
import requests, re, urllib2, os, cookielib, json, webbrowser

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def SearchImage(query):
	image_type="ActiOn"
	query= query.split()
	query='+'.join(query)
	url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
	header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
	}
	soup = get_soup(url,header)


	ActualImages=[]
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    ActualImages.append((link,Type))

	return ActualImages[0][0]


#search_query = raw_input("What's Your Emergency: ")
#webbrowser.open(SearchImage(search_query))
