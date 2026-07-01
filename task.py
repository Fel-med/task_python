

#EXERCISE 1
def exercise1():
    print("Running Exercise 1...")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    comparison(num1, num2)

def comparison(num1, num2):

    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")


#EXERCISE 2
def exercise2():
    print("Running Exercise 2...")
    tax=0
    income = float(input("Enter your income: "))
    if income < 50000:
        tax=10
    elif income < 100000:
        tax=20
    else:
        tax=30
    print(f"Your tax rate is {tax}%")
    print(f"Your tax amount is {income * tax / 100}")

#EXERCISE 3
def exercise3():
    print("Running Exercise 3...")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi:.2f}. You are underweight.")
    elif bmi < 25:
        print(f"Your BMI is {bmi:.2f}. You are normal weight.")
    else:
        print(f"Your BMI is {bmi:.2f}. You are overweight.")

#EXERCISE 4
def exercise4():
    print("Running Exercise 4...")
    ls = []
    for i in range(3):
        ls.append(int(input(f"Enter number {i+1}: ")))
    ls.sort()
    print("The sorted numbers are: ")
    for i in range(3):
        print(f"Number {i+1}: {ls[i]}")

#EXERCISE 5
def exercise5():
    print("Running Exercise 5...")
    num = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    while num < 1 or num > 7:
        num = int(input("Enter a number between 1 and 7: "))
    print(f"The day corresponding to {num} is {days[num-1]}")

#EXERCISE 6
def exercise6():
    print("Running Exercise 6...")
    age = 0
    while age < 0:
        age = int(input("Enter your age: "))
    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior.")

#EXERCISE 7
def exercise7():
    print("Running Exercise 7...")
    letter = input("Enter a letter: ")
    if letter == "" :
        print("You did not enter a letter.")
    elif letter.isalpha() and len(letter) == 1:
        letter = letter.lower()
        if letter == "y":
            print(f"{letter} is sometimes a vowel and sometimes a consonant.")
        elif letter in "aeiou":
            print(f"{letter} is a vowel.")
        else:
            print(f"{letter} is a consonant.")
    else:
        print("You did not enter a single letter.")


def FizzBuzz():
    print("Running FizzBuzz...")
    n = int(input("Enter a number: "))
    if n < 1 or n > 10**5:
        print("Please enter a positive number between 1 and 100000.")
        return
    else:
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print(f"{i} : FizzBuzz")
            elif i % 3 == 0:
                print(f"{i} : Fizz")
            elif i % 5 == 0:
                print(f"{i} : Buzz")
            else:
                print(i)
            print("------------------------------")



#the main function that will run the exercises
def list():
    print("which exercise do you want to run?\n1. Exercise 1 - Number Comparison\n2. Exercise 2 - Tax Calculator\n3. Exercise 3 - BMI Calculator\n4. Exercise 4 - Sorting Numbers\n5. Exercise 5 - Day of the Week\n6. Exercise 6 - Age Group Classifier\n7. Exercise 7 - vowel or consonant\n8. Exercise 8 - FizzBuzz\n9. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        exercise1()
    elif choice == 2:
        exercise2()
    elif choice == 3:
        exercise3()
    elif choice == 4:
        exercise4()
    elif choice == 5:
        exercise5()
    elif choice == 6:
        exercise6()
    elif choice == 7:
        exercise7()
    elif choice == 8:
        FizzBuzz()
    elif choice == 9:
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
    list()

list()