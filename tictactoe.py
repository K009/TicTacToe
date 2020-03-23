game = [[0, 1, 0],
        [0, 0, 1],
        [0, 1, 0],]


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
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) and row[0] != 0:
			print("Winner")
	for col in range(len(game)):
		check = []

		for row in game:
			check.append(row[col])

		if check.count(check[0]) == len(check) and check[0] != 0:
			print("Winner")


game = game_board(game, jut_display = True)
game = game_board(game, player = 1, row = 1, column = 1)
win(game)