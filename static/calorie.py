goal = int(input("How many calories are you hoping to eat today?: "))
cont = input("Do you want to continue adding?: ")
calories = 0
while cont == "yes":
    cal = int(input("How many calories do you wish to add? "))
    calories = calories + cal
    cont = input("Do you want to continue adding?: ")
if calories >= goal:
    print("Congrats You have achieved your goal!")
else:
    print("You have not achieved your goal")
    print("Complete")