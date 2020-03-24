import itertools


game = [[0, 1, 1],
        [0, 1, 1],
        [1, 1, 0],]


def game_board(game_map, player = 0, row = 0, column = 0, jut_display = False):
	try:
		print("   0  1  2")
		if not jut_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map
	except IndexError as e:
		print("Error: make sure that row/column has a value 0,1 or 2",e)
	except Exception as e:
		print("Something bad happened.", e)


def win(current_game):
	# Horizontal
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print(f"Player {row[0]} is the winner horizontally.")

	# Vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0:
			print("Winner")

	# Diagonal
	diags=[]
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if diags.count(diags[0]) == len(diags) and diags[0] != 0:
			print(f"Player {diags[0]} is the winner diagonally. (/)")

	# Diagonal
	diags=[]
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	print(diags)

play = True
players = [1,2]
while play:
	game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]

	game_won = False
	game = game_board(game, jut_display = True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player {current_player}")
		column_choice = int(input("Choose a column you wanna play (0, 1, 2): "))
		row_choice = int(input("Choose a row you wanna play (0, 1, 2): "))
		game = game_board(game, current_player, row_choice, column_choice)






















