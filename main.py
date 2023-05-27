# English Grammar
import random

v1 = ["add", "allow", "act", "ask", "abuse", "awake", "amend", "aquire",
      "appear", "anounce", "apply", "arrest", "attend", "arest", "attract", "avoid"]
v2 = []
for v in v1:
    match v1:
        case "run":
            v2.append("ran")
        case _:
            v2.append(v + "ed")
prepositions = ["in", "on", "up"]
subjects = ["I", "we", "you", "he", "she", "it", "they"]
# name = input("Enter any name you want to use as a subject : ")
# subjects.append(name)
adverbs = ["genlty", "happily", "sadly", "quietly", "slowly"]
marks = [".", "?", ",", "!"]
random_v1 = random.randint(0, len(v1))
random_v2 = random.randint(0, len(v2))
random_preposition = random.randint(0, len(prepositions))
random_subject = random.randint(0, len(subjects))

random_sentence = f"{subjects[random_subject].capitalize()} {v1[random_v1]}{marks[0]}"
print(random_sentence)
