import random
round = 1
ties = numround = total_rounds = computer_score = player_score = 0
rol = ["rock", "paper", "scissors"]

beats = {
	"rock": "scissors",
	"paper": "rock",
	"scissors": "paper"
}

def compare(choose, comp_ch):
	global ties, player_score, computer_score
	if choose == comp_ch:
		print("It's a tie!")
		ties += 1
	elif beats[choose] == comp_ch:
		print("You win!")
		player_score += 1
	else:
		print("You lose!")
		computer_score += 1

while numround < 5:
	try:
		print(f"Round {round}")
		choose = input("Choose rock, paper, or scissors: ").lower()
		if choose not in rol:
			raise ValueError
		comp_ch = random.choice(rol)
		print(f"Computer chose: {comp_ch}")
		compare(choose, comp_ch)
		print(f"Score - You: {player_score} | Computer: {computer_score}")
		total_rounds += 1
		numround += 1
		
		if computer_score == 3:
			print(f"Score - You: {player_score} | Computer: {computer_score}")
			print("Computer wins the game!")
			exit()
		elif player_score == 3:
			print(f"Score - You: {player_score} | Computer: {computer_score}")
			print("You win the game!")
			exit()
	except ValueError:
		print("Invalid input. Please enter rock, paper, or scissors.")