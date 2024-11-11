import matplotlib.pyplot as plt
from copy import deepcopy
# import matplotlib.colors as mcolors
#Easy
# matrix1=[
#     [0, 0, 0, 1, 1, 1, 0, 0],
#     [1, 1, 1, 1, 'M', 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 'R', 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1]
# ]
#Medium
# matrix1 = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 'M', 0, 0, 0, 'B', 'A', 1,1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
##########bad
# matrix1=[
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 'L', 1, 'M', 1],
#     [1, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 'O', 'R', 'B', 0, 0, 1],
#     [1, 1, 0, 1, 1, 1, 0, 1],
#     [0, 1, 0, 'A', 0, 1, 0, 1],
#     [0, 1, 0, 0, 0, 0, 0, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1]
# ]
###########
# matrix1 = [
#     [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [1, 1, 'R', 0, 0, 1, 1, 1, 1, 1, 0],
#     [1, 0, 0, 0, 'O', 1, 1, 0, 0, 1, 0],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     [1, 0, 'A', 0, 'L', 1, 1, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 'M', 0, 'B', 0, 1, 1],
#     [1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# ]
##########################################
matrix1 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 'M', 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 'L', 0, 1],
    [1, 0, 1, 0, 0, 'A', 1, 1, 1, 1, 1],
    [1, 1, 1, 'B', 'R', 'O', 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
]
fixed_targets = {
    (1, 4): 'M',
    (5, 5): 'A',
    (4, 8): 'L'
}
class State:
    def __init__(self, matrix):
        self.matrix = matrix
        self.target_borders = [['red' if cell == 'M' else 'aqua' if cell == 'A' else 'orange' if cell == 'L' else None for cell in row] for row in matrix]
        self.fig, self.ax = plt.subplots(1, 5)
        self.print(self.matrix, self.ax[0])
        self.fig.canvas.mpl_connect('key_press_event', self.press)
        

    def print(self, matrix, ax):
        rows = len(matrix)
        cols = len(matrix[0])
        ax.clear()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    color = 'black'
                elif matrix[i][j] == 'R':
                    color = 'red'
                elif matrix[i][j] == 'B':
                    color = 'aqua'
                elif matrix[i][j] == 'O':
                    color = 'orange'
                else:
                    color = 'white'  

                draw = plt.Rectangle((j, i), 1, 1, color=color)
                ax.add_patch(draw)

                border_color = self.target_borders[i][j]
                if border_color is not None:
                    border_draw = plt.Rectangle((j, i), 1, 1, edgecolor=border_color, facecolor='none', linewidth=2)
                    ax.add_patch(border_draw)

        ax.set_xlim([0, cols])
        ax.set_ylim([0, rows])
        ax.set_xticks([])
        ax.set_yticks([])

        plt.draw()

    def simulate_move(self, matrix, direction):
        matrix_copy = deepcopy(matrix)
        positions = [(i, j) for i in range(len(matrix_copy)) for j in range(len(matrix_copy[0])) if matrix_copy[i][j] in ['R', 'B', 'O']]

        for (i, j) in positions:
            new_i, new_j = i, j
            while self.can_move(matrix_copy, new_i, new_j, direction):
                if direction == 'right':
                    new_j += 1
                elif direction == 'left':
                    new_j -= 1
                elif direction == 'down':
                    new_i += 1
                elif direction == 'up':
                    new_i -= 1
                
                self.check_goal(matrix_copy, i, j, new_j, new_i)

            if (new_i, new_j) != (i, j):
                matrix_copy[new_i][new_j] = matrix_copy[i][j]
                matrix_copy[i][j] = 0

        return matrix_copy

    def can_move(self,matrix, i, j, direction):
        if direction == 'right':
            if j + 1 < len(matrix[0]) and matrix[i][j + 1] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'left':
            if j - 1 >= 0 and matrix[i][j - 1] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'down':
            if i + 1 < len(matrix) and matrix[i + 1][j] not in [1, 'R', 'B', 'O']:
                return True
        elif direction == 'up':
            if i - 1 >= 0 and matrix[i - 1][j] not in [1, 'R', 'B', 'O']:
                return True
        return False

    

    def check_goal(self, matrix, i, j, new_j, new_i):
        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
            if matrix[i][j] == 'R' and self.matrix[new_i][new_j] == 'M':
                matrix[new_i][new_j] = 0
                self.target_borders[new_i][new_j] = None

            if matrix[i][j] == 'B' and self.matrix[new_i][new_j] == 'A':
                matrix[new_i][new_j] = 0
                self.target_borders[new_i][new_j] = None

            if matrix[i][j] == 'O' and self.matrix[new_i][new_j] == 'L':
                matrix[new_i][new_j] = 0
                self.target_borders[new_i][new_j] = None

    def press(self, event):
        if event.key == 'right':
            self.move('right')
        elif event.key == 'left':
            self.move('left')
        elif event.key == 'up':
            self.move('up')
        elif event.key == 'down':
            self.move('down')

        directions = ['right', 'left', 'up', 'down']
        for idx, direction in enumerate(directions, start=1):
            simulated_matrix = self.simulate_move(self.matrix, direction)
            self.print(simulated_matrix, self.ax[idx])
        
        plt.draw()
    def move(self, direction):
        self.matrix = self.simulate_move(self.matrix, direction)
        self.print(self.matrix, self.ax[0])
        plt.draw()

State_instance = State(matrix1)
plt.show()