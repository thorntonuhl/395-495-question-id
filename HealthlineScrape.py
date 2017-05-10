from bs4 import BeautifulSoup
import urllib2, csv

content = []


def getHealthlineLinkContent(link):

	html_doc = urllib2.urlopen(link).read()
	soup = BeautifulSoup(html_doc, "html.parser")
	title = soup.title.text.lstrip()
	body = soup.find("article", { "class" : "article"})
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

links = ["http://www.healthline.com/health/first-aid/emergency-kit-for-home",
"http://www.healthline.com/health/first-aid/car-emergency-kit",
"http://www.healthline.com/health/first-aid/cold-weather-safety",
"http://www.healthline.com/health/first-aid/hot-weather-safety",
"http://www.healthline.com/health/first-aid/travel-first-aid",
"http://www.healthline.com/health/first-aid/first-aid-for-kids",
"http://www.healthline.com/health/first-aid/first-aid-for-seniors",
"http://www.healthline.com/health/first-aid/bites-stings",
"http://www.healthline.com/health/first-aid/allergy-attacks",
"http://www.healthline.com/health/first-aid/cpr",
"http://www.healthline.com/health/first-aid/heimlich-maneuver",
"http://www.healthline.com/health/first-aid/stopping-bleeding",
"http://www.healthline.com/health/first-aid/wrapping-strains-and-sprains",
"http://www.healthline.com/health/first-aid/broken-bones",
"http://www.healthline.com/health/first-aid/eye-care"]


for link in links:
	content.append(getHealthlineLinkContent(link))

with open("HealthlineContent.csv", 'wb') as f:
    wr = csv.writer(f, dialect='excel')
    wr.writerow(["Title", "Story"])
    for story in content:
    	wr.writerow([story[0], story[1]])
