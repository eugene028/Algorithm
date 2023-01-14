scores=[['Kim',90,70],['Lee',100,90],['Cha',95,90],['Ma',89,88]]
avg1=(scores[0][1]+scores[0][2])/2
scores[0].append(round(avg1,1))
avg2=(scores[1][1]+scores[1][2])/2
scores[1].append(round(avg2,1))
avg3=(scores[2][1]+scores[2][2])/2
scores[2].append(round(avg3,1))
avg4=(scores[3][1]+scores[3][2])/2
scores[3].append(round(avg4,1))
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print()
print(scores)



