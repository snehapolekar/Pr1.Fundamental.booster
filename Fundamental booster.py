print("Welcome to the Interactive Personal Data Collector!!")

name = input("Please enter your name :")
age = int(input("Please enter your age :"))
height = float(input("Please enter your height in meters :"))
fav_num = int(input("Please enter your favourite number :"))

print("Thank you! Here is the information we collected : ")

print(f"Name: {name}(Type: {type(name)}, Memory Address : {id(name)})")
print(f"age: {age}(Type: {type(age)}, Memory Address : {id(age)})")
print(f"height: {height}(Type: {type(height)}, Memory Address : {id(height)})")
print(f"fav_num: {fav_num}(Type: {type(fav_num)}, Memory Address : {id(fav_num)})")

current_year = 2026

birth_year=current_year-age

print(f"Your birth year is approximately:{birth_year}(based on your age of 17)")

print("Thank you for using the Personal Data Collector.")
print("Goodbye!!")


