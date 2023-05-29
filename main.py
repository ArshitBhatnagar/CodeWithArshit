# English Grammar
"""randomizing the sentences"""
import random

subjects = ["I", "we", "you", "he", "she", "it", "they"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "aquire",
      "appear", "anounce", "apply", "arrest", "attend", "attract", "avoid"]

v2 = []
v3 = []
v4 = []

# initializing v2, v3 and v4
for v in v1:
# removing e before abuse as it's second form will be abused but in this code it will be abuseed
    if v[-1]=="e":
        v=v[0:len(v)-1]
    match v:
        case "run":
            v2.append("ran")
        case _:
            v2.append(v + "ed")
            v4.append(v + "ing")

for v in v2:
    match v:
        case "ran":
            v3.append("run")
        case _:
            v3.append(v)
prepositions = ["in", "on", "up"]

adverbs = ["genlty", "happily", "sadly", "quietly", "slowly"]

marks = [".", "?", ",", "!"]

# randomizing
random_subject = random.randint(0, len(subjects)-1)
random_v1 = random.randint(0, len(v1)-1)
random_v2 = random.randint(0, len(v2)-1)
random_v3 = random.randint(0, len(v3)-1)
random_v4 = random.randint(0, len(v4)-1)
random_preposition = random.randint(0, len(prepositions)-1)

# applying random
subject = subjects[random_subject]
verb1 = v1[random_v1]
verb2 = v2[random_v2]
verb3 = v3[random_v3]
verb4 = v4[random_v4]
preposition = prepositions[random_preposition]

match verb1:
    case "add":
        OBJECTS = "2 and 2"
    case _:
        OBJECTS = ""

match subject.lower():
    case "i":
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
    match verb1:
        case _:
            singular_verb1 = verb1 + "s"
elif not SINGULAR:
    singular_verb1 = verb1

# Execution
# need to remove space before mark
RANDOM_SENTENCE = ""
choice = input("Enter which type of sentence (tense) do you want to generate : ")
match choice.lower():
    case "present indefinite":
        RANDOM_SENTENCE = f"{subject.capitalize()} {singular_verb1} {OBJECTS}{marks[0]}"
    case "past indefinite":
        RANDOM_SENTENCE = f"{subject.capitalize()} {verb2} {OBJECTS}{marks[0]}"
    case "future indefinite":
        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} {verb1} {OBJECTS}{marks[0]}"

    case "present progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_BE} {verb4} {OBJECTS}{marks[0]}"
    case "past progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} {PAST_HELPING} {verb4} {OBJECTS}{marks[0]}"
    case "future progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} be {verb4} {OBJECTS}{marks[0]}"

    case "present perfect":
        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} {verb3} {OBJECTS}{marks[0]}"
    case "past perfect":
        RANDOM_SENTENCE = f"{subject.capitalize()} had {verb3} {OBJECTS}{marks[0]}"
    case "future perfect":
        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} have {verb3} {OBJECTS}{marks[0]}"

    case "present perfect progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} {TO_HAVE} been {verb4} {OBJECTS}{marks[0]}"
    case "past perfect progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} had been {verb4} {OBJECTS}{marks[0]}"
    case "future perfect progressive":
        RANDOM_SENTENCE = f"{subject.capitalize()} {FUTURE_HELPING} have been {verb4} {OBJECTS}{marks[0]}"

    case _:
        RANDOM_SENTENCE = f"{choice} is not a type of tense."

print(RANDOM_SENTENCE)

# inputing the sentence and outputing the type and tense of sentence
