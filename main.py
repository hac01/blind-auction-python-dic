from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import *
print(logo)
bid={}
bid_finish=False

def find_highest_bidder(biding_rec):
  highest_bid=0
  winner=""
  for bidder in biding_rec:
    bid_amount=biding_rec[bidder]
    if bid_amount > highest_bid:
      highest_bid=bid_amount
      winner=bidder
  print(f"The winner is {winner} and the highest bid is ${highest_bid}")

while not bid_finish:
   #print("welcome to Bid auction")
   name=input("what's your name??")
   val=int(input("What is your bid?: $ "))
   bid[name]=val
  #print(bid)
   con=input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
   if con == "yes":
     clear()
   elif con == "no":
     bid_finish=True
     find_highest_bidder(bid)
     #print(bid)
   else :
     print("You Have entered something which doesn't exists")

#

