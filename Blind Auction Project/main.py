import art
print(art.logo)
print("Welcome to the secret auction program!")
auction = {}
bidding = True
max_value = 0
winning_key = ""
# TODO-1: Ask the user for input
while bidding:
    name = input("What is your name?: ")
    amount = input("what is your bid?: $")
    # TODO-2: Save data into dictionary {name: price}
    auction[name] = int(amount)
    # TODO-3: Whether if new bids need to be added
    new_bid = input("Are there any other bidders? type 'yes' or 'no':\n")
    if new_bid.lower() == "yes":
        print("\n" * 20)
    elif new_bid.lower() == "no":
        print("\n" * 20)
        bidding = False
# TODO-4: Compare bids in dictionary
        for key in auction:
            if auction[key] > max_value:
                max_value = auction[key]
                winning_key = key
        print(f"The winner is {winning_key} with a bid of ${max_value}!")


