# Pam F. Set the scene of the Story
print("~ Tales of Princessland ~")
print("A Work of Fiction")
print()
print(
  "You are The Good fairy of Columbia in LaLa Land, and you're trying to grant a special wish to the chosen princess."
)
print()
print("You decide to go on a flight at LaLa Land to grant your special wish!")
print()
print(
  "You are outside The Villages of Kings Contrivance, and you see three different princesses asking for special wishes to be granted. You could talk to:"
)
# Display the princess choices
print(
  "  A. The Princess Pamela, who wants to move to a warm climate and live happily ever after"
)
print(
  "  B. The Princess Brittany, who wants a new job in a warm climate where she and her family will live happily ever after"
)
print(
  "  C. The Princess Dasja, who wants a new home for her and her beautiful family"
)
print()
# Prompt user to select a princess
answer = input(
  "Who will the Good fairy select? Please select option A through C: ")
if (answer == 'A'):
  print("You meet with Princess Pamela, and ask her to solve a math problem")
  # Display math problem to be solved
  result = input("How much does 2 + 3 = ")
  # Display positive message for correct answer
  if (int(result) == 5):
    print(
      "Your wish will be granted immediately. Please pack all your possessions so you can move to a warm climate and live happily ever after !!!"
    )
# Display negative message for incorrect answer
  else:
    print("Your special wish will not be granted")
    print("You will remain in this cold climate forever")
elif (answer == 'B'):
  print("You meet with Princess Brittany and ask her to solve a math problem")
  # Display math problem to be solved
  result = input("How much does 7 + 3 = ")
  # Display positive message for correct answer
  if (int(result) == 10):
    print(
      "Your wish will be granted immediately. Please pack up your family, a new job is waiting for you in a warm climate where you and your family will live happily ever after !!!"
    )
# Display negative message for incorrect answer
  else:
    print("Your special wish will not be granted")
    print("You will remain at your current job in this cold climate")
else:
  print("You meet with Princess Dasja, and ask her to solve a math problem")
  # Display math problem to be solved
  result = input("How much does 4 + 3 = ")
  # Display positive message for correct answer
  if (int(result) == 7):
    print(
      "Your wish will be granted immediately. Please pack up your family, a new home for you and your beautiful family is waiting for you in Hampton, VA !!!"
    )
# Display negative message for incorrect answer
  else:
    print("Your special wish will not be granted")
    print(
      "You and your husband must continue to save in order to get a new home")
# print blank line for readability
print()
# Display End of Story message
print("~ The End ~")


