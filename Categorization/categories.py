tag = -1

categories = [
                      "What if",
                      "Should I",
                      "What should I do if",
                      "How do I",
                      "What is",
                      "How can I tell if",
                      "Do I",
                      "What do I do if",
                      "Can I give them",
                      "What are the signs and symptoms of",
                      "How do I treat",
                      "When should I call 911?",
                      "Should I try",
                      "How long should I",
                      "How will I know if",
                      "What does"
                      ]

#Tester list of questions, default input is a text file
question_list = [
    
    "What is asthma?",
    "How can I tell if someone is having an asthma attack?",
    "What sort of medication will they use?",
    "What does an inhaler look like?",
    "What is a spacer?",
    "When should I call 911?",
    "What do I do if the person stops breathing?",
    "What do I do if the bleeding soaks through the item I've used?",
    "What should I do if there is an embedded object in the wound?",
    "Should I wash the wound?",
    
]

#Categorize function
def categorize(question, categories):

    tag = -1
    
    counter = 0

    #While loop for n question substrings
    while counter < len(question):
        
        #If substring in category question list
        if question[0:counter] in categories:

            tag_finder = 0

            #If we have the question category, tag it
            #Initial tag = index in question list
            while tag_finder < len(categories):

                if question[0:counter] == categories[tag_finder]:

                    tag = tag_finder

                    tag_finder = len(categories) + 1

                else:

                    tag_finder = tag_finder + 1

            counter = len(question) + 1

        else:

            #If we're at the very end and it hasn't been found, kill function
            if counter == len(question) - 1:

                print question , "***Question form not found***"
                print ""

                return

            #Otherwise just hit next substring
            counter = counter + 1


    print "Question:" , question , "Question form: \""+ categories[tag]+ "________?\""
    print ""


#Read text file
with open("q_list.txt", "r") as ins:
    content = []
    for line in ins:
        content.append(line)
        
#Categorize each question in text file
for line in content:
    categorize(line, categories)