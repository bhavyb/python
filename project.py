print("Welcome to the Interactive Personal Data Collector\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
number = int(input("Please enter your favourite number: "))

print("\nThank you! Here is the information we collected:\n")

print("Name: ",name,"(Type: ",type(name),", Memory Address: ", id(name), ")")
print("Age: ",age,"(Type: ",type(age),", Memory Address: ", id(age), ")")
print("Height: ",height,"(Type: ",type(height),", Memory Address: ", id(height), ")")
print("Favourite number: ",number,"(Type: ",type(number),", Memory Address: ", id(number), ")")


current_y = 2025
birth_y = current_y - age
print("Your birth year is approximately: ",birth_y, "(based on your age of ",age,")")