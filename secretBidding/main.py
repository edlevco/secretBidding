import os

def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For Unix/Linux/MacOS
    else:
        _ = os.system('clear')


from art import logo
print("Welcome to the secret bidding project")


allBids = {}
print(logo)
moreBidders = True
while moreBidders:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  allBids[name] = bid
  runAgain = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if runAgain == "no":
    moreBidders = False
  elif runAgain == "yes":
    clear()

maxBid = 0
winner = ""
for bid in allBids:
  if allBids[bid] > maxBid:
    maxBid = allBids[bid]
    winner = bid

print(f"The winner is {winner} with a bid of ${maxBid}")


  
  

  

  




