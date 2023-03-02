from pprint import pprint

maze = [            ##迷宮地圖(1是牆壁、0是通道)
    [1,1,1,1,1,1],  ## (1,1) (1,2) 
    [1,0,1,0,1,1],  ## (2,1) (2,2)
    [1,0,1,0,0,1],  ## (3,1) (3,2) 地圖的指標
    [1,0,0,0,1,1],
    [1,0,1,0,0,1],
    [1,1,1,1,1,1]
]

directions = [             ##lambda可以建立虛擬函數
    lambda x, y: (x-1, y), ##往上走
    lambda x, y: (x+1, y), ##往下走
    lambda x, y: (x, y-1), ##往左走
    lambda x, y: (x, y+1) ##往右走
]

def maze_solve(x, y, goal_x, goal_y):
    ##解迷宮程式，xy是迷宮入口，goal_x, goal_y是迷宮出口
    maze[x][y] = 2 ##所經過的路徑用2來表示
    stack = [] ##建立路徑堆疊
    stack.append((x, y)) ##將路徑push入堆疊
    print("迷宮開始")
    while (len(stack) > 0):
        cur = stack[-1] ##目前位置
        if cur[0] == goal_x and cur[1] == goal_y: 
            print("抵達出口")
            return True ##抵達出口表示true
        for dir in directions: ##依照上下左右來走迷宮
            next = dir((cur[0], cur[1]))
            if maze[next[0]][next[1]] == 0: ##如果是通道可以走
                stack.append(next)
                maze[next[0]][next[1]] = 2 ##用2來標記所走過的路
                break
            else: ##如果進入死路，則回朔
                maze[cur[0]][cur[1]] = 3 ##標記是死路
                stack.pop()
    #else:
    #    print("沒有路徑")
    #   return False

maze_solve(1,1,4,4)
pprint(maze)
