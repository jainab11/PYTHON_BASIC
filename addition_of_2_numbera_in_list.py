lst =[2,9,20,31,45]
new = [2, ]
for i in range(0, len(lst)):
  new.append(lst[i] + lst[i+1])
print(new)
