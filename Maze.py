
import random
# from cmu_112_graphics import *
# follow steps of the DFS algorithm in TP guide
# https://www.cs.cmu.edu/~112/notes/student-tp-guides/Mazes.pdf


class Maze():
    def __init__(self, width):
        # make sure the width and height is odd
        # use the idea from maze guide - 5.DFS part
        self.width = (width // 2) * 2 + 1

        # two unit every time to allow walls form between neighbors
        self.directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        # initialize the maze and the visited matrix
        self.matrix = None

    def inBound(self, new_row, new_col, start, end):
        if (new_row >= start[0] and new_row <= end[0]
                and new_col >= start[1] and new_col <= end[1]):
            return True

    def generate_matrix_dfs(self, start, end, visited):
        # set the start place and end place 0
        # self.matrix = -np.ones((self.height, self.width))
        (startRow, startCol) = start
        (endRow, endCol) = end
        self.matrix[startRow][startCol] = 0
        self.matrix[endRow][endCol] = 0

        def backtrack(row, col):
            # Add the current location to the visited set
            visited[row][col] = 1

            # Loop over all four neighbors of the current location in random order
            random.shuffle(self.directions)
            for d in self.directions:
                new_row = row + d[0]
                new_col = col + d[1]

                # if the neighbor is out of bound, continue
                if (not self.inBound(new_row, new_col, start, end)):
                    continue

                # if the neighbor has already been visited, continue
                if (visited[new_row][new_col] == 1):
                    continue

                # else, do dfs

                # set neighbor as visited
                visited[new_row][new_col] = 1
                self.matrix[new_row][new_col] = 0

                # wall between original and current position
                wall_row = (row + new_row) // 2
                wall_col = (col + new_col) // 2

                # set it as visited & remove the wall
                visited[wall_row][wall_col] = 1
                self.matrix[wall_row][wall_col] = 0

                # backtrack
                backtrack(new_row, new_col)

        backtrack(startRow, startCol)
        self.matrix[endRow-1][endCol] = 0
        self.matrix[endRow][endCol-1] = 0

    def generateMaze(self):
        self.matrix = [([-1]*self.width) for row in range(self.width)]
        visited = [[0 for i in range(self.width)] for j in range(self.width)]
        self.generate_matrix_dfs(
            (1, 1), (self.width - 2, self.width - 2), visited)

    def print_matrix(self):
        for i in range(self.width):
            for j in range(self.width):
                if self.matrix[i][j] == -1:
                    print('□', end=' ')
                elif self.matrix[i][j] == 0:
                    print(' ', end=' ')
            print('')
    

# # Test Function
# maze = Maze(14)
# maze.generateMaze()
# maze.print_matrix()

# def print_matrix(self):
#         for i in range(self.width):
#             for j in range(self.width):
#                 if self.matrix[i][j] == -1:
#                     print('□', end=' ')
#                 elif self.matrix[i][j] == 0:
#                     print(' ', end=' ')
#             print('')

