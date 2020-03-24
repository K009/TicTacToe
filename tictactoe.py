import itertools


def game_board(game_map, player = 0, row = 0, column = 0, jut_display = False):
	try:
		if game_map[row][column] != 0:
			print("This position is occupied! Choose another.")
			return game_map, False

		print("   0  1  2")
		if not jut_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("Error: make sure that row/column has a value 0,1 or 2",e)
		return game_map, False

	except Exception as e:
		print("Something bad happened.", e)
		return game_map, False


def win(current_game):

	def all_same(l):
		if row.count(row[0]) == len(row) and row[0] != 0:
			return True
		else:
			return False
	# Horizontal
	for row in game:
		if all_same(row):
			print(f"Player {row[0]} is the winner horizontally. (-)")

	# Vertical
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if all_same(check):
			print(f"Player {check[0]} is the winner vertically. (|)")

	# Diagonal
	diags=[]
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
			print(f"Player {diags[0]} is the winner diagonally. (/)")

	# Diagonal
	diags=[]
	for ix in range(len(game)):
		diags.append(game[ix][ix])
	if all_same(row):
		print(f"Player {diags[0]} is the winner diagonally. (\)")		

play = True
players = [1,2]
while play:
	game = [[0, 0, 0],
	        [0, 0, 0],
	        [0, 0, 0]]

	game_won = False
	game, _ = game_board(game, jut_display = True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player {current_player}")
		played = False

		while not played:
			column_choice = int(input("Choose a column you wanna play (0, 1, 2): "))
			row_choice = int(input("Choose a row you wanna play (0, 1, 2): "))
			game, played = game_board(game, current_player, row_choice, column_choice)






















