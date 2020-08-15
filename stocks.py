import json

def loadme():
  with open('./data.json', 'r') as f:
    data_json = json.load(f)
  return data_json


def saveme(dict):
  with open('data.json', 'w') as f:
    json.dump(dict, f)


def start(stocktype):
  jsondict = loadme()
  #print(jsondict)
  items = jsondict[stocktype]
  if stocktype == 'inventory':
    query = "No. of units you have now: "
  else:
    query = "No. of units needed daily: "
  print(f"\nYou currently have {len(items)} items.")
  askAdd = input("Would you like to edit? (Y/N)")
  if askAdd == "Y":
    print("You would be asked to enter item names. Input `cancel` or `stop` to stop adding.")
    nameItm = "X"
    stopMe = ['cancel', 'stop']
    while(nameItm.lower() not in stopMe):
      nameItm = input("\nName of item: ")
      if nameItm.lower() not in stopMe:
        items[nameItm] = int(input(query))
    #print(items)
    jsondict[stocktype] = items
    saveme(jsondict)
    
    