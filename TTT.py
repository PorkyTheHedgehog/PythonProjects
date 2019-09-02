from collections import defaultdict

num = [str(x) for x in "0  1   2   3 "]
sep = [str(x) for x in "  --- --- --- "]
a = [str(x) for x in "A|   |   |   |"]
b = [str(x) for x in "B|   |   |   |"]
c = [str(x) for x in "C|   |   |   |"]
turn = 1
pc = defaultdict(int)


def validity(choice, ttt):
    if choice[0].lower() not in "abc" or choice[1] not in "123":
        return False
    elif ttt[["a","b","c"].index(choice[0].lower()) * 2 + 2][int(choice[1]) * 4 - 1] != " ":
        return False
    else:
        return True


while True:

    if turn % 2 == 1:
        piece = "X"
    else: piece = "O"
    print("Turn: {} ".format(turn))

    ttt = [num, sep, a, sep, b, sep, c, sep]
    for x in ttt:
        print("".join(x))

    print("Piece in play: {}".format(piece))
    choice = input("Using this format(<letter><number>), where would you like to place your piece?")
    valid = validity(choice, ttt)

    if valid == True:
        ttt[["a","b","c"].index(choice[0].lower()) * 2 + 2][int(choice[1]) * 4 - 1] = piece
        pc[piece] += 1
        pc["total"] += 1
        if pc[piece] > 2:
            if ttt[2][3] == piece and ttt[2][7] == piece and ttt[2][11] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[4][3] == piece and ttt[4][7] == piece and ttt[4][11] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[6][3] == piece and ttt[6][7] == piece and ttt[6][11] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[2][3] == piece and ttt[4][3] == piece and ttt[6][3] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[2][7] == piece and ttt[4][7] == piece and ttt[6][7] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[2][11] == piece and ttt[4][11] == piece and ttt[6][11] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[2][3] == piece and ttt[4][7] == piece and ttt[6][11] == piece:
                result = "{} wins".format(piece)
                break
            elif ttt[6][3] == piece and ttt[4][7] == piece and ttt[2][11] == piece:
                result = "{} wins".format(piece)
                break
            elif pc["total"] == 9:
                result = ("Draw")
                break
        turn += 1
        print("")
    elif valid == False:
       print("")
       print("Sorry, your choice is invalid.")
       print("")

for x in ttt:
    print("".join(x))
print(result)

