#guess number game between 0 and 100

import random

def game():
	rand = random.randint(0,100)  
	
	while True:  
		guess = 0
		userIn = None 
		
		while guess < 3:  
			try:
				if userIn is None:  
					userIn = int(input("I'm thinking of a number! Try to guess the number I'm thinking of: "))
				elif userIn > rand:
					userIn = int(input("Too High! Guess again: "))
				elif userIn == rand:
					print("You guessed it!")
					choice = input("Want to play again? y or n: ").strip().lower()
					if choice == 'y': 
						return game()  
					elif choice == 'n': 
						exitgame()
				else: 
					userIn = int(input("Too Low! Guess again: "))

				if userIn != rand:
					guess += 1
					
			except ValueError:
				print("Invalid input. Please enter a number.")

		if userIn > rand:
			print("Too High!")
		elif userIn < rand:
			print("Too Low!")

		cont = input("That's 3 guesses! Continue guessing? y or n: ").strip().lower()
		if cont == 'y':
			continue 
		elif cont == 'n':  
			print(f"Game over! The number was {rand}")
			exitgame()	

def exitgame():
	print("Thanks for playing!")
	exit()

if __name__ == "__main__":
	game()