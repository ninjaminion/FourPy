board = [[0 for x in xrange(6)] for x in xrange(7)]
def printboard():
        sepline = "+-+-+-+-+-+-+-+"
        line = "|"
        line1 = line + str(board[0][0]) + line + str(board[1][0]) + line + str(board[2][0]) + line + str(board[3][0]) + line + str(board[4][0]) + line + str(board[5][0]) + line + str(board[6][0]) + line
        line2 = line + str(board[0][1]) + line + str(board[1][1]) + line + str(board[2][1]) + line + str(board[3][1]) + line + str(board[4][1]) + line + str(board[5][1]) + line + str(board[6][1]) + line
        line3 = line + str(board[0][2]) + line + str(board[1][2]) + line + str(board[2][2]) + line + str(board[3][2]) + line + str(board[4][2]) + line + str(board[5][2]) + line + str(board[6][2]) + line
        line4 = line + str(board[0][3]) + line + str(board[1][3]) + line + str(board[2][3]) + line + str(board[3][3]) + line + str(board[4][3]) + line + str(board[5][3]) + line + str(board[6][3]) + line
        line5 = line + str(board[0][4]) + line + str(board[1][4]) + line + str(board[2][4]) + line + str(board[3][4]) + line + str(board[4][4]) + line + str(board[5][4]) + line + str(board[6][4]) + line
        line6 = line + str(board[0][5]) + line + str(board[1][5]) + line + str(board[2][5]) + line + str(board[3][5]) + line + str(board[4][5]) + line + str(board[5][5]) + line + str(board[6][5]) + line
        print sepline + "\n" + line1 + sepline + "\n" + line2 + sepline + "\n" + line3 + sepline + "\n" + line4 + sepline + "\n" + line5 + sepline + "\n" + line6 
