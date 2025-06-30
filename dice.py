import random
# for x in range(1,6):
#     for y in range(1,6):
#         print(x,y)
class Dice:
    # def __init__(self):
    #     pass
    
    def roll(self):
        first= random.randint(1,6)
        second= random.randint(1,6)
        return (first,second)


dice = Dice()

ans = dice.roll()
print(ans)




