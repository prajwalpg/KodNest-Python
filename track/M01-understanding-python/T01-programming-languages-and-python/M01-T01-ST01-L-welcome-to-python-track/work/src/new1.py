print("welcome")

name = input("\nEnter your name: ")

n = int(input("\nHow many topics you learned? "))

for i in range(n):
    topic = input("Enter topic " + str(i + 1) + ": ")

reason = input("\nWhy did you select Python? ")

goal = input("\nWhat is your career goal? ")

programming = input("\nProgramming means: ")

python = input("Python is: ")

n = int(input("How many things will you learn herte? "))

for i in range(n):
    learning = input("Enter learning topic " + str(i + 1) + ": ")

print("\nMY PYTHON TRACK")

print("My Name:", name)

print("\nWhat I Learned in F Month:")
print("You entered", n, "topics.")

print("\nWhy I Selected Python:", reason)

print("\nMy Career Goal:", goal)

print("\nWhat I Understood Today:")
print("Programming means:", programming)
print("Python is:", python)