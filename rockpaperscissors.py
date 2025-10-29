import random
round = 1
ties  = total_rounds = computer_score = player_score = 0
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

def final_result():
	global round, ties, total_rounds, computer_score, player_score
	if player_score > computer_score:
		print(f"Match Over! You won {player_score}-{computer_score}!")
	elif player_score == computer_score:
		print(f"Match Over! It's a tie at {player_score}-{computer_score}!")
	else:
		print(f"Match Over! Computer won {player_score}-{computer_score}!")
	play = input(f"Total rounds: {total_rounds} \nTies: {ties} \n Play again? (yes/no): ")
	if play.lower() == "yes":
		round = 1
		ties  = total_rounds = computer_score = player_score = 0
		game()
	if play.lower() == "no":
		print("Thanks for playing!")
		exit()

def game():
	global round, total_rounds, player_score, computer_score, ties
	while round < 6:
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
			round += 1
			
			if computer_score == 3:
				print("Computer wins the game!")
				final_result()
				exit()
			elif player_score == 3:
				print("You win the game!")
				final_result()
				exit()
			elif round == 6:
				final_result()
		except ValueError:
			print("Invalid input. Please enter rock, paper, or scissors.")

if __name__ == "__main__":
	game()

