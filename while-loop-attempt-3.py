import random

player = []
dealer = []

player_bank = 100
dealer_bank = 5000000000

response_1 = "You win!"
response_2 = "You lose!"

def draw_card(): #draw one card at a time
	player.append(random.randrange(2, 11))
	if sum(dealer) < 21:
		dealer.append(random.randrange(2, 11))

def end_game():
	print "***********"
	total_user = sum(player)
	total_dealer = sum(dealer)
	print "The dealer had these cards: %s" % dealer
	print "The total for his hand is %s" %total_dealer
	print "Your cards were: %s" % player
	print "Your total for your hand is: %s" % total_user
	if (total_user <= 21) < (total_dealer < 21):
		print response_1
		exit()
	elif (total_user < 21) > total_dealer <= 21:
		print "Sorry dude, %s" response_2
		exit()
	elif total_user <= 21 and total_dealer < 21 and total_user < total_dealer:
		print "Boohoo, %s" response_2
		exit()
	elif total_user <= 21 and total_dealer > 21:
		print "The dealer got busted! %s" respone1 
		
		exit()
	elif total_user == total_dealer:
		print "Sorry dude, the dealer won this round."
		exit()
	elif total_user > 21 and total_dealer < 21:
		print "You busted. The dealer won this round."
		exit()
	elif total_user > 21 and total_dealer > 21:
		print "Well you both lose!"
		exit()

win = 'win' or 'won'

def wager():
	if win in response_1:
		player_bank += w
		dealer_bank -= w
	else:
		player_bank -= w
		dealer_bank += w


def blackjack(): #gameplay
	draw_card()
	draw_card()
	hand = 0
	for i in player:
		player_total = sum(player)
	for i in dealer:
		dealer_total = sum(dealer)
	print "Here are your cards: %s" % player
	print "Your total is: %s" % player_total
	print "The dealer reveals this card: %s" % dealer[0]
	print "Would you like to 'hit' or 'stay'?"
	answer = raw_input("Type hit or stay:  ")
	while answer != 'stay':
		draw_card()
		for i in player:
			player_total = sum(player)
		for i in dealer:
			dealer_total = sum(dealer)
		print "Here are your new cards: %s" % player
		print "Your NEW total is: %s" % player_total
		if player_total >= 21:
			end_game()
		elif player_total <= 21:
			print "Would you like to 'hit' or 'stay'?"
		answer = raw_input()
	else: 
		end_game()


print "Welcome to our blackjack table!"
print "What is your wager fine gentleman/woman?"
w = raw_input("Place your bet here: $")
print "The dealer will match."
print "Please, let's see your first two cards."
blackjack()

