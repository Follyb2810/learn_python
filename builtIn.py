import random

for i in range(3):
    print(random.random()*10)

members=['folly','babs','akin','akin','tobi']
leader =random.choice(members)
leaders =random.choices(members)
print(leader)
print(leaders)
numbers =[1,2,3,4,5,6]
lead = random.choice(numbers)
print(lead)