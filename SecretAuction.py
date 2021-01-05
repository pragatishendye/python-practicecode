"""
 Secret Auction program.
 This program takes in bids and displays the winner who made the highest bid.
 Created by Pragathi Shendye
"""

import os, subprocess

print("Welcome to the secret auction!")
bids = dict()
keep_bidding = True


def highest_bid(bid_data):
    highest = 0
    winner = ''
    for bidder in bid_data:
        current_bid = bid_data[bidder]
        if current_bid > highest:
            highest = current_bid
            winner = bidder
    print(f"The bid winner is {winner} with a bid of ${highest}")


def clear():
    if os.name in [('dos', 'nt')]:
        subprocess.call('cls')


while keep_bidding:
    name = input(f"What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    next_bid = input("Does anyone else want to bid? Type 'yes' or 'no': \n")
    if next_bid == "yes":
        clear()                             # clear the screen for every new bid
    else:
        keep_bidding = False


highest_bid(bids)