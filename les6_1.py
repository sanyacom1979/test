import json

q1 = input("Как тебя зовут?")
q2 = input("где живешь?")
q3 = input("твое хобби?")

dict = {"q1": q1, "q2": q2, "q3" : q3}

with open("wict.json", mode = "w") as js:
    json.dump(dict, js)


