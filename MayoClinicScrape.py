from bs4 import BeautifulSoup
import urllib2, csv

content = []

def getMayoClinicLinks(link):
	html_doc = urllib2.urlopen(link).read()
	soup = BeautifulSoup(html_doc, "html.parser")
	body = soup.find("div", { "index" })
	atags = body.findAll("a", href=True)
	links = []
	for a in atags:
		links.append(link + a["href"][1:])

	return links

def getMayoClinicLinkContent(link):

	html_doc = urllib2.urlopen(link).read()
	soup = BeautifulSoup(html_doc, "html.parser")
	title = soup.title.text.lstrip()
	body = soup.find("div", { "id" : "main-content"})
	ptags = body.findAll("p")
	litags = body.findAll("li", href = False)


	text = []
	for tag in litags:
		atags = tag.findAll("a", href=True)
		if len(atags) < 1:
			text.append(tag.text)

	final_text = ""

	for p in ptags:
		p = p.text.encode('ascii', 'ignore')
		final_text += p + " "
		
	for t in text:
		if "http" not in t:
			t = t.encode('ascii', 'ignore')
			final_text += t + " "


	return [title.lstrip(), final_text.lstrip()]


links = getMayoClinicLinks("http://www.mayoclinic.org/first-aid/")
for link in links:
	content.append(getMayoClinicLinkContent(link))

with open("MayoContent.csv", 'wb') as f:
    wr = csv.writer(f, dialect='excel')
    wr.writerow(["Title", "Story"])
    for story in content:
    	wr.writerow([story[0], story[1]])
