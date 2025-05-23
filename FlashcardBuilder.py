import json
import random

print("Welcome to the flashcard program")
flashcards = {}
def add():
  while True:
    user_english = input("What word would you like to add?")
    if user_english == "Back to start":
      break
    translation = input(f"What is the translation of {user_english}?")
    if translation == "Back to start":
      break
    flashcards[user_english] = translation
    print(f"{user_english} is now recorded to mean:", flashcards[user_english])

def quiz():
  try:
    with open("flashcards.json", "r") as f:
      stored_flashcards = json.load(f)
  except FileNotFoundError:
    print("No flashcards found. Please add some first.")
    return
  if not stored_flashcards:
    print("Flashcard list is empty")
    return
  words = list(stored_flashcards.keys())
  random.shuffle(words)
  for word in words:
    while True:
      guess = input(f"What is the translation of {word}?")
      if guess == stored_flashcards[word]:
        print("Correct")
        break 
      else:
        print("Incorrect, try again:")
while True:
  menu = input("Menu: add|quiz|exit\n")
  if menu == "add":
    try:
      with open("flashcards.json", "r") as f:
          saved_flashcards = json.load(f)
    except FileNotFoundError:
      saved_flashcards = {}
    flashcards.update(saved_flashcards)
    add()
    with open("flashcards.json", "w") as f:
      json.dump(flashcards, f)
    print("Flashcard Saved")
  elif menu == "quiz":
    quiz()
  elif menu == "exit":
    print("Goodbye")
    break
  else:
    print("Invalid input")