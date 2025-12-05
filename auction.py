is_auction_done = False

# the varible will allow us to follow up on while loop

members = {}

while not is_auction_done:

	any_more_members = input("Participating in auction ? ").lower()
	if any_more_members == "yes":
		name = input("Enter your name ").lower()
		bid = int(input("Enter your bid "))
		members[name] = bid
		# print(members)
	
	elif any_more_members == "no":
	
		if members: # Check if anyone bid
		
			max_bid = 0
			winner = ""
			# this is how we iterate through a object to access key and value pairs.
			for name, bid in members.items():
			# comparing them together to select the highest bid.
				if bid > max_bid:
					max_bid = bid
					winner = name
			
			print(f"\nThe winner is {winner} with a bid of ${max_bid}!")
			print("All bids:", members)
	
		else:
			print("No one participated in the auction.")
			is_auction_done = True # This ends the loop
			
	else:
	
	    print("Please enter valid input.")