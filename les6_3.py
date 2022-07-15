import pickle

q1 = input("Как тебя зовут?")
q2 = input("где живешь?")
q3 = input("твое хобби?")

dict = {"q1": q1, "q2": q2, "q3" : q3}

with open("wict.picle", mode = "wb") as pcl:
    pickle.dump(dict, pcl)

with open("wict.picle", mode = "rb") as pcl:
    dict = pickle.load(pcl)
b = 0
if dict["q1"] == "alex":
    b += 1
if dict["q2"] == "moskow":
    b += 1
if dict["q3"] == "football":
    b += 1

print(f"Сумма баллов = {b}")