# English Grammar
"""randomizing the sentences"""
import random

subjects = ["I", "we", "you", "he", "she", "it", "they", "boy", "girl"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)
for subject in subjects:
    match subject:
        case "I":
            IOBJECTIVE_SUBJECT = "me"
            IPOSSESIVE_SUBJECT = "mine"
        case "we":
            WEOBJECTIVE_SUBJECT = "us"
            WEPOSSESIVE_SUBJECT = "our"
        case "you":
            YOUOBJECTIVE_SUBJECT = "you"
            YOUPOSSESIVE_SUBJECT = "your"
        case "he":
            HEOBJECTIVE_SUBJECT = "him"
            HEPOSSESIVE_SUBJECT = "his"
        case "she":
            SHEOBJECTIVE_SUBJECT = "her"
            SHEPOSSESIVE_SUBJECT = "her"
        case "it":
            ITOBJECTIVE_SUBJECT = "it"
            ITPOSSESIVE_SUBJECT = "it's"
        case "they":
            THEYOBJECTIVE_SUBJECT = "them"
            THEYPOSSESIVE_SUBJECT = "their"
        case "boy":
            BOYOBJECTIVE_SUBJECT = subject
            BOYPOSSESIVE_SUBJECT = subject + "'s"
        case "girl":
            GIRLOBJECTIVE_SUBJECT = subject
            GIRLPOSSESIVE_SUBJECT = subject + "'s"

objective_subjects = [IOBJECTIVE_SUBJECT, WEOBJECTIVE_SUBJECT, YOUOBJECTIVE_SUBJECT, HEOBJECTIVE_SUBJECT, SHEOBJECTIVE_SUBJECT, ITOBJECTIVE_SUBJECT, THEYOBJECTIVE_SUBJECT, BOYOBJECTIVE_SUBJECT, GIRLOBJECTIVE_SUBJECT]
possesive_subjects = [IPOSSESIVE_SUBJECT, WEPOSSESIVE_SUBJECT, YOUPOSSESIVE_SUBJECT, HEPOSSESIVE_SUBJECT, SHEPOSSESIVE_SUBJECT, ITPOSSESIVE_SUBJECT, THEYPOSSESIVE_SUBJECT, BOYPOSSESIVE_SUBJECT, GIRLPOSSESIVE_SUBJECT]

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "acquire",
      "appear", "announce", "apply", "arrest", "attend", "attract", "avoid"]

prepositions = ["in", "on", "up"]

adverbs = ["genlty", "happily", "sadly", "quietly", "slowly"]

marks = [".", "?", ",", "!"]

articles = ["a", "an", "the"]

# randomizing
random_subject = random.randint(1, len(subjects))
random_v1 = random.randint(1, len(v1))
random_preposition = random.randint(1, len(prepositions))
random_articles = random.randint(1, len(articles))
RANDOM_OBJECTIVE_SUBJECT = random.randint(1, len(objective_subjects))
RANDOM_POSSESIVE_SUBJECT = random.randint(1, len(possesive_subjects))

# applying random
subject = subjects[random_subject -1]
verb1 = v1[random_v1 -1]
preposition = prepositions[random_preposition -1]
article = articles[random_articles -1]
OBJECTIVE_SUBJECT = objective_subjects[RANDOM_OBJECTIVE_SUBJECT - 1]
POSSESIVE_SUBJECT = objective_subjects[RANDOM_POSSESIVE_SUBJECT - 1]

# initializing VERB2, VERB3 and verb4
match verb1:
# removing e before abuse as it's second form will be abused but in this code it will be abuseed

    case "run":
        VERB2 = "ran"
    case _:
        if verb1[-1]=="e":
            v=verb1[0: -1]
            v_ing = verb1[0: -1]
        elif verb1[-1]=="y":
            v = verb1[0: -1] + "i"
            v_ing = verb1[0: -1]
        else:
            v = verb1
            v_ing = verb1
        VERB2 = v + "ed"
        verb4 = v_ing + "ing"

match verb1:
    case "ran":
        VERB3 = "run"
    case _:
        VERB3 = VERB2

match verb1:
    case "add":
        objects = [f"{random.randint(1, 100)} and {random.randint(1, 100)}"]
    case "allow":
        objects = [OBJECTIVE_SUBJECT]
    case "act":
        objects = ["the play", "the drama"]
    case "ask":
        objects = [OBJECTIVE_SUBJECT]
    case "abuse":
        objects = [OBJECTIVE_SUBJECT]
    case "amend":
        objects = ["the situation", "the soil", f"{POSSESIVE_SUBJECT} policy"]
    case "acquire":
        objects = ["the money", "the books", "the control", f"reputation from {subject}"]
    case "announce":
        objects = ["the result", "the winnner", f"{POSSESIVE_SUBJECT} retirement", f"{POSSESIVE_SUBJECT} plan"]
    case "apply":
        objects = ["the sunscreen"]
    case "arrest":
        objects = [OBJECTIVE_SUBJECT]
    case "attend":
        objects = ["the meeting", "the class", "the party"]
    case "attract":
        objects = [OBJECTIVE_SUBJECT]
    case "avoid":
        objects = [OBJECTIVE_SUBJECT, "the question"]
    case _:
        objects = []
if objects:
    if len(objects) == 1:
        OBJ = objects[0]
    else:
        random_object = random.randint(1, len(objects))
        OBJ = objects[random_object -1]
else:
    OBJ = ""
match subject:
    case "I":
        FUTURE_HELPING = "shall"
        TO_HAVE = "have"
        PAST_HELPING = "was"
        TO_BE = "am"
        SINGULAR = False
        TO_DO = "do"

    case "we":
        FUTURE_HELPING = "shall"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False
        TO_DO = "do"

    case "you":
        FUTURE_HELPING = "will"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False
        TO_DO = "do"

    case "they":
        FUTURE_HELPING = "will"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False
        TO_DO = "do"

    case "boy":
        FUTURE_HELPING = "will"
        TO_HAVE = "has"
        PAST_HELPING = "was"
        TO_BE = "is"
        SINGULAR = True
        TO_DO = "does"
        subject = articles[2] + " " + subject

    case "girl":
        FUTURE_HELPING = "will"
        TO_HAVE = "has"
        PAST_HELPING = "was"
        TO_BE = "is"
        SINGULAR = True
        TO_DO = "does"
        subject = articles[2] + " " + subject

    case _:
        FUTURE_HELPING = "will"
        TO_HAVE = "has"
        PAST_HELPING = "was"
        TO_BE = "is"
        SINGULAR = True
        TO_DO = "does"

if SINGULAR:
    if verb1[-1]=="y":
        singular_verb1 = verb1[0: -2] + "ies"
    else:
        singular_verb1 = verb1 + "s"
elif not SINGULAR:
    singular_verb1 = verb1

# Execution
choice = input("What would you want to do : ")
match choice.lower():
    case "generate sentence":
        tense = input("Tense : ")
        TYPES = input("Type (default:Affirmative) : ")
        if TYPES == "":
            TYPES = "Affirmative"
        match TYPES.lower():

            case "affirmative":
                match tense.lower():
                    case "present indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {singular_verb1} {OBJ}"
                    case "past indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {VERB2} {OBJ}"
                    case "future indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} {verb1} {OBJ}"

                    case "present progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_BE} {verb4} {OBJ}"
                    case "past progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {PAST_HELPING} {verb4} {OBJ}"
                    case "future progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} be {verb4} {OBJ}"

                    case "present perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} {VERB3} {OBJ}"
                    case "past perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} had {VERB3} {OBJ}"
                    case "future perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} have {VERB3} {OBJ}"

                    case "present perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} been {verb4} {OBJ}"
                    case "past perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} had been {verb4} {OBJ}"
                    case "future perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} have been {verb4} {OBJ}"

                    case _:
                        RANDOM_SENTENCE = f"{tense} is not a type of tense!!!"

            case "negative":
                match tense.lower():
                    case "present indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_DO} not {verb1} {OBJ}"
                    case "past indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} did not {VERB2} {OBJ}"
                    case "future indefinite":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} not {verb1} {OBJ}"

                    case "present progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_BE} not {verb4} {OBJ}"
                    case "past progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {PAST_HELPING} not {verb4} {OBJ}"
                    case "future progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} not be {verb4} {OBJ}"

                    case "present perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} not {VERB3} {OBJ}"
                    case "past perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} had not {VERB3} {OBJ}"
                    case "future perfect":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} not have {VERB3} {OBJ}"

                    case "present perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} not been {verb4} {OBJ}"
                    case "past perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} had not been {verb4} {OBJ}"
                    case "future perfect progressive":
                        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} have not been {verb4} {OBJ}"

                    case _:
                        RANDOM_SENTENCE = f"{tense} is not a type of tense!!!"

            case "interrogative":
                match tense.lower():
                    case "present indefinite":
                        RANDOM_SENTENCE = f"{TO_DO.capitalize()} {subject} {verb1} {OBJ}"
                    case "past indefinite":
                        RANDOM_SENTENCE = f"Did {subject} {VERB2} {OBJ}"
                    case "future indefinite":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} {verb1} {OBJ}"

                    case "present progressive":
                        RANDOM_SENTENCE = f"{TO_BE.capitalize()} {subject} {verb4} {OBJ}"
                    case "past progressive":
                        RANDOM_SENTENCE = f"{PAST_HELPING.capitalize()} {subject} {verb4} {OBJ}"
                    case "future progressive":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} be {verb4} {OBJ}"

                    case "present perfect":
                        RANDOM_SENTENCE = f"{TO_HAVE.capitalize()} {subject} {VERB3} {OBJ}"
                    case "past perfect":
                        RANDOM_SENTENCE = f"Had {subject} {VERB3} {OBJ}"
                    case "future perfect":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} have {VERB3} {OBJ}"

                    case "present perfect progressive":
                        RANDOM_SENTENCE = f"{TO_HAVE.capitalize()} {subject} been {verb4} {OBJ}"
                    case "past perfect progressive":
                        RANDOM_SENTENCE = f"Had {subject} been {verb4} {OBJ}"
                    case "future perfect progressive":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} have been {verb4} {OBJ}"

                    case _:
                        RANDOM_SENTENCE = f"{tense} is not a type of tense!!!"

            case "negative interrogative":
                match tense.lower():
                    case "present indefinite":
                        RANDOM_SENTENCE = f"{TO_DO.capitalize()} {subject} not {verb1} {OBJ}"
                    case "past indefinite":
                        RANDOM_SENTENCE = f"Did {subject} not {VERB2} {OBJ}"
                    case "future indefinite":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} not {verb1} {OBJ}"

                    case "present progressive":
                        RANDOM_SENTENCE = f"{TO_BE.capitalize()} {subject} not {verb4} {OBJ}"
                    case "past progressive":
                        RANDOM_SENTENCE = f"{PAST_HELPING.capitalize()} {subject} not {verb4} {OBJ}"
                    case "future progressive":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} not be {verb4} {OBJ}"

                    case "present perfect":
                        RANDOM_SENTENCE = f"{TO_HAVE.capitalize()} {subject} not {VERB3} {OBJ}"
                    case "past perfect":
                        RANDOM_SENTENCE = f"Had {subject} not {VERB3} {OBJ}"
                    case "future perfect":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} not have {VERB3} {OBJ}"

                    case "present perfect progressive":
                        RANDOM_SENTENCE = f"{TO_HAVE.capitalize()} {subject} not been {verb4} {OBJ}"
                    case "past perfect progressive":
                        RANDOM_SENTENCE = f"Had {subject} not been {verb4} {OBJ}"
                    case "future perfect progressive":
                        RANDOM_SENTENCE = f"{FUTURE_HELPING.capitalize()} {subject} have not been {verb4} {OBJ}"

                    case _:
                        RANDOM_SENTENCE = f"{tense} is not a type of tense!!!"

            case _:
                RANDOM_SENTENCE = f"{TYPES} is not a type of sentence!!!"
        RANDOM_SENTENCE = RANDOM_SENTENCE.strip() + marks[0]
        print(RANDOM_SENTENCE)

    case "finding tense":
# inputing the sentence and outputing the type and tense of sentence
        sentence = input("Sentence : ")
        if (sentence.find("will have been") != -1 or sentence.find("shall have been") != -1) and sentence.find("ing") != -1:
            TENSE = "Future perfect progressive"
        elif sentence.find("had been") != -1 and sentence.fing("ing") != -1:
            TENSE = "Past perfect progressive"
        elif (sentence.find("have been") != -1 or sentence.find("has been") != -1) and sentence.find("ing") != -1:
            TENSE = "Present perfect progressive"

        elif sentence.find("will have") != -1 or sentence.find("shall have") != -1:
            TENSE = "Future perfect"
        elif sentence.find("had") != -1:
            TENSE = "Past perfect"
        elif sentence.find("have") != -1 or sentence.find("has") != -1:
            TENSE = "Present perfect"

        elif (sentence.find("will be") != -1 or sentence.find("shall be") != -1) and sentence.find("ing") != -1:
            TENSE = "Future progressive"
        elif (sentence.find("was") != -1 or sentence.find("were") != -1) and sentence.find("ing") != -1:
            TENSE = "Past progressive"
        elif (sentence.find("is") != -1 or sentence.find("am") != -1 or sentence.find("are") != -1) and sentence.find("ing") != -1:
            TENSE = "Present progressive"

        elif sentence.find("will") != -1 or sentence.find("shall") != -1:
            TENSE = "Future indefinite"
        elif sentence.find("ed") != -1 or sentence.find("ran") != -1:
            TENSE = "Past indefinite"
        else:
            TENSE = "Present indefinite"

        print(TENSE)
 # Want to output the type of sentence also

 # need to generate passive sentence also
 # and convert active to passive and passive to active
