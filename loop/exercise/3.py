'''Exercise 3: The weight of a person on the moon is 1/6th the weight of a
person standing on earth. Say that your weight on earth increases by 1 kg
every year. Write a program that will print your weight on the moon every
year for the next 10 years. (Your initial weight can be anything.)'''

we=int(input("enter your weight : "))
i=0
while i<=10:
    wm=(1/6)*we
    we+=1
    i+=1
    print(wm)


