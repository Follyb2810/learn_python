for x in range(4):
    for y in range(1,4):
        print((x,y)) 

numbers = [5,2,5,2,2]

for item in numbers:
    print(item * '*')

for item in numbers:
    output=''
    for inner in range(item):
         output += 'x'
    print(output)