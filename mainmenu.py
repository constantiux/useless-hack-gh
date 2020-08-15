#import inventory

def title():
  print("=========")
  print("Main menu")
  print("=========")
  print("")

def say():
  title()
  print("1) Update user demand")
  print("2) Update stock inventory")
  choice = "0"
  choices = ["1","2"]
  while(choice not in choices):
    choice = input("Select: ")
    if choice not in choices:
      print("Wrong input, try again.")
  if choice == "1":
    print("One")
  elif choice == "2":
    print("Two")