name=input("Enter your name: ")
age=int(input("Enter your age: "))
# print(f"Name = {name} , age = {age}")
city=input("Your current city ? ")
food= input("your favourite food ")
colour=input("your fav colour ? ")
animal=input("Your spirit animal ? ")
hobby=input("your hobby/passion ? ")

print("===="*6)

print(f"Hi {name}, this is your personality report :")
print(f"You are {age*12} months old")
print(f"You are from {city} amd enjoy doing {hobby} while eating {food}")
print(f"Your favourite colour is {colour} and your spirit animal is {animal}")
print("===="*6)

# The Personality Code is made using parts of your name, favorite color, age, and animal:
# name[:2].upper() + last digit of age + animal initial + color initial
print("Your Personality Code is :",name[:2].upper()+str(age)[-1]+animal[0]+colour[0])
if age<18:
    print("You are a young explorer")
elif age<30:
    print("You are an adventurer")
else:
    print("You are a wise owl ")
print("===="*6)

print("Thank you for using our service :)")