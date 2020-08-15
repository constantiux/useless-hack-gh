import json

def loadme():
  with open('data.json', 'r') as f:
    data_json = json.load(f)
  return data_json


def mode():
  ans = "test"
  expected = ['daily', 'weekly', 'monthly']
  while(ans not in expected):
    ans = input("\nReplenish supply daily/weekly/monthly? ").lower()
    if ans in expected:
      if ans == 'daily':
        return 1
      elif ans == 'weekly':
        return 7
      else:
        return 30


def start():
  jsondict = loadme()
  #print(jsondict)
  demand = jsondict['demand']
  inventory = jsondict['inventory']
  multiplier = mode()
  negative = 0
  for name, val in demand.items():
    if name in inventory.keys() and (inventory[name] < val * multiplier):
      print(f"Item {name} is undersupplied!")
      negative += 1
    elif name not in inventory.keys():
      print(f"Item {name} is undersupplied!")
      negative += 1
  if negative == 0:
    print("No item is undersupplied. You are good to go!")