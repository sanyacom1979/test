import json

with open("wict.json") as js:
    dict = json.load(js)
b = 0
if dict["q1"] == "alex":
    b += 1
if dict["q2"] == "moskow":
    b += 1
if dict["q3"] == "football":
    b += 1

print(f"Сумма баллов = {b}")





