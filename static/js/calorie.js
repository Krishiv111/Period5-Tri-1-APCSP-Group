var goal = prompt("What is your Calorie Goal for today?");
    var count = document.querySelector(".count-input-field")
var calculateButton = document.querySelector(".calculate");
    var result = document.querySelector(".result");
var statement = document.querySelector(".result-statement");

while add == "yes":
    cal = int(input("How many calories do you wish to add? "))
    calories = calories + cal
    cont = input("Do you want to continue adding?: ")
if calories >= goal:
    print("Congrats You have achieved your goal!")
else:
    print("You have not achieved your goal")