from bs4 import BeautifulSoup
import urllib2, csv

content = []

def getHarvardHealthLinkContent(link):
	html_doc = urllib2.urlopen(link).read()
	soup = BeautifulSoup(html_doc, "html.parser")
	title = soup.title.text.lstrip()
	body = soup.find("main", { "class" : "main" })
	body = body.find("div", {"class" : "e-content entry-content"})
	ptags = body.findAll("p")
	page_content = ""
	for p in ptags:
		p = p.text.encode('ascii', 'ignore')
		page_content += p + " "
	title = title.encode('ascii', 'ignore')
	return [title.lstrip(), page_content.lstrip()]

links = ["http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-direct-pressure-to-stop-bleeding", 
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-bleeding", 
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-choking",
"http://www.health.harvard.edu/heart-health/emergencies-and-first-aid-cardiopulmonary-resuscitation",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-mouth-to-mouth-resuscitation",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-emergency-checklist",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-recovery-position",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-removing-a-stuck-ring",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-heimlich-maneuver-on-an-adult",
"http://www.health.harvard.edu/pain/emergencies-and-first-aid-how-to-make-a-sling",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-heimlich-maneuver-on-an-infant",
"http://www.health.harvard.edu/pain/emergencies-and-first-aid-back-injuries",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-medical-identification-tags",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-heimlich-maneuver-on-a-child",
"http://www.health.harvard.edu/family_health_guide/emergencies-and-first-aid-a-well-stocked-first-aid-kit",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-how-to-stop-a-nosebleed",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-removing-a-speck-from-the-eye",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-butterfly-bandage",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-emergency-phone-numbers",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-childbirth",
"http://www.health.harvard.edu/pain/emergencies-and-first-aid-broken-bones",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-removing-a-fishhook",
"http://www.health.harvard.edu/staying-healthy/emergencies-and-first-aid-birth-of-the-placenta",
"http://www.health.harvard.edu/pain/emergencies-and-first-aid-how-to-splint-a-fracture"]

for link in links:
	content.append(getHarvardHealthLinkContent(link))

with open("HarvardHealthContent.csv", 'wb') as f:
    wr = csv.writer(f, dialect='excel')
    wr.writerow(["Title", "Story"])
    for story in content:
    	wr.writerow([story[0], story[1]])
