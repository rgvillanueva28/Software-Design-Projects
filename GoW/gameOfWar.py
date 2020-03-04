from game import Game

if __name__ == "__main__":
	g = Game()
	g.play()
	winner = g.getWinner()
	if(winner == None):
		print("Tie game.")
	else:
		print("\nWinner = ", winner.getName())