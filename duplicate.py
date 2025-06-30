dup=[1,2,3,4,1,1,3,3,4]
uniq =[]
for item in dup:
    if(item in uniq):
        continue
    else:
        uniq.append(item)
print(uniq)

