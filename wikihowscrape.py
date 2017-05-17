from bs4 import BeautifulSoup
import urllib2, pickle, csv

questions = []

def getQuestionsFromPage(link):
	results = []
	try:
	    html_doc = urllib2.urlopen(link).read()
	    soup = BeautifulSoup(html_doc, "html.parser")
	    qs = soup.findAll("li", { "class" : "qa_aq" })
	    for q in qs:
	    	try:
	    		question = q.find("div", {"class":"qa_q_txt question"}).string
	    		question = question.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\xa0', " ")
	    	except:
	    		question = ""
	    	try:	
	    		answer = q.find("div", {"class":"qa_answer answer"}).string
	    		answer = answer.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u'\xa0', " ")
	    		down = q.find("a", {"class":"wh_vote_down wh_vote_box"}).span.string
	    		up = q.find("a", {"class":"wh_vote_up wh_vote_box"}).span.string
	    	except:
	    		answer = ""
	    		down = ""
	    		up = ""


	    	results.append([question, answer, down, up])
	except:
		results = ["", "", "", ""]
	return results


def getWikiLinks(link):
	html_doc = urllib2.urlopen(link).read()
	soup = BeautifulSoup(html_doc, "html.parser")
	body = soup.find("div", { "id" : "bodycontents" })
	atags = body.findAll("a", href=True)
	links = []
	for a in atags:
		links.append(a["href"][2:])

	return links



links = getWikiLinks("http://www.wikihow.com/Category:First-Aid-and-Emergencies")

with open("wikihow.csv", 'wb') as f:
    wr = csv.writer(f, dialect='excel')
    wr.writerow(["Question", "Answer", "Not Helpful", "Helpful"])
    for link in links:
    	results = getQuestionsFromPage("http://" + link)
    	for result in results:
    		wr.writerow(result)

