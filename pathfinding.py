
# read the TP Pathfinding Guide
# read the pseudocode description of Dijkstra’s algorithm
# read the A* algorithm article
# https://brilliant.org/wiki/a-star-search/
# https://www.cs.cmu.edu/~112/notes/student-tp-guides/Pathfinding.pdf

from copy import deepcopy


class Dijkstra():
    def __init__(self, maze, start, target):
        self.maze = maze
        self.start = start
        self.row = start[0]
        self.col = start[1]
        self.target = target
        self.targetRow = target[0]
        self.targetCol = target[1]
        # move directions up down left and right
        self.dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def isLegalMove(self, row, col, board):
        if (row < 0 or row > len(board)-1
            or col < 0 or col > len(board[0]) - 1
                or board[row][col] != 0):
            return False
        return True

    def possibleMoveArea(self):

        def isLegalMove(row, col, board):
            if (row < 0 or row > len(board)-1
                or col < 0 or col > len(board[0])-1
                    or board[row][col] != 0):
                return False
            return True

        possibleMoveArea = []
        for (drow, dcol) in self.dir:
            newRow = drow + self.row
            newCol = dcol + self.col
            if isLegalMove(newRow, newCol, self.maze) == True:
                possibleMoveArea.append((newRow, newCol))
        return possibleMoveArea

    # use Dijkstra to find shortest path
    def dijkstra(self):
        # need visited to save time
        visited = [[0 for i in range(len(self.maze[0]))]
                   for j in range(len(self.maze))]
        queue = []

        # initial state
        queue.append([(self.start[0], self.start[1])])
        visited[self.start[0]][self.start[1]] = 1

        while (len(queue) != 0):
            cur_path = queue.pop(0)
            cur_row, cur_col = cur_path[-1]
            if cur_row == self.targetRow and cur_col == self.targetCol:
                return cur_path
                
            # Loop over each unvisited neighbor of the node
            for d in self.dir:
                new_row = cur_row + d[0]
                new_col = cur_col + d[1]

                # exclude invalid or revisit
                if not self.isLegalMove(new_row, new_col, self.maze):
                    continue
                if visited[new_row][new_col] == 1:
                    continue

                new_path = deepcopy(cur_path)
                new_path.append((new_row, new_col))
                visited[new_row][new_col] = 1
                queue.append(new_path)
        return

    def getDistance(self, row, col):
        return 1

    def pathFinding(self):
        return self.dijkstra()
       


# Test code
# board = [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#          [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
#          [1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
#          [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#          [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0],
#          [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1]]

# a = Dijkstra(board, (0, 4), (0, 0))
# print(a.pathFinding())
# print(a.dijkstra())
