from bs4 import BeautifulSoup
import urllib2, pickle, csv

questions = []

def getQuestionsFromPage(link):
    html_doc = urllib2.urlopen(link).read()
    soup = BeautifulSoup(html_doc, "html.parser")
    questions = []
    p_tags = soup.find_all('p')
    for p in p_tags:
        if p.string != None and p.string[-1] == "?":
            questions.append(p.string.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"999", "911").replace(u'\xa0', " "))
    return questions

# link = "http://www.redcross.org.uk/What-we-do/First-aid/Baby-and-Child-First-Aid/Allergic-reaction/Questions-and-answers"
everyday_first_aid = [ "Bleeding-heavily", "Stroke", "Heart-attack", "Broken-bone", "Head-injury", "Choking", "Unresponsive-and-breathing", "Unresponsive-and-not-breathing", "Unresponsive-and-not-breathing-when-an-AED-is-available", "Burns", "Seizures", "Diabetes", "Asthma-attack", "Poisoning", "Distress", "Strains-and-sprains", "Hypothermia", "Meningitis", "Severe-allergic-reaction"]

baby_and_child_first_aid = ["Allergic-reaction", "Asthma-attack", "Bleeding-heavily", "Broken-bone", "Burns", "Choking-baby", "Choking-child", "Croup", "Epileptic-seizure", "Febrile-seizure", "Fever", "Head-injury", "Meningitis", "Nosebleed", "Poisoning", "Unresponsive-and-breathing-baby", "Unresponsive-and-breathing-child", "Unresponsive-and-not-breathing-baby", "Unresponsive-and-not-breathing-child", "Vomiting-and-diarrhoea"]

for i in everyday_first_aid:
    link = "http://www.redcross.org.uk/What-we-do/First-aid/Everyday-First-Aid/" + i + "/Questions-and-answers"
    print link
    questions += (getQuestionsFromPage(link)) # += is slow but acceptable for this data size

for i in baby_and_child_first_aid:
    link = "http://www.redcross.org.uk/What-we-do/First-aid/Baby-and-Child-First-Aid/" + i + "/Questions-and-answers"
    print link
    questions += (getQuestionsFromPage(link))

with open("britishredcross.csv", 'wb') as f:
    wr = csv.writer(f, dialect='excel')
    for q in questions:
        wr.writerow([q])


# def getLinks(homepage, keyWords=[], saveFile=""):
#     links = []
#     links_to_check = [homepage]
#     links_checked = []
#     while len(links_to_check) > 0:
#         currlink = links_to_check[0]
#         if not currlink in links_checked:
#             print "Looking at: " + currlink
#             links_to_check = links_to_check[1:]
#             links_checked.append(currlink)
#             html = ""
#             try:
#                 html = urllib2.urlopen(currlink).read()
#             except (urllib2.HTTPError, urllib2.URLError):
#                 print("Link Failed")
#             if html != "":
#                 if 'questions-and-answers' in currlink:
#                     links.append(currlink)
#                     print "ADDED!"
#                 soup = BeautifulSoup(html, "html.parser")
#                 for href in soup.find_all('a', href=True):
#                     link = href['href'].lower()
#                     if len(link) > 0 and link[0] == "/":
#                         link = homepage + link[1:]
#                     if not link in links_checked and (link[0] == "/" or homepage in link) and all(w in link for w in keyWords):
#                         links_to_check.append(link)
#     if saveFile != "":
#         pickle.dump(links, saveFile)
#     return links

# print getLinks("http://www.redcross.org.uk/What-we-do/First-aid/", saveFile="links.pkl", keyWords = ['first-aid'])
