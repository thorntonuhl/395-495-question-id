import pickle

# categories = [
#                       "What if",
#                       "Should I",
#                       "What should I do if",
#                       "How do I",
#                       "What is",
#                       "How can I tell if",
#                       "Do I",
#                       "What do I do if",
#                       "Can I give them",
#                       "What are the signs and symptoms of",
#                       "How do I treat",
#                       "When should I call 911?",
#                       "Should I try",
#                       "How long should I",
#                       "How will I know if",
#                       "What does"
#                     ]

categories = [
                      "What if",
                      "Should I",
                      "What should I do",
                      "How do I",
                      "What is",
                      "How can I tell",
                      "Do I",
                      "What do I",
                      "Can I",
                      "What are",
                      "When",
                      "Should I try",
                      "How long should I",
                      "How will I know",
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

                print question , "***Question form not found***\n"

                return question, "Uncategorized"

            #Otherwise just hit next substring
            counter = counter + 1


    print "Question:" , question , "Question form: \""+ categories[tag]+ "________?\"\n"
    return question, categories[tag]

#Skeleton for auto_category fn
def auto_category(question):

    char_counter = 0

    question_form = ""

    space_save1 = 0

    space_save2 = 0

    new_word = ""

    #Iterate through question characters
    while char_counter < len(question):

        if question[char_counter] == ' ':

            space_save2 = char_counter
            
            #Isolate each word, can define set of rules for any word
            new_word = question[space_save1:space_save2]

            #Rules for 'of' - ignore what comes before
            if new_word == "of":

                question_form = question[0:space_save2]

                return question_form

            else:

                space_save1 = space_save2 + 1

        #Rules for comma, ignore situational setup (what comes before
        if question[char_counter] == ",":

            question_form = question[(char_counter+2):len(question)]

            return question_form

        #Continue iteration if nothing matches
        char_counter = char_counter + 1


    return "Categorization failed :("

     

#print auto_category("What sort of medication will they use?")
#print auto_category("If a bone looks unnatural or dislocated, should I put it back in its place?")
                                   
'''
#Read text file
with open("q_list.txt", "r") as ins:
    content = []
    for line in ins:
        content.append(line)

# FOR LATER: abstract this data structure to a nested dictionary
categorized_questions = {}
categorized_questions["Uncategorized"] = []
for c in categories:
    categorized_questions[c] = []


#Categorize each question in text file
with open("categories.txt", "w") as out:
    for line in content:
        q,k = categorize(line, categories)
        categorized_questions[k].append(q)


#pickle.dump(categorized_questions, open("categorized_questions.pkl", "wb"))
#print categorized_questions
'''
