names=['folly','babs','akin']
name ='folly'
numbers =[3,2,6,9,1,0]
max = numbers[0]

for item in numbers:
    if(max < item):
        max = item
    print(max)
