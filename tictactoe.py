game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],]


def game_board(game_map, player = 0, row = 0, column = 0, jut_display = False):
	try:
		print("   0  1  2")
		if not jut_display:
			game_map[row][column] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map
	except:
		print("Something went wrong!")

game = game_board(game, jut_display = True)
game = game_board(game, player = 1, row = 1, column = 1)