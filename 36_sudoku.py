board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]

a = 0 ##檢查是否為False

lists = ["1", "2", "3", "4","5", "6","7","8", "9"]

for i in range(len(board)): ##橫的
    reco = {}
    for j in range(len(board[0])):
        if board[i][j] in lists:
            if board[i][j] in reco:
                reco[board[i][j]] += 1
            else:
                reco[board[i][j]] = 1
    for key, value in reco.items():
        if value >1:
            print(False)
            a = 1
        else:
            pass

for i in range(len(board)): ##直的
    reco = {}
    for j in range(len(board[0])):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
    for key, value in reco.items():
        if value >1:
            print(False)
            a = 1
        else:
            pass

##小的9宮格還沒寫
reco = {}
for j in range(0, 3):
    for i in range(0,3):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(0, 3):
    for i in range(3,6):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(0, 3):
    for i in range(6,9):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(3, 6):
    for i in range(0,3):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(3, 6):
    for i in range(3,6):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(3, 6):
    for i in range(6,9):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(6, 9):
    for i in range(0,3):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(6, 9):
    for i in range(3,6):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

reco = {}
for j in range(6, 9):
    for i in range(6,9):
        if board[j][i] in lists:
            if board[j][i] in reco:
                reco[board[j][i]] += 1
            else:
                reco[board[j][i]] = 1
for key, value in reco.items():
    if value >1:
        print(False)
        a = 1
    else:
        pass

if a == 0:
    print(True)
