# ============================================================
# Python Final Project 2026
# Name: john canady
# Date: 5/6/2026
# Project Title: how to count to 3 
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""



# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("---------------------")



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))

print("Welcome!")
print("today you're gonna learn to count to 3!")
score = int(input("what is the first number?"))
if score == 1:
    print("Good job")
elif score != 1:
     print("try again!")
else:
    score = score + 1
    print("Keep practicing!")

score = int(input("what is the second number?"))
if score == 2:
    print("Good job")
elif score != 2:
     print("try again!")
else:
    score = score + 1
    print("Keep practicing!")

score = int(input("what is the third number?"))
if score == 3:
    print("Good job")
elif score != 3:
     print("try again!")
else:
    score = score + 1
    print("Keep practicing!")

# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.

# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")

 

# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.

print("----------------------------")
print("Thanks for using my program!")
