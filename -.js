{
    "0": {
        "substeps": [
            {
                "links": [
                    {
                        "fingernails": "http://www.webmd.com/skin-problems-and-treatments/tc/nail-problems-and-injuries-topic-overview"
                    }
                ],
                "text": "Symptoms of acute attack include difficulty talking or walking because of shortness of breath or lips or fingernails turning blue.",
                "type": "911-conditional-list-item"
            }
        ],
        "text": "Call 911",
        "type": "911-conditional"
    },
    "1": {
        "substeps": [
            {
                "conditionals": [
                    "if the person has an individualized asthma action plan from a health care provider"
                ],
                "nonconditionals": "Find out.",
                "text": "Find out if the person has an individualized asthma action plan from a health care provider.",
                "type": "conditional"
            },
            {
                "conditionals": [
                    "If so"
                ],
                "nonconditionals": ", follow its directions for giving asthma medication and seeking medical help for acute asthma attack.",
                "text": "If so, follow its directions for giving asthma medication and seeking medical help for acute asthma attack.",
                "type": "conditional"
            }
        ],
        "text": "1. Follow the Person's Asthma Plan, if Possible",
        "type": "action"
    },
    "2": {
        "substeps": [
            {
                "links": [],
                "text": "Sit the person upright comfortably and loosen tight clothing.",
                "type": "list-item"
            },
            {
                "links": [],
                "text": "If the person has asthma medication, such as an inhaler, assist in using it.",
                "type": "list-item"
            },
            {
                "links": [
                    {
                        "first aid": "http://www.webmd.com/a-to-z-guides/wound-care-10/slideshow-first-aid-essentials"
                    }
                ],
                "text": "If the person doesn't have an inhaler, use one from a first aid kit or borrow someone else's.",
                "type": "list-item"
            }
        ],
        "text": "If the person doesn't have an asthma plan:",
        "type": "list"
    },
    "3": {
        "substeps": [
            {
                "links": [],
                "text": "Remove cap and shake inhaler well.",
                "type": "action"
            },
            {
                "links": [],
                "text": "Insert inhaler into spacer.",
                "type": "action"
            },
            {
                "links": [
                    {
                        "mouth": "http://www.webmd.com/oral-health/anatomy-of-the-mouth"
                    }
                ],
                "text": "Have the person breathe out completely and put mouth tightly around spacer mouthpiece.",
                "type": "info"
            },
            {
                "links": [],
                "text": "Press inhaler once to deliver a puff.",
                "type": "action"
            },
            {
                "links": [
                    {
                        "mouth": "http://www.webmd.com/oral-health/ss/slideshow-mouth-problems"
                    }
                ],
                "text": "Have the person breathe in slowly through the mouth and then hold breath for 10 seconds.",
                "type": "info"
            },
            {
                "links": [],
                "text": "Give a total of four puffs, waiting about a minute between each puff.",
                "type": "action"
            }
        ],
        "text": "3. Use Inhaler With a Spacer, if Possible",
        "type": "action"
    },
    "4": {
        "substeps": [
            {
                "links": [],
                "text": "Remove the inhaler cap and shake well.",
                "type": "action"
            },
            {
                "links": [],
                "text": "Have the person breathe out all the way and seal lips tightly around inhaler mouthpiece.",
                "type": "info"
            },
            {
                "links": [],
                "text": "As the person starts to breathe in slowly, press down on inhaler one time.",
                "type": "info"
            },
            {
                "links": [],
                "text": "The person should keep breathing in as slowly and deeply as possible (about five to seven seconds) and then hold breath for 10 seconds.",
                "type": "info"
            },
            {
                "links": [],
                "text": "Give a total of four puffs, waiting about one minute between each puff.",
                "type": "action"
            }
        ],
        "text": "4. Use Inhaler Without a Spacer, if Necessary",
        "type": "action"
    },
    "5": {
        "conditionals": [
            "if Breathing Is Still a Problem"
        ],
        "nonconditionals": "5. Continue Using Inhaler ",
        "substeps": [
            {
                "links": [
                    {
                        "trouble breathing": "http://www.webmd.com/lung/breathing-problems-causes-tests-treatments"
                    }
                ],
                "text": "After four puffs, wait four minutes.",
                "type": "action"
            },
            {
                "conditionals": [
                    "If the person still has trouble breathing"
                ],
                "nonconditionals": ", give another set of four puffs.",
                "text": "If the person still has trouble breathing, give another set of four puffs.",
                "type": "conditional"
            },
            {
                "action": "If there's still little or no improvement, give four puffs .",
                "loop-condition": "every four minutes until ambulance arrives",
                "text": "If there's still little or no improvement, give four puffs every four minutes until ambulance arrives.",
                "type": "until-conditional"
            },
            {
                "conditionals": [
                    "If the person is having a severe attack"
                ],
                "nonconditionals": ", give up to six to eight puffs every five minutes.",
                "text": "If the person is having a severe attack, give up to six to eight puffs every five minutes.",
                "type": "conditional"
            }
        ],
        "text": "5. Continue Using Inhaler if Breathing Is Still a Problem",
        "type": "conditional"
    },
    "6": {
        "action": "6. Monitor the Person Until Help Arrives",
        "loop-condition": "6 . Monitor the Person Until Help Arrives",
        "substeps": [
            {
                "links": [],
                "text": "Do not mistake drowsiness as a sign of improvement; it could mean asthma is worsening.",
                "type": "info"
            },
            {
                "conditionals": [
                    "if you no longer hear wheezing"
                ],
                "nonconditionals": "Do not assume the person's asthma is improving.",
                "text": "Do not assume the person's asthma is improving if you no longer hear wheezing.",
                "type": "conditional"
            }
        ],
        "text": "6. Monitor the Person Until Help Arrives",
        "type": "until-conditional"
    },
    "7": {
        "substeps": [
            {
                "links": [
                    {
                        "medications": "http://www.webmd.com/drugs/index-drugs.aspx"
                    }
                ],
                "text": "An emergency room doctor will check the severity of the attack and provide treatment, including medications.",
                "type": "info"
            },
            {
                "links": [],
                "text": "The person may be discharged home or hospitalized for further care, depending on response to treatment.",
                "type": "info"
            }
        ],
        "text": "7.",
        "type": "action"
    },
    "8": {
        "substeps": [],
        "text": "Follow Up",
        "type": "action"
    }
}