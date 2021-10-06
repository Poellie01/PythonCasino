import os
import random
import time

wallet = int(0)


def main_menu():

	clearConsole()
	print("----[Welcome to Casino Royale]----")
	print("----[Select your game]----\n")

	print("[1] Roulette | [4] Blackjack | [7] Coming Soon")
	print("[2] Poker | [5] Horses | [8] Coming Soon")
	print("[3] Slots | [6] Coming Soon | [9] Exit" + "\n")

	print("Wallet: $", wallet)
	game = input("Please Select your game: ")

	if game == "1":
		roulette(wallet)
	elif game == "3":
		slots()
	elif game == "4":
		blackjack()
	elif game == "5":
		horses()



def roulette():

	colors = ['Red', 'Black', 'Green']
	random_color = random.choice(colors)

	clearConsole()
	winning_number = random.randint(0,36)

	print(winning_number)

	print("----[Now playing Roulette]----")
	bet = int(input("Please place your bets [USD]: "))
	bet_number = int(input("On which number? "))

	if bet_number == winning_number:
		winnings = bet * 36
		print("Winning number is: ", winning_number, random_color)
		print("Congratulations! You could've won ", winnings)
		time.sleep(3.5)
		wallet = winnings + wallet
		main_menu()
		# return wallet
	else:
		print("Too bad! You lost! Winning number was: \n", winning_number)
		time.sleep(3.5)
		main_menu()


def blackjack():
	clearConsole()

	dealerHand = random.randint(17,27)
	playerHand = random.randint(17,27)

	print("----[Now playing Blackjack]----")
	print("----[Select 0 bet to go back to main menu]----")
	bet = int(input("Please place your bet [USD]: "))

	winnings = bet * 2

	if playerHand == 21:
		winnings = bet * 2.5

	print("Dealer drew: ", dealerHand)
	print("You got: ", playerHand)

	if dealerHand > 21:
		print("Congratulations! You won: $", winnings)
		time.sleep(3.5)
		main_menu()
	else:
		print("Too bad, you lost.")
		time.sleep(3)
		main_menu()

def slots():
	print("----[Now playing Tycoon Manya]----")
	print("")

	pepper = ['Black Pepper', 'Red Pepper', 'Green Pepper']
	lemon = ['Black lemon', 'Red lemon', 'Green lemon']
	apple = ['Black apple', 'Red apple', 'Green apple']

	random_pepper = random.choice(pepper)
	random_lemon = random.choice(lemon)
	random_apple = random.choice(apple)

	
	bet = input("Please place your bets [Minimum $10]: ")

	winnings = bet * 250

	print("| " + random_pepper + " | " + random_lemon + " | " + random_apple)


	if random_pepper.startswith("Black") & random_apple.startswith("Black") & random_lemon.startswith("Black"):
		print("Awesome! You won nothing! You could've won: " + "$",winnings)
		time.sleep(3) 
	elif random_pepper.startswith("Red") & random_apple.startswith("Red") & random_lemon.startswith("Red"):
		print("Congratulations! You won nothing! You could've won: " + "$",winnings)
		time.sleep(3)
	elif random_pepper.startswith("Green") & random_apple.startswith("Green") & random_lemon.startswith("Green"):
		print("Congrats! You won $0 You could've won: " + "$",winnings)
		time.sleep(3)
	else:
		print("Too bad, wack")

	slots()



def horses():
	print("----[NOW PLAYING]----")
	print("----[Horse betting]----")

	horses_list = ['Jack','Charlie','Billy','Harry','Alfie','George','Murphy']

	print(horses_list)

	print("\n")
	selected_horse = input("Please select your horse: ")
	bet = input("How much would you like to bet?: ")

	winnings = bet * 6

	random_horse = random.choice(horses_list)


	if selected_horse == random_horse:
		print("Congratulations! Your horse won! You won: ")
	else:
		print("Too bad! You lost!")
		print("Winning horse was: " + random_horse)
		time.sleep(3)

	clearConsole()
	horses()

def clearConsole():
	command = 'clear'
	if os.name in ('nt','dos'):
		command = 'cls'
	os.system(command)


main_menu()

