# English Grammar
import random

subjects = ["I", "we", "you", "he", "she", "it", "they"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "aquire",
      "appear", "anounce", "apply", "arrest", "attend", "arest", "attract", "avoid"]
v2 = []
for v in v1:
    match v:
        case "run":
            v2.append("ran")
        case _:
            v2.append(v + "ed")
# need to remove e before abuse as it's second form will be abused but in this code it will be abuseed

v3 = []
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
random_preposition = random.randint(0, len(prepositions)-1)

# applying random

subject = subjects[random_subject]
verb1 = v1[random_v1]
verb2 = v2[random_v2]
verb3 = v3[random_v3]
preposition = v1[random_preposition]

match subject.lower():
    case "i":
        future_helping = "shall"

    case "we":
        future_helping = "shall"
    
    case _:
        future_helping = "will"

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

print(random_sentence)
