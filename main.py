# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
#print(names)

names_length = len(names)

random_name=random.randint(0,names_length-1)
pay_bill=names[random_name]
print(f'{pay_bill} is going to buy the meal today!')




