score = [90,80,92,88,75,88,80,80,90,90,90,75]

for s in range(1,101):
    if (s in score):
        myoung = score.count(s)
        print("{}점 {}명".format(s,myoung))