import urllib, urllib2, webbrowser
from bs4 import BeautifulSoup

def SearchYouTube(textToSearch):
	query = urllib.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	links = soup.findAll(attrs={'class':'yt-uix-tile-link'})
	return 'https://www.youtube.com' + "/embed/"+ links[0]['href'][9:]
#search_query = raw_input("What's Your Emergency: ")
#webbrowser.open(SearchYouTube(search_query))
