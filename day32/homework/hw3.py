list=[1,2,3,4,5,6]
new=[]
for i in range(len(list)):

  if list[i]%2 > 0:
     new.append(list[i])
     print(new)