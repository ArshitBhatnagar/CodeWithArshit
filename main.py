# English Grammar
"""randomizing the sentences"""
import random
import re

subjects = ["I", "we", "you", "he", "she", "it", "they", "boy", "girl"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)
for subject in subjects:
    match subject:
        case "I":
            IOBJECTIVE_SUBJECT = "me"
            IPOSSESSIVE_SUBJECT = "mine"
        case "we":
            WEOBJECTIVE_SUBJECT = "us"
            WEPOSSESSIVE_SUBJECT = "our"
        case "you":
            YOUOBJECTIVE_SUBJECT = "you"
            YOUPOSSESSIVE_SUBJECT = "your"
        case "he":
            HEOBJECTIVE_SUBJECT = "him"
            HEPOSSESSIVE_SUBJECT = "his"
        case "she":
            SHEOBJECTIVE_SUBJECT = "her"
            SHEPOSSESSIVE_SUBJECT = "her"
        case "it":
            ITOBJECTIVE_SUBJECT = "it"
            ITPOSSESSIVE_SUBJECT = "it\'s"
        case "they":
            THEYOBJECTIVE_SUBJECT = "them"
            THEYPOSSESSIVE_SUBJECT = "their"
        case "boy":
            BOYOBJECTIVE_SUBJECT = subject
            BOYPOSSESSIVE_SUBJECT = subject + "\'s"
        case "girl":
            GIRLOBJECTIVE_SUBJECT = subject
            GIRLPOSSESSIVE_SUBJECT = subject + "\'s"

objective_subjects = [IOBJECTIVE_SUBJECT, WEOBJECTIVE_SUBJECT, YOUOBJECTIVE_SUBJECT, HEOBJECTIVE_SUBJECT, SHEOBJECTIVE_SUBJECT, ITOBJECTIVE_SUBJECT, THEYOBJECTIVE_SUBJECT, BOYOBJECTIVE_SUBJECT, GIRLOBJECTIVE_SUBJECT]
POSSESSIVE_subjects = [IPOSSESSIVE_SUBJECT, WEPOSSESSIVE_SUBJECT, YOUPOSSESSIVE_SUBJECT, HEPOSSESSIVE_SUBJECT, SHEPOSSESSIVE_SUBJECT, ITPOSSESSIVE_SUBJECT, THEYPOSSESSIVE_SUBJECT, BOYPOSSESSIVE_SUBJECT, GIRLPOSSESSIVE_SUBJECT]

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "acquire",
      "appear", "announce", "apply", "arrest", "attend", "attract", "avoid"]

prepositions = ["in", "on", "up"]

adverbs = ["gently", "happily", "sadly", "quietly", "slowly"]

marks = [".", "?", ",", "!"]

articles = ["a", "an", "the"]

# randomizing
random_subject = random.randint(1, len(subjects))
random_v1 = random.randint(1, len(v1))
random_preposition = random.randint(1, len(prepositions))
random_articles = random.randint(1, len(articles))
RANDOM_OBJECTIVE_SUBJECT = random.randint(1, len(objective_subjects))
RANDOM_POSSESSIVE_SUBJECT = random.randint(1, len(POSSESSIVE_subjects))

# applying random
subject = subjects[random_subject -1]
verb1 = v1[random_v1 -1]
preposition = prepositions[random_preposition -1]
article = articles[random_articles -1]
OBJECTIVE_SUBJECT = objective_subjects[RANDOM_OBJECTIVE_SUBJECT - 1]
POSSESSIVE_SUBJECT = objective_subjects[RANDOM_POSSESSIVE_SUBJECT - 1]

# initializing VERB2, VERB3 and verb4
match verb1:
# removing e before abuse as it's second form will be abused

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
        objects = ["the situation", "the soil", f"{POSSESSIVE_SUBJECT} policy"]
    case "acquire":
        objects = ["the money", "the books", "the control", f"reputation from {subject}"]
    case "announce":
        objects = ["the result", "the winner", f"{POSSESSIVE_SUBJECT} retirement", f"{POSSESSIVE_SUBJECT} plan"]
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
# need to add since/for in perfect progressive
def generate_sentence():
    """Generate the type of sentence that the user has inputted"""
    tense = input("tense : ")
    types = input("Type (default:Affirmative) : ")
    if types == "":
        types = "Affirmative"
    match types.lower():
        case "affirmative":
            match tense.lower():
                case "present indefinite":
                    random_sentence = f"{subject.capitalize()} {singular_verb1} {OBJ}"
                case "past indefinite":
                    random_sentence = f"{subject.capitalize()} {VERB2} {OBJ}"
                case "future indefinite":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} {verb1} {OBJ}"

                case "present progressive":
                    random_sentence = f"{subject.capitalize()} {TO_BE} {verb4} {OBJ}"
                case "past progressive":
                    random_sentence = f"{subject.capitalize()} {PAST_HELPING} {verb4} {OBJ}"
                case "future progressive":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} be {verb4} {OBJ}"

                case "present perfect":
                    random_sentence = f"{subject.capitalize()} {TO_HAVE} {VERB3} {OBJ}"
                case "past perfect":
                    random_sentence = f"{subject.capitalize()} had {VERB3} {OBJ}"
                case "future perfect":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} have {VERB3} {OBJ}"

                case "present perfect progressive":
                    random_sentence = f"{subject.capitalize()} {TO_HAVE} been {verb4} {OBJ}"
                case "past perfect progressive":
                    random_sentence = f"{subject.capitalize()} had been {verb4} {OBJ}"
                case "future perfect progressive":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} have been {verb4} {OBJ}"

                case _:
                    random_sentence = f"{tense} is not a type of tense!!!"

        case "negative":
            match tense.lower():
                case "present indefinite":
                    random_sentence = f"{subject.capitalize()} {TO_DO} not {verb1} {OBJ}"
                case "past indefinite":
                    random_sentence = f"{subject.capitalize()} did not {VERB2} {OBJ}"
                case "future indefinite":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} not {verb1} {OBJ}"

                case "present progressive":
                    random_sentence = f"{subject.capitalize()} {TO_BE} not {verb4} {OBJ}"
                case "past progressive":
                    random_sentence = f"{subject.capitalize()} {PAST_HELPING} not {verb4} {OBJ}"
                case "future progressive":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} not be {verb4} {OBJ}"

                case "present perfect":
                    random_sentence = f"{subject.capitalize()} {TO_HAVE} not {VERB3} {OBJ}"
                case "past perfect":
                    random_sentence = f"{subject.capitalize()} had not {VERB3} {OBJ}"
                case "future perfect":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} not have {VERB3} {OBJ}"

                case "present perfect progressive":
                    random_sentence = f"{subject.capitalize()} {TO_HAVE} not been {verb4} {OBJ}"
                case "past perfect progressive":
                    random_sentence = f"{subject.capitalize()} had not been {verb4} {OBJ}"
                case "future perfect progressive":
                    random_sentence = f"{subject.capitalize()} {FUTURE_HELPING} have not been {verb4} {OBJ}"

                case _:
                    random_sentence = f"{tense} is not a type of tense!!!"

        case "interrogative":
            match tense.lower():
                case "present indefinite":
                    random_sentence = f"{TO_DO.capitalize()} {subject} {verb1} {OBJ}"
                case "past indefinite":
                    random_sentence = f"Did {subject} {VERB2} {OBJ}"
                case "future indefinite":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} {verb1} {OBJ}"

                case "present progressive":
                    random_sentence = f"{TO_BE.capitalize()} {subject} {verb4} {OBJ}"
                case "past progressive":
                    random_sentence = f"{PAST_HELPING.capitalize()} {subject} {verb4} {OBJ}"
                case "future progressive":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} be {verb4} {OBJ}"

                case "present perfect":
                    random_sentence = f"{TO_HAVE.capitalize()} {subject} {VERB3} {OBJ}"
                case "past perfect":
                    random_sentence = f"Had {subject} {VERB3} {OBJ}"
                case "future perfect":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} have {VERB3} {OBJ}"

                case "present perfect progressive":
                    random_sentence = f"{TO_HAVE.capitalize()} {subject} been {verb4} {OBJ}"
                case "past perfect progressive":
                    random_sentence = f"Had {subject} been {verb4} {OBJ}"
                case "future perfect progressive":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} have been {verb4} {OBJ}"

                case _:
                    random_sentence = f"{tense} is not a type of tense!!!"

        case "negative interrogative":
            match tense.lower():
                case "present indefinite":
                    random_sentence = f"{TO_DO.capitalize()} {subject} not {verb1} {OBJ}"
                case "past indefinite":
                    random_sentence = f"Did {subject} not {VERB2} {OBJ}"
                case "future indefinite":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} not {verb1} {OBJ}"

                case "present progressive":
                    random_sentence = f"{TO_BE.capitalize()} {subject} not {verb4} {OBJ}"
                case "past progressive":
                    random_sentence = f"{PAST_HELPING.capitalize()} {subject} not {verb4} {OBJ}"
                case "future progressive":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} not be {verb4} {OBJ}"

                case "present perfect":
                    random_sentence = f"{TO_HAVE.capitalize()} {subject} not {VERB3} {OBJ}"
                case "past perfect":
                    random_sentence = f"Had {subject} not {VERB3} {OBJ}"
                case "future perfect":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} not have {VERB3} {OBJ}"

                case "present perfect progressive":
                    random_sentence = f"{TO_HAVE.capitalize()} {subject} not been {verb4} {OBJ}"
                case "past perfect progressive":
                    random_sentence = f"Had {subject} not been {verb4} {OBJ}"
                case "future perfect progressive":
                    random_sentence = f"{FUTURE_HELPING.capitalize()} {subject} have not been {verb4} {OBJ}"

                case _:
                    random_sentence = f"{tense} is not a type of tense!!!"

        case _:
            random_sentence = f"{types} is not a type of sentence!!!"
    random_sentence = random_sentence.strip() + marks[0]
    print(random_sentence)

def finding_tense():
    """Find the tense of the sentence inputted from user"""

    global sentence
    global tense
    global types

# inputting the sentence and outputting the type and tense of sentence
    sentence = input("Sentence : ")
    sentence = sentence.lower()

# converting con
    if "\'" in sentence:
        if "n\'t" in sentence:
            sentence = sentence.replace("n\'t", " not")
        if "\'s" in sentence:
            if "been" in sentence:
                sentence = sentence.replace("\'s", " has")
            else:
                sentence = sentence.replace("\'s", " is")
        if "\'ll" in sentence:
            if "i" in sentence or "we" in sentence:
                sentence = sentence.replace("\'ll", " shall")
            else:
                sentence = sentence.replace("\'ll", " will")
        if "\'d" in sentence:
            sentence = sentence.replace("\'d", " had")
        if "\'m" in sentence:
            sentence = sentence.replace("\'m", " am")
        if "\'ve" in sentence:
            sentence = sentence.replace("\'ve", " have")
        if "\'re" in sentence:
            sentence = sentence.replace("\'re", " are")

        print("Simpler form :", sentence)

# listing the type of sentence
    if "not" in sentence:
        types = "Negative Interrogative" if "?" in sentence else "Negative"

    else:
        types = "Interrogative" if "?" in sentence else "Affirmative"

# listing the tense of sentence
    match types:
        case "Affirmative":
            if re.search(r"(will|shall) have been", sentence) is not None and "ing" in sentence:
                tense = "Future perfect progressive"
            elif "had been" in sentence and "ing" in sentence:
                tense = "Past perfect progressive"
            elif re.search(r"(has|have) been", sentence) is not None and "ing" in sentence:
                tense = "Present perfect progressive"

            elif re.search(r"(will|shall) have", sentence) is not None:
                tense = "Future perfect"
            elif "had" in sentence:
                tense = "Past perfect"
            elif re.search(r"have|has", sentence) is not None:
                tense = "Present perfect"

            elif re.search(r"(will|shall) be", sentence) is not None and "ing" in sentence:
                tense = "Future progressive"
            elif re.search(r"was|were", sentence) is not None and "ing" in sentence:
                tense = "Past progressive"
            elif re.search(r"is|am|are", sentence) is not None and "ing" in sentence:
                tense = "Present progressive"

            elif re.search(r"will|shall", sentence) is not None:
                tense = "Future indefinite"
            elif re.search(r"ed|ran", sentence) is not None:
                tense = "Past indefinite"
            else:
                tense = "Present indefinite"

        case "Negative":
            if re.search(r"(will|shall) not have been", sentence) is not None and "ing" in sentence:
                tense = "Future perfect progressive"
            elif "had not been" in sentence and "ing" in sentence:
                tense = "Past perfect progressive"
            elif re.search(r"(has|have) not been", sentence) is not None and "ing" in sentence:
                tense = "Present perfect progressive"

            elif re.search(r"(will|shall) not have", sentence) is not None:
                tense = "Future perfect"
            elif "had not" in sentence:
                tense = "Past perfect"
            elif re.search(r"(have|has) not", sentence) is not None:
                tense = "Present perfect"

            elif re.search(r"(will|shall) not be", sentence) is not None and "ing" in sentence:
                tense = "Future progressive"
            elif re.search(r"(was|were) not", sentence) is not None and "ing" in sentence:
                tense = "Past progressive"
            elif re.search(r"(is|am|are) not", sentence) is not None and "ing" in sentence:
                tense = "Present progressive"

            elif re.search(r"(will|shall) not", sentence) is not None:
                tense = "Future indefinite"
            elif re.search(r"ed|ran", sentence) is not None:
                tense = "Past indefinite"
            else:
                tense = "Present indefinite"

        case "Interrogative":
            if re.search(r"will|shall", sentence) is not None and "ing" in sentence and "have been" in sentence:
                tense = "Future perfect progressive"
            elif "had" in sentence and "ing" in sentence and "been" in sentence:
                tense = "Past perfect progressive"
            elif re.search(r"has|have", sentence) is not None and "ing" in sentence and "been" in sentence:
                tense = "Present perfect progressive"

            elif re.search(r"will|shall", sentence) is not None and "have" in sentence:
                tense = "Future perfect"
            elif "had" in sentence:
                tense = "Past perfect"
            elif re.search(r"(have|has)", sentence) is not None:
                tense = "Present perfect"

            elif re.search(r"will|shall", sentence) is not None and "ing" in sentence and "be" in sentence:
                tense = "Future progressive"
            elif re.search(r"was|were", sentence) is not None and "ing" in sentence:
                tense = "Past progressive"
            elif re.search(r"(is|am|are)", sentence) is not None and "ing" in sentence:
                tense = "Present progressive"

            elif re.search(r"will|shall", sentence) is not None:
                tense = "Future indefinite"
            elif "did" in sentence:
                tense = "Past indefinite"
            else:
                tense = "Present indefinite"

        case "Negative Interrogative":
            if re.search(r"will|shall", sentence) is not None and "ing" in sentence and "have not been" in sentence:
                tense = "Future perfect progressive"
            elif "had" in sentence and "ing" in sentence and "not been" in sentence:
                tense = "Past perfect progressive"
            elif re.search(r"has|have", sentence) is not None and "ing" in sentence and "not been" in sentence:
                tense = "Present perfect progressive"

            elif re.search(r"will|shall", sentence) is not None and "not have" in sentence:
                tense = "Future perfect"
            elif "had" in sentence:
                tense = "Past perfect"
            elif re.search(r"have|has", sentence) is not None:
                tense = "Present perfect"

            elif re.search(r"will|shall", sentence) is not None and "ing" in sentence and "not be" in sentence:
                tense = "Future progressive"
            elif re.search(r"was|were", sentence) is not None and "ing" in sentence:
                tense = "Past progressive"
            elif re.search(r"is|am|are", sentence) is not None and "ing" in sentence:
                tense = "Present progressive"

            elif re.search(r"will|shall", sentence) is not None:
                tense = "Future indefinite"
            elif "did" in sentence:
                tense = "Past indefinite"
            else:
                tense = "Present indefinite"

    print("tense :", tense)
    print("Type :", types)

def convert_active():
    """Converts active to passive"""
    finding_tense()

    global sentence
    global tense
    global types

    match types.lower():
        case "affirmative":
            match tense.lower():
                case "present indefinite":
                    pass
                case "present progressive":
                    pass
                case "present perfect":
                    pass
                case "present perfect progressive":
                    pass

                case "past indefinite":
                    pass
                case "past progressive":
                    pass
                case "past perfect":
                    pass
                case "past perfect progressive":
                    pass

                case "future indefinite":
                    pass
                case "future progressive":
                    pass
                case "future perfect":
                    pass
                case "future perfect progressive":
                    pass

        case "negative":
            pass
        case "interrogative":
            pass
        case "negative interrogative":
            pass

choice = input("What would you want to do : ")
match choice.lower():
    case "generate sentence":
        generate_sentence()

    case "finding tense":
        finding_tense()

    case "convert":
        convert_active()

    case "testing":
        reply = input("Which part you are testing : ")
        match reply:
            case "generate sentence":
                while True:
                    generate_sentence()
                    cut = input(">>")
                    if cut == "quit":
                        break

            case "finding tense":
                while True:
                    finding_tense()
                    cut = input(">>")
                    if cut == "quit":
                        break

    case _:
        print(f"Sorry, I am not able to {choice}!")

# need to generate passive sentence also
# and convert active to passive and passive to active

# need to convert type of sentence also inputted by the user
