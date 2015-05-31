__author__ = 'poke19962008'

states  = ["AP", "AS", "BR", "CH", "DL", "GA", "GJ", "HP", "HR", "JH", "JK", "KA", "KL", "LD", "MH", "ML",
           "MP", "NG", "OR", "PB", "PY", "RJ", "SK", "TG", "TN", "TR", "UK", "UP", "WB"]

for i in states:
    file_name = "%s.txt" % i

    with open(file_name, "r") as file_:
        data = file_.readlines()

    tweet = 0
    for j in data:
        if j != "\n":
            tweet = tweet + 1

    print(i + ": " + str(tweet))