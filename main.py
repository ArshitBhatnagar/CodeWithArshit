# English Grammar
"""randomizing the sentences"""
import random

subjects = ["I", "we", "you", "he", "she", "it", "they", "the boy", "the girl"]
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
        case "the boy":
            BOYOBJECTIVE_SUBJECT = subject
            BOYPOSSESIVE_SUBJECT = subject + "'s"
        case "the girl":
            GIRLOBJECTIVE_SUBJECT = subject
            GIRLPOSSESIVE_SUBJECT = subject + "'s"

objective_subjects = [IOBJECTIVE_SUBJECT, WEOBJECTIVE_SUBJECT, YOUOBJECTIVE_SUBJECT, HEOBJECTIVE_SUBJECT, SHEOBJECTIVE_SUBJECT, ITOBJECTIVE_SUBJECT, THEYOBJECTIVE_SUBJECT, BOYOBJECTIVE_SUBJECT, GIRLOBJECTIVE_SUBJECT]
objective_subjects = [IPOSSESIVE_SUBJECT, WEPOSSESIVE_SUBJECT, YOUPOSSESIVE_SUBJECT, HEPOSSESIVE_SUBJECT, SHEPOSSESIVE_SUBJECT, ITPOSSESIVE_SUBJECT, THEYPOSSESIVE_SUBJECT, BOYPOSSESIVE_SUBJECT, GIRLPOSSESIVE_SUBJECT]

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "acquire",
      "appear", "announce", "apply", "arrest", "attend", "attract", "avoid"]

prepositions = ["in", "on", "up"]

adverbs = ["genlty", "happily", "sadly", "quietly", "slowly"]

marks = [".", "?", ",", "!"]

# randomizing
random_subject = random.randint(1, len(subjects))
random_v1 = random.randint(1, len(v1))
random_preposition = random.randint(1, len(prepositions))

# applying random
subject = subjects[random_subject -1]
verb1 = v1[random_v1 -1]
preposition = prepositions[random_preposition -1]

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

match subject:
    case "I":
        OBJECTIVE_SUBJECT = IOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = IPOSSESIVE_SUBJECT
    case "we":
        OBJECTIVE_SUBJECT = WEOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = WEPOSSESIVE_SUBJECT
    case "you":
        OBJECTIVE_SUBJECT = YOUOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = YOUPOSSESIVE_SUBJECT
    case "he":
        OBJECTIVE_SUBJECT = HEOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = HEPOSSESIVE_SUBJECT
    case "she":
        OBJECTIVE_SUBJECT = SHEOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = SHEPOSSESIVE_SUBJECT
    case "it":
        OBJECTIVE_SUBJECT = ITOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = ITPOSSESIVE_SUBJECT
    case "they":
        OBJECTIVE_SUBJECT = THEYOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = THEYPOSSESIVE_SUBJECT
    case "the boy":
        OBJECTIVE_SUBJECT = BOYOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = BOYPOSSESIVE_SUBJECT
    case "the girl":
        OBJECTIVE_SUBJECT = GIRLOBJECTIVE_SUBJECT
        POSSESIVE_SUBJECT = GIRLPOSSESIVE_SUBJECT

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
        objects = ["the situation", "soil", f"{POSSESIVE_SUBJECT} policy"]
    case "acquire":
        objects = ["money", "books", "control", f"reputation from {subject}"]
    case "announce":
        objects = ["result", "winnner", f"{POSSESIVE_SUBJECT} retirement", f"{POSSESIVE_SUBJECT} plan"]
    case "apply":
        objects = ["sunscreen"]
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

    case "we":
        FUTURE_HELPING = "shall"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False

    case "you":
        FUTURE_HELPING = "will"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False

    case "they":
        FUTURE_HELPING = "will"
        TO_HAVE = "have"
        PAST_HELPING = "were"
        TO_BE = "are"
        SINGULAR = False

    case _:
        FUTURE_HELPING = "will"
        TO_HAVE = "has"
        PAST_HELPING = "was"
        TO_BE = "is"
        SINGULAR = True

if SINGULAR:
    if verb1[-1]=="y":
        singular_verb1 = verb1[0: -2] + "ies"
    else:
        singular_verb1 = verb1 + "s"
elif not SINGULAR:
    singular_verb1 = verb1

# Execution
# need to remove space before mark

choice = input("Enter which type of sentence (tense) do you want to generate : ")
match choice.lower():
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
        RANDOM_SENTENCE = f"{choice} is not a type of tense"

RANDOM_SENTENCE = RANDOM_SENTENCE.strip() + marks[0]
print(RANDOM_SENTENCE)

# inputing the sentence and outputing the type and tense of sentence
