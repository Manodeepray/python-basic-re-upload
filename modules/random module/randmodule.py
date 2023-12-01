import random
print("any random no. from 0 to 100 : \n")
print(random.randint(0,100))#donot put name of module elsewhere
food=["ravioli","chaat","bhel","chalk"]
print("random food item from list food [ravioli chaat bhel chalk ] : \n")
print(random.choice(food))
print(food )
print("after shuffeling \n")
random.shuffle(food)
print(food)