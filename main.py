import os
import random
import time

#TODO Add Poker game


#Main menu to select game
def main_menu(wallet):
	clearConsole()
	print("----[Welcome to Casino Royale Bjorn bitchboy]----")
	print("----[Select your game]----\n")

	print("[1] Roulette 	 [4] Blackjack 	 	[7] Deposit money")
	print("[2] Poker 	 [5] Horses 		 [8] Widthdraw money")
	print("[3] Slots 	 [6] Blackjack V2 	 [9] Exit" + "\n")
	# errorHandling(wallet)

	print("Wallet: $", wallet)
	game = int(input("\nPlease Select your game: "))

	if game == 1:
		roulette(wallet)
	elif game == 3:
		slots(wallet)
	elif game == 4:
		blackjack(wallet)
	elif game == 5:
		horses(wallet)
	elif game == 6:
		blackjackV2(wallet)
	elif game == 7:
		depositFunds(wallet)
	elif game == 8:
		withdrawFunds(wallet)	

# Function to clear console at start of other functions
def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)

#Shows the current wallet
def showWallet(wallet):
	print("\nWallet: $", wallet , "\n")

#Shows to bet 0 to go to main menu
def showTip():
	print("\n----[Useful Tip]----")
	print("\nTo go back at the main menu at any given time, press the right shift key.")

#Checks whether the bet was over the wallet amount
def betCheck(wallet, bet):

	if bet == 0:
		main_menu(wallet)
	
	if wallet == 0:
		print("Sorry! Not enough funds!")
		time.sleep(3)
		main_menu(wallet)

	if bet > wallet:
		print("Not enough funds for that bet!")
		time.sleep(1.4)
		main_menu(wallet)

#Deposit new funds into wallet
def depositFunds(wallet):

	clearConsole()

	print("----[Deposit Funds]----\n")
	deposit = int(input("How much would you like to deposit?: $"))

	wallet += deposit

	print("Succesfully updated wallet with: $", deposit)
	time.sleep(2)

	main_menu(wallet)

#Withdraw funds from wallet
def withdrawFunds(wallet):

	clearConsole()
	print("----[Withdraw Funds]----\n")
	withdrawal = int(input("How much would you like to withdraw?: $"))

	wallet -= withdrawal

	print("Succesfully withdrawed: $", withdrawal)
	time.sleep(2)
	main_menu(wallet)

#Select different slot machine.
def slots(wallet):

	clearConsole()

	print("====[Welcome to Slots!]====\n")
	

	print("[1] Tycoon Maniya\n")
	print("[2] Fire Joker\n")
	print("[3] Sweet Bonanza\n")

	slot_choice = input("Please select your choice: ")

	if slot_choice == "1":
		tycoon(wallet)
	elif slot_choice == "2":
		fire_joker(wallet)
	elif slot_choice == "3":
		sweet_bonanza(wallet)
	else:
		main_menu(wallet)

#Roulette game
def roulette(wallet):

	colors = ['Red', 'Black', 'Green']
	random_color = random.choice(colors)

	clearConsole()
	winning_number = random.randint(0,36)

	print("----[Now playing Roulette]----\n")
	showWallet(wallet)

	bet = int(input("Please place your bets [USD]: "))
	
	betCheck(wallet, bet)
	
	bet_number = int(input("On which number? "))

	if bet_number == winning_number:
		winnings = bet * 36
		print("Winning number is: ", winning_number, random_color)
		print("Congratulations! You could've won ", winnings)
		time.sleep(3.5)
		wallet += winnings
		main_menu(wallet)
	else:
		print("Too bad! You lost! Winning number was: \n", winning_number)
		wallet -= bet
		time.sleep(3.5)
		main_menu(wallet)

	return wallet

#Blackjack game
def blackjack(wallet):
	clearConsole()

	dealerHand = random.randint(17,27)
	playerHand = random.randint(17,27)


	print("----[Now playing Blackjack]----\n")
	print("If you bet 0, you'll return to the main menu\n")

	showWallet(wallet)
	bet = int(input("\nPlease place your bet [USD]: "))


	winnings = bet * 2
	winningsbj = bet * 2.5
	
	betCheck(wallet, bet)

	print("Dealer drew: ", dealerHand)
	time.sleep(1)
	print("You got: ", playerHand)
	time.sleep(1.4)

	if dealerHand > 21:
		print("Congratulations! You won: $", winnings)
		time.sleep(3.5)
		wallet += winnings
		blackjack(wallet)
	elif playerHand == 21:
		print("Congratulions! Blackjack! You won: $",winnings)
		wallet += winningsbj
		time.sleep(1.4)
		blackjack(wallet)
	elif playerHand > 21:
		print("Too bad, you lost.")
		time.sleep(3)
		wallet -= bet
		blackjack(wallet)

	return wallet

#New blackjack with betting and standing.
def blackjackV2(wallet, totalPlayer=0, totalDealer=0, game_continued=None):

	clearConsole()

	if game_continued == False:
		# This is in the beginning
		firstCard_player = random.randint(1,11)
		firstCard_dealer = random.randint(1,11)

		secondCard_player = random.randint(1,11)
		secondCard_dealer = random.randint(1,11)
	else:
		firstCard_player = random.randint(1,11)
		firstCard_dealer = random.randint(1,11)

		secondCard_player = random.randint(1,11)
		secondCard_dealer = random.randint(1,11)


	# TODO We need to write a switch that knows if the game is continued so it adds the new card to totalPlayer and totalDealer


	print("----[Now playing Blackjack]----")
	print("If you bet 0, you'll return to the main menu\n")
	print("Wallet: $", wallet)


	bet = int(input("Please place your bets: $"))

	print("First card: ",firstCard_player)
	time.sleep(2)
	print("Dealer first card: ", firstCard_dealer)
	time.sleep(2)
	print("Second card player: ", secondCard_player)
	time.sleep(1)
	totalPlayer = firstCard_player + secondCard_player
	print("Total: ", totalPlayer)

	totalDealer = firstCard_dealer + secondCard_dealer
	# print(totalDealer)

	if totalPlayer <= 20:
		stbet = input("Do you want to stand or bet? s/b: ")
		if stbet == "b":
			card = random.randint(1,11)
			print("New card: ", card)
			time.sleep(1.5)
			card += totalPlayer
			if totalPlayer > 22:
				print("Cards: ",totalPlayer)
				print("Too bad! You lost!")
				time.sleep(2)
			elif totalPlayer == 21:
				print("Cards: ", totalPlayer)
				print("Blackjack!")
			else:
				if totalPlayer < totalDealer and totalDealer >= 17:
					print("Your Cards: ", totalPlayer)
					print("Dealer got: ")
					print("Too bad! You lost!")
					time.sleep(3)
					blackjackV2(wallet)
				elif totalplayer > totalDealer and totalDealer <= 17:
				else:
					card1 = random.randint(1,11)
					card += totalPlayer
					blackjackV2(wallet, totalPlayer, totalDealer, game_continued=True)
		if stbet =="s":
			

#Fire joker slot machine
def fire_joker(wallet):

	clearConsole()

	lane1 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']
	lane2 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']
	lane3 = ['Fire Joker','Grapes','Banana','Lemon','Pear','Strawberry']

	random_lane1 = random.choice(lane1)
	random_lane2 = random.choice(lane2)
	random_lane3 = random.choice(lane3)

	print("----[Now playing Fire Joker]----\n")

	print("If you bet 0, you'll return to the main menu\n")

	showWallet(wallet)
	bet = int(input("\nPlease place your bet: $"))
	
	betCheck(wallet, bet)
	winning_jackpot = bet * 12300
	winning1 = bet * 12
	
	winner = "Congratulations! You won: $", winning1

	jackpot = "[JACKPOT] CONGRATULATIONS! YOU WON THE JACKPOT! You could've won: $",winning_jackpot

	for i in lane1:

		random_lane1 = random.choice(lane1)
		random_lane2 = random.choice(lane2)
		random_lane3 = random.choice(lane3)

		print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
		time.sleep(0.2)

		if random_lane1.startswith("Fire Joker") & random_lane2.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(jackpot)
			wallet += winning_jackpot
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane1.startswith("Fire Joker") & random_lane2.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane1.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)
		elif random_lane2.startswith("Fire Joker") & random_lane3.startswith("Fire Joker"):
			print(winner)
			wallet += winning1
			time.sleep(5)
			fire_joker(wallet)

	print("You lost! Too bad.")
	wallet -= bet
	time.sleep(2)
	fire_joker(wallet)

	return wallet

#Tycoon slot machine
def tycoon(wallet):

	clearConsole()
	

	pepper = ['Black Pepper', 'Red Pepper', 'Green Pepper']
	lemon = ['Black lemon', 'Red lemon', 'Green lemon']
	apple = ['Black apple', 'Red apple', 'Green apple']

	random_pepper = random.choice(pepper)
	random_lemon = random.choice(lemon)
	random_apple = random.choice(apple)

	print("----[Now playing Tycoon Manya]----")

	showWallet(wallet)
	bet = int(input("\nPlease place your bets [Minimum $10]: "))

	betCheck(wallet, bet)
	
	winnings = bet * 250	

	winner = "<JACKPOT> Congratulations! You won:" , "$" , winnings
	
	for i in range(8):
		print("| " + random_pepper + " | " + random_lemon + " | " + random_apple)
		time.sleep(0.8)

		if random_pepper.startswith("Black") & random_apple.startswith("Black") & random_lemon.startswith("Black"):
			print(winner)
			wallet += winnings
			time.sleep(3) 
			tycoon(wallet)
		elif random_pepper.startswith("Red") & random_apple.startswith("Red") & random_lemon.startswith("Red"):
			print(winner)
			wallet += winnings
			time.sleep(3)
			tycoon(wallet)
		elif random_pepper.startswith("Green") & random_apple.startswith("Green") & random_lemon.startswith("Green"):
			print(winner)
			wallet += winnings
			time.sleep(3)
			tycoon(wallet)
	
	print("To bad! You lost!")
	wallet -= bet
	time.sleep(3)	

	tycoon(wallet)

	return wallet

#Sweet bonanza slot machine game
def sweet_bonanza(wallet):
		clearConsole()
		lane1 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		lane2 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		lane3 = ['Bonus Bomb','Grapes','Banana','Lemon','Pear','Strawberry']
		print("----[Now playing Sweet Bonanza]----\n")
		
		showWallet(wallet)
		bet = int(input("\nPlease place your bets: $"))

		betCheck(wallet, bet)

		for i in lane1:

			random_lane1 = random.choice(lane1)
			random_lane2 = random.choice(lane2)
			random_lane3 = random.choice(lane3)

			multipliers = ['5','10','25','50','100']

			print("| " + random_lane1 + " | " + random_lane2 + " | " + random_lane3 + " | ")
			time.sleep(0.2)

			if random_lane1.startswith("Bonus Bomb") & random_lane2.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
			elif random_lane1.startswith("Bonus Bomb") & random_lane2.startswith("Bonus Bomb"):				
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				sweet_bonanza(wallet)
			elif random_lane1.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
			elif random_lane2.startswith("Bonus Bomb") & random_lane3.startswith("Bonus Bomb"):
				bbm = random.choice(multipliers)
				bbmPlusBet = int(bbm) * bet
				wallet += bbmPlusBet
				print("Congratulations: $",bbmPlusBet)
				time.sleep(3)
				sweet_bonanza(wallet)
				print("Too bad! You lost!")
				wallet += int(bbmPlusBet)
				time.sleep(1.5)
		
		wallet -= bet
		sweet_bonanza(wallet)

		return wallet

#Horse betting
def horses(wallet):

	clearConsole()

	print("----[NOW PLAYING]----\n")
	print("----[Horse betting]----\n")

	showTip()
	showWallet(wallet)

	horses_list = ['Jack','Charlie','Billy','Harry','Alfie','George','Murphy']

	print(horses_list, "\n")

	selected_horse = input("Please select your horse: ")
	
	bet = input("How much would you like to bet?: ")
	
	#Check if bet is an integer
	if errorHandling(bet, wallet, selected_horse):
	
		betCheck(wallet, bet)

		winnings = bet * 6

		random_horse = random.choice(horses_list)


		if selected_horse == random_horse:
			print("Congratulations! Your horse won! You won: ")
			wallet += winnings
		else:
			print("Too bad! You lost!")
			wallet -= bet
			print("Winning horse was: " + random_horse)
			time.sleep(3)

		clearConsole()
		horses()

#First menu to start main menu and to some checks
def first_menu():
	clearConsole()
	print("----[Welcome to Casino Royale]----\n")
	wallet = int(input("Please deposit funds: $"))
	errorHandling(wallet)
	main_menu(wallet)

#Check if int
def errorHandling(arg1, arg2="", arg3="", arg4=""):
	if isinstance(arg1, int):
		pass
	else:
		usage()

#Restarts scripts when input is not a int
def usage():
	print("Please use an integer! Stupid ass bitch! ")
	time.sleep(1.3)

first_menu()
