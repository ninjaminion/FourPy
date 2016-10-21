board = [[0 for x in xrange(6)] for x in xrange(7)]
player = 1
win = 0
def user():
	exit = 0
	ok = [1,2,3,4,5,6,7]
	while exit == 0: 
		user = int(raw_input("Player " +str(player)+ ", Which column would you like to place your piece?"))
		if user in ok:
			exit = 1
		else:
			print "Invalid Input!"
	return user
def putter(x):
        x = x - 1
        var = 0
        for n in board[x]:
            if n == 0:
                break
            else:
                var = var + 1
        board[x][var] = player
def printboard():
        sepline = "+-+-+-+-+-+-+-+ \n"
        line = "|"
        line1 = line + str(board[0][5]) + line + str(board[1][5]) + line + str(board[2][5]) + line + str(board[3][5]) + line + str(board[4][5]) + line + str(board[5][5]) + line + str(board[6][5]) + line + "\n"
        line2 = line + str(board[0][4]) + line + str(board[1][4]) + line + str(board[2][4]) + line + str(board[3][4]) + line + str(board[4][4]) + line + str(board[5][4]) + line + str(board[6][4]) + line + "\n"
        line3 = line + str(board[0][3]) + line + str(board[1][3]) + line + str(board[2][3]) + line + str(board[3][3]) + line + str(board[4][3]) + line + str(board[5][3]) + line + str(board[6][3]) + line + "\n"
        line4 = line + str(board[0][2]) + line + str(board[1][2]) + line + str(board[2][2]) + line + str(board[3][2]) + line + str(board[4][2]) + line + str(board[5][2]) + line + str(board[6][2]) + line + "\n"
        line5 = line + str(board[0][1]) + line + str(board[1][1]) + line + str(board[2][1]) + line + str(board[3][1]) + line + str(board[4][1]) + line + str(board[5][1]) + line + str(board[6][1]) + line + "\n"
        line6 = line + str(board[0][0]) + line + str(board[1][0]) + line + str(board[2][0]) + line + str(board[3][0]) + line + str(board[4][0]) + line + str(board[5][0]) + line + str(board[6][0]) + line + "\n"
        print sepline + line1 + sepline + line2 + sepline + line3 + sepline + line4 + sepline + line5 + sepline + line6 + sepline
while win == 0:
        printboard()
        putter(user())
        if player == 1:
                player = 2
        elif player == 2:
                player = 1

print()sdfghsdkhksdgdjk