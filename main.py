import stocks
import evaluate

def header():
  print("====================")
  print("Hello, Welcome User!")
  print("====================")


def menus():
  print("")
  print("1) Update user demand")
  print("2) Update stock inventory")
  print("3) Evaluate")
  print("")


def say():
  header()
  while(1):
    menus()
    choice = "0"
    choices = ["1","2","3"]
    while(choice not in choices):
      choice = input("Select: ")
      if choice not in choices:
        print("Wrong input, try again.")
    if choice == "1":
      stocks.start('demand')
    elif choice == "2":
      stocks.start('inventory')
    elif choice == "3":
      evaluate.start()


say()