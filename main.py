# English Grammar
import random

subjects = ["I", "we", "you", "he", "she", "it", "they"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "aquire",
      "appear", "anounce", "apply", "arrest", "attend", "attract", "avoid"]
v2 = []
for v in v1:
# removing e before abuse as it's second form will be abused but in this code it will be abuseed
    if v[-1]=="e":
        v=v[0:len(v)-1]
    match v:
        case "run":
            v2.append("ran")
        case _:
            v2.append(v + "ed")

v3 = []
for v in v2:
    match v:
        case "ran":
            v3.append("run")
        case _:
            v3.append(v) 

v4 = []
for v in v1:
    if v[-1]=="e":
        v=v[0:len(v)-1]
    match v:
        case _:
            v4.append(v + "ing")

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
preposition = v1[random_preposition]

match subject.lower():
    case "i":
        future_helping = "shall"
        to_have = "have"
        past_helping = "was"

    case "we":
        future_helping = "shall"
        to_have = "have"
        past_helping = "were"

    case "you":
        future_helping = "will"
        to_have = "have"
        past_helping = "were"

    case "they":
        future_helping = "will"
        to_have = "have"
        past_helping = "were"
    
    case _:
        future_helping = "will"
        to_have = "has"
        past_helping = "was"

# Execution
random_sentence = ""
choice = input("Enter which type of sentence (tense) do you want to generate : ")
match choice.lower():
    case "present indefinite":
        random_sentence = f"{subject.capitalize()} {verb1}{marks[0]}"
    case "past indefinite":
        random_sentence = f"{subject.capitalize()} {verb2}{marks[0]}"
    case "future indefinite":
        random_sentence = f"{subject.capitalize()} {future_helping} {verb1}{marks[0]}"

    case "present progressive":
        random_sentence = f"{subject.capitalize()} {verb4}{marks[0]}"
    case "past progressive":
        random_sentence = f"{subject.capitalize()} {past_helping} {verb4}{marks[0]}"
    case "future progressive":
        random_sentence = f"{subject.capitalize()} {future_helping} be {verb4}{marks[0]}"

    case "present perfect":
        random_sentence = f"{subject.capitalize()} {to_have} {verb3}{marks[0]}"
    case "past perfect":
        random_sentence = f"{subject.capitalize()} had {verb3}{marks[0]}"
    case "future perfect":
        random_sentence = f"{subject.capitalize()} {future_helping} have {verb3}{marks[0]}"

    case "present perfect progressive":
        random_sentence = f"{subject.capitalize()} {to_have} been {verb4}{marks[0]}"
    case "past perfect progressive":
        random_sentence = f"{subject.capitalize()} had been {verb4}{marks[0]}"
    case "future perfect progressive":
        random_sentence = f"{subject.capitalize()} {future_helping} have been {verb4}{marks[0]}"

    case _:
        random_sentence = f"{choice} is not a type of tense."

print(random_sentence)

# inputing the sentence and outputing the type and tense of sentence